
import google.generativeai as genai

GOOGLE_API_KEY="AIzaSyATtqtW-xsrsW5EUKxQnAWvRdKi04hDJ0c"

def flash_model():
    """Create a flash model using Google Generative AI."""
    genai.configure(api_key=GOOGLE_API_KEY)
    return genai.GenerativeModel('gemini-1.5-flash')

genai_model = flash_model()