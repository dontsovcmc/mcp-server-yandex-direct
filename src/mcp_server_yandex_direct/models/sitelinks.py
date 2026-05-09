"""Pydantic models for Sitelinks service."""

from pydantic import Field

from .common import YDBase, IdsCriteria, LimitOffset, ActionResult


class SitelinksSelectionCriteria(YDBase):
    Ids: list[int] | None = Field(default=None, description="Filter by sitelinks set IDs")


class SitelinksGetParams(YDBase):
    SelectionCriteria: SitelinksSelectionCriteria = Field(description="Criteria for selecting sitelinks sets")
    FieldNames: list[str] = Field(description="Sitelinks set field names to return")
    Page: LimitOffset | None = Field(default=None, description="Pagination settings")


class SitelinkItem(YDBase):
    Title: str | None = Field(default=None, description="Sitelink title text")
    Href: str | None = Field(default=None, description="Sitelink URL")
    Description: str | None = Field(default=None, description="Sitelink description text")
    TurboPageId: int | None = Field(default=None, description="Turbo page ID for the sitelink")


class SitelinksSetGetItem(YDBase):
    Id: int | None = Field(default=None, description="Sitelinks set ID")
    Sitelinks: list[SitelinkItem] | None = Field(default=None, description="List of sitelinks in the set")


class SitelinksGetResult(YDBase):
    SitelinksSets: list[SitelinksSetGetItem] | None = Field(default=None, description="List of sitelinks sets matching the criteria")
    LimitedBy: int | None = Field(default=None, description="Indicates next page offset if results were truncated")


class SitelinksSetAddItem(YDBase):
    Sitelinks: list[SitelinkItem] = Field(description="List of sitelinks in the set")


class SitelinksAddParams(YDBase):
    SitelinksSets: list[SitelinksSetAddItem] = Field(description="List of sitelinks sets to add")


class SitelinksAddResult(YDBase):
    AddResults: list[ActionResult] = Field(description="Results of add operations")


class SitelinksDeleteParams(YDBase):
    SelectionCriteria: IdsCriteria = Field(description="IDs of sitelinks sets to delete")


class SitelinksDeleteResult(YDBase):
    DeleteResults: list[ActionResult] = Field(description="Results of delete operations")
