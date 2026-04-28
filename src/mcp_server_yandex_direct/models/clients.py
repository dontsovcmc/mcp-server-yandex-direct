"""Pydantic models for Clients service."""

from .common import YDBase, ActionResult


class ClientsSelectionCriteria(YDBase):
    Logins: list[str] | None = None
    Archived: str | None = None


class ClientsGetParams(YDBase):
    FieldNames: list[str]


class ClientGetItem(YDBase):
    Login: str | None = None
    ClientId: int | None = None
    ClientInfo: str | None = None
    AccountQuality: float | None = None
    Type: str | None = None
    CountryId: int | None = None
    Currency: str | None = None
    Phone: str | None = None
    Archived: str | None = None
    CreatedAt: str | None = None
    Grants: list[dict] | None = None
    Notification: dict | None = None
    Representatives: list[dict] | None = None
    Restrictions: list[dict] | None = None
    Settings: list[dict] | None = None
    BonusesCount: int | None = None


class ClientsGetResult(YDBase):
    Clients: list[ClientGetItem] | None = None


class ClientUpdateItem(YDBase):
    ClientInfo: str | None = None
    Notification: dict | None = None
    Phone: str | None = None
    Settings: list[dict] | None = None


class ClientsUpdateParams(YDBase):
    Clients: list[ClientUpdateItem]


class ClientsUpdateResult(YDBase):
    UpdateResults: list[ActionResult]
