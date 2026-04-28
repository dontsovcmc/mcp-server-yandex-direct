"""Pydantic models for Sitelinks service."""

from .common import YDBase, IdsCriteria, LimitOffset, ActionResult


class SitelinksSelectionCriteria(YDBase):
    Ids: list[int] | None = None


class SitelinksGetParams(YDBase):
    SelectionCriteria: SitelinksSelectionCriteria
    FieldNames: list[str]
    Page: LimitOffset | None = None


class SitelinkItem(YDBase):
    Title: str | None = None
    Href: str | None = None
    Description: str | None = None
    TurboPageId: int | None = None


class SitelinksSetGetItem(YDBase):
    Id: int | None = None
    Sitelinks: list[SitelinkItem] | None = None


class SitelinksGetResult(YDBase):
    SitelinksSets: list[SitelinksSetGetItem] | None = None
    LimitedBy: int | None = None


class SitelinksSetAddItem(YDBase):
    Sitelinks: list[SitelinkItem]


class SitelinksAddParams(YDBase):
    SitelinksSets: list[SitelinksSetAddItem]


class SitelinksAddResult(YDBase):
    AddResults: list[ActionResult]


class SitelinksDeleteParams(YDBase):
    SelectionCriteria: IdsCriteria


class SitelinksDeleteResult(YDBase):
    DeleteResults: list[ActionResult]
