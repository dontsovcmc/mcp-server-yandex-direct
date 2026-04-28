"""Pydantic models for AgencyClients service."""

from .common import YDBase, LimitOffset, ActionResult


class AgencyClientsSelectionCriteria(YDBase):
    Logins: list[str] | None = None
    Archived: str | None = None


class AgencyClientsGetParams(YDBase):
    SelectionCriteria: AgencyClientsSelectionCriteria
    FieldNames: list[str]
    Page: LimitOffset | None = None


class AgencyClientGetItem(YDBase):
    Login: str | None = None
    ClientId: int | None = None
    ClientInfo: str | None = None
    Type: str | None = None
    CountryId: int | None = None
    Currency: str | None = None
    Phone: str | None = None
    AccountQuality: float | None = None
    Archived: str | None = None
    Grants: list[dict] | None = None
    Notification: dict | None = None
    Representatives: list[dict] | None = None
    Restrictions: list[dict] | None = None
    Settings: list[dict] | None = None


class AgencyClientsGetResult(YDBase):
    Clients: list[AgencyClientGetItem] | None = None
    LimitedBy: int | None = None


class AgencyClientAddItem(YDBase):
    Login: str
    FirstName: str
    LastName: str
    Currency: str
    Grants: list[dict] | None = None
    Notification: dict | None = None
    Settings: list[dict] | None = None


class AgencyClientsAddParams(YDBase):
    Clients: list[AgencyClientAddItem]


class AgencyClientsAddResult(YDBase):
    AddResults: list[ActionResult]


class AgencyClientUpdateItem(YDBase):
    Login: str
    ClientInfo: str | None = None
    Grants: list[dict] | None = None
    Notification: dict | None = None
    Phone: str | None = None
    Settings: list[dict] | None = None


class AgencyClientsUpdateParams(YDBase):
    Clients: list[AgencyClientUpdateItem]


class AgencyClientsUpdateResult(YDBase):
    UpdateResults: list[ActionResult]
