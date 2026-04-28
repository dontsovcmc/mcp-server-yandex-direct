"""Pydantic models for Dictionaries service."""

from .common import YDBase


class DictionariesGetParams(YDBase):
    DictionaryNames: list[str]


class DictionariesGetResult(YDBase):
    GeoRegions: list[dict] | None = None
    Currencies: list[dict] | None = None
    MetroStations: list[dict] | None = None
    TimeZones: list[dict] | None = None
    Constants: dict | None = None
    AdCategories: list[dict] | None = None
    OperationSystemVersions: list[dict] | None = None
    ProductivityAssertions: list[dict] | None = None
    SupplySidePlatforms: list[dict] | None = None
    Interests: list[dict] | None = None
    AudienceCriteriaTypes: list[dict] | None = None
    AudienceDemographicProfiles: list[dict] | None = None
    FilterSchemas: list[dict] | None = None
