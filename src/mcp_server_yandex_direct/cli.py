"""CLI interface for Yandex Direct tools.

Usage: mcp-server-yandex-direct <command> [options]
Without arguments starts MCP server (stdio transport).
"""

import argparse
import json
import sys

from . import __version__
from . import server


def main(argv: list[str] | None = None):
    parser = argparse.ArgumentParser(
        prog="mcp-server-yandex-direct",
        description="Yandex Direct: MCP-server and CLI",
    )
    parser.add_argument("--version", action="version", version=f"%(prog)s {__version__}")
    sub = parser.add_subparsers(dest="command")

    # ── Campaigns ──
    p = sub.add_parser("campaigns-get", help="Get campaigns")
    p.add_argument("params_json")

    p = sub.add_parser("campaigns-add", help="Add campaigns")
    p.add_argument("params_json")

    p = sub.add_parser("campaigns-update", help="Update campaigns")
    p.add_argument("params_json")

    p = sub.add_parser("campaigns-delete", help="Delete campaigns")
    p.add_argument("ids")

    p = sub.add_parser("campaigns-suspend", help="Suspend campaigns")
    p.add_argument("ids")

    p = sub.add_parser("campaigns-resume", help="Resume campaigns")
    p.add_argument("ids")

    p = sub.add_parser("campaigns-archive", help="Archive campaigns")
    p.add_argument("ids")

    p = sub.add_parser("campaigns-unarchive", help="Unarchive campaigns")
    p.add_argument("ids")

    # ── AdGroups ──
    p = sub.add_parser("adgroups-get", help="Get ad groups")
    p.add_argument("params_json")

    p = sub.add_parser("adgroups-add", help="Add ad groups")
    p.add_argument("params_json")

    p = sub.add_parser("adgroups-update", help="Update ad groups")
    p.add_argument("params_json")

    p = sub.add_parser("adgroups-delete", help="Delete ad groups")
    p.add_argument("ids")

    # ── Ads ──
    p = sub.add_parser("ads-get", help="Get ads")
    p.add_argument("params_json")

    p = sub.add_parser("ads-add", help="Add ads")
    p.add_argument("params_json")

    p = sub.add_parser("ads-update", help="Update ads")
    p.add_argument("params_json")

    p = sub.add_parser("ads-delete", help="Delete ads")
    p.add_argument("ids")

    p = sub.add_parser("ads-suspend", help="Suspend ads")
    p.add_argument("ids")

    p = sub.add_parser("ads-resume", help="Resume ads")
    p.add_argument("ids")

    p = sub.add_parser("ads-archive", help="Archive ads")
    p.add_argument("ids")

    p = sub.add_parser("ads-unarchive", help="Unarchive ads")
    p.add_argument("ids")

    p = sub.add_parser("ads-moderate", help="Moderate ads")
    p.add_argument("ids")

    # ── Keywords ──
    p = sub.add_parser("keywords-get", help="Get keywords")
    p.add_argument("params_json")

    p = sub.add_parser("keywords-add", help="Add keywords")
    p.add_argument("params_json")

    p = sub.add_parser("keywords-update", help="Update keywords")
    p.add_argument("params_json")

    p = sub.add_parser("keywords-delete", help="Delete keywords")
    p.add_argument("ids")

    p = sub.add_parser("keywords-suspend", help="Suspend keywords")
    p.add_argument("ids")

    p = sub.add_parser("keywords-resume", help="Resume keywords")
    p.add_argument("ids")

    # ── Bids ──
    p = sub.add_parser("bids-get", help="Get bids")
    p.add_argument("params_json")

    p = sub.add_parser("bids-set", help="Set bids")
    p.add_argument("params_json")

    p = sub.add_parser("bids-set-auto", help="Set auto bids")
    p.add_argument("params_json")

    # ── BidModifiers ──
    p = sub.add_parser("bidmodifiers-get", help="Get bid modifiers")
    p.add_argument("params_json")

    p = sub.add_parser("bidmodifiers-add", help="Add bid modifiers")
    p.add_argument("params_json")

    p = sub.add_parser("bidmodifiers-delete", help="Delete bid modifiers")
    p.add_argument("params_json")

    p = sub.add_parser("bidmodifiers-set", help="Set bid modifiers")
    p.add_argument("params_json")

    # ── Sitelinks ──
    p = sub.add_parser("sitelinks-get", help="Get sitelinks")
    p.add_argument("params_json")

    p = sub.add_parser("sitelinks-add", help="Add sitelinks")
    p.add_argument("params_json")

    p = sub.add_parser("sitelinks-delete", help="Delete sitelinks")
    p.add_argument("ids")

    # ── AdImages ──
    p = sub.add_parser("adimages-get", help="Get ad images")
    p.add_argument("params_json")

    p = sub.add_parser("adimages-add", help="Add ad images")
    p.add_argument("params_json")

    p = sub.add_parser("adimages-delete", help="Delete ad images")
    p.add_argument("params_json")

    # ── AdVideos ──
    p = sub.add_parser("advideos-get", help="Get ad videos")
    p.add_argument("params_json")

    p = sub.add_parser("advideos-add", help="Add ad videos")
    p.add_argument("params_json")

    # ── AdExtensions ──
    p = sub.add_parser("adextensions-get", help="Get ad extensions")
    p.add_argument("params_json")

    p = sub.add_parser("adextensions-add", help="Add ad extensions")
    p.add_argument("params_json")

    p = sub.add_parser("adextensions-delete", help="Delete ad extensions")
    p.add_argument("ids")

    # ── AudienceTargets ──
    p = sub.add_parser("audiencetargets-get", help="Get audience targets")
    p.add_argument("params_json")

    p = sub.add_parser("audiencetargets-add", help="Add audience targets")
    p.add_argument("params_json")

    p = sub.add_parser("audiencetargets-delete", help="Delete audience targets")
    p.add_argument("ids")

    p = sub.add_parser("audiencetargets-suspend", help="Suspend audience targets")
    p.add_argument("ids")

    p = sub.add_parser("audiencetargets-resume", help="Resume audience targets")
    p.add_argument("ids")

    p = sub.add_parser("audiencetargets-set-bids", help="Set bids for audience targets")
    p.add_argument("params_json")

    # ── RetargetingLists ──
    p = sub.add_parser("retargetinglists-get", help="Get retargeting lists")
    p.add_argument("params_json")

    p = sub.add_parser("retargetinglists-add", help="Add retargeting lists")
    p.add_argument("params_json")

    p = sub.add_parser("retargetinglists-update", help="Update retargeting lists")
    p.add_argument("params_json")

    p = sub.add_parser("retargetinglists-delete", help="Delete retargeting lists")
    p.add_argument("ids")

    # ── NegativeKeywordSharedSets ──
    p = sub.add_parser("negkeywordsets-get", help="Get negative keyword shared sets")
    p.add_argument("params_json")

    p = sub.add_parser("negkeywordsets-add", help="Add negative keyword shared sets")
    p.add_argument("params_json")

    p = sub.add_parser("negkeywordsets-update", help="Update negative keyword shared sets")
    p.add_argument("params_json")

    p = sub.add_parser("negkeywordsets-delete", help="Delete negative keyword shared sets")
    p.add_argument("ids")

    # ── Feeds ──
    p = sub.add_parser("feeds-get", help="Get feeds")
    p.add_argument("params_json")

    p = sub.add_parser("feeds-add", help="Add feeds")
    p.add_argument("params_json")

    p = sub.add_parser("feeds-update", help="Update feeds")
    p.add_argument("params_json")

    p = sub.add_parser("feeds-delete", help="Delete feeds")
    p.add_argument("ids")

    # ── Creatives ──
    p = sub.add_parser("creatives-get", help="Get creatives")
    p.add_argument("params_json")

    p = sub.add_parser("creatives-add", help="Add creatives")
    p.add_argument("params_json")

    # ── KeywordsResearch ──
    p = sub.add_parser("keywordsresearch-deduplicate", help="Deduplicate keywords")
    p.add_argument("params_json")

    p = sub.add_parser("keywordsresearch-has-search-volume", help="Check keyword search volume")
    p.add_argument("params_json")

    # ── Leads ──
    p = sub.add_parser("leads-get", help="Get leads")
    p.add_argument("params_json")

    # ── Changes ──
    p = sub.add_parser("changes-check", help="Check changes")
    p.add_argument("params_json")

    p = sub.add_parser("changes-check-dictionaries", help="Check dictionary changes")
    p.add_argument("params_json", nargs="?", default="{}")

    p = sub.add_parser("changes-check-campaigns", help="Check campaign changes")
    p.add_argument("params_json")

    # ── Dictionaries ──
    p = sub.add_parser("dictionaries-get", help="Get dictionaries")
    p.add_argument("names", help="Comma-separated: Currencies,Regions,TimeZones,...")

    # ── Clients ──
    p = sub.add_parser("clients-get", help="Get client info")
    p.add_argument("params_json")

    p = sub.add_parser("clients-update", help="Update client settings")
    p.add_argument("params_json")

    # ── AgencyClients ──
    p = sub.add_parser("agencyclients-get", help="Get agency clients")
    p.add_argument("params_json")

    p = sub.add_parser("agencyclients-add", help="Add agency clients")
    p.add_argument("params_json")

    p = sub.add_parser("agencyclients-update", help="Update agency clients")
    p.add_argument("params_json")

    # ── TurboPages ──
    p = sub.add_parser("turbopages-get", help="Get Turbo pages")
    p.add_argument("params_json")

    # ── Reports ──
    p = sub.add_parser("reports-get", help="Get report (TSV)")
    p.add_argument("params_json")
    p.add_argument("--headers-json", default="{}")

    # ── Parse and dispatch ──

    args = parser.parse_args(argv)
    if not args.command:
        parser.print_help()
        sys.exit(1)

    handlers = {
        "campaigns-get": lambda: print(server.yd_campaigns_get(args.params_json)),
        "campaigns-add": lambda: print(server.yd_campaigns_add(args.params_json)),
        "campaigns-update": lambda: print(server.yd_campaigns_update(args.params_json)),
        "campaigns-delete": lambda: print(server.yd_campaigns_delete(args.ids)),
        "campaigns-suspend": lambda: print(server.yd_campaigns_suspend(args.ids)),
        "campaigns-resume": lambda: print(server.yd_campaigns_resume(args.ids)),
        "campaigns-archive": lambda: print(server.yd_campaigns_archive(args.ids)),
        "campaigns-unarchive": lambda: print(server.yd_campaigns_unarchive(args.ids)),
        "adgroups-get": lambda: print(server.yd_adgroups_get(args.params_json)),
        "adgroups-add": lambda: print(server.yd_adgroups_add(args.params_json)),
        "adgroups-update": lambda: print(server.yd_adgroups_update(args.params_json)),
        "adgroups-delete": lambda: print(server.yd_adgroups_delete(args.ids)),
        "ads-get": lambda: print(server.yd_ads_get(args.params_json)),
        "ads-add": lambda: print(server.yd_ads_add(args.params_json)),
        "ads-update": lambda: print(server.yd_ads_update(args.params_json)),
        "ads-delete": lambda: print(server.yd_ads_delete(args.ids)),
        "ads-suspend": lambda: print(server.yd_ads_suspend(args.ids)),
        "ads-resume": lambda: print(server.yd_ads_resume(args.ids)),
        "ads-archive": lambda: print(server.yd_ads_archive(args.ids)),
        "ads-unarchive": lambda: print(server.yd_ads_unarchive(args.ids)),
        "ads-moderate": lambda: print(server.yd_ads_moderate(args.ids)),
        "keywords-get": lambda: print(server.yd_keywords_get(args.params_json)),
        "keywords-add": lambda: print(server.yd_keywords_add(args.params_json)),
        "keywords-update": lambda: print(server.yd_keywords_update(args.params_json)),
        "keywords-delete": lambda: print(server.yd_keywords_delete(args.ids)),
        "keywords-suspend": lambda: print(server.yd_keywords_suspend(args.ids)),
        "keywords-resume": lambda: print(server.yd_keywords_resume(args.ids)),
        "bids-get": lambda: print(server.yd_bids_get(args.params_json)),
        "bids-set": lambda: print(server.yd_bids_set(args.params_json)),
        "bids-set-auto": lambda: print(server.yd_bids_set_auto(args.params_json)),
        "bidmodifiers-get": lambda: print(server.yd_bidmodifiers_get(args.params_json)),
        "bidmodifiers-add": lambda: print(server.yd_bidmodifiers_add(args.params_json)),
        "bidmodifiers-delete": lambda: print(server.yd_bidmodifiers_delete(args.params_json)),
        "bidmodifiers-set": lambda: print(server.yd_bidmodifiers_set(args.params_json)),
        "sitelinks-get": lambda: print(server.yd_sitelinks_get(args.params_json)),
        "sitelinks-add": lambda: print(server.yd_sitelinks_add(args.params_json)),
        "sitelinks-delete": lambda: print(server.yd_sitelinks_delete(args.ids)),
        "adimages-get": lambda: print(server.yd_adimages_get(args.params_json)),
        "adimages-add": lambda: print(server.yd_adimages_add(args.params_json)),
        "adimages-delete": lambda: print(server.yd_adimages_delete(args.params_json)),
        "advideos-get": lambda: print(server.yd_advideos_get(args.params_json)),
        "advideos-add": lambda: print(server.yd_advideos_add(args.params_json)),
        "adextensions-get": lambda: print(server.yd_adextensions_get(args.params_json)),
        "adextensions-add": lambda: print(server.yd_adextensions_add(args.params_json)),
        "adextensions-delete": lambda: print(server.yd_adextensions_delete(args.ids)),
        "audiencetargets-get": lambda: print(server.yd_audiencetargets_get(args.params_json)),
        "audiencetargets-add": lambda: print(server.yd_audiencetargets_add(args.params_json)),
        "audiencetargets-delete": lambda: print(server.yd_audiencetargets_delete(args.ids)),
        "audiencetargets-suspend": lambda: print(server.yd_audiencetargets_suspend(args.ids)),
        "audiencetargets-resume": lambda: print(server.yd_audiencetargets_resume(args.ids)),
        "audiencetargets-set-bids": lambda: print(server.yd_audiencetargets_set_bids(args.params_json)),
        "retargetinglists-get": lambda: print(server.yd_retargetinglists_get(args.params_json)),
        "retargetinglists-add": lambda: print(server.yd_retargetinglists_add(args.params_json)),
        "retargetinglists-update": lambda: print(server.yd_retargetinglists_update(args.params_json)),
        "retargetinglists-delete": lambda: print(server.yd_retargetinglists_delete(args.ids)),
        "negkeywordsets-get": lambda: print(server.yd_negkeywordsets_get(args.params_json)),
        "negkeywordsets-add": lambda: print(server.yd_negkeywordsets_add(args.params_json)),
        "negkeywordsets-update": lambda: print(server.yd_negkeywordsets_update(args.params_json)),
        "negkeywordsets-delete": lambda: print(server.yd_negkeywordsets_delete(args.ids)),
        "feeds-get": lambda: print(server.yd_feeds_get(args.params_json)),
        "feeds-add": lambda: print(server.yd_feeds_add(args.params_json)),
        "feeds-update": lambda: print(server.yd_feeds_update(args.params_json)),
        "feeds-delete": lambda: print(server.yd_feeds_delete(args.ids)),
        "creatives-get": lambda: print(server.yd_creatives_get(args.params_json)),
        "creatives-add": lambda: print(server.yd_creatives_add(args.params_json)),
        "keywordsresearch-deduplicate": lambda: print(server.yd_keywordsresearch_deduplicate(args.params_json)),
        "keywordsresearch-has-search-volume": lambda: print(server.yd_keywordsresearch_has_search_volume(args.params_json)),
        "leads-get": lambda: print(server.yd_leads_get(args.params_json)),
        "changes-check": lambda: print(server.yd_changes_check(args.params_json)),
        "changes-check-dictionaries": lambda: print(server.yd_changes_check_dictionaries(args.params_json)),
        "changes-check-campaigns": lambda: print(server.yd_changes_check_campaigns(args.params_json)),
        "dictionaries-get": lambda: print(server.yd_dictionaries_get(args.names)),
        "clients-get": lambda: print(server.yd_clients_get(args.params_json)),
        "clients-update": lambda: print(server.yd_clients_update(args.params_json)),
        "agencyclients-get": lambda: print(server.yd_agencyclients_get(args.params_json)),
        "agencyclients-add": lambda: print(server.yd_agencyclients_add(args.params_json)),
        "agencyclients-update": lambda: print(server.yd_agencyclients_update(args.params_json)),
        "turbopages-get": lambda: print(server.yd_turbopages_get(args.params_json)),
        "reports-get": lambda: print(server.yd_reports_get(args.params_json, args.headers_json)),
    }

    handler = handlers.get(args.command)
    if handler:
        handler()
    else:
        parser.print_help()
        sys.exit(1)
