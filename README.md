# mcp-server-yandex-direct

mcp-name: io.github.dontsovcmc/yandex-direct

MCP server for Yandex Direct API v5 — campaigns, ads, keywords, bids, audiences, retargeting, reports and more.

## Features

- 79 MCP tools covering all 22 Yandex Direct API v5 services + Reports
- CLI interface with 79 commands
- Pydantic models for request/response validation
- Agency mode support (`Client-Login` header)

## Installation

```bash
pip install mcp-server-yandex-direct
```

## Configuration

### Environment variables

| Variable | Required | Description |
|----------|----------|-------------|
| `YD_TOKEN` | Yes | OAuth token for Yandex Direct API |
| `YD_CLIENT_LOGIN` | No | Client login for agency accounts |
| `YD_LANG` | No | Response language: `ru`, `en`, `uk` |

### Claude Code

Add to your MCP settings:

```json
{
  "mcpServers": {
    "yandex-direct": {
      "command": "uvx",
      "args": ["mcp-server-yandex-direct"],
      "env": {
        "YD_TOKEN": "your-oauth-token"
      }
    }
  }
}
```

## CLI Usage

```bash
# Get campaigns
mcp-server-yandex-direct campaigns-get '{"SelectionCriteria": {}, "FieldNames": ["Id", "Name", "State"]}'

# Suspend campaigns
mcp-server-yandex-direct campaigns-suspend 123,456

# Get ads for a campaign
mcp-server-yandex-direct ads-get '{"SelectionCriteria": {"CampaignIds": [123]}, "FieldNames": ["Id", "Type", "State"]}'

# Get dictionaries
mcp-server-yandex-direct dictionaries-get Currencies,Regions

# Get report
mcp-server-yandex-direct reports-get '{"params": {"SelectionCriteria": {"DateFrom": "2026-01-01", "DateTo": "2026-04-28"}, "FieldNames": ["Date", "CampaignId", "Clicks", "Cost"], "ReportName": "My Report", "ReportType": "CAMPAIGN_PERFORMANCE_REPORT", "DateRangeType": "CUSTOM_DATE", "Format": "TSV"}}'
```

## API Services

| Service | Methods | Tools |
|---------|---------|-------|
| Campaigns | get, add, update, delete, suspend, resume, archive, unarchive | 8 |
| AdGroups | get, add, update, delete | 4 |
| Ads | get, add, update, delete, suspend, resume, archive, unarchive, moderate | 9 |
| Keywords | get, add, update, delete, suspend, resume | 6 |
| Bids | get, set, setAuto | 3 |
| BidModifiers | get, add, delete, set | 4 |
| Sitelinks | get, add, delete | 3 |
| AdImages | get, add, delete | 3 |
| AdVideos | get, add | 2 |
| AdExtensions | get, add, delete | 3 |
| AudienceTargets | get, add, delete, suspend, resume, setBids | 6 |
| RetargetingLists | get, add, update, delete | 4 |
| NegativeKeywordSharedSets | get, add, update, delete | 4 |
| Feeds | get, add, update, delete | 4 |
| Creatives | get, add | 2 |
| KeywordsResearch | deduplicate, hasSearchVolume | 2 |
| Leads | get | 1 |
| Changes | check, checkDictionaries, checkCampaigns | 3 |
| Dictionaries | get | 1 |
| Clients | get, update | 2 |
| AgencyClients | get, add, update | 3 |
| TurboPages | get | 1 |
| Reports | get | 1 |
| **Total** | | **79** |

## Development

```bash
pip install -e ".[test]"
pytest tests/ -v
```

## License

MIT
