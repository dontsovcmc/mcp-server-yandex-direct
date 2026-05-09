"""Pydantic models for AdExtensions service."""

from pydantic import Field

from .common import YDBase, IdsCriteria, LimitOffset, ActionResult


class AdExtensionsSelectionCriteria(YDBase):
    Ids: list[int] | None = Field(default=None, description="Filter by ad extension IDs")
    Types: list[str] | None = Field(default=None, description="Filter by ad extension types")
    States: list[str] | None = Field(default=None, description="Filter by ad extension states")
    Statuses: list[str] | None = Field(default=None, description="Filter by moderation statuses")
    ModifiedSince: str | None = Field(default=None, description="Return extensions modified after this timestamp")


class AdExtensionsGetParams(YDBase):
    SelectionCriteria: AdExtensionsSelectionCriteria = Field(description="Criteria for selecting ad extensions")
    FieldNames: list[str] = Field(description="Ad extension field names to return")
    CalloutFieldNames: list[str] | None = Field(default=None, description="Fields to return for callout extensions")
    Page: LimitOffset | None = Field(default=None, description="Pagination settings")


class AdExtensionGetItem(YDBase):
    Id: int | None = Field(default=None, description="Ad extension ID")
    Type: str | None = Field(default=None, description="Ad extension type")
    Status: str | None = Field(default=None, description="Moderation status")
    State: str | None = Field(default=None, description="Ad extension state")
    StatusClarification: str | None = Field(default=None, description="Reason for rejection or other status clarification")
    Associated: str | None = Field(default=None, description="Whether the extension is associated with an ad (YES or NO)")
    Callout: dict | None = Field(default=None, description="Callout extension parameters")


class AdExtensionsGetResult(YDBase):
    AdExtensions: list[AdExtensionGetItem] | None = Field(default=None, description="List of ad extensions matching the criteria")
    LimitedBy: int | None = Field(default=None, description="Indicates next page offset if results were truncated")


class AdExtensionAddItem(YDBase):
    Callout: dict | None = Field(default=None, description="Callout extension parameters")


class AdExtensionsAddParams(YDBase):
    AdExtensions: list[AdExtensionAddItem] = Field(description="List of ad extensions to add")


class AdExtensionsAddResult(YDBase):
    AddResults: list[ActionResult] = Field(description="Results of add operations")


class AdExtensionsDeleteParams(YDBase):
    SelectionCriteria: IdsCriteria = Field(description="IDs of ad extensions to delete")


class AdExtensionsDeleteResult(YDBase):
    DeleteResults: list[ActionResult] = Field(description="Results of delete operations")
