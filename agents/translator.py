# agents/translator.py
from deep_translator import GoogleTranslator
from config import DEFAULT_LANGUAGE

def translate(text: str, source: str = "auto", target: str = DEFAULT_LANGUAGE) -> str:
    """
    Translates text from source to target language using GoogleTranslator.
    
    Parameters:
    - text: str — text to translate
    - source: str — source language (default: auto-detect)
    - target: str — target language (default from config)

    Returns:
    - Translated string or error message
    """
    try:
        return GoogleTranslator(source=source, target=target).translate(text)
    except Exception as e:
        return f"❌ Translation failed: {str(e)}"
