
import { Message } from "@/types/chat";
import { format } from "date-fns";

interface ChatMessageProps {
  message: Message;
  animate?: boolean;
}

export function ChatMessage({ message, animate = true }: ChatMessageProps) {
  return (
    <div 
      className={`message message-${message.role}`}
      style={{ 
        animationDelay: animate ? `${Math.random() * 0.3}s` : '0s',
      }}
    >
      <div className="message-bubble">
        {message.content}
      </div>
      <time className="message-time">
        {format(message.timestamp, 'HH:mm')}
      </time>
    </div>
  );
}
