"""Tests for CLI interface — all 79 commands."""

import re
from pathlib import Path
from unittest.mock import patch

import pytest

from mcp_server_yandex_direct.cli import main


def test_cli_parsers_count():
    src = (Path(__file__).parent.parent / "src/mcp_server_yandex_direct/cli.py").read_text()
    parsers = set(re.findall(r'sub\.add_parser\("([^"]+)"', src))
    assert len(parsers) == 79, f"Expected 79 subparsers, got {len(parsers)}"


def test_cli_commands_count():
    # All 79 ACTIONS + 3 special cases (ids_commands, dictionaries-get, changes-check-dictionaries, reports-get)
    # are handled via elif branches — check ACTIONS has 79 entries
    from mcp_server_yandex_direct.actions import ACTIONS
    assert len(ACTIONS) == 79


# Verify each subparser exists in ACTIONS or is a known special case
def test_cli_parity():
    src = (Path(__file__).parent.parent / "src/mcp_server_yandex_direct/cli.py").read_text()
    parsers = set(re.findall(r'sub\.add_parser\("([^"]+)"', src))
    from mcp_server_yandex_direct.actions import ACTIONS
    for cmd in parsers:
        assert cmd in ACTIONS, f"CLI subparser '{cmd}' has no corresponding ACTIONS entry"


# (argv_list, api_method_name, expected_call_args)
# fmt: off
CLI_COMMANDS = [
    # params_json commands (pass raw JSON dict to API)
    (["campaigns-get", "{}"],               "campaigns_get",                   True),
    (["campaigns-add", "{}"],               "campaigns_add",                   True),
    (["campaigns-update", "{}"],            "campaigns_update",                True),
    # ids commands (SelectionCriteria.Ids)
    (["campaigns-delete", "1,2"],           "campaigns_delete",                True),
    (["campaigns-suspend", "1"],            "campaigns_suspend",               True),
    (["campaigns-resume", "1"],             "campaigns_resume",                True),
    (["campaigns-archive", "1"],            "campaigns_archive",               True),
    (["campaigns-unarchive", "1"],          "campaigns_unarchive",             True),
    # adgroups
    (["adgroups-get", "{}"],                "adgroups_get",                    True),
    (["adgroups-add", "{}"],                "adgroups_add",                    True),
    (["adgroups-update", "{}"],             "adgroups_update",                 True),
    (["adgroups-delete", "1,2"],            "adgroups_delete",                 True),
    # ads
    (["ads-get", "{}"],                     "ads_get",                         True),
    (["ads-add", "{}"],                     "ads_add",                         True),
    (["ads-update", "{}"],                  "ads_update",                      True),
    (["ads-delete", "1"],                   "ads_delete",                      True),
    (["ads-suspend", "1"],                  "ads_suspend",                     True),
    (["ads-resume", "1"],                   "ads_resume",                      True),
    (["ads-archive", "1"],                  "ads_archive",                     True),
    (["ads-unarchive", "1"],               "ads_unarchive",                   True),
    (["ads-moderate", "1"],                "ads_moderate",                    True),
    # keywords
    (["keywords-get", "{}"],               "keywords_get",                    True),
    (["keywords-add", "{}"],               "keywords_add",                    True),
    (["keywords-update", "{}"],            "keywords_update",                 True),
    (["keywords-delete", "1"],             "keywords_delete",                 True),
    (["keywords-suspend", "1"],            "keywords_suspend",                True),
    (["keywords-resume", "1"],             "keywords_resume",                 True),
    # bids
    (["bids-get", "{}"],                   "bids_get",                        True),
    (["bids-set", "{}"],                   "bids_set",                        True),
    (["bids-set-auto", "{}"],              "bids_set_auto",                   True),
    # bidmodifiers
    (["bidmodifiers-get", "{}"],           "bidmodifiers_get",                True),
    (["bidmodifiers-add", "{}"],           "bidmodifiers_add",                True),
    (["bidmodifiers-delete", "{}"],        "bidmodifiers_delete",             True),
    (["bidmodifiers-set", "{}"],           "bidmodifiers_set",                True),
    # sitelinks
    (["sitelinks-get", "{}"],              "sitelinks_get",                   True),
    (["sitelinks-add", "{}"],              "sitelinks_add",                   True),
    (["sitelinks-delete", "1"],            "sitelinks_delete",                True),
    # adimages
    (["adimages-get", "{}"],               "adimages_get",                    True),
    (["adimages-add", "{}"],               "adimages_add",                    True),
    (["adimages-delete", "{}"],            "adimages_delete",                 True),
    # advideos
    (["advideos-get", "{}"],               "advideos_get",                    True),
    (["advideos-add", "{}"],               "advideos_add",                    True),
    # adextensions
    (["adextensions-get", "{}"],           "adextensions_get",                True),
    (["adextensions-add", "{}"],           "adextensions_add",                True),
    (["adextensions-delete", "1"],         "adextensions_delete",             True),
    # audiencetargets
    (["audiencetargets-get", "{}"],        "audiencetargets_get",             True),
    (["audiencetargets-add", "{}"],        "audiencetargets_add",             True),
    (["audiencetargets-delete", "1"],      "audiencetargets_delete",          True),
    (["audiencetargets-suspend", "1"],     "audiencetargets_suspend",         True),
    (["audiencetargets-resume", "1"],      "audiencetargets_resume",          True),
    (["audiencetargets-set-bids", "{}"],   "audiencetargets_set_bids",        True),
    # retargetinglists
    (["retargetinglists-get", "{}"],       "retargetinglists_get",            True),
    (["retargetinglists-add", "{}"],       "retargetinglists_add",            True),
    (["retargetinglists-update", "{}"],    "retargetinglists_update",         True),
    (["retargetinglists-delete", "1"],     "retargetinglists_delete",         True),
    # negkeywordsets
    (["negkeywordsets-get", "{}"],         "negkeywordsets_get",              True),
    (["negkeywordsets-add", "{}"],         "negkeywordsets_add",              True),
    (["negkeywordsets-update", "{}"],      "negkeywordsets_update",           True),
    (["negkeywordsets-delete", "1"],       "negkeywordsets_delete",           True),
    # feeds
    (["feeds-get", "{}"],                  "feeds_get",                       True),
    (["feeds-add", "{}"],                  "feeds_add",                       True),
    (["feeds-update", "{}"],               "feeds_update",                    True),
    (["feeds-delete", "1"],                "feeds_delete",                    True),
    # creatives
    (["creatives-get", "{}"],              "creatives_get",                   True),
    (["creatives-add", "{}"],              "creatives_add",                   True),
    # keywordsresearch
    (["keywordsresearch-deduplicate", "{}"],          "keywordsresearch_deduplicate",       True),
    (["keywordsresearch-has-search-volume", "{}"],    "keywordsresearch_has_search_volume", True),
    # leads
    (["leads-get", "{}"],                  "leads_get",                       True),
    # changes
    (["changes-check", "{}"],              "changes_check",                   True),
    (["changes-check-dictionaries"],       "changes_check_dictionaries",      True),
    (["changes-check-campaigns", "{}"],    "changes_check_campaigns",         True),
    # dictionaries
    (["dictionaries-get", "Currencies"],   "dictionaries_get",                True),
    # clients
    (["clients-get", "{}"],                "clients_get",                     True),
    (["clients-update", "{}"],             "clients_update",                  True),
    # agencyclients
    (["agencyclients-get", "{}"],          "agencyclients_get",               True),
    (["agencyclients-add", "{}"],          "agencyclients_add",               True),
    (["agencyclients-update", "{}"],       "agencyclients_update",            True),
    # turbopages
    (["turbopages-get", "{}"],             "turbopages_get",                  True),
    # reports
    (["reports-get", "{}"],                "reports_get",                     True),
]
# fmt: on


@pytest.mark.parametrize("argv,api_method,_", CLI_COMMANDS)
def test_cli_command(argv, api_method, _):
    # Patch _dispatch to bypass Pydantic validation — we only verify routing here
    with patch("mcp_server_yandex_direct.cli._dispatch", return_value={}) as mock_dispatch:
        with patch("mcp_server_yandex_direct.cli._get_api"):
            with patch("builtins.print"):
                main(argv)
    mock_dispatch.assert_called_once()
    # Verify the action routed to the correct API method
    action_arg = mock_dispatch.call_args[0][0]
    assert action_arg.api_method == api_method
