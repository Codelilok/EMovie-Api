from json import loads
from typing import Any, Optional, List
from pydantic import BaseModel, HttpUrl, field_validator

# --- Simplified V1 Parts (Included here so you don't need the V1 folder) ---

class ContentImageModel(BaseModel):
    poster: Optional[str] = None
    background: Optional[str] = None

class ResourceModel(BaseModel):
    """Contains the stream/download links"""
    http_url: Optional[str] = None
    m3u8_url: Optional[str] = None
    trailer_url: Optional[str] = None  # Here is your trailer feature!

class MetadataModel(BaseModel):
    """Movie info like plot and year"""
    description: Optional[str] = None
    year: Optional[int] = None
    rating: Optional[str] = None

# --- V2 Specific Models ---

class OPS(BaseModel):
    trace_id: str
    search_abt: str
    q: str

class SearchResultsItem(BaseModel):
    """This is a single Movie or TV Show result"""
    id: str
    title: str
    postTitle: str
    detailPath: str
    poster: Optional[str] = None
    subtitles: Optional[List[str]] = None
    season: Optional[int] = 0
    imdbRatingCount: Optional[int] = None

    @field_validator("subtitles", mode="before")
    def validate_subtitles(cls, value: str) -> list[str]:
        if not value:
            return []
        return value.split(",") if isinstance(value, str) else value

    @property
    def download_page_url(self) -> str:
        """The internal link used to get the download file"""
        return f"https://aoneroom.com{self.detailPath}"

class SearchResultsModel(BaseModel):
    """The full list of search results"""
    items: List[SearchResultsItem]

class SpecificItemDetailsModel(BaseModel):
    """The final data for a movie, including the download link and trailer"""
    subject: SearchResultsItem
    resource: ResourceModel
    metadata: MetadataModel
