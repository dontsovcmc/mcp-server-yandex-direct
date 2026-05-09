"""Pydantic models for KeywordsResearch service."""

from pydantic import Field

from .common import YDBase


class DeduplicateParams(YDBase):
    Keywords: list[str] = Field(description="Keywords to deduplicate")


class DeduplicateResultItem(YDBase):
    Keyword: str | None = Field(default=None, description="Original keyword")
    Deduplicated: str | None = Field(default=None, description="Deduplicated keyword or None if it is a duplicate")


class DeduplicateResult(YDBase):
    DeduplicateResults: list[DeduplicateResultItem] | None = Field(default=None, description="Deduplication results")


class HasSearchVolumeItem(YDBase):
    Keyword: str = Field(description="Keyword to check search volume for")
    RegionIds: list[int] | None = Field(default=None, description="Region IDs to check search volume in")


class HasSearchVolumeParams(YDBase):
    Keywords: list[HasSearchVolumeItem] = Field(description="Keywords to check for search volume")


class HasSearchVolumeResultItem(YDBase):
    Keyword: str | None = Field(default=None, description="Checked keyword")
    HasSearchVolume: str | None = Field(default=None, description="Whether the keyword has search volume (YES or NO)")


class HasSearchVolumeResult(YDBase):
    HasSearchVolumeResults: list[HasSearchVolumeResultItem] | None = Field(default=None, description="Search volume check results")
