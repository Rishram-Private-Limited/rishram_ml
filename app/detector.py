import google.generativeai as genai
import spacy
from app.utils import extract_confidence_score
import config

nlp = spacy.load("en_core_web_sm")

genai.configure(api_key=config.GEMINI_API_KEY)

def ai_text_detector(paragraph):
    
    doc = nlp(paragraph)
    sentences = [sent.text for sent in doc.sents]
    
   
    model = genai.GenerativeModel('models/gemini-1.5-pro')
    
    results = []

    for sentence in sentences:
        prompt = f"Detect if this sentence is AI-generated. Give a confidence score (0-100): {sentence}"

        try:
            
            response = model.generate_content(prompt)
            print(f"API response: {response.text}")
            confidence_score = extract_confidence_score(response)
            results.append({"sentence": sentence, "ai_confidence": confidence_score})
        except Exception as e:
            print(f"Error processing sentence: {str(e)}")
            results.append({"sentence": sentence, "ai_confidence": f"Error: {str(e)}"})
    
    return results