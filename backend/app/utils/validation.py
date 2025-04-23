# backend/app/utils/validation.py
def validate_query(text: str) -> bool:
    """
    Validates a query string.
    
    Args:
        text: The query string to validate.
    
    Returns:
        True if valid, False otherwise.
    """
    return bool(text and text.strip())