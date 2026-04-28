"""Client for Yandex Direct API v5.

Docs: https://yandex.com/dev/direct/doc/en/concepts/overview
Base URL: https://api.direct.yandex.com/json/v5/{service}
Auth: Authorization: Bearer {token}
Protocol: JSON-RPC-like — POST with {"method": "...", "params": {...}}
"""

import logging
import sys

import requests

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s", stream=sys.stderr)
log = logging.getLogger(__name__)

BASE_URL = "https://api.direct.yandex.com/json/v5"


class YandexDirectAPI:
    """Synchronous client for Yandex Direct API v5."""

    def __init__(self, token: str, client_login: str = "", lang: str = ""):
        self.session = requests.Session()
        self.session.headers.update({
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json; charset=utf-8",
            "Accept": "application/json",
        })
        if client_login:
            self.session.headers["Client-Login"] = client_login
        if lang:
            self.session.headers["Accept-Language"] = lang

    def _call(self, service: str, method: str, params: dict | None = None) -> dict:
        """Universal method for all Yandex Direct API v5 calls."""
        body: dict = {"method": method}
        if params is not None:
            body["params"] = params
        resp = self.session.post(f"{BASE_URL}/{service}", json=body, timeout=30)
        if not resp.ok:
            raise RuntimeError(f"{service}.{method} -> HTTP {resp.status_code}: {resp.text}")
        data = resp.json()
        if "error" in data:
            err = data["error"]
            raise RuntimeError(
                f"{service}.{method} -> error {err.get('error_code')}: "
                f"{err.get('error_string', '')} — {err.get('error_detail', '')}"
            )
        return data.get("result", data)

    def _call_report(self, body: dict, extra_headers: dict | None = None) -> str:
        """Call Reports API — returns raw TSV/CSV text."""
        headers = dict(self.session.headers)
        if extra_headers:
            headers.update(extra_headers)
        resp = self.session.post(
            f"{BASE_URL}/reports",
            json=body,
            headers=headers,
            timeout=120,
        )
        if not resp.ok:
            raise RuntimeError(f"reports -> HTTP {resp.status_code}: {resp.text}")
        return resp.text

    # ── Campaigns ──────────────────────────────────────────────────────

    def campaigns_get(self, params: dict) -> dict:
        return self._call("campaigns", "get", params)

    def campaigns_add(self, params: dict) -> dict:
        return self._call("campaigns", "add", params)

    def campaigns_update(self, params: dict) -> dict:
        return self._call("campaigns", "update", params)

    def campaigns_delete(self, params: dict) -> dict:
        return self._call("campaigns", "delete", params)

    def campaigns_suspend(self, params: dict) -> dict:
        return self._call("campaigns", "suspend", params)

    def campaigns_resume(self, params: dict) -> dict:
        return self._call("campaigns", "resume", params)

    def campaigns_archive(self, params: dict) -> dict:
        return self._call("campaigns", "archive", params)

    def campaigns_unarchive(self, params: dict) -> dict:
        return self._call("campaigns", "unarchive", params)

    # ── AdGroups ───────────────────────────────────────────────────────

    def adgroups_get(self, params: dict) -> dict:
        return self._call("adgroups", "get", params)

    def adgroups_add(self, params: dict) -> dict:
        return self._call("adgroups", "add", params)

    def adgroups_update(self, params: dict) -> dict:
        return self._call("adgroups", "update", params)

    def adgroups_delete(self, params: dict) -> dict:
        return self._call("adgroups", "delete", params)

    # ── Ads ─────────────────────────────────────────────────────────────

    def ads_get(self, params: dict) -> dict:
        return self._call("ads", "get", params)

    def ads_add(self, params: dict) -> dict:
        return self._call("ads", "add", params)

    def ads_update(self, params: dict) -> dict:
        return self._call("ads", "update", params)

    def ads_delete(self, params: dict) -> dict:
        return self._call("ads", "delete", params)

    def ads_suspend(self, params: dict) -> dict:
        return self._call("ads", "suspend", params)

    def ads_resume(self, params: dict) -> dict:
        return self._call("ads", "resume", params)

    def ads_archive(self, params: dict) -> dict:
        return self._call("ads", "archive", params)

    def ads_unarchive(self, params: dict) -> dict:
        return self._call("ads", "unarchive", params)

    def ads_moderate(self, params: dict) -> dict:
        return self._call("ads", "moderate", params)

    # ── Keywords ────────────────────────────────────────────────────────

    def keywords_get(self, params: dict) -> dict:
        return self._call("keywords", "get", params)

    def keywords_add(self, params: dict) -> dict:
        return self._call("keywords", "add", params)

    def keywords_update(self, params: dict) -> dict:
        return self._call("keywords", "update", params)

    def keywords_delete(self, params: dict) -> dict:
        return self._call("keywords", "delete", params)

    def keywords_suspend(self, params: dict) -> dict:
        return self._call("keywords", "suspend", params)

    def keywords_resume(self, params: dict) -> dict:
        return self._call("keywords", "resume", params)

    # ── Bids ────────────────────────────────────────────────────────────

    def bids_get(self, params: dict) -> dict:
        return self._call("bids", "get", params)

    def bids_set(self, params: dict) -> dict:
        return self._call("bids", "set", params)

    def bids_set_auto(self, params: dict) -> dict:
        return self._call("bids", "setAuto", params)

    # ── BidModifiers ────────────────────────────────────────────────────

    def bidmodifiers_get(self, params: dict) -> dict:
        return self._call("bidmodifiers", "get", params)

    def bidmodifiers_add(self, params: dict) -> dict:
        return self._call("bidmodifiers", "add", params)

    def bidmodifiers_delete(self, params: dict) -> dict:
        return self._call("bidmodifiers", "delete", params)

    def bidmodifiers_set(self, params: dict) -> dict:
        return self._call("bidmodifiers", "set", params)

    # ── Sitelinks ───────────────────────────────────────────────────────

    def sitelinks_get(self, params: dict) -> dict:
        return self._call("sitelinks", "get", params)

    def sitelinks_add(self, params: dict) -> dict:
        return self._call("sitelinks", "add", params)

    def sitelinks_delete(self, params: dict) -> dict:
        return self._call("sitelinks", "delete", params)

    # ── AdImages ────────────────────────────────────────────────────────

    def adimages_get(self, params: dict) -> dict:
        return self._call("adimages", "get", params)

    def adimages_add(self, params: dict) -> dict:
        return self._call("adimages", "add", params)

    def adimages_delete(self, params: dict) -> dict:
        return self._call("adimages", "delete", params)

    # ── AdVideos ────────────────────────────────────────────────────────

    def advideos_get(self, params: dict) -> dict:
        return self._call("advideos", "get", params)

    def advideos_add(self, params: dict) -> dict:
        return self._call("advideos", "add", params)

    # ── AdExtensions ────────────────────────────────────────────────────

    def adextensions_get(self, params: dict) -> dict:
        return self._call("adextensions", "get", params)

    def adextensions_add(self, params: dict) -> dict:
        return self._call("adextensions", "add", params)

    def adextensions_delete(self, params: dict) -> dict:
        return self._call("adextensions", "delete", params)

    # ── AudienceTargets ─────────────────────────────────────────────────

    def audiencetargets_get(self, params: dict) -> dict:
        return self._call("audiencetargets", "get", params)

    def audiencetargets_add(self, params: dict) -> dict:
        return self._call("audiencetargets", "add", params)

    def audiencetargets_delete(self, params: dict) -> dict:
        return self._call("audiencetargets", "delete", params)

    def audiencetargets_suspend(self, params: dict) -> dict:
        return self._call("audiencetargets", "suspend", params)

    def audiencetargets_resume(self, params: dict) -> dict:
        return self._call("audiencetargets", "resume", params)

    def audiencetargets_set_bids(self, params: dict) -> dict:
        return self._call("audiencetargets", "setBids", params)

    # ── RetargetingLists ────────────────────────────────────────────────

    def retargetinglists_get(self, params: dict) -> dict:
        return self._call("retargetinglists", "get", params)

    def retargetinglists_add(self, params: dict) -> dict:
        return self._call("retargetinglists", "add", params)

    def retargetinglists_update(self, params: dict) -> dict:
        return self._call("retargetinglists", "update", params)

    def retargetinglists_delete(self, params: dict) -> dict:
        return self._call("retargetinglists", "delete", params)

    # ── NegativeKeywordSharedSets ───────────────────────────────────────

    def negkeywordsets_get(self, params: dict) -> dict:
        return self._call("negativekeywordsharedsets", "get", params)

    def negkeywordsets_add(self, params: dict) -> dict:
        return self._call("negativekeywordsharedsets", "add", params)

    def negkeywordsets_update(self, params: dict) -> dict:
        return self._call("negativekeywordsharedsets", "update", params)

    def negkeywordsets_delete(self, params: dict) -> dict:
        return self._call("negativekeywordsharedsets", "delete", params)

    # ── Feeds ───────────────────────────────────────────────────────────

    def feeds_get(self, params: dict) -> dict:
        return self._call("feeds", "get", params)

    def feeds_add(self, params: dict) -> dict:
        return self._call("feeds", "add", params)

    def feeds_update(self, params: dict) -> dict:
        return self._call("feeds", "update", params)

    def feeds_delete(self, params: dict) -> dict:
        return self._call("feeds", "delete", params)

    # ── Creatives ───────────────────────────────────────────────────────

    def creatives_get(self, params: dict) -> dict:
        return self._call("creatives", "get", params)

    def creatives_add(self, params: dict) -> dict:
        return self._call("creatives", "add", params)

    # ── KeywordsResearch ────────────────────────────────────────────────

    def keywordsresearch_deduplicate(self, params: dict) -> dict:
        return self._call("keywordsresearch", "deduplicate", params)

    def keywordsresearch_has_search_volume(self, params: dict) -> dict:
        return self._call("keywordsresearch", "hasSearchVolume", params)

    # ── Leads ───────────────────────────────────────────────────────────

    def leads_get(self, params: dict) -> dict:
        return self._call("leads", "get", params)

    # ── Changes ─────────────────────────────────────────────────────────

    def changes_check(self, params: dict) -> dict:
        return self._call("changes", "check", params)

    def changes_check_dictionaries(self, params: dict | None = None) -> dict:
        return self._call("changes", "checkDictionaries", params)

    def changes_check_campaigns(self, params: dict) -> dict:
        return self._call("changes", "checkCampaigns", params)

    # ── Dictionaries ────────────────────────────────────────────────────

    def dictionaries_get(self, params: dict) -> dict:
        return self._call("dictionaries", "get", params)

    # ── Clients ─────────────────────────────────────────────────────────

    def clients_get(self, params: dict) -> dict:
        return self._call("clients", "get", params)

    def clients_update(self, params: dict) -> dict:
        return self._call("clients", "update", params)

    # ── AgencyClients ───────────────────────────────────────────────────

    def agencyclients_get(self, params: dict) -> dict:
        return self._call("agencyclients", "get", params)

    def agencyclients_add(self, params: dict) -> dict:
        return self._call("agencyclients", "add", params)

    def agencyclients_update(self, params: dict) -> dict:
        return self._call("agencyclients", "update", params)

    # ── TurboPages ──────────────────────────────────────────────────────

    def turbopages_get(self, params: dict) -> dict:
        return self._call("turbopages", "get", params)

    # ── Reports ─────────────────────────────────────────────────────────

    def reports_get(self, body: dict, extra_headers: dict | None = None) -> str:
        return self._call_report(body, extra_headers)
