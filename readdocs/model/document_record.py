from sqlalchemy import Column, String, DateTime, JSON, func
from readdocs.repo.datasourcs import Base

class Document(Base):
    __tablename__ = "document"

    document_id = Column(String, primary_key=True, index=True)
    document_name = Column(String, nullable=True)
    document_url = Column(String, nullable=False)
    user_id = Column(String, nullable=False)
    business_id = Column(String, nullable=True)
    meta_data = Column(JSON, nullable=True)  # Renamed from 'metadata'
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now())