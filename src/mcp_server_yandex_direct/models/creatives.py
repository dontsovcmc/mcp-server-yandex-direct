"""Pydantic models for Creatives service."""

from pydantic import Field

from .common import YDBase, LimitOffset, ActionResult


class CreativesSelectionCriteria(YDBase):
    Ids: list[int] | None = Field(default=None, description="Creative IDs to filter by")
    Types: list[str] | None = Field(default=None, description="Creative types to filter by")


class CreativesGetParams(YDBase):
    SelectionCriteria: CreativesSelectionCriteria = Field(description="Criteria for selecting creatives")
    FieldNames: list[str] = Field(description="Names of fields to return")
    Page: LimitOffset | None = Field(default=None, description="Pagination settings")


class CreativeGetItem(YDBase):
    Id: int | None = Field(default=None, description="Creative ID")
    Type: str | None = Field(default=None, description="Creative type")
    Name: str | None = Field(default=None, description="Creative name")
    PreviewUrl: str | None = Field(default=None, description="URL for the creative preview")
    ThumbnailUrl: str | None = Field(default=None, description="URL for the creative thumbnail")
    Width: int | None = Field(default=None, description="Creative width in pixels")
    Height: int | None = Field(default=None, description="Creative height in pixels")


class CreativesGetResult(YDBase):
    Creatives: list[CreativeGetItem] | None = Field(default=None, description="List of creatives")
    LimitedBy: int | None = Field(default=None, description="Offset for the next page if results are truncated")


class CreativeAddItem(YDBase):
    VideoExtensionCreative: dict | None = Field(default=None, description="Video extension creative parameters")
    CpcVideoCreative: dict | None = Field(default=None, description="CPC video creative parameters")
    CpmVideoCreative: dict | None = Field(default=None, description="CPM video creative parameters")
    CanvasCreative: dict | None = Field(default=None, description="Canvas creative parameters")
    HtmlVideoCreative: dict | None = Field(default=None, description="HTML5 video creative parameters")


class CreativesAddParams(YDBase):
    Creatives: list[CreativeAddItem] = Field(description="Creatives to add")


class CreativesAddResult(YDBase):
    AddResults: list[ActionResult] = Field(description="Results of the add operation")
