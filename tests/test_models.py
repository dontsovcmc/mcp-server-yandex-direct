"""Pydantic model validation tests — one per service minimum."""

from mcp_server_yandex_direct.models.common import IdsCriteria, LimitOffset, ActionResult
from mcp_server_yandex_direct.models.campaigns import (
    CampaignsGetResult, CampaignsAddResult, CampaignsGetParams,
    CampaignsSelectionCriteria,
)
from mcp_server_yandex_direct.models.adgroups import AdGroupsGetResult
from mcp_server_yandex_direct.models.ads import AdsGetResult
from mcp_server_yandex_direct.models.keywords import KeywordsGetResult
from mcp_server_yandex_direct.models.bids import BidsGetResult
from mcp_server_yandex_direct.models.bidmodifiers import BidModifiersGetResult
from mcp_server_yandex_direct.models.sitelinks import SitelinksGetResult
from mcp_server_yandex_direct.models.adimages import AdImagesGetResult
from mcp_server_yandex_direct.models.advideos import AdVideosGetResult
from mcp_server_yandex_direct.models.adextensions import AdExtensionsGetResult
from mcp_server_yandex_direct.models.audiencetargets import AudienceTargetsGetResult
from mcp_server_yandex_direct.models.retargetinglists import RetargetingListsGetResult
from mcp_server_yandex_direct.models.negativekeywordsharedsets import (
    NegativeKeywordSharedSetsGetResult,
)
from mcp_server_yandex_direct.models.feeds import FeedsGetResult
from mcp_server_yandex_direct.models.creatives import CreativesGetResult
from mcp_server_yandex_direct.models.keywordsresearch import DeduplicateResult, HasSearchVolumeResult
from mcp_server_yandex_direct.models.leads import LeadsGetResult
from mcp_server_yandex_direct.models.changes import ChangesCheckResult, ChangesCheckDictionariesResult
from mcp_server_yandex_direct.models.dictionaries import DictionariesGetResult
from mcp_server_yandex_direct.models.clients import ClientsGetResult
from mcp_server_yandex_direct.models.agencyclients import AgencyClientsGetResult
from mcp_server_yandex_direct.models.turbopages import TurboPagesGetResult


# ── Common ──

def test_ids_criteria():
    c = IdsCriteria(Ids=[1, 2, 3])
    assert c.Ids == [1, 2, 3]


def test_limit_offset_defaults():
    p = LimitOffset()
    assert p.Limit == 10000
    assert p.Offset == 0


def test_action_result():
    r = ActionResult.model_validate({"Id": 123, "Warnings": [], "Errors": []})
    assert r.Id == 123


def test_action_result_with_error():
    r = ActionResult.model_validate({
        "Id": None,
        "Errors": [{"Code": 8800, "Message": "Duplicate"}],
    })
    assert r.Id is None
    assert r.Errors[0].Code == 8800


# ── Campaigns ──

def test_campaigns_get_params():
    p = CampaignsGetParams(
        SelectionCriteria=CampaignsSelectionCriteria(Ids=[1, 2]),
        FieldNames=["Id", "Name"],
    )
    assert p.FieldNames == ["Id", "Name"]
    assert p.SelectionCriteria.Ids == [1, 2]


def test_campaigns_get_result():
    r = CampaignsGetResult.model_validate({
        "Campaigns": [
            {"Id": 123, "Name": "Test Campaign", "State": "ON", "Status": "ACCEPTED"},
            {"Id": 456, "Name": "Another", "State": "SUSPENDED"},
        ],
        "LimitedBy": 10000,
    })
    assert len(r.Campaigns) == 2
    assert r.Campaigns[0].Id == 123
    assert r.LimitedBy == 10000


def test_campaigns_get_result_extra_fields():
    r = CampaignsGetResult.model_validate({
        "Campaigns": [{"Id": 1, "UnknownField": "value"}],
    })
    assert r.Campaigns[0].Id == 1


def test_campaigns_add_result():
    r = CampaignsAddResult.model_validate({
        "AddResults": [
            {"Id": 789, "Warnings": []},
            {"Id": None, "Errors": [{"Code": 8800, "Message": "Duplicate"}]},
        ],
    })
    assert r.AddResults[0].Id == 789
    assert r.AddResults[1].Errors[0].Code == 8800


# ── AdGroups ──

def test_adgroups_get_result():
    r = AdGroupsGetResult.model_validate({
        "AdGroups": [
            {"Id": 10, "Name": "Group 1", "CampaignId": 100, "Status": "ACCEPTED"},
        ],
    })
    assert r.AdGroups[0].CampaignId == 100


# ── Ads ──

def test_ads_get_result():
    r = AdsGetResult.model_validate({
        "Ads": [
            {"Id": 20, "AdGroupId": 10, "CampaignId": 100, "Type": "TEXT_AD", "State": "ON"},
        ],
    })
    assert r.Ads[0].Type == "TEXT_AD"


# ── Keywords ──

def test_keywords_get_result():
    r = KeywordsGetResult.model_validate({
        "Keywords": [
            {"Id": 30, "Keyword": "buy shoes", "AdGroupId": 10, "State": "ON"},
        ],
    })
    assert r.Keywords[0].Keyword == "buy shoes"


# ── Bids ──

def test_bids_get_result():
    r = BidsGetResult.model_validate({
        "Bids": [
            {"KeywordId": 30, "Bid": 1500000, "CurrentSearchPrice": 1200000},
        ],
    })
    assert r.Bids[0].Bid == 1500000


# ── BidModifiers ──

def test_bidmodifiers_get_result():
    r = BidModifiersGetResult.model_validate({
        "BidModifiers": [
            {"Id": 40, "CampaignId": 100, "Type": "DEMOGRAPHICS_ADJUSTMENT"},
        ],
    })
    assert r.BidModifiers[0].Type == "DEMOGRAPHICS_ADJUSTMENT"


# ── Sitelinks ──

def test_sitelinks_get_result():
    r = SitelinksGetResult.model_validate({
        "SitelinksSets": [
            {"Id": 50, "Sitelinks": [{"Title": "About", "Href": "https://example.com/about"}]},
        ],
    })
    assert r.SitelinksSets[0].Sitelinks[0].Title == "About"


# ── AdImages ──

def test_adimages_get_result():
    r = AdImagesGetResult.model_validate({
        "AdImages": [
            {"AdImageHash": "abc123", "Name": "logo.png", "Type": "REGULAR"},
        ],
    })
    assert r.AdImages[0].AdImageHash == "abc123"


# ── AdVideos ──

def test_advideos_get_result():
    r = AdVideosGetResult.model_validate({
        "AdVideos": [
            {"Id": 60, "Name": "promo.mp4", "Status": "ACCEPTED"},
        ],
    })
    assert r.AdVideos[0].Name == "promo.mp4"


# ── AdExtensions ──

def test_adextensions_get_result():
    r = AdExtensionsGetResult.model_validate({
        "AdExtensions": [
            {"Id": 70, "Type": "CALLOUT", "Status": "ACCEPTED"},
        ],
    })
    assert r.AdExtensions[0].Type == "CALLOUT"


# ── AudienceTargets ──

def test_audiencetargets_get_result():
    r = AudienceTargetsGetResult.model_validate({
        "AudienceTargets": [
            {"Id": 80, "AdGroupId": 10, "RetargetingListId": 5, "State": "ON"},
        ],
    })
    assert r.AudienceTargets[0].RetargetingListId == 5


# ── RetargetingLists ──

def test_retargetinglists_get_result():
    r = RetargetingListsGetResult.model_validate({
        "RetargetingLists": [
            {"Id": 90, "Name": "Visitors", "IsAvailable": "YES"},
        ],
    })
    assert r.RetargetingLists[0].Name == "Visitors"


# ── NegativeKeywordSharedSets ──

def test_negkeywordsets_get_result():
    r = NegativeKeywordSharedSetsGetResult.model_validate({
        "NegativeKeywordSharedSets": [
            {"Id": 100, "Name": "Excluded", "NegativeKeywords": ["free", "cheap"]},
        ],
    })
    assert r.NegativeKeywordSharedSets[0].NegativeKeywords == ["free", "cheap"]


# ── Feeds ──

def test_feeds_get_result():
    r = FeedsGetResult.model_validate({
        "Feeds": [
            {"Id": 110, "Name": "Products", "Status": "ACCEPTED", "NumberOfItems": 500},
        ],
    })
    assert r.Feeds[0].NumberOfItems == 500


# ── Creatives ──

def test_creatives_get_result():
    r = CreativesGetResult.model_validate({
        "Creatives": [
            {"Id": 120, "Type": "VIDEO_EXTENSION_CREATIVE", "Width": 640, "Height": 480},
        ],
    })
    assert r.Creatives[0].Width == 640


# ── KeywordsResearch ──

def test_deduplicate_result():
    r = DeduplicateResult.model_validate({
        "DeduplicateResults": [
            {"Keyword": "buy shoes", "Deduplicated": "buy shoes"},
        ],
    })
    assert r.DeduplicateResults[0].Keyword == "buy shoes"


def test_has_search_volume_result():
    r = HasSearchVolumeResult.model_validate({
        "HasSearchVolumeResults": [
            {"Keyword": "buy shoes", "HasSearchVolume": "YES"},
        ],
    })
    assert r.HasSearchVolumeResults[0].HasSearchVolume == "YES"


# ── Leads ──

def test_leads_get_result():
    r = LeadsGetResult.model_validate({
        "Leads": [
            {"Id": 130, "TurboPageId": 10, "CampaignId": 100},
        ],
    })
    assert r.Leads[0].TurboPageId == 10


# ── Changes ──

def test_changes_check_result():
    r = ChangesCheckResult.model_validate({
        "Timestamp": "2026-04-28T12:00:00Z",
        "CampaignIds": [1, 2],
    })
    assert r.CampaignIds == [1, 2]


def test_changes_check_dictionaries_result():
    r = ChangesCheckDictionariesResult.model_validate({
        "Timestamp": "2026-04-28T12:00:00Z",
    })
    assert r.Timestamp is not None


# ── Dictionaries ──

def test_dictionaries_get_result():
    r = DictionariesGetResult.model_validate({
        "Currencies": [{"Currency": "RUB", "Properties": []}],
        "GeoRegions": [{"GeoRegionId": 1, "GeoRegionName": "Moscow"}],
    })
    assert len(r.Currencies) == 1


# ── Clients ──

def test_clients_get_result():
    r = ClientsGetResult.model_validate({
        "Clients": [
            {"Login": "user1", "ClientId": 1000, "Type": "CLIENT"},
        ],
    })
    assert r.Clients[0].Login == "user1"


# ── AgencyClients ──

def test_agencyclients_get_result():
    r = AgencyClientsGetResult.model_validate({
        "Clients": [
            {"Login": "agency_client", "ClientId": 2000, "Currency": "RUB"},
        ],
    })
    assert r.Clients[0].Currency == "RUB"


# ── TurboPages ──

def test_turbopages_get_result():
    r = TurboPagesGetResult.model_validate({
        "TurboPages": [
            {"Id": 140, "Name": "Landing", "Href": "https://example.com"},
        ],
    })
    assert r.TurboPages[0].Href == "https://example.com"
