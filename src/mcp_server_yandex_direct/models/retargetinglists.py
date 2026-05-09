"""Pydantic models for RetargetingLists service."""

from pydantic import Field

from .common import YDBase, IdsCriteria, LimitOffset, ActionResult


class RetargetingListsSelectionCriteria(YDBase):
    Ids: list[int] | None = Field(default=None, description="Retargeting list IDs to filter by")


class RetargetingListsGetParams(YDBase):
    SelectionCriteria: RetargetingListsSelectionCriteria = Field(description="Criteria for selecting retargeting lists")
    FieldNames: list[str] = Field(description="Names of fields to return")
    Page: LimitOffset | None = Field(default=None, description="Pagination settings")


class RetargetingListGetItem(YDBase):
    Id: int | None = Field(default=None, description="Retargeting list ID")
    Name: str | None = Field(default=None, description="Retargeting list name")
    Description: str | None = Field(default=None, description="Retargeting list description")
    IsAvailable: str | None = Field(default=None, description="Whether the retargeting list is available for use")
    Rules: list[dict] | None = Field(default=None, description="Retargeting list rules (conditions and goals)")


class RetargetingListsGetResult(YDBase):
    RetargetingLists: list[RetargetingListGetItem] | None = Field(default=None, description="List of retargeting lists")
    LimitedBy: int | None = Field(default=None, description="Offset for the next page if results are truncated")


class RetargetingListAddItem(YDBase):
    Name: str = Field(description="Retargeting list name")
    Description: str | None = Field(default=None, description="Retargeting list description")
    Rules: list[dict] = Field(description="Retargeting list rules (conditions and goals)")


class RetargetingListsAddParams(YDBase):
    RetargetingLists: list[RetargetingListAddItem] = Field(description="Retargeting lists to add")


class RetargetingListsAddResult(YDBase):
    AddResults: list[ActionResult] = Field(description="Results of the add operation")


class RetargetingListUpdateItem(YDBase):
    Id: int = Field(description="Retargeting list ID to update")
    Name: str | None = Field(default=None, description="New retargeting list name")
    Description: str | None = Field(default=None, description="New retargeting list description")
    Rules: list[dict] | None = Field(default=None, description="New retargeting list rules")


class RetargetingListsUpdateParams(YDBase):
    RetargetingLists: list[RetargetingListUpdateItem] = Field(description="Retargeting lists to update")


class RetargetingListsUpdateResult(YDBase):
    UpdateResults: list[ActionResult] = Field(description="Results of the update operation")


class RetargetingListsDeleteParams(YDBase):
    SelectionCriteria: IdsCriteria = Field(description="IDs of retargeting lists to delete")


class RetargetingListsDeleteResult(YDBase):
    DeleteResults: list[ActionResult] = Field(description="Results of the delete operation")
