import re

def is_strong_password(password):
    # Check for minimum length of 8 characters
    if len(password) < 8:
        return False
    
    # Check for the presence of both uppercase and lowercase characters
    if not re.search("[a-z]", password) or not re.search("[A-Z]", password):
        return False
    
    # Check for at least one digit
    if not re.search("\d", password):
        return False
    
    # If all conditions are met
    return True

# Example usage
password = "example1"
print(is_strong_password(password))  # This should return True if the password meets the criteria
