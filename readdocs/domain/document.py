from datetime import datetime
from typing import Optional
from pydantic import BaseModel

class Document(BaseModel):
    document_id: str
    document_name: Optional[str] = None
    document_url: str
    user_id: str
    business_id: Optional[str] = None
    meta_data: Optional[dict] = None  # Match SQLAlchemy model
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

    class Config:
        orm_mode = True