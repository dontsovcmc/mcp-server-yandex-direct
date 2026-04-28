"""Pydantic models for RetargetingLists service."""

from .common import YDBase, IdsCriteria, LimitOffset, ActionResult


class RetargetingListsSelectionCriteria(YDBase):
    Ids: list[int] | None = None


class RetargetingListsGetParams(YDBase):
    SelectionCriteria: RetargetingListsSelectionCriteria
    FieldNames: list[str]
    Page: LimitOffset | None = None


class RetargetingListGetItem(YDBase):
    Id: int | None = None
    Name: str | None = None
    Description: str | None = None
    IsAvailable: str | None = None
    Rules: list[dict] | None = None


class RetargetingListsGetResult(YDBase):
    RetargetingLists: list[RetargetingListGetItem] | None = None
    LimitedBy: int | None = None


class RetargetingListAddItem(YDBase):
    Name: str
    Description: str | None = None
    Rules: list[dict]


class RetargetingListsAddParams(YDBase):
    RetargetingLists: list[RetargetingListAddItem]


class RetargetingListsAddResult(YDBase):
    AddResults: list[ActionResult]


class RetargetingListUpdateItem(YDBase):
    Id: int
    Name: str | None = None
    Description: str | None = None
    Rules: list[dict] | None = None


class RetargetingListsUpdateParams(YDBase):
    RetargetingLists: list[RetargetingListUpdateItem]


class RetargetingListsUpdateResult(YDBase):
    UpdateResults: list[ActionResult]


class RetargetingListsDeleteParams(YDBase):
    SelectionCriteria: IdsCriteria


class RetargetingListsDeleteResult(YDBase):
    DeleteResults: list[ActionResult]
