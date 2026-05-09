"""Common Pydantic models shared across Yandex Direct API v5 services."""

from pydantic import BaseModel, ConfigDict, Field


class YDBase(BaseModel):
    """Base model for all Yandex Direct models — tolerates unknown fields."""
    model_config = ConfigDict(extra="allow")


class IdsCriteria(YDBase):
    """Selection by IDs — used by delete/suspend/resume/archive/unarchive."""
    Ids: list[int] = Field(description="List of object IDs to operate on")


class LimitOffset(YDBase):
    """Pagination."""
    Limit: int = Field(default=10000, description="Maximum number of objects to return")
    Offset: int = Field(default=0, description="Number of objects to skip from the beginning")


class ExceptionNotification(YDBase):
    Code: int | None = Field(default=None, description="Error or warning code")
    Message: str | None = Field(default=None, description="Error or warning message text")
    Details: str | None = Field(default=None, description="Detailed error or warning description")


class ActionResult(YDBase):
    """Result of a single add/update/delete/suspend/resume/archive/unarchive operation."""
    Id: int | None = Field(default=None, description="ID of the created or affected object")
    Warnings: list[ExceptionNotification] | None = Field(default=None, description="List of warnings for this operation")
    Errors: list[ExceptionNotification] | None = Field(default=None, description="List of errors for this operation")


class MultiIdsActionResult(YDBase):
    """Wrapper for batch action results."""
    AddResults: list[ActionResult] | None = Field(default=None, description="Results of add operations")
    UpdateResults: list[ActionResult] | None = Field(default=None, description="Results of update operations")
    DeleteResults: list[ActionResult] | None = Field(default=None, description="Results of delete operations")
    SuspendResults: list[ActionResult] | None = Field(default=None, description="Results of suspend operations")
    ResumeResults: list[ActionResult] | None = Field(default=None, description="Results of resume operations")
    ArchiveResults: list[ActionResult] | None = Field(default=None, description="Results of archive operations")
    UnarchiveResults: list[ActionResult] | None = Field(default=None, description="Results of unarchive operations")
    ModerateResults: list[ActionResult] | None = Field(default=None, description="Results of moderate operations")
    SetResults: list[ActionResult] | None = Field(default=None, description="Results of set operations")
    SetBidsResults: list[ActionResult] | None = Field(default=None, description="Results of set bids operations")
