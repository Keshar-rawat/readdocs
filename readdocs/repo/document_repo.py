
from sqlalchemy.orm import Session
from readdocs.model.document_record import Document

class DocumentRepo:
    def __init__(self, db: Session):
        self.db = db

    def get_all(self):
        return self.db.query(Document).all()

    def create(self, document: Document):
        self.db.add(document)
        self.db.commit()
        self.db.refresh(document)
        return document