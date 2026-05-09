"""Pydantic models for AgencyClients service."""

from pydantic import Field

from .common import YDBase, LimitOffset, ActionResult


class AgencyClientsSelectionCriteria(YDBase):
    Logins: list[str] | None = Field(default=None, description="Client logins to filter by")
    Archived: str | None = Field(default=None, description="Filter by archived status (YES or NO)")


class AgencyClientsGetParams(YDBase):
    SelectionCriteria: AgencyClientsSelectionCriteria = Field(description="Criteria for selecting agency clients")
    FieldNames: list[str] = Field(description="Names of fields to return")
    Page: LimitOffset | None = Field(default=None, description="Pagination settings")


class AgencyClientGetItem(YDBase):
    Login: str | None = Field(default=None, description="Client login")
    ClientId: int | None = Field(default=None, description="Client ID")
    ClientInfo: str | None = Field(default=None, description="Client description text")
    Type: str | None = Field(default=None, description="Client type")
    CountryId: int | None = Field(default=None, description="Country ID from the geo regions dictionary")
    Currency: str | None = Field(default=None, description="Account currency code")
    Phone: str | None = Field(default=None, description="Contact phone number")
    AccountQuality: float | None = Field(default=None, description="Account quality score")
    Archived: str | None = Field(default=None, description="Whether the client is archived (YES or NO)")
    Grants: list[dict] | None = Field(default=None, description="Granted access permissions")
    Notification: dict | None = Field(default=None, description="Notification settings")
    Representatives: list[dict] | None = Field(default=None, description="Agency representatives for this client")
    Restrictions: list[dict] | None = Field(default=None, description="Account restrictions")
    Settings: list[dict] | None = Field(default=None, description="Client settings")


class AgencyClientsGetResult(YDBase):
    Clients: list[AgencyClientGetItem] | None = Field(default=None, description="List of agency clients")
    LimitedBy: int | None = Field(default=None, description="Offset for the next page if results are truncated")


class AgencyClientAddItem(YDBase):
    Login: str = Field(description="Login for the new client")
    FirstName: str = Field(description="Client first name")
    LastName: str = Field(description="Client last name")
    Currency: str = Field(description="Account currency code")
    Grants: list[dict] | None = Field(default=None, description="Access permissions to grant")
    Notification: dict | None = Field(default=None, description="Notification settings")
    Settings: list[dict] | None = Field(default=None, description="Client settings")


class AgencyClientsAddParams(YDBase):
    Clients: list[AgencyClientAddItem] = Field(description="Clients to add")


class AgencyClientsAddResult(YDBase):
    AddResults: list[ActionResult] = Field(description="Results of the add operation")


class AgencyClientUpdateItem(YDBase):
    Login: str = Field(description="Login of the client to update")
    ClientInfo: str | None = Field(default=None, description="New client description text")
    Grants: list[dict] | None = Field(default=None, description="New access permissions")
    Notification: dict | None = Field(default=None, description="New notification settings")
    Phone: str | None = Field(default=None, description="New contact phone number")
    Settings: list[dict] | None = Field(default=None, description="New client settings")


class AgencyClientsUpdateParams(YDBase):
    Clients: list[AgencyClientUpdateItem] = Field(description="Clients to update")


class AgencyClientsUpdateResult(YDBase):
    UpdateResults: list[ActionResult] = Field(description="Results of the update operation")
