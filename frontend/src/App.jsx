import { useState, useRef, useEffect } from 'react'
import './App.css'

function App() {
  const [messages, setMessages] = useState([])
  const [input, setInput] = useState('')
  const [loading, setLoading] = useState(false)
  const messagesEndRef = useRef(null)

  const scrollToBottom = () => {
    messagesEndRef.current?.scrollIntoView({ behavior: 'smooth' })
  }

  useEffect(() => {
    scrollToBottom()
  }, [messages])

  const sendMessage = async (e) => {
    e.preventDefault()
    if (!input.trim() || loading) return

    const userMessage = { role: 'user', content: input }
    setMessages(prev => [...prev, userMessage])
    setInput('')
    setLoading(true)

    try {
      const response = await fetch('http://localhost:8000/chat', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ message: input })
      })

      const data = await response.json()
      const botMessage = { role: 'assistant', content: data.response }
      setMessages(prev => [...prev, botMessage])
    } catch (error) {
      const errorMessage = { role: 'assistant', content: '❌ שגיאה בתקשורת עם השרת' }
      setMessages(prev => [...prev, errorMessage])
    } finally {
      setLoading(false)
    }
  }

  return (
    <div className="chat-container">
      <div className="chat-header">
        <h1>🤖 מנהל המשימות שלי</h1>
        <p>ספרי לי מה את צריכה לעשות, ואני אדאג לשאר</p>
      </div>

      <div className="messages">
        {messages.length === 0 && (
          <div className="welcome">
            <h2>👋 שלום!</h2>
            <p>אני כאן כדי לעזור לך לנהל את המשימות שלך</p>
            <div className="examples">
              <p>דוגמאות למה את יכולה לבקש:</p>
              <ul>
                <li>"הוסיפי משימה: פגישה עם הלקוח ביום שני"</li>
                <li>"מה המשימות שלי למחר?"</li>
                <li>"הראי לי את כל המשימות"</li>
                <li>"סמני את המשימה הראשונה כהושלמה"</li>
              </ul>
            </div>
          </div>
        )}

        {messages.map((msg, idx) => (
          <div key={idx} className={`message ${msg.role}`}>
            <div className="message-content">
              {msg.content}
            </div>
          </div>
        ))}

        {loading && (
          <div className="message assistant">
            <div className="message-content loading">
              <span></span><span></span><span></span>
            </div>
          </div>
        )}

        <div ref={messagesEndRef} />
      </div>

      <form onSubmit={sendMessage} className="input-form">
        <input
          type="text"
          value={input}
          onChange={(e) => setInput(e.target.value)}
          placeholder="כתבי כאן את הבקשה שלך..."
          disabled={loading}
        />
        <button type="submit" disabled={loading || !input.trim()}>
          שלחי
        </button>
      </form>
    </div>
  )
}

export default App
