"""Pydantic models for TurboPages service."""

from .common import YDBase, LimitOffset


class TurboPagesSelectionCriteria(YDBase):
    Ids: list[int] | None = None


class TurboPagesGetParams(YDBase):
    SelectionCriteria: TurboPagesSelectionCriteria
    FieldNames: list[str]
    Page: LimitOffset | None = None


class TurboPageGetItem(YDBase):
    Id: int | None = None
    Name: str | None = None
    Href: str | None = None


class TurboPagesGetResult(YDBase):
    TurboPages: list[TurboPageGetItem] | None = None
    LimitedBy: int | None = None
