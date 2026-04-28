"""Pydantic models for AdExtensions service."""

from .common import YDBase, IdsCriteria, LimitOffset, ActionResult


class AdExtensionsSelectionCriteria(YDBase):
    Ids: list[int] | None = None
    Types: list[str] | None = None
    States: list[str] | None = None
    Statuses: list[str] | None = None
    ModifiedSince: str | None = None


class AdExtensionsGetParams(YDBase):
    SelectionCriteria: AdExtensionsSelectionCriteria
    FieldNames: list[str]
    CalloutFieldNames: list[str] | None = None
    Page: LimitOffset | None = None


class AdExtensionGetItem(YDBase):
    Id: int | None = None
    Type: str | None = None
    Status: str | None = None
    State: str | None = None
    StatusClarification: str | None = None
    Associated: str | None = None
    Callout: dict | None = None


class AdExtensionsGetResult(YDBase):
    AdExtensions: list[AdExtensionGetItem] | None = None
    LimitedBy: int | None = None


class AdExtensionAddItem(YDBase):
    Callout: dict | None = None


class AdExtensionsAddParams(YDBase):
    AdExtensions: list[AdExtensionAddItem]


class AdExtensionsAddResult(YDBase):
    AddResults: list[ActionResult]


class AdExtensionsDeleteParams(YDBase):
    SelectionCriteria: IdsCriteria


class AdExtensionsDeleteResult(YDBase):
    DeleteResults: list[ActionResult]
