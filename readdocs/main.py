from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.responses import JSONResponse
from PyPDF2 import PdfReader
import io

app = FastAPI(title="File Reader API")

@app.post("/read-file/")
async def read_file(file: UploadFile = File(...)):
    # Get file extension
    filename = file.filename
    if filename.endswith(".txt"):
        contents = await file.read()
        text = contents.decode("utf-8")
    elif filename.endswith(".pdf"):
        pdf_reader = PdfReader(io.BytesIO(await file.read()))
        text = ""
        for page in pdf_reader.pages:
            text += page.extract_text() or ""
    else:
        raise HTTPException(status_code=400, detail="Only .txt and .pdf files are supported")

    return JSONResponse(content={"filename": filename, "content": text})
