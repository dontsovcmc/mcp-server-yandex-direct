"""Pydantic models for Clients service."""

from pydantic import Field

from .common import YDBase, ActionResult


class ClientsSelectionCriteria(YDBase):
    Logins: list[str] | None = Field(default=None, description="Client logins to filter by")
    Archived: str | None = Field(default=None, description="Filter by archived status (YES or NO)")


class ClientsGetParams(YDBase):
    FieldNames: list[str] = Field(description="Names of fields to return")


class ClientGetItem(YDBase):
    Login: str | None = Field(default=None, description="Client login")
    ClientId: int | None = Field(default=None, description="Client ID")
    ClientInfo: str | None = Field(default=None, description="Client description text")
    AccountQuality: float | None = Field(default=None, description="Account quality score")
    Type: str | None = Field(default=None, description="Client type (CLIENT or AGENCY)")
    CountryId: int | None = Field(default=None, description="Country ID from the geo regions dictionary")
    Currency: str | None = Field(default=None, description="Account currency code")
    Phone: str | None = Field(default=None, description="Contact phone number")
    Archived: str | None = Field(default=None, description="Whether the client is archived (YES or NO)")
    CreatedAt: str | None = Field(default=None, description="Account creation date")
    Grants: list[dict] | None = Field(default=None, description="Granted access permissions")
    Notification: dict | None = Field(default=None, description="Notification settings")
    Representatives: list[dict] | None = Field(default=None, description="Agency representatives for this client")
    Restrictions: list[dict] | None = Field(default=None, description="Account restrictions")
    Settings: list[dict] | None = Field(default=None, description="Client settings")
    BonusesCount: int | None = Field(default=None, description="Number of bonus points available")


class ClientsGetResult(YDBase):
    Clients: list[ClientGetItem] | None = Field(default=None, description="List of clients")


class ClientUpdateItem(YDBase):
    ClientInfo: str | None = Field(default=None, description="New client description text")
    Notification: dict | None = Field(default=None, description="New notification settings")
    Phone: str | None = Field(default=None, description="New contact phone number")
    Settings: list[dict] | None = Field(default=None, description="New client settings")


class ClientsUpdateParams(YDBase):
    Clients: list[ClientUpdateItem] = Field(description="Clients to update")


class ClientsUpdateResult(YDBase):
    UpdateResults: list[ActionResult] = Field(description="Results of the update operation")
