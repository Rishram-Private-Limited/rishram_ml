def extract_confidence_score(response):
    try:
        text = response.text.strip()
        
        # Look for patterns like "score: 85" or "85%" or "confidence: 85"
        import re
        matches = re.search(r'(\d{1,3})(?:\s*%|\s*confidence|\s*score)', text, re.IGNORECASE)
        
        if matches:
            score = int(matches.group(1))
        else:
            # Fallback: extract first number found
            matches = re.search(r'\b(\d{1,3})\b', text)
            if matches:
                score = int(matches.group(1))
            else:
                # Last resort: extract all digits (original method)
                score = int("".join(filter(str.isdigit, text)))
        
        return min(max(score, 0), 100)
    except Exception as e:
        print(f"Error extracting confidence score: {e}")
        return "Unknown"