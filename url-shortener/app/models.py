from datetime import datetime

class URLStore:
    def __init__(self):
        self.data = {}

    def add(self, short_code, url):
        # Fix: use datetime.utcnow().isoformat() for correct timestamp
        from datetime import datetime
        self.data[short_code] = {
            "url": url,
            "clicks": 0,
            "created_at": datetime.utcnow().isoformat()
        }

    def get(self, short_code):
        return self.data.get(short_code)

    def increment_click(self, short_code):
        if short_code in self.data:
            self.data[short_code]["clicks"] += 1

    def exists(self, short_code):
        return short_code in self.data

    def find_by_url(self, url):
        for code, info in self.data.items():
            if info["url"] == url:
                return code
        return None

store = URLStore()