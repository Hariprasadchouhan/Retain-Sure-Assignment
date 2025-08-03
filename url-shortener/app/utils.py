import random
import string
import re

def generate_short_code(length=6):
    """Generate a random alphanumeric short code of given length."""
    chars = string.ascii_letters + string.digits
    return ''.join(random.choices(chars, k=length))

def is_valid_url(url):
    """Basic URL validation."""
    # Simple regex for http(s) URLs
    pattern = re.compile(
        r'^(https?://)'  # http:// or https://
        r'([A-Za-z0-9.-]+)'  # domain
        r'(:\d+)?'  # optional port
        r'(/.*)?$'  # path
    )
    return bool(pattern.match(url))