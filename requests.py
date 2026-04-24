import httpx
from typing import Optional

# These are the magic headers that make v2 work globally
DEFAULT_HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Platform": "pc",
    "Referer": "https://moviebox.ph",
    "Accept": "application/json, text/plain, */*",
    "Origin": "https://moviebox.ph"
}

class Session:
    """The 'Handshake' Engine for your Hosted API"""
    
    def __init__(self, proxy: Optional[str] = None):
        self.headers = DEFAULT_HEADERS
        self.proxy = proxy
        # We use httpx.AsyncClient for high-speed hosted performance
        self.client = httpx.AsyncClient(
            headers=self.headers,
            proxy=self.proxy,
            timeout=30.0,
            follow_redirects=True
        )

    async def get(self, url: str, params: Optional[dict] = None):
        """Standard GET request for searching and getting links"""
        response = await self.client.get(url, params=params)
        response.raise_for_status()  # This alerts you if the site is down
        return response.json()

    async def close(self):
        """Closes the connection when done"""
        await self.client.aclose()
EOFcat << 'EOF' > requests.py
import httpx
from typing import Optional

# These are the magic headers that make v2 work globally
DEFAULT_HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Platform": "pc",
    "Referer": "https://moviebox.ph",
    "Accept": "application/json, text/plain, */*",
    "Origin": "https://moviebox.ph"
}

class Session:
    """The 'Handshake' Engine for your Hosted API"""
    
    def __init__(self, proxy: Optional[str] = None):
        self.headers = DEFAULT_HEADERS
        self.proxy = proxy
        # We use httpx.AsyncClient for high-speed hosted performance
        self.client = httpx.AsyncClient(
            headers=self.headers,
            proxy=self.proxy,
            timeout=30.0,
            follow_redirects=True
        )

    async def get(self, url: str, params: Optional[dict] = None):
        """Standard GET request for searching and getting links"""
        response = await self.client.get(url, params=params)
        response.raise_for_status()  # This alerts you if the site is down
        return response.json()

    async def close(self):
        """Closes the connection when done"""
        await self.client.aclose()
