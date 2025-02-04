from sqlalchemy import Column, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from backend.database.database import Base
from datetime import datetime
import uuid

class Message(Base):
    __tablename__ = "messages"
    
    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    conversation_id = Column(String, ForeignKey('conversations.id', ondelete='CASCADE'))
    role = Column(String, nullable=False)
    content = Column(String, nullable=False)
    timestamp = Column(DateTime, default=datetime.utcnow)
    
    conversation = relationship("Conversation", backref="messages")

    @staticmethod
    def create(conversation_id, role, content):
        """Cria uma nova mensagem"""
        from backend.database.database import SessionLocal
        
        db = SessionLocal()
        try:
            message = Message(
                conversation_id=conversation_id,
                role=role,
                content=content
            )
            db.add(message)
            db.commit()
            db.refresh(message)
            return message.id
        finally:
            db.close()

    @staticmethod
    def get_by_conversation(conversation_id):
        """Retorna todas as mensagens de uma conversa"""
        from backend.database.database import SessionLocal
        
        db = SessionLocal()
        try:
            return db.query(Message)\
                .filter_by(conversation_id=conversation_id)\
                .order_by(Message.timestamp.asc())\
                .all()
        finally:
            db.close()