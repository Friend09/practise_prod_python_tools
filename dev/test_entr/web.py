def valid_url(url: str) -> bool:
    if not url.startswith("https://"):
        if not url.startswith("http://"):
            return False

    return True
