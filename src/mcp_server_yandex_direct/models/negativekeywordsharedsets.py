"""Pydantic models for NegativeKeywordSharedSets service."""

from pydantic import Field

from .common import YDBase, IdsCriteria, LimitOffset, ActionResult


class NegativeKeywordSharedSetsSelectionCriteria(YDBase):
    Ids: list[int] | None = Field(default=None, description="Shared set IDs to filter by")


class NegativeKeywordSharedSetsGetParams(YDBase):
    SelectionCriteria: NegativeKeywordSharedSetsSelectionCriteria = Field(description="Criteria for selecting shared sets")
    FieldNames: list[str] = Field(description="Names of fields to return")
    Page: LimitOffset | None = Field(default=None, description="Pagination settings")


class NegativeKeywordSharedSetGetItem(YDBase):
    Id: int | None = Field(default=None, description="Shared set ID")
    Name: str | None = Field(default=None, description="Shared set name")
    NegativeKeywords: list[str] | None = Field(default=None, description="List of negative keywords in the set")


class NegativeKeywordSharedSetsGetResult(YDBase):
    NegativeKeywordSharedSets: list[NegativeKeywordSharedSetGetItem] | None = Field(default=None, description="List of negative keyword shared sets")
    LimitedBy: int | None = Field(default=None, description="Offset for the next page if results are truncated")


class NegativeKeywordSharedSetAddItem(YDBase):
    Name: str = Field(description="Shared set name")
    NegativeKeywords: list[str] = Field(description="List of negative keywords to add")


class NegativeKeywordSharedSetsAddParams(YDBase):
    NegativeKeywordSharedSets: list[NegativeKeywordSharedSetAddItem] = Field(description="Shared sets to add")


class NegativeKeywordSharedSetsAddResult(YDBase):
    AddResults: list[ActionResult] = Field(description="Results of the add operation")


class NegativeKeywordSharedSetUpdateItem(YDBase):
    Id: int = Field(description="Shared set ID to update")
    Name: str | None = Field(default=None, description="New shared set name")
    NegativeKeywords: list[str] | None = Field(default=None, description="New list of negative keywords")


class NegativeKeywordSharedSetsUpdateParams(YDBase):
    NegativeKeywordSharedSets: list[NegativeKeywordSharedSetUpdateItem] = Field(description="Shared sets to update")


class NegativeKeywordSharedSetsUpdateResult(YDBase):
    UpdateResults: list[ActionResult] = Field(description="Results of the update operation")


class NegativeKeywordSharedSetsDeleteParams(YDBase):
    SelectionCriteria: IdsCriteria = Field(description="IDs of shared sets to delete")


class NegativeKeywordSharedSetsDeleteResult(YDBase):
    DeleteResults: list[ActionResult] = Field(description="Results of the delete operation")
