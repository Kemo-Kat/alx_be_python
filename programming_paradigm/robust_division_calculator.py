def safe_divide(numerator, denominator):
    """
    Safely divides two numbers with comprehensive error handling.
    
    Args:
        numerator: The numerator as a string
        denominator: The denominator as a string
        
    Returns:
        str: The result of division or appropriate error message
    """
    try:
        # Attempt to convert inputs to floats
        num = float(numerator)
        den = float(denominator)
    except ValueError:
        return "Error: Please enter numeric values only."
    
    try:
        # Attempt division
        result = num / den
        return str(result)
    except ZeroDivisionError:
        return "Error: Cannot divide by zero."
