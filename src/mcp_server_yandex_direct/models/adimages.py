"""Pydantic models for AdImages service."""

from .common import YDBase, LimitOffset, ActionResult


class AdImagesSelectionCriteria(YDBase):
    AdImageHashes: list[str] | None = None
    Associated: str | None = None


class AdImagesGetParams(YDBase):
    SelectionCriteria: AdImagesSelectionCriteria
    FieldNames: list[str]
    Page: LimitOffset | None = None


class AdImageGetItem(YDBase):
    AdImageHash: str | None = None
    OriginalUrl: str | None = None
    PreviewUrl: str | None = None
    Name: str | None = None
    Type: str | None = None
    Subtype: str | None = None
    Associated: str | None = None


class AdImagesGetResult(YDBase):
    AdImages: list[AdImageGetItem] | None = None
    LimitedBy: int | None = None


class AdImageAddItem(YDBase):
    ImageData: str | None = None
    Name: str | None = None


class AdImagesAddParams(YDBase):
    AdImages: list[AdImageAddItem]


class AdImagesAddResult(YDBase):
    AddResults: list[ActionResult]


class AdImagesDeleteParams(YDBase):
    SelectionCriteria: dict


class AdImagesDeleteResult(YDBase):
    DeleteResults: list[ActionResult]
