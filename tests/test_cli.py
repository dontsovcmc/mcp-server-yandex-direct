"""Tests for CLI interface — all 79 commands."""

import re
from pathlib import Path
from unittest.mock import patch

import pytest

from mcp_server_yandex_direct.cli import main


def test_cli_parity():
    src = (Path(__file__).parent.parent / "src/mcp_server_yandex_direct/cli.py").read_text()
    parsers = set(re.findall(r'sub\.add_parser\("([^"]+)"', src))
    handlers = set(re.findall(r'"([^"]+)":\s*lambda', src))
    assert parsers == handlers, f"Mismatch: parsers-handlers={parsers - handlers}, handlers-parsers={handlers - parsers}"
    assert len(parsers) == 79


# (argv_list, expected_server_function_name)
# fmt: off
CLI_COMMANDS = [
    # --- campaigns ---
    (["campaigns-get", "{}"], "yd_campaigns_get"),
    (["campaigns-add", "{}"], "yd_campaigns_add"),
    (["campaigns-update", "{}"], "yd_campaigns_update"),
    (["campaigns-delete", "1,2"], "yd_campaigns_delete"),
    (["campaigns-suspend", "1"], "yd_campaigns_suspend"),
    (["campaigns-resume", "1"], "yd_campaigns_resume"),
    (["campaigns-archive", "1"], "yd_campaigns_archive"),
    (["campaigns-unarchive", "1"], "yd_campaigns_unarchive"),

    # --- adgroups ---
    (["adgroups-get", "{}"], "yd_adgroups_get"),
    (["adgroups-add", "{}"], "yd_adgroups_add"),
    (["adgroups-update", "{}"], "yd_adgroups_update"),
    (["adgroups-delete", "1,2"], "yd_adgroups_delete"),

    # --- ads ---
    (["ads-get", "{}"], "yd_ads_get"),
    (["ads-add", "{}"], "yd_ads_add"),
    (["ads-update", "{}"], "yd_ads_update"),
    (["ads-delete", "1"], "yd_ads_delete"),
    (["ads-suspend", "1"], "yd_ads_suspend"),
    (["ads-resume", "1"], "yd_ads_resume"),
    (["ads-archive", "1"], "yd_ads_archive"),
    (["ads-unarchive", "1"], "yd_ads_unarchive"),
    (["ads-moderate", "1"], "yd_ads_moderate"),

    # --- keywords ---
    (["keywords-get", "{}"], "yd_keywords_get"),
    (["keywords-add", "{}"], "yd_keywords_add"),
    (["keywords-update", "{}"], "yd_keywords_update"),
    (["keywords-delete", "1"], "yd_keywords_delete"),
    (["keywords-suspend", "1"], "yd_keywords_suspend"),
    (["keywords-resume", "1"], "yd_keywords_resume"),

    # --- bids ---
    (["bids-get", "{}"], "yd_bids_get"),
    (["bids-set", "{}"], "yd_bids_set"),
    (["bids-set-auto", "{}"], "yd_bids_set_auto"),

    # --- bidmodifiers ---
    (["bidmodifiers-get", "{}"], "yd_bidmodifiers_get"),
    (["bidmodifiers-add", "{}"], "yd_bidmodifiers_add"),
    (["bidmodifiers-delete", "{}"], "yd_bidmodifiers_delete"),
    (["bidmodifiers-set", "{}"], "yd_bidmodifiers_set"),

    # --- sitelinks ---
    (["sitelinks-get", "{}"], "yd_sitelinks_get"),
    (["sitelinks-add", "{}"], "yd_sitelinks_add"),
    (["sitelinks-delete", "1"], "yd_sitelinks_delete"),

    # --- adimages ---
    (["adimages-get", "{}"], "yd_adimages_get"),
    (["adimages-add", "{}"], "yd_adimages_add"),
    (["adimages-delete", "{}"], "yd_adimages_delete"),

    # --- advideos ---
    (["advideos-get", "{}"], "yd_advideos_get"),
    (["advideos-add", "{}"], "yd_advideos_add"),

    # --- adextensions ---
    (["adextensions-get", "{}"], "yd_adextensions_get"),
    (["adextensions-add", "{}"], "yd_adextensions_add"),
    (["adextensions-delete", "1"], "yd_adextensions_delete"),

    # --- audiencetargets ---
    (["audiencetargets-get", "{}"], "yd_audiencetargets_get"),
    (["audiencetargets-add", "{}"], "yd_audiencetargets_add"),
    (["audiencetargets-delete", "1"], "yd_audiencetargets_delete"),
    (["audiencetargets-suspend", "1"], "yd_audiencetargets_suspend"),
    (["audiencetargets-resume", "1"], "yd_audiencetargets_resume"),
    (["audiencetargets-set-bids", "{}"], "yd_audiencetargets_set_bids"),

    # --- retargetinglists ---
    (["retargetinglists-get", "{}"], "yd_retargetinglists_get"),
    (["retargetinglists-add", "{}"], "yd_retargetinglists_add"),
    (["retargetinglists-update", "{}"], "yd_retargetinglists_update"),
    (["retargetinglists-delete", "1"], "yd_retargetinglists_delete"),

    # --- negkeywordsets ---
    (["negkeywordsets-get", "{}"], "yd_negkeywordsets_get"),
    (["negkeywordsets-add", "{}"], "yd_negkeywordsets_add"),
    (["negkeywordsets-update", "{}"], "yd_negkeywordsets_update"),
    (["negkeywordsets-delete", "1"], "yd_negkeywordsets_delete"),

    # --- feeds ---
    (["feeds-get", "{}"], "yd_feeds_get"),
    (["feeds-add", "{}"], "yd_feeds_add"),
    (["feeds-update", "{}"], "yd_feeds_update"),
    (["feeds-delete", "1"], "yd_feeds_delete"),

    # --- creatives ---
    (["creatives-get", "{}"], "yd_creatives_get"),
    (["creatives-add", "{}"], "yd_creatives_add"),

    # --- keywordsresearch ---
    (["keywordsresearch-deduplicate", "{}"], "yd_keywordsresearch_deduplicate"),
    (["keywordsresearch-has-search-volume", "{}"], "yd_keywordsresearch_has_search_volume"),

    # --- leads ---
    (["leads-get", "{}"], "yd_leads_get"),

    # --- changes ---
    (["changes-check", "{}"], "yd_changes_check"),
    (["changes-check-dictionaries"], "yd_changes_check_dictionaries"),
    (["changes-check-campaigns", "{}"], "yd_changes_check_campaigns"),

    # --- dictionaries ---
    (["dictionaries-get", "Currencies"], "yd_dictionaries_get"),

    # --- clients ---
    (["clients-get", "{}"], "yd_clients_get"),
    (["clients-update", "{}"], "yd_clients_update"),

    # --- agencyclients ---
    (["agencyclients-get", "{}"], "yd_agencyclients_get"),
    (["agencyclients-add", "{}"], "yd_agencyclients_add"),
    (["agencyclients-update", "{}"], "yd_agencyclients_update"),

    # --- turbopages ---
    (["turbopages-get", "{}"], "yd_turbopages_get"),

    # --- reports ---
    (["reports-get", "{}"], "yd_reports_get"),
]
# fmt: on


def test_cli_commands_count():
    assert len(CLI_COMMANDS) == 79


@pytest.mark.parametrize("argv,expected_func", CLI_COMMANDS)
def test_cli_command(argv, expected_func):
    with patch("mcp_server_yandex_direct.cli.server") as mock_server:
        getattr(mock_server, expected_func).return_value = '{"status":"OK"}'
        with patch("builtins.print"):
            main(argv)
        getattr(mock_server, expected_func).assert_called_once()
