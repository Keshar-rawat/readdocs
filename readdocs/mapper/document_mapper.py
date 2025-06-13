
from readdocs.model.document_record import Document
from readdocs.domain.document import Document

def to_schema(document: Document) -> Document:
    return Document.from_orm(document)