
export function TypingIndicator() {
  return (
    <div className="message message-assistant" style={{ animationDelay: '0s' }}>
      <div className="typing-indicator">
        <span className="typing-dot" style={{ animationDelay: '0s' }} />
        <span className="typing-dot" style={{ animationDelay: '0.2s' }} />
        <span className="typing-dot" style={{ animationDelay: '0.4s' }} />
      </div>
    </div>
  );
}
