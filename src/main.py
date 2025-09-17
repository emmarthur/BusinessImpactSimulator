
from fastapi import FastAPI, Body
from fastapi.middleware.cors import CORSMiddleware
from fastapi import UploadFile, File
from core.domain_classifier import DomainClassifier
import json

app = FastAPI()
origins = ["http://localhost:5173"]

# Initialize the domain classifier
domain_classifier = DomainClassifier()

@app.get("/")
def read_root():
    return {"message": "Business Impact Simulator API is running!"}

@app.post("/api/process-project")
def get_description(description:str = Body(..., embed = True)):
    return {"description": "hello to you too programmer: "+description}
@app.post("/api/process-project-file")
async def get_file(file: UploadFile = File(...)):
    content = await file.read()
    return {"filename": file.filename, "content_type": file.content_type, "content": content.decode()}
app.add_middleware(
    CORSMiddleware,
    allow_origins = ["http://localhost:5173"],
    allow_methods=["*"],
    allow_headers=["*"],
)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8001)