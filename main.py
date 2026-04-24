from fastapi import FastAPI, HTTPException
from core import MovieBoxV2Engine
import uvicorn

app = FastAPI(
    title="ECOWSCO MOVIES API",
    description="""
    ## A blazing-fast REST API to search, discover, and stream movies & TV series. 
    Full CORS support with no API key required.
    
    ### API Endpoints
    Complete reference for all available endpoints grouped by function. 
    Click any endpoint below to expand details and test the live response.
    """,
    version="2.0.0",
    openapi_tags=[
        {"name": "Discovery", "description": "Endpoints for homepage, trending content, and banners."},
        {"name": "Search Tools", "description": "Smart search and real-time auto-complete suggestions."},
        {"name": "Streaming & Downloads", "description": "Extract direct MP4 links, trailers, cast, and ratings."},
    ]
)

engine = MovieBoxV2Engine()

@app.get("/", include_in_schema=False)
def root():
    return {
        "message": "ECOWSCO MOVIES API is Live!", 
        "status": "Online",
        "documentation": "/docs",
        "base_endpoint": "/api"
    }

# --- DISCOVERY GROUP ---

@app.get("/api/homepage", tags=["Discovery"], summary="Get Trending & Banners")
async def get_home():
    try:
        return await engine.get_homepage()
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/api/category/{cat_id}", tags=["Discovery"], summary="Browse by Genre")
async def get_genre(cat_id: str, page: int = 1):
    try:
        return await engine.get_category(cat_id, page)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# --- SEARCH TOOLS GROUP ---

@app.get("/api/search", tags=["Search Tools"], summary="Full Database Search")
async def search_movie(q: str):
    try:
        return await engine.search(q)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/api/suggestions", tags=["Search Tools"], summary="Auto-complete Suggestions")
async def search_suggestions(q: str):
    try:
        return await engine.get_suggestions(q)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# --- STREAMING & DOWNLOADS GROUP ---

@app.get("/api/details", tags=["Streaming & Downloads"], summary="Get Play Links, Cast & Ranking")
async def get_movie_details(path: str):
    try:
        details = await engine.get_details(path)
        return {
            "title": details.subject.title,
            "rating": details.subject.imdbRatingCount,
            # ⚠️ you used details.stars but it's not in your model
            # so this may break unless you add it in models.py
            "download_url": details.resource.http_url,
            "trailer_url": details.resource.trailer_url,
            "description": details.metadata.description,
            "subtitles": details.subject.subtitles
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/api/related", tags=["Streaming & Downloads"], summary="More Like This")
async def get_related(path: str):
    try:
        details_raw = await engine.get_details(path)
        return details_raw.get("postList", [])
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
