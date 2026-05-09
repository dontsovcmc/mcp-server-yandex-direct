"""Pydantic models for Dictionaries service."""

from pydantic import Field

from .common import YDBase


class DictionariesGetParams(YDBase):
    DictionaryNames: list[str] = Field(description="Names of dictionaries to retrieve")


class DictionariesGetResult(YDBase):
    GeoRegions: list[dict] | None = Field(default=None, description="Geographic regions dictionary")
    Currencies: list[dict] | None = Field(default=None, description="Currencies dictionary")
    MetroStations: list[dict] | None = Field(default=None, description="Metro stations dictionary")
    TimeZones: list[dict] | None = Field(default=None, description="Time zones dictionary")
    Constants: dict | None = Field(default=None, description="API constants dictionary")
    AdCategories: list[dict] | None = Field(default=None, description="Ad categories dictionary")
    OperationSystemVersions: list[dict] | None = Field(default=None, description="Operating system versions dictionary")
    ProductivityAssertions: list[dict] | None = Field(default=None, description="Productivity assertions dictionary")
    SupplySidePlatforms: list[dict] | None = Field(default=None, description="Supply-side platforms (SSP) dictionary")
    Interests: list[dict] | None = Field(default=None, description="User interests dictionary")
    AudienceCriteriaTypes: list[dict] | None = Field(default=None, description="Audience criteria types dictionary")
    AudienceDemographicProfiles: list[dict] | None = Field(default=None, description="Audience demographic profiles dictionary")
    FilterSchemas: list[dict] | None = Field(default=None, description="Filter schemas for dynamic ads")
