from fastapi import APIRouter
from app.detector import ai_text_detector
from pydantic import BaseModel
from app.remover import remove_ai_content

router = APIRouter()

@router.post("/detect/")
async def detect_text(data: dict):
    paragraph = data.get("text", "")
    result = ai_text_detector(paragraph)
    return {"results": result}

class TextInput(BaseModel):
    text: str

@router.post("/remove-ai-content")
def remove_ai_text(data: TextInput):
    cleaned_text = remove_ai_content(data.text)
    return {"cleaned_text": cleaned_text}