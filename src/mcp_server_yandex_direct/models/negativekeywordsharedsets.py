"""Pydantic models for NegativeKeywordSharedSets service."""

from .common import YDBase, IdsCriteria, LimitOffset, ActionResult


class NegativeKeywordSharedSetsSelectionCriteria(YDBase):
    Ids: list[int] | None = None


class NegativeKeywordSharedSetsGetParams(YDBase):
    SelectionCriteria: NegativeKeywordSharedSetsSelectionCriteria
    FieldNames: list[str]
    Page: LimitOffset | None = None


class NegativeKeywordSharedSetGetItem(YDBase):
    Id: int | None = None
    Name: str | None = None
    NegativeKeywords: list[str] | None = None


class NegativeKeywordSharedSetsGetResult(YDBase):
    NegativeKeywordSharedSets: list[NegativeKeywordSharedSetGetItem] | None = None
    LimitedBy: int | None = None


class NegativeKeywordSharedSetAddItem(YDBase):
    Name: str
    NegativeKeywords: list[str]


class NegativeKeywordSharedSetsAddParams(YDBase):
    NegativeKeywordSharedSets: list[NegativeKeywordSharedSetAddItem]


class NegativeKeywordSharedSetsAddResult(YDBase):
    AddResults: list[ActionResult]


class NegativeKeywordSharedSetUpdateItem(YDBase):
    Id: int
    Name: str | None = None
    NegativeKeywords: list[str] | None = None


class NegativeKeywordSharedSetsUpdateParams(YDBase):
    NegativeKeywordSharedSets: list[NegativeKeywordSharedSetUpdateItem]


class NegativeKeywordSharedSetsUpdateResult(YDBase):
    UpdateResults: list[ActionResult]


class NegativeKeywordSharedSetsDeleteParams(YDBase):
    SelectionCriteria: IdsCriteria


class NegativeKeywordSharedSetsDeleteResult(YDBase):
    DeleteResults: list[ActionResult]
