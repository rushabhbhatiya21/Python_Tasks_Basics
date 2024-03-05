import re


def is_valid_url(url):
    url_pattern = re.compile(
        r'^(https?|ftp)://'  # Protocol (http, https, or ftp)
        r'([a-zA-Z0-9.-]+)'  # Domain (can include letters, numbers, dots, and hyphens)
        r'(\.[a-zA-Z]{2,})'  # Top-level domain (at least two letters)
        r'(:\d+)?'  # Optional port number
        r'(/[^#\s]*)?'  # Optional path
        r'(#[^\s]*)?$'  # Optional fragment identifier (hash)
    )
    return bool(re.match(url_pattern, url))


url_to_check = "https://www.example.com/path/page?query=value#fragment"
if is_valid_url(url_to_check):
    print("The URL is valid.")
else:
    print("The URL is not valid.")
