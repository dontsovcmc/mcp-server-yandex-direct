"""Pydantic models for TurboPages service."""

from pydantic import Field

from .common import YDBase, LimitOffset


class TurboPagesSelectionCriteria(YDBase):
    Ids: list[int] | None = Field(default=None, description="Turbo page IDs to filter by")


class TurboPagesGetParams(YDBase):
    SelectionCriteria: TurboPagesSelectionCriteria = Field(description="Criteria for selecting turbo pages")
    FieldNames: list[str] = Field(description="Names of fields to return")
    Page: LimitOffset | None = Field(default=None, description="Pagination settings")


class TurboPageGetItem(YDBase):
    Id: int | None = Field(default=None, description="Turbo page ID")
    Name: str | None = Field(default=None, description="Turbo page name")
    Href: str | None = Field(default=None, description="Turbo page URL")


class TurboPagesGetResult(YDBase):
    TurboPages: list[TurboPageGetItem] | None = Field(default=None, description="List of turbo pages")
    LimitedBy: int | None = Field(default=None, description="Offset for the next page if results are truncated")
