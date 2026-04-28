"""Pydantic models for Creatives service."""

from .common import YDBase, LimitOffset, ActionResult


class CreativesSelectionCriteria(YDBase):
    Ids: list[int] | None = None
    Types: list[str] | None = None


class CreativesGetParams(YDBase):
    SelectionCriteria: CreativesSelectionCriteria
    FieldNames: list[str]
    Page: LimitOffset | None = None


class CreativeGetItem(YDBase):
    Id: int | None = None
    Type: str | None = None
    Name: str | None = None
    PreviewUrl: str | None = None
    ThumbnailUrl: str | None = None
    Width: int | None = None
    Height: int | None = None


class CreativesGetResult(YDBase):
    Creatives: list[CreativeGetItem] | None = None
    LimitedBy: int | None = None


class CreativeAddItem(YDBase):
    VideoExtensionCreative: dict | None = None
    CpcVideoCreative: dict | None = None
    CpmVideoCreative: dict | None = None
    CanvasCreative: dict | None = None
    HtmlVideoCreative: dict | None = None


class CreativesAddParams(YDBase):
    Creatives: list[CreativeAddItem]


class CreativesAddResult(YDBase):
    AddResults: list[ActionResult]
