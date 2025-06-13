
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from readdocs.service.document_service import DocumentService
from readdocs.repo.document_repo import DocumentRepo
from readdocs.mapper.document_mapper import to_schema
from readdocs.domain.document import Document
from readdocs.repo.datasourcs import DataSource

router = APIRouter(prefix="/documents", tags=["Documents"])

def get_db():
    db = DataSource().get_session()
    try:
        yield db
    finally:
        DataSource().close_session(db)

@router.get("/", response_model=list[Document])
def get_documents(db: Session = Depends(get_db)):
    repo = DocumentRepo(db)
    service = DocumentService(repo)
    documents = service.list_documents()
    return [to_schema(doc) for doc in documents]

@router.post("/", response_model=Document)
def create_document(document: Document, db: Session = Depends(get_db)):
    repo = DocumentRepo(db)
    service = DocumentService(repo)
    created = service.add_document(document.dict())
    return to_schema(created)