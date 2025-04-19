import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate

load_dotenv()


def get_llm():
    return ChatGoogleGenerativeAI(
        model="models/gemini-1.5-pro", 
        google_api_key=os.getenv("GEMINI_API_KEY"),
        temperature=0.7,
    )

def remove_ai_content(text: str) -> str:
    if not text or not text.strip():
        return "Error: No text provided."
    
    prompt_template = PromptTemplate(
    input_variables=["text"],
    template="""
You are an expert at rewriting content to sound naturally human-written.
Rewrite the following text to maintain its meaning while:
- Using more varied sentence structures
- Avoiding overly formal or robotic language
- Make grammatical errors that a human might make
- Write it like a human , it cannot be detected by AI detectors
- Adding natural human inconsistencies in style
- Incorporating occasional informality where appropriate
- Varying vocabulary choices
- Avoiding repetitive phrases or structures

Original Text:
{text}

Rewritten Human-like Version:
"""
)

    try:
        llm = get_llm()
        chain = LLMChain(llm=llm, prompt=prompt_template)
        
        result = chain.run({"text": text})
        return result.strip()
    except Exception as e:
        error_message = f"Error processing text: {str(e)}"
        print(error_message) 
        return f"Failed to process text: {str(e)}"
