"""Pydantic models for AdImages service."""

from pydantic import Field

from .common import YDBase, LimitOffset, ActionResult


class AdImagesSelectionCriteria(YDBase):
    AdImageHashes: list[str] | None = Field(default=None, description="Filter by ad image hashes")
    Associated: str | None = Field(default=None, description="Filter by association status (YES or NO)")


class AdImagesGetParams(YDBase):
    SelectionCriteria: AdImagesSelectionCriteria = Field(description="Criteria for selecting ad images")
    FieldNames: list[str] = Field(description="Ad image field names to return")
    Page: LimitOffset | None = Field(default=None, description="Pagination settings")


class AdImageGetItem(YDBase):
    AdImageHash: str | None = Field(default=None, description="Unique hash of the ad image")
    OriginalUrl: str | None = Field(default=None, description="URL of the original uploaded image")
    PreviewUrl: str | None = Field(default=None, description="URL of the image preview")
    Name: str | None = Field(default=None, description="Ad image name")
    Type: str | None = Field(default=None, description="Image type")
    Subtype: str | None = Field(default=None, description="Image subtype")
    Associated: str | None = Field(default=None, description="Whether the image is associated with an ad (YES or NO)")


class AdImagesGetResult(YDBase):
    AdImages: list[AdImageGetItem] | None = Field(default=None, description="List of ad images matching the criteria")
    LimitedBy: int | None = Field(default=None, description="Indicates next page offset if results were truncated")


class AdImageAddItem(YDBase):
    ImageData: str | None = Field(default=None, description="Base64-encoded image data")
    Name: str | None = Field(default=None, description="Ad image name")


class AdImagesAddParams(YDBase):
    AdImages: list[AdImageAddItem] = Field(description="List of ad images to add")


class AdImagesAddResult(YDBase):
    AddResults: list[ActionResult] = Field(description="Results of add operations")


class AdImagesDeleteParams(YDBase):
    SelectionCriteria: dict = Field(description="Selection criteria for ad images to delete")


class AdImagesDeleteResult(YDBase):
    DeleteResults: list[ActionResult] = Field(description="Results of delete operations")
