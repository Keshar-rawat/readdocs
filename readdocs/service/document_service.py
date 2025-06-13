
from readdocs.repo.document_repo import DocumentRepo
from readdocs.model.document_record import Document

class DocumentService:
    def __init__(self, repo: DocumentRepo):
        self.repo = repo

    def list_documents(self):
        return self.repo.get_all()

    def add_document(self, document_data):
        document = Document(**document_data)
        return self.repo.create(document)