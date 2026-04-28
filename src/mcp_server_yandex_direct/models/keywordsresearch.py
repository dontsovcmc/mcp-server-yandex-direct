"""Pydantic models for KeywordsResearch service."""

from .common import YDBase


class DeduplicateParams(YDBase):
    Keywords: list[str]


class DeduplicateResultItem(YDBase):
    Keyword: str | None = None
    Deduplicated: str | None = None


class DeduplicateResult(YDBase):
    DeduplicateResults: list[DeduplicateResultItem] | None = None


class HasSearchVolumeItem(YDBase):
    Keyword: str
    RegionIds: list[int] | None = None


class HasSearchVolumeParams(YDBase):
    Keywords: list[HasSearchVolumeItem]


class HasSearchVolumeResultItem(YDBase):
    Keyword: str | None = None
    HasSearchVolume: str | None = None


class HasSearchVolumeResult(YDBase):
    HasSearchVolumeResults: list[HasSearchVolumeResultItem] | None = None
