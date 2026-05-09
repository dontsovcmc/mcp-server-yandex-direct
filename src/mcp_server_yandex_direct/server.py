"""MCP server for Yandex Direct API v5."""

import json
import logging
import os
import sys

from mcp.server.fastmcp import FastMCP

from .yd_api import YandexDirectAPI

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s", stream=sys.stderr)
log = logging.getLogger(__name__)

mcp = FastMCP(
    "yandex-direct",
    instructions=(
        "Yandex Direct API v5 server. 22 services: campaigns, adgroups, ads, keywords, "
        "bids, bidmodifiers, sitelinks, adimages, advideos, adextensions, audiencetargets, "
        "retargetinglists, negativekeywordsharedsets, feeds, creatives, keywordsresearch, "
        "leads, changes, dictionaries, clients, agencyclients, turbopages. "
        "Plus Reports API for analytics (TSV output). "
        "Protocol: JSON-RPC-like POST with {method, params}. "
        "Most tools accept params_json (JSON string). "
        "Action tools (delete/suspend/resume/archive) accept comma-separated IDs."
    ),
)

_api_instance: YandexDirectAPI | None = None


def _get_api() -> YandexDirectAPI:
    global _api_instance
    if _api_instance is None:
        token = os.getenv("YD_TOKEN")
        if not token:
            raise RuntimeError("YD_TOKEN environment variable is required")
        client_login = os.getenv("YD_CLIENT_LOGIN", "")
        lang = os.getenv("YD_LANG", "")
        timeout = int(os.getenv("YD_TIMEOUT", "30"))
        file_timeout = int(os.getenv("YD_FILE_TIMEOUT", "120"))
        _api_instance = YandexDirectAPI(
            token, client_login=client_login, lang=lang,
            timeout=timeout, file_timeout=file_timeout,
        )
    return _api_instance


def _to_json(data) -> str:
    return json.dumps(data, ensure_ascii=False)


def _parse_json(s: str, label: str = "input"):
    """Parse JSON string with a clear error message."""
    try:
        return json.loads(s)
    except json.JSONDecodeError as e:
        raise ValueError(f"Invalid JSON in {label}: {e}") from e


def _ids(ids_str: str) -> dict:
    """Parse comma-separated IDs into SelectionCriteria dict."""
    return {"SelectionCriteria": {"Ids": [int(x.strip()) for x in ids_str.split(",")]}}


# ── Campaigns ──────────────────────────────────────────────────────────


@mcp.tool()
def yd_campaigns_get(params_json: str) -> str:
    """Get campaigns. Args: params_json — JSON with SelectionCriteria, FieldNames, Page."""
    return _to_json(_get_api().campaigns_get(_parse_json(params_json, "params_json")))


@mcp.tool()
def yd_campaigns_add(params_json: str) -> str:
    """Add campaigns. Args: params_json — JSON with Campaigns array."""
    return _to_json(_get_api().campaigns_add(_parse_json(params_json, "params_json")))


@mcp.tool()
def yd_campaigns_update(params_json: str) -> str:
    """Update campaigns. Args: params_json — JSON with Campaigns array."""
    return _to_json(_get_api().campaigns_update(_parse_json(params_json, "params_json")))


@mcp.tool()
def yd_campaigns_delete(ids: str) -> str:
    """Delete campaigns. Args: ids — comma-separated campaign IDs."""
    return _to_json(_get_api().campaigns_delete(_ids(ids)))


@mcp.tool()
def yd_campaigns_suspend(ids: str) -> str:
    """Suspend campaigns. Args: ids — comma-separated campaign IDs."""
    return _to_json(_get_api().campaigns_suspend(_ids(ids)))


@mcp.tool()
def yd_campaigns_resume(ids: str) -> str:
    """Resume campaigns. Args: ids — comma-separated campaign IDs."""
    return _to_json(_get_api().campaigns_resume(_ids(ids)))


@mcp.tool()
def yd_campaigns_archive(ids: str) -> str:
    """Archive campaigns. Args: ids — comma-separated campaign IDs."""
    return _to_json(_get_api().campaigns_archive(_ids(ids)))


@mcp.tool()
def yd_campaigns_unarchive(ids: str) -> str:
    """Unarchive campaigns. Args: ids — comma-separated campaign IDs."""
    return _to_json(_get_api().campaigns_unarchive(_ids(ids)))


# ── AdGroups ───────────────────────────────────────────────────────────


@mcp.tool()
def yd_adgroups_get(params_json: str) -> str:
    """Get ad groups. Args: params_json — JSON with SelectionCriteria, FieldNames, Page."""
    return _to_json(_get_api().adgroups_get(_parse_json(params_json, "params_json")))


@mcp.tool()
def yd_adgroups_add(params_json: str) -> str:
    """Add ad groups. Args: params_json — JSON with AdGroups array."""
    return _to_json(_get_api().adgroups_add(_parse_json(params_json, "params_json")))


@mcp.tool()
def yd_adgroups_update(params_json: str) -> str:
    """Update ad groups. Args: params_json — JSON with AdGroups array."""
    return _to_json(_get_api().adgroups_update(_parse_json(params_json, "params_json")))


@mcp.tool()
def yd_adgroups_delete(ids: str) -> str:
    """Delete ad groups. Args: ids — comma-separated ad group IDs."""
    return _to_json(_get_api().adgroups_delete(_ids(ids)))


# ── Ads ─────────────────────────────────────────────────────────────────


@mcp.tool()
def yd_ads_get(params_json: str) -> str:
    """Get ads. Args: params_json — JSON with SelectionCriteria, FieldNames, Page."""
    return _to_json(_get_api().ads_get(_parse_json(params_json, "params_json")))


@mcp.tool()
def yd_ads_add(params_json: str) -> str:
    """Add ads. Args: params_json — JSON with Ads array."""
    return _to_json(_get_api().ads_add(_parse_json(params_json, "params_json")))


@mcp.tool()
def yd_ads_update(params_json: str) -> str:
    """Update ads. Args: params_json — JSON with Ads array."""
    return _to_json(_get_api().ads_update(_parse_json(params_json, "params_json")))


@mcp.tool()
def yd_ads_delete(ids: str) -> str:
    """Delete ads. Args: ids — comma-separated ad IDs."""
    return _to_json(_get_api().ads_delete(_ids(ids)))


@mcp.tool()
def yd_ads_suspend(ids: str) -> str:
    """Suspend ads. Args: ids — comma-separated ad IDs."""
    return _to_json(_get_api().ads_suspend(_ids(ids)))


@mcp.tool()
def yd_ads_resume(ids: str) -> str:
    """Resume ads. Args: ids — comma-separated ad IDs."""
    return _to_json(_get_api().ads_resume(_ids(ids)))


@mcp.tool()
def yd_ads_archive(ids: str) -> str:
    """Archive ads. Args: ids — comma-separated ad IDs."""
    return _to_json(_get_api().ads_archive(_ids(ids)))


@mcp.tool()
def yd_ads_unarchive(ids: str) -> str:
    """Unarchive ads. Args: ids — comma-separated ad IDs."""
    return _to_json(_get_api().ads_unarchive(_ids(ids)))


@mcp.tool()
def yd_ads_moderate(ids: str) -> str:
    """Send ads for moderation. Args: ids — comma-separated ad IDs."""
    return _to_json(_get_api().ads_moderate(_ids(ids)))


# ── Keywords ────────────────────────────────────────────────────────────


@mcp.tool()
def yd_keywords_get(params_json: str) -> str:
    """Get keywords. Args: params_json — JSON with SelectionCriteria, FieldNames, Page."""
    return _to_json(_get_api().keywords_get(_parse_json(params_json, "params_json")))


@mcp.tool()
def yd_keywords_add(params_json: str) -> str:
    """Add keywords. Args: params_json — JSON with Keywords array."""
    return _to_json(_get_api().keywords_add(_parse_json(params_json, "params_json")))


@mcp.tool()
def yd_keywords_update(params_json: str) -> str:
    """Update keywords. Args: params_json — JSON with Keywords array."""
    return _to_json(_get_api().keywords_update(_parse_json(params_json, "params_json")))


@mcp.tool()
def yd_keywords_delete(ids: str) -> str:
    """Delete keywords. Args: ids — comma-separated keyword IDs."""
    return _to_json(_get_api().keywords_delete(_ids(ids)))


@mcp.tool()
def yd_keywords_suspend(ids: str) -> str:
    """Suspend keywords. Args: ids — comma-separated keyword IDs."""
    return _to_json(_get_api().keywords_suspend(_ids(ids)))


@mcp.tool()
def yd_keywords_resume(ids: str) -> str:
    """Resume keywords. Args: ids — comma-separated keyword IDs."""
    return _to_json(_get_api().keywords_resume(_ids(ids)))


# ── Bids ────────────────────────────────────────────────────────────────


@mcp.tool()
def yd_bids_get(params_json: str) -> str:
    """Get bids. Args: params_json — JSON with SelectionCriteria, FieldNames, Page."""
    return _to_json(_get_api().bids_get(_parse_json(params_json, "params_json")))


@mcp.tool()
def yd_bids_set(params_json: str) -> str:
    """Set bids. Args: params_json — JSON with Bids array."""
    return _to_json(_get_api().bids_set(_parse_json(params_json, "params_json")))


@mcp.tool()
def yd_bids_set_auto(params_json: str) -> str:
    """Set auto bids. Args: params_json — JSON with Bids array."""
    return _to_json(_get_api().bids_set_auto(_parse_json(params_json, "params_json")))


# ── BidModifiers ────────────────────────────────────────────────────────


@mcp.tool()
def yd_bidmodifiers_get(params_json: str) -> str:
    """Get bid modifiers. Args: params_json — JSON with SelectionCriteria, FieldNames, Page."""
    return _to_json(_get_api().bidmodifiers_get(_parse_json(params_json, "params_json")))


@mcp.tool()
def yd_bidmodifiers_add(params_json: str) -> str:
    """Add bid modifiers. Args: params_json — JSON with BidModifiers array."""
    return _to_json(_get_api().bidmodifiers_add(_parse_json(params_json, "params_json")))


@mcp.tool()
def yd_bidmodifiers_delete(params_json: str) -> str:
    """Delete bid modifiers. Args: params_json — JSON with SelectionCriteria."""
    return _to_json(_get_api().bidmodifiers_delete(_parse_json(params_json, "params_json")))


@mcp.tool()
def yd_bidmodifiers_set(params_json: str) -> str:
    """Set bid modifiers. Args: params_json — JSON with BidModifiers array."""
    return _to_json(_get_api().bidmodifiers_set(_parse_json(params_json, "params_json")))


# ── Sitelinks ───────────────────────────────────────────────────────────


@mcp.tool()
def yd_sitelinks_get(params_json: str) -> str:
    """Get sitelinks sets. Args: params_json — JSON with SelectionCriteria, FieldNames, Page."""
    return _to_json(_get_api().sitelinks_get(_parse_json(params_json, "params_json")))


@mcp.tool()
def yd_sitelinks_add(params_json: str) -> str:
    """Add sitelinks sets. Args: params_json — JSON with SitelinksSets array."""
    return _to_json(_get_api().sitelinks_add(_parse_json(params_json, "params_json")))


@mcp.tool()
def yd_sitelinks_delete(ids: str) -> str:
    """Delete sitelinks sets. Args: ids — comma-separated sitelinks set IDs."""
    return _to_json(_get_api().sitelinks_delete(_ids(ids)))


# ── AdImages ────────────────────────────────────────────────────────────


@mcp.tool()
def yd_adimages_get(params_json: str) -> str:
    """Get ad images. Args: params_json — JSON with SelectionCriteria, FieldNames, Page."""
    return _to_json(_get_api().adimages_get(_parse_json(params_json, "params_json")))


@mcp.tool()
def yd_adimages_add(params_json: str) -> str:
    """Add ad images. Args: params_json — JSON with AdImages array."""
    return _to_json(_get_api().adimages_add(_parse_json(params_json, "params_json")))


@mcp.tool()
def yd_adimages_delete(params_json: str) -> str:
    """Delete ad images. Args: params_json — JSON with SelectionCriteria (AdImageHashes)."""
    return _to_json(_get_api().adimages_delete(_parse_json(params_json, "params_json")))


# ── AdVideos ────────────────────────────────────────────────────────────


@mcp.tool()
def yd_advideos_get(params_json: str) -> str:
    """Get ad videos. Args: params_json — JSON with SelectionCriteria, FieldNames, Page."""
    return _to_json(_get_api().advideos_get(_parse_json(params_json, "params_json")))


@mcp.tool()
def yd_advideos_add(params_json: str) -> str:
    """Add ad videos. Args: params_json — JSON with AdVideos array."""
    return _to_json(_get_api().advideos_add(_parse_json(params_json, "params_json")))


# ── AdExtensions ────────────────────────────────────────────────────────


@mcp.tool()
def yd_adextensions_get(params_json: str) -> str:
    """Get ad extensions. Args: params_json — JSON with SelectionCriteria, FieldNames, Page."""
    return _to_json(_get_api().adextensions_get(_parse_json(params_json, "params_json")))


@mcp.tool()
def yd_adextensions_add(params_json: str) -> str:
    """Add ad extensions. Args: params_json — JSON with AdExtensions array."""
    return _to_json(_get_api().adextensions_add(_parse_json(params_json, "params_json")))


@mcp.tool()
def yd_adextensions_delete(ids: str) -> str:
    """Delete ad extensions. Args: ids — comma-separated ad extension IDs."""
    return _to_json(_get_api().adextensions_delete(_ids(ids)))


# ── AudienceTargets ─────────────────────────────────────────────────────


@mcp.tool()
def yd_audiencetargets_get(params_json: str) -> str:
    """Get audience targets. Args: params_json — JSON with SelectionCriteria, FieldNames, Page."""
    return _to_json(_get_api().audiencetargets_get(_parse_json(params_json, "params_json")))


@mcp.tool()
def yd_audiencetargets_add(params_json: str) -> str:
    """Add audience targets. Args: params_json — JSON with AudienceTargets array."""
    return _to_json(_get_api().audiencetargets_add(_parse_json(params_json, "params_json")))


@mcp.tool()
def yd_audiencetargets_delete(ids: str) -> str:
    """Delete audience targets. Args: ids — comma-separated audience target IDs."""
    return _to_json(_get_api().audiencetargets_delete(_ids(ids)))


@mcp.tool()
def yd_audiencetargets_suspend(ids: str) -> str:
    """Suspend audience targets. Args: ids — comma-separated audience target IDs."""
    return _to_json(_get_api().audiencetargets_suspend(_ids(ids)))


@mcp.tool()
def yd_audiencetargets_resume(ids: str) -> str:
    """Resume audience targets. Args: ids — comma-separated audience target IDs."""
    return _to_json(_get_api().audiencetargets_resume(_ids(ids)))


@mcp.tool()
def yd_audiencetargets_set_bids(params_json: str) -> str:
    """Set bids for audience targets. Args: params_json — JSON with Bids array."""
    return _to_json(_get_api().audiencetargets_set_bids(_parse_json(params_json, "params_json")))


# ── RetargetingLists ────────────────────────────────────────────────────


@mcp.tool()
def yd_retargetinglists_get(params_json: str) -> str:
    """Get retargeting lists. Args: params_json — JSON with SelectionCriteria, FieldNames, Page."""
    return _to_json(_get_api().retargetinglists_get(_parse_json(params_json, "params_json")))


@mcp.tool()
def yd_retargetinglists_add(params_json: str) -> str:
    """Add retargeting lists. Args: params_json — JSON with RetargetingLists array."""
    return _to_json(_get_api().retargetinglists_add(_parse_json(params_json, "params_json")))


@mcp.tool()
def yd_retargetinglists_update(params_json: str) -> str:
    """Update retargeting lists. Args: params_json — JSON with RetargetingLists array."""
    return _to_json(_get_api().retargetinglists_update(_parse_json(params_json, "params_json")))


@mcp.tool()
def yd_retargetinglists_delete(ids: str) -> str:
    """Delete retargeting lists. Args: ids — comma-separated retargeting list IDs."""
    return _to_json(_get_api().retargetinglists_delete(_ids(ids)))


# ── NegativeKeywordSharedSets ───────────────────────────────────────────


@mcp.tool()
def yd_negkeywordsets_get(params_json: str) -> str:
    """Get negative keyword shared sets. Args: params_json — JSON with SelectionCriteria, FieldNames, Page."""
    return _to_json(_get_api().negkeywordsets_get(_parse_json(params_json, "params_json")))


@mcp.tool()
def yd_negkeywordsets_add(params_json: str) -> str:
    """Add negative keyword shared sets. Args: params_json — JSON with NegativeKeywordSharedSets array."""
    return _to_json(_get_api().negkeywordsets_add(_parse_json(params_json, "params_json")))


@mcp.tool()
def yd_negkeywordsets_update(params_json: str) -> str:
    """Update negative keyword shared sets. Args: params_json — JSON with NegativeKeywordSharedSets array."""
    return _to_json(_get_api().negkeywordsets_update(_parse_json(params_json, "params_json")))


@mcp.tool()
def yd_negkeywordsets_delete(ids: str) -> str:
    """Delete negative keyword shared sets. Args: ids — comma-separated set IDs."""
    return _to_json(_get_api().negkeywordsets_delete(_ids(ids)))


# ── Feeds ───────────────────────────────────────────────────────────────


@mcp.tool()
def yd_feeds_get(params_json: str) -> str:
    """Get feeds. Args: params_json — JSON with SelectionCriteria, FieldNames, Page."""
    return _to_json(_get_api().feeds_get(_parse_json(params_json, "params_json")))


@mcp.tool()
def yd_feeds_add(params_json: str) -> str:
    """Add feeds. Args: params_json — JSON with Feeds array."""
    return _to_json(_get_api().feeds_add(_parse_json(params_json, "params_json")))


@mcp.tool()
def yd_feeds_update(params_json: str) -> str:
    """Update feeds. Args: params_json — JSON with Feeds array."""
    return _to_json(_get_api().feeds_update(_parse_json(params_json, "params_json")))


@mcp.tool()
def yd_feeds_delete(ids: str) -> str:
    """Delete feeds. Args: ids — comma-separated feed IDs."""
    return _to_json(_get_api().feeds_delete(_ids(ids)))


# ── Creatives ───────────────────────────────────────────────────────────


@mcp.tool()
def yd_creatives_get(params_json: str) -> str:
    """Get creatives. Args: params_json — JSON with SelectionCriteria, FieldNames, Page."""
    return _to_json(_get_api().creatives_get(_parse_json(params_json, "params_json")))


@mcp.tool()
def yd_creatives_add(params_json: str) -> str:
    """Add creatives. Args: params_json — JSON with Creatives array."""
    return _to_json(_get_api().creatives_add(_parse_json(params_json, "params_json")))


# ── KeywordsResearch ────────────────────────────────────────────────────


@mcp.tool()
def yd_keywordsresearch_deduplicate(params_json: str) -> str:
    """Deduplicate keywords. Args: params_json — JSON with Keywords array."""
    return _to_json(_get_api().keywordsresearch_deduplicate(_parse_json(params_json, "params_json")))


@mcp.tool()
def yd_keywordsresearch_has_search_volume(params_json: str) -> str:
    """Check search volume for keywords. Args: params_json — JSON with Keywords array."""
    return _to_json(_get_api().keywordsresearch_has_search_volume(_parse_json(params_json, "params_json")))


# ── Leads ───────────────────────────────────────────────────────────────


@mcp.tool()
def yd_leads_get(params_json: str) -> str:
    """Get leads from Turbo pages. Args: params_json — JSON with SelectionCriteria, FieldNames, Page."""
    return _to_json(_get_api().leads_get(_parse_json(params_json, "params_json")))


# ── Changes ─────────────────────────────────────────────────────────────


@mcp.tool()
def yd_changes_check(params_json: str) -> str:
    """Check changes. Args: params_json — JSON with FieldNames, Timestamp, CampaignIds, etc."""
    return _to_json(_get_api().changes_check(_parse_json(params_json, "params_json")))


@mcp.tool()
def yd_changes_check_dictionaries(params_json: str = "{}") -> str:
    """Check dictionary changes. Args: params_json — JSON (can be empty {})."""
    p = _parse_json(params_json, "params_json")
    return _to_json(_get_api().changes_check_dictionaries(p or None))


@mcp.tool()
def yd_changes_check_campaigns(params_json: str) -> str:
    """Check campaign changes. Args: params_json — JSON with Timestamp."""
    return _to_json(_get_api().changes_check_campaigns(_parse_json(params_json, "params_json")))


# ── Dictionaries ────────────────────────────────────────────────────────


@mcp.tool()
def yd_dictionaries_get(names: str) -> str:
    """Get dictionaries. Args: names — comma-separated: Currencies,Regions,TimeZones,GeoRegions,MetroStations,Constants,AdCategories,OperationSystemVersions,ProductivityAssertions,SupplySidePlatforms,Interests,AudienceCriteriaTypes,AudienceDemographicProfiles,FilterSchemas."""
    name_list = [n.strip() for n in names.split(",")]
    return _to_json(_get_api().dictionaries_get({"DictionaryNames": name_list}))


# ── Clients ─────────────────────────────────────────────────────────────


@mcp.tool()
def yd_clients_get(params_json: str) -> str:
    """Get client info. Args: params_json — JSON with FieldNames."""
    return _to_json(_get_api().clients_get(_parse_json(params_json, "params_json")))


@mcp.tool()
def yd_clients_update(params_json: str) -> str:
    """Update client settings. Args: params_json — JSON with Clients array."""
    return _to_json(_get_api().clients_update(_parse_json(params_json, "params_json")))


# ── AgencyClients ───────────────────────────────────────────────────────


@mcp.tool()
def yd_agencyclients_get(params_json: str) -> str:
    """Get agency clients. Args: params_json — JSON with SelectionCriteria, FieldNames, Page."""
    return _to_json(_get_api().agencyclients_get(_parse_json(params_json, "params_json")))


@mcp.tool()
def yd_agencyclients_add(params_json: str) -> str:
    """Add agency clients. Args: params_json — JSON with Clients array."""
    return _to_json(_get_api().agencyclients_add(_parse_json(params_json, "params_json")))


@mcp.tool()
def yd_agencyclients_update(params_json: str) -> str:
    """Update agency clients. Args: params_json — JSON with Clients array."""
    return _to_json(_get_api().agencyclients_update(_parse_json(params_json, "params_json")))


# ── TurboPages ──────────────────────────────────────────────────────────


@mcp.tool()
def yd_turbopages_get(params_json: str) -> str:
    """Get Turbo pages. Args: params_json — JSON with SelectionCriteria, FieldNames, Page."""
    return _to_json(_get_api().turbopages_get(_parse_json(params_json, "params_json")))


# ── Reports ─────────────────────────────────────────────────────────────


@mcp.tool()
def yd_reports_get(params_json: str, headers_json: str = "{}") -> str:
    """Get report (TSV). Args: params_json — JSON report definition, headers_json — optional extra headers JSON."""
    extra = _parse_json(headers_json, "headers_json")
    return _get_api().reports_get(_parse_json(params_json, "params_json"), extra or None)
