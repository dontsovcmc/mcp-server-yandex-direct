"""CLI interface for Yandex Direct tools.

Usage: mcp-server-yandex-direct <command> [options]
Without arguments starts MCP server (stdio transport).
"""

import argparse
import sys

from . import __version__
from .actions import ACTIONS
from .server import _dispatch, _get_api, _parse_json, _to_json


def _ids_params(ids_str: str) -> dict:
    """Convert comma-separated IDs string to SelectionCriteria dict."""
    return {"SelectionCriteria": {"Ids": [int(x.strip()) for x in ids_str.split(",")]}}


def main(argv: list[str] | None = None):
    parser = argparse.ArgumentParser(
        prog="mcp-server-yandex-direct",
        description="Yandex Direct: MCP-server and CLI",
    )
    parser.add_argument("--version", action="version", version=f"%(prog)s {__version__}")
    parser.add_argument("--env", metavar="PATH", help="Загрузить переменные окружения из файла (формат KEY=VALUE)")
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

    # Commands that take comma-separated integer IDs → SelectionCriteria
    _ids_commands = {
        "campaigns-delete", "campaigns-suspend", "campaigns-resume",
        "campaigns-archive", "campaigns-unarchive",
        "adgroups-delete",
        "ads-delete", "ads-suspend", "ads-resume", "ads-archive", "ads-unarchive", "ads-moderate",
        "keywords-delete", "keywords-suspend", "keywords-resume",
        "sitelinks-delete",
        "adextensions-delete",
        "audiencetargets-delete", "audiencetargets-suspend", "audiencetargets-resume",
        "retargetinglists-delete",
        "negkeywordsets-delete",
        "feeds-delete",
    }

    api = _get_api()

    if args.command in _ids_commands:
        params = _ids_params(args.ids)
        print(_to_json(_dispatch(ACTIONS[args.command], api, params)))
    elif args.command == "dictionaries-get":
        params = {"DictionaryNames": [n.strip() for n in args.names.split(",")]}
        print(_to_json(_dispatch(ACTIONS["dictionaries-get"], api, params)))
    elif args.command == "changes-check-dictionaries":
        print(_to_json(_dispatch(ACTIONS["changes-check-dictionaries"], api, {})))
    elif args.command == "reports-get":
        extra = _parse_json(args.headers_json, "headers_json") if args.headers_json != "{}" else None
        params = {"body": _parse_json(args.params_json, "params_json"), "extra_headers": extra}
        print(_to_json(_dispatch(ACTIONS["reports-get"], api, params)))
    elif args.command in ACTIONS:
        params = _parse_json(args.params_json, "params_json")
        print(_to_json(_dispatch(ACTIONS[args.command], api, params)))
    else:
        parser.print_help()
        sys.exit(1)
