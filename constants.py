import os

# 1. The Secret Servers
# These are the backend addresses for MovieBox v2
MIRROR_HOSTS = ("h5-api.aoneroom.com",)

# This allows you to change the host easily later if one goes down
SELECTED_HOST = os.getenv("MOVIEBOX_API_HOST_V2") or MIRROR_HOSTS[0]
BASE_URL = f"https://{SELECTED_HOST}"

# 2. Subject Types (The "Categories")
# We define these here so we don't need the v1 folder
class SubjectType:
    MOVIES = "movies"
    TV_SERIES = "tv"
    ANIME = "anime"
    MUSIC = "music"
    EDUCATION = "education"

# This list helps your code know which items are "Single" (like a movie) 
# versus "Multiple" (like a TV series with episodes)
SINGLE_ITEM_SUBJECT_TYPES = {
    SubjectType.MUSIC,
    SubjectType.MOVIES,
    SubjectType.ANIME,
    SubjectType.EDUCATION,
}

# 3. The "Bypass" Headers
# These trick the server into thinking you are a real user on a PC
REFERER = "https://moviebox.ph"

DEFAULT_REQUEST_HEADERS = {
    "Platform": "pc",
    "Accept": "application/json",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Referer": REFERER,
    "Origin": "https://moviebox.ph"
}
