from typing import List

from pydantic import BaseModel, Field


class Section(BaseModel):
    id: int = Field(..., description="The unique identifier for the section")
    name: str = Field(..., description="The original topic name")
    article: str = Field(..., description="The Markdown article content")


class Article(BaseModel):
    sections: List[Section] = Field(
        ..., description="A list of sections in the article"
    )
