import { useState } from 'react'

function StoryGenerator() {
  const [prompt, setPrompt] = useState('')
  const [story, setStory] = useState('')
  const [loading, setLoading] = useState(false)

  const handleSubmit = async (e) => {
    e.preventDefault()
    if (!prompt.trim()) return

    setLoading(true)
    try {
      const token = localStorage.getItem('token')
      const response = await fetch('http://localhost:8000/create_mythology', {
        method: 'POST',
        headers: { 
          'Content-Type': 'application/json',
          'Authorization': `Bearer ${token}`
        },
        body: JSON.stringify({ prompt })
      })
      
      if (response.ok) {
        const data = await response.json()
        setStory(data.mythology)
      } else {
        setStory('Error generating story. Please try again.')
      }
    } catch (error) {
      console.error('Error generating story:', error)
      setStory('Error generating story. Please try again.')
    } finally {
      setLoading(false)
    }
  }

  return (
    <div className="min-h-screen bg-gradient-to-br from-amber-900 via-stone-900 to-black p-6">
      <div className="max-w-4xl mx-auto">
        <header className="text-center mb-8">
          <h1 className="text-4xl font-bold text-white mb-2">🌟 Story Generator</h1>
          <p className="text-gray-300">Create your mythology stories</p>
        </header>

        <div className="grid grid-cols-1 lg:grid-cols-2 gap-8">
          {/* Input Section */}
          <div className="bg-stone-800 rounded-xl p-6 shadow-2xl">
            <h2 className="text-2xl font-semibold text-white mb-4">🎭 Your Story Request</h2>
            <form onSubmit={handleSubmit} className="space-y-4">
              <textarea
                value={prompt}
                onChange={(e) => setPrompt(e.target.value)}
                placeholder="Describe the story you want... (e.g., 'Create a story about the first dragon' or 'Tell me about the moon shattering')"
                className="w-full h-32 px-4 py-3 bg-stone-700 border-0 rounded-lg text-white placeholder-gray-400 focus:outline-none focus:ring-2 focus:ring-amber-500 resize-none"
                required
              />
              <button
                type="submit"
                disabled={loading || !prompt.trim()}
                className="w-full py-3 px-4 bg-amber-800 text-white font-semibold rounded-lg disabled:opacity-50 disabled:cursor-not-allowed"
              >
                {loading ? '🌟 Creating Story...' : '✨ Create Story'}
              </button>
            </form>

            {/* Deity Status */}
            {loading && (
              <div className="mt-6 space-y-2">
                <p className="text-gray-300 text-sm">Generating your story:</p>
                <div className="space-y-1 text-xs">
                  <div className="text-yellow-400">🎪 Trickster - Adding chaos...</div>
                  <div className="text-red-400">⚔️ Warrior - Forging conflict...</div>
                  <div className="text-blue-400">📚 Wisdom - Weaving knowledge...</div>
                  <div className="text-green-400">🌿 Nature - Growing life...</div>
                  <div className="text-gray-400">💀 Death - Shaping endings...</div>
                  <div className="text-purple-400">🕸️ Weaver - Binding all...</div>
                </div>
              </div>
            )}
          </div>

          {/* Story Output Section */}
          <div className="bg-stone-800 rounded-xl p-6 shadow-2xl">
            <h2 className="text-2xl font-semibold text-white mb-4">📜 Your Story</h2>
            <div className="bg-stone-900 rounded-lg p-4 min-h-[300px] max-h-[500px] overflow-y-auto">
              {story ? (
                <div className="text-gray-200 whitespace-pre-wrap leading-relaxed">
                  {story}
                </div>
              ) : (
                <div className="text-gray-500 italic text-center mt-20">
                  Your story will appear here...
                </div>
              )}
            </div>
          </div>
        </div>
      </div>
    </div>
  )
}

export default StoryGenerator