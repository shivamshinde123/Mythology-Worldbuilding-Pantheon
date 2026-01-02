# Mythology Worldbuilding Pantheon

A multi-agent AI system where different deity archetypes collaborate to create rich, coherent mythologies through structured interaction patterns.

## 🌟 Core Concept

Imagine a pantheon of AI gods, each with distinct personalities and domains, working together to weave mythologies. Five deity agents embody different archetypes (Trickster, Warrior, Wisdom, Nature, Death) while a sixth agent (Creation Weaver) synthesizes their perspectives into coherent narratives.

**The Magic**: Each agent has a unique voice and perspective, but they collaborate to create stories that are greater than the sum of their parts. The system maintains consistency across multiple story sessions, building a rich mythology world over time.

## 🎭 The Divine Pantheon

### **Kethix - The Trickster** 🎪
- **Domain**: Chaos, Change, Transformation, Subversion
- **Personality**: Witty, playful, asks "what if?", loves plot twists
- **Role**: Adds unexpected elements, finds loopholes, injects irony
- **Temperature**: 0.9 (highest creativity)

### **Valdris - The Warrior** ⚔️
- **Domain**: Conflict, Honor, Strength, Justice, Trials
- **Personality**: Direct, honor-bound, strategic, protector mentality
- **Role**: Establishes stakes, creates trials, defines honor codes
- **Temperature**: 0.6 (consistent principles)

### **Aetherion - The Wisdom** 📚
- **Domain**: Knowledge, Magic, Secrets, Understanding
- **Personality**: Patient, contemplative, mysterious, asks "how?" and "why?"
- **Role**: Explains mechanisms, establishes magic systems, reveals truth
- **Temperature**: 0.7 (balanced)

### **Sylvara - The Nature** 🌿
- **Domain**: Life, Seasons, Growth, Wilderness, Cycles
- **Personality**: Cyclical thinker, nurturing but harsh, primal, ancient
- **Role**: Creates ecosystems, shows interconnection, voices nature
- **Temperature**: 0.7 (balanced)

### **Mortanis - The Death** 💀
- **Domain**: Endings, Rebirth, Finality, Afterlife, Memory
- **Personality**: Solemn but gentle, patient, inevitable, fair
- **Role**: Makes endings meaningful, establishes afterlife concepts
- **Temperature**: 0.5 (measured and solemn)

### **Nyssara - The Creation Weaver** 🕸️
- **Domain**: Synthesis, Harmony, Storytelling, Connection
- **Personality**: Diplomatic, big-picture thinker, narrative-focused
- **Role**: Synthesizes all contributions, resolves contradictions
- **Temperature**: 0.7 (balanced)

## 🔄 How It Works

### The Collaborative Process

1. **Problem Analysis**: Creation Weaver analyzes your request and identifies what elements are needed
2. **Divine Council**: All five deity agents contribute their unique perspectives on your request
3. **Synthesis**: Creation Weaver combines all perspectives into one coherent, flowing narrative
4. **Memory Storage**: The completed story is saved to the lore database for future consistency

### Example Flow
```
User: "Create a story about the first dragon"

Step 1: Weaver identifies needed elements (origin, powers, impact, etc.)

Step 2: Each deity contributes:
- Trickster: "Dragons were born from a cosmic prank gone wrong..."
- Warrior: "The first dragon was forged in divine combat..."
- Wisdom: "Dragons are living repositories of ancient knowledge..."
- Nature: "Dragons emerged from the earth's molten heart..."
- Death: "Dragons bridge life and death, eternal yet mortal..."

Step 3: Weaver synthesizes into one epic dragon origin story

Step 4: Story saved to database for future reference
```

## 🧠 Memory & Consistency

The system maintains a **Lore Database** that stores every story created. When you request a new story, all agents can see previous stories, ensuring:

- **Consistency**: New stories don't contradict existing lore
- **Continuity**: Stories reference and build upon each other
- **World Building**: Each story adds to a growing mythology world

### Example of Memory in Action
```
Session 1: "Create a story about the moon shattering"
→ Creates moon story, saves to database

Session 2: "Create a story about wild magic"
→ Agents see moon story, create magic story that references moon shattering
→ "After the moon shattered, magic became unpredictable..."

Session 3: "Create a story about sea monsters"
→ Agents see both previous stories
→ "The wandering seas, born from the moon's shattering, spawned creatures..."
```

## 🏗️ Technical Architecture

### Core Components

```
mythology-pantheon/
├── backend/                  # FastAPI backend server
│   ├── agents/              # AI deity agents
│   │   ├── base_agent.py    # Base class with LangChain integration
│   │   ├── trickster_agent.py # Kethix implementation
│   │   ├── warrior_agent.py # Valdris implementation
│   │   ├── wisdom_agent.py  # Aetherion implementation
│   │   ├── nature_agent.py  # Sylvara implementation
│   │   ├── death_agent.py   # Mortanis implementation
│   │   └── weaver_agent.py  # Nyssara implementation
│   ├── orchestration/       # Collaboration management
│   │   ├── coordinator.py   # Main user interface
│   │   └── collaboration_patterns.py # Multi-agent workflow
│   ├── agent_memory/        # Story persistence system
│   │   └── lore_database.py # Story storage and retrieval
│   ├── auth_db/             # Database models and connection
│   │   ├── base.py         # SQLAlchemy base
│   │   ├── connection.py   # Database connection
│   │   └── models.py       # User and API models
│   ├── auth/                # Authentication services
│   │   └── auth_service.py # JWT and password handling
│   ├── api/                 # API endpoints
│   │   └── routes.py       # FastAPI routes
│   ├── prompts/             # Agent personalities
│   │   └── agent_prompts.py # Detailed character prompts
│   └── main.py              # Server entry point
├── frontend/                 # React web application
│   ├── src/                 # React source code
│   │   ├── pages/          # Application pages
│   │   ├── App.jsx         # Main app component
│   │   └── main.jsx        # React entry point
│   ├── index.html          # HTML template
│   ├── package.json        # Node.js dependencies
│   ├── tailwind.config.js  # Tailwind CSS configuration
│   └── vite.config.js      # Vite build configuration
├── .gitignore               # Git ignore patterns
└── README.md                # Project documentation
```

### Key Technologies
- **FastAPI**: REST API framework
- **React**: Frontend user interface with Vite
- **LangChain**: Agent framework and LLM integration
- **OpenAI GPT-4**: Language model powering the agents
- **SQLAlchemy**: Database ORM for user authentication
- **SQLite**: Database for user data
- **Tailwind CSS**: Utility-first CSS framework
- **Python AsyncIO**: Concurrent agent execution
- **JWT**: Authentication tokens
- **JSON**: Story persistence and export

## 🚀 Getting Started

### Prerequisites
- Python 3.8+
- Node.js 16+
- OpenAI API key

### Installation

1. **Clone the repository**
```bash
git clone https://github.com/shivamshinde123/Mythology-Worldbuilding-Pantheon.git
cd Mythology-Worldbuilding-Pantheon
```

2. **Install backend dependencies**
```bash
# Install uv if you don't have it
pip install uv

# Install dependencies with uv
cd backend
uv sync
```

3. **Install frontend dependencies**
```bash
# Navigate to frontend directory
cd ../frontend
npm install
```

4. **Set up environment**
```bash
# Create .env file in backend folder
echo "OPENAI_API_KEY=your_api_key_here" > backend/.env
echo "SECRET_KEY=your_secret_key_here" >> backend/.env
echo "DATABASE_URL=sqlite+aiosqlite:///./mythology.db" >> backend/.env
```

**Required Environment Variables:**
- `OPENAI_API_KEY`: Your OpenAI API key for GPT-4 access
- `SECRET_KEY`: Secret key for JWT token encryption (generate a secure random string)
- `DATABASE_URL`: Database connection string (SQLite by default)

### Running the Application

1. **Start the backend server**
```bash
cd backend
uv run python main.py
```

2. **Start the frontend development server**
```bash
# In a new terminal
cd frontend
npm run dev
```

3. **Access the application**
- Register a new account or login in broswer
- Start creating mythological stories!

## 🎨 What Makes This Special

### 1. **Character-Driven Storytelling**
Unlike generic AI story generators, each agent has a distinct personality, speech pattern, and philosophical approach. Stories feel like they emerge from actual divine beings with different motivations.

### 2. **Emergent Complexity**
Simple agent interactions create unexpectedly rich narratives. The tension between Trickster's chaos and Warrior's order, or Death's finality and Nature's cycles, generates compelling conflicts.

### 3. **Consistency Engine**
The memory system prevents contradictions across sessions. Your mythology world grows coherently over time, with each story adding to a larger tapestry.

### 4. **Collaborative Synthesis**
The Creation Weaver doesn't just combine ideas, it finds elegant ways to resolve contradictions and create unified narratives that honor all perspectives.

### 5. **Scalable Architecture**
Easy to add new agents, modify collaboration patterns, or extend functionality. The system is designed for growth and experimentation.

## 🔮 Example Output

**Request**: "Create a story about the moon shattering"

**Result**: A rich narrative that might include:
- Trickster's cosmic prank that started it all
- Warrior's attempt to prevent the catastrophe  
- Wisdom's explanation of the magical consequences
- Nature's description of how tides went wild
- Death's perspective on the souls that escaped
- Weaver's synthesis into one epic tale

Each agent's contribution feels authentic to their character while serving the larger narrative.

## 🛠️ Future Enhancements

### Planned Features
- **Advanced Collaboration Patterns**: Debate modes, sequential chains
- **Export Formats**: PDF, ePub, formatted documents
- **Visual Elements**: AI-generated artwork for stories
- **Campaign Management**: Organize stories into themed collections

### Extensibility
- Add new deity archetypes (Love, War, Craft, etc.)
- Create specialized collaboration patterns
- Integrate with other AI models
- Add voice synthesis for audio storytelling

## 📚 Use Cases

### **Writers & Creators**
- Generate rich backstories for fantasy worlds
- Create consistent mythologies for games/novels
- Overcome writer's block with collaborative inspiration

### **Game Masters**
- Build campaign lore with interconnected stories
- Create pantheons with distinct divine personalities
- Generate consistent world-building content

### **Educators**
- Teach mythology and storytelling concepts
- Demonstrate collaborative AI systems
- Explore narrative structure and character development

### **Researchers**
- Study multi-agent collaboration patterns
- Explore emergent narrative generation
- Investigate AI personality consistency

## 🤝 Contributing

We welcome contributions! Areas of interest:
- New deity archetypes and personalities
- Enhanced collaboration patterns
- UI/UX improvements
- Performance optimizations
- Documentation and examples

## 📄 License

MIT License - Feel free to use, modify, and distribute.

## 🙏 Acknowledgments

Inspired by the rich tradition of collaborative storytelling and the emerging field of multi-agent AI systems. Special thanks to the mythology traditions of cultures worldwide that inform our understanding of archetypal divine personalities.

---

*"In the beginning was the Word, and the Word was spoken by many voices, each adding their thread to the tapestry of existence."* - The Creation Weaver