# file upload
# get file list
# get metadata

# f
from typing import Optional, List
from readdocs.domain.common import PublicRequest
from typing import List
from readdocs.domain.document import Document



class DocumentUploadRequest(PublicRequest):
    file: bytes
    file_name: str
    user_id: str
    business_id: Optional[str] = None
    metadata: Optional[dict] = None

class DocumentUploadResponse(PublicRequest):
    document_id: str
    document_url: str
    message: str = "Upload successful"


class GetFileListRequest(PublicRequest):
    user_id: str
    business_id: Optional[str] = None

class GetFileListResponse(PublicRequest):
    documents: List[Document]