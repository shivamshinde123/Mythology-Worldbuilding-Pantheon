from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from sqlalchemy.ext.asyncio import AsyncSession
from auth.auth_service import authenticate_user, create_access_token, get_user, get_password_hash, verify_token
from auth_db.models import UserCreate, UserDB, Token, MythologyRequest, MythologyResponse
from auth_db.connection import get_db, engine
from auth_db.base import Base
from orchestration.coordinator import MythologyCoordinator
import asyncio
from datetime import timedelta
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="Mythology Worldbuiling API", version="1.0.0")

app.add_middleware(
    CORSMiddleware, 
    allow_origins=["*"], 
    allow_credentials=True, 
    allow_methods=["*"], 
    allow_headers=["*"]
)

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

async def get_current_user(token:str = Depends(oauth2_scheme), db: AsyncSession = Depends(get_db)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )

    token_data = verify_token(token, credentials_exception)
    user = await get_user(db, username=token_data.username)

    if user is None:
        raise credentials_exception

    return user 

@app.on_event("startup")
async def on_startup():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

@app.get("/")
async def root():
    return {"message": "Mythology API is running"}

@app.post("/signup", response_model=Token)
async def signup(user: UserCreate, db: AsyncSession = Depends(get_db)):
    try:
        db_user = await get_user(db, username=user.username)
        if db_user:
            raise HTTPException(status_code=400, detail="Username already registered")
        
        hashed_password = get_password_hash(user.password)
        new_user = UserDB(username=user.username, hashed_password=hashed_password)
        db.add(new_user)
        await db.commit()
        await db.refresh(new_user)

        access_token_expires = timedelta(minutes=30)
        access_token = create_access_token(
            data={"sub": new_user.username}, expires_delta=access_token_expires
        )
        return {"access_token": access_token, "token_type": "bearer"}
    except HTTPException:
        raise
    except Exception as e:
        await db.rollback()
        raise HTTPException(status_code=500, detail=f"Failed to create user: {str(e)}")

@app.post("/token", response_model=Token)
async def login(form_data: OAuth2PasswordRequestForm = Depends(), db: AsyncSession = Depends(get_db)):
    try:
        user = await authenticate_user(db, form_data.username, form_data.password)
        if not user:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Incorrect username or password",
                headers={"WWW-Authenticate": "Bearer"},
            )
        access_token_expires = timedelta(minutes=30)
        access_token = create_access_token(
            data={"sub": user.username}, expires_delta=access_token_expires
        )
        return {"access_token": access_token, "token_type": "bearer"}
    except HTTPException:
        raise
    except Exception as e:
        import traceback
        error_details = traceback.format_exc()
        raise HTTPException(status_code=500, detail=f"Login failed: {str(e)} | Traceback: {error_details}")


@app.post("/create_mythology", response_model=MythologyResponse)
async def create_mythology(request: MythologyRequest, current_user: UserDB = Depends(get_current_user)):
    try:
        coordinator = MythologyCoordinator()
        mythology_data = await coordinator.create_mythology(request.prompt)
        return {"mythology": mythology_data.get("final_mythology", "No mythology generated")}
    except Exception as e:
        raise HTTPException(status_code=500, detail="Failed to generate mythology")