"""Common Pydantic models shared across Yandex Direct API v5 services."""

from pydantic import BaseModel, ConfigDict


class YDBase(BaseModel):
    """Base model for all Yandex Direct models — tolerates unknown fields."""
    model_config = ConfigDict(extra="allow")


class IdsCriteria(YDBase):
    """Selection by IDs — used by delete/suspend/resume/archive/unarchive."""
    Ids: list[int]


class LimitOffset(YDBase):
    """Pagination."""
    Limit: int = 10000
    Offset: int = 0


class ExceptionNotification(YDBase):
    Code: int | None = None
    Message: str | None = None
    Details: str | None = None


class ActionResult(YDBase):
    """Result of a single add/update/delete/suspend/resume/archive/unarchive operation."""
    Id: int | None = None
    Warnings: list[ExceptionNotification] | None = None
    Errors: list[ExceptionNotification] | None = None


class MultiIdsActionResult(YDBase):
    """Wrapper for batch action results."""
    AddResults: list[ActionResult] | None = None
    UpdateResults: list[ActionResult] | None = None
    DeleteResults: list[ActionResult] | None = None
    SuspendResults: list[ActionResult] | None = None
    ResumeResults: list[ActionResult] | None = None
    ArchiveResults: list[ActionResult] | None = None
    UnarchiveResults: list[ActionResult] | None = None
    ModerateResults: list[ActionResult] | None = None
    SetResults: list[ActionResult] | None = None
    SetBidsResults: list[ActionResult] | None = None
