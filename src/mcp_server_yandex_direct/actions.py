"""Action catalog for Yandex Direct API v5 — 79 actions across 16 domains."""

from dataclasses import dataclass, field

from pydantic import BaseModel

from .models import (
    # campaigns
    CampaignsGetParams,
    CampaignsAddParams,
    CampaignsUpdateParams,
    CampaignsActionParams,
    # adgroups
    AdGroupsGetParams,
    AdGroupsAddParams,
    AdGroupsUpdateParams,
    AdGroupsDeleteParams,
    # ads
    AdsGetParams,
    AdsAddParams,
    AdsUpdateParams,
    AdsActionParams,
    # keywords
    KeywordsGetParams,
    KeywordsAddParams,
    KeywordsUpdateParams,
    KeywordsActionParams,
    # bids
    BidsGetParams,
    BidsSetParams,
    BidsSetAutoParams,
    # bidmodifiers
    BidModifiersGetParams,
    BidModifiersAddParams,
    BidModifiersDeleteParams,
    BidModifiersSetParams,
    # sitelinks
    SitelinksGetParams,
    SitelinksAddParams,
    SitelinksDeleteParams,
    # adimages
    AdImagesGetParams,
    AdImagesAddParams,
    AdImagesDeleteParams,
    # advideos
    AdVideosGetParams,
    AdVideosAddParams,
    # adextensions
    AdExtensionsGetParams,
    AdExtensionsAddParams,
    AdExtensionsDeleteParams,
    # audiencetargets
    AudienceTargetsGetParams,
    AudienceTargetsAddParams,
    AudienceTargetsDeleteParams,
    AudienceTargetsActionParams,
    AudienceTargetsSetBidsParams,
    # retargetinglists
    RetargetingListsGetParams,
    RetargetingListsAddParams,
    RetargetingListsUpdateParams,
    RetargetingListsDeleteParams,
    # negativekeywordsharedsets
    NegativeKeywordSharedSetsGetParams,
    NegativeKeywordSharedSetsAddParams,
    NegativeKeywordSharedSetsUpdateParams,
    NegativeKeywordSharedSetsDeleteParams,
    # feeds
    FeedsGetParams,
    FeedsAddParams,
    FeedsUpdateParams,
    FeedsDeleteParams,
    # creatives
    CreativesGetParams,
    CreativesAddParams,
    # keywordsresearch
    DeduplicateParams,
    HasSearchVolumeParams,
    # leads
    LeadsGetParams,
    # changes
    ChangesCheckParams,
    ChangesCheckCampaignsParams,
    # dictionaries
    DictionariesGetParams,
    # clients
    ClientsGetParams,
    ClientsUpdateParams,
    # agencyclients
    AgencyClientsGetParams,
    AgencyClientsAddParams,
    AgencyClientsUpdateParams,
    # turbopages
    TurboPagesGetParams,
    # reports
    ReportsGetBody,
)


@dataclass(frozen=True, slots=True)
class Action:
    id: str
    domain: str
    description: str
    params_model: type[BaseModel] | None
    api_method: str
    is_destructive: bool = False
    keywords: list[str] = field(default_factory=list)


_ACTIONS_LIST: list[Action] = [
    # ── Campaigns ──────────────────────────────────────────────────────────
    Action(
        id="campaigns-get",
        domain="campaigns",
        description="Получить список кампаний с фильтрацией по критериям",
        params_model=CampaignsGetParams,
        api_method="campaigns_get",
        keywords=["кампании", "получить", "список", "campaigns", "get"],
    ),
    Action(
        id="campaigns-add",
        domain="campaigns",
        description="Создать новые кампании",
        params_model=CampaignsAddParams,
        api_method="campaigns_add",
        keywords=["кампании", "создать", "добавить", "campaigns", "add", "create"],
    ),
    Action(
        id="campaigns-update",
        domain="campaigns",
        description="Обновить параметры кампаний",
        params_model=CampaignsUpdateParams,
        api_method="campaigns_update",
        keywords=["кампании", "обновить", "изменить", "campaigns", "update"],
    ),
    Action(
        id="campaigns-delete",
        domain="campaigns",
        description="Удалить кампании",
        params_model=CampaignsActionParams,
        api_method="campaigns_delete",
        is_destructive=True,
        keywords=["кампании", "удалить", "campaigns", "delete"],
    ),
    Action(
        id="campaigns-suspend",
        domain="campaigns",
        description="Остановить (приостановить) кампании",
        params_model=CampaignsActionParams,
        api_method="campaigns_suspend",
        keywords=["кампании", "остановить", "приостановить", "campaigns", "suspend", "pause"],
    ),
    Action(
        id="campaigns-resume",
        domain="campaigns",
        description="Возобновить (запустить) кампании",
        params_model=CampaignsActionParams,
        api_method="campaigns_resume",
        keywords=["кампании", "возобновить", "запустить", "включить", "campaigns", "resume", "start"],
    ),
    Action(
        id="campaigns-archive",
        domain="campaigns",
        description="Архивировать кампании",
        params_model=CampaignsActionParams,
        api_method="campaigns_archive",
        keywords=["кампании", "архив", "архивировать", "campaigns", "archive"],
    ),
    Action(
        id="campaigns-unarchive",
        domain="campaigns",
        description="Разархивировать кампании",
        params_model=CampaignsActionParams,
        api_method="campaigns_unarchive",
        keywords=["кампании", "разархивировать", "вернуть из архива", "campaigns", "unarchive"],
    ),

    # ── AdGroups ───────────────────────────────────────────────────────────
    Action(
        id="adgroups-get",
        domain="adgroups",
        description="Получить список групп объявлений",
        params_model=AdGroupsGetParams,
        api_method="adgroups_get",
        keywords=["группы", "объявления", "adgroups", "get", "список"],
    ),
    Action(
        id="adgroups-add",
        domain="adgroups",
        description="Создать группы объявлений",
        params_model=AdGroupsAddParams,
        api_method="adgroups_add",
        keywords=["группы", "создать", "добавить", "adgroups", "add"],
    ),
    Action(
        id="adgroups-update",
        domain="adgroups",
        description="Обновить группы объявлений",
        params_model=AdGroupsUpdateParams,
        api_method="adgroups_update",
        keywords=["группы", "обновить", "adgroups", "update"],
    ),
    Action(
        id="adgroups-delete",
        domain="adgroups",
        description="Удалить группы объявлений",
        params_model=AdGroupsDeleteParams,
        api_method="adgroups_delete",
        is_destructive=True,
        keywords=["группы", "удалить", "adgroups", "delete"],
    ),

    # ── Ads ────────────────────────────────────────────────────────────────
    Action(
        id="ads-get",
        domain="ads",
        description="Получить список объявлений",
        params_model=AdsGetParams,
        api_method="ads_get",
        keywords=["объявления", "получить", "ads", "get", "список"],
    ),
    Action(
        id="ads-add",
        domain="ads",
        description="Создать объявления",
        params_model=AdsAddParams,
        api_method="ads_add",
        keywords=["объявления", "создать", "добавить", "ads", "add"],
    ),
    Action(
        id="ads-update",
        domain="ads",
        description="Обновить объявления",
        params_model=AdsUpdateParams,
        api_method="ads_update",
        keywords=["объявления", "обновить", "ads", "update"],
    ),
    Action(
        id="ads-delete",
        domain="ads",
        description="Удалить объявления",
        params_model=AdsActionParams,
        api_method="ads_delete",
        is_destructive=True,
        keywords=["объявления", "удалить", "ads", "delete"],
    ),
    Action(
        id="ads-suspend",
        domain="ads",
        description="Остановить (приостановить) объявления",
        params_model=AdsActionParams,
        api_method="ads_suspend",
        keywords=["объявления", "остановить", "приостановить", "ads", "suspend", "pause"],
    ),
    Action(
        id="ads-resume",
        domain="ads",
        description="Возобновить (запустить) объявления",
        params_model=AdsActionParams,
        api_method="ads_resume",
        keywords=["объявления", "возобновить", "запустить", "включить", "ads", "resume"],
    ),
    Action(
        id="ads-archive",
        domain="ads",
        description="Архивировать объявления",
        params_model=AdsActionParams,
        api_method="ads_archive",
        keywords=["объявления", "архив", "ads", "archive"],
    ),
    Action(
        id="ads-unarchive",
        domain="ads",
        description="Разархивировать объявления",
        params_model=AdsActionParams,
        api_method="ads_unarchive",
        keywords=["объявления", "разархивировать", "ads", "unarchive"],
    ),
    Action(
        id="ads-moderate",
        domain="ads",
        description="Отправить объявления на модерацию",
        params_model=AdsActionParams,
        api_method="ads_moderate",
        keywords=["объявления", "модерация", "ads", "moderate"],
    ),

    # ── Keywords ───────────────────────────────────────────────────────────
    Action(
        id="keywords-get",
        domain="keywords",
        description="Получить список ключевых слов",
        params_model=KeywordsGetParams,
        api_method="keywords_get",
        keywords=["ключевые слова", "keywords", "get", "список"],
    ),
    Action(
        id="keywords-add",
        domain="keywords",
        description="Добавить ключевые слова",
        params_model=KeywordsAddParams,
        api_method="keywords_add",
        keywords=["ключевые слова", "keywords", "add", "создать", "добавить"],
    ),
    Action(
        id="keywords-update",
        domain="keywords",
        description="Обновить ключевые слова",
        params_model=KeywordsUpdateParams,
        api_method="keywords_update",
        keywords=["ключевые слова", "keywords", "update", "обновить"],
    ),
    Action(
        id="keywords-delete",
        domain="keywords",
        description="Удалить ключевые слова",
        params_model=KeywordsActionParams,
        api_method="keywords_delete",
        is_destructive=True,
        keywords=["ключевые слова", "keywords", "delete", "удалить"],
    ),
    Action(
        id="keywords-suspend",
        domain="keywords",
        description="Остановить ключевые слова",
        params_model=KeywordsActionParams,
        api_method="keywords_suspend",
        keywords=["ключевые слова", "keywords", "suspend", "остановить"],
    ),
    Action(
        id="keywords-resume",
        domain="keywords",
        description="Возобновить ключевые слова",
        params_model=KeywordsActionParams,
        api_method="keywords_resume",
        keywords=["ключевые слова", "keywords", "resume", "возобновить", "включить"],
    ),

    # ── Bids ───────────────────────────────────────────────────────────────
    Action(
        id="bids-get",
        domain="bidding",
        description="Получить ставки для ключевых слов",
        params_model=BidsGetParams,
        api_method="bids_get",
        keywords=["ставки", "bids", "get", "цена", "ключевые слова"],
    ),
    Action(
        id="bids-set",
        domain="bidding",
        description="Установить ставки для ключевых слов",
        params_model=BidsSetParams,
        api_method="bids_set",
        keywords=["ставки", "bids", "set", "установить", "цена"],
    ),
    Action(
        id="bids-set-auto",
        domain="bidding",
        description="Установить автоматические ставки для ключевых слов",
        params_model=BidsSetAutoParams,
        api_method="bids_set_auto",
        keywords=["ставки", "bids", "авто", "auto", "автоматически"],
    ),

    # ── BidModifiers ───────────────────────────────────────────────────────
    Action(
        id="bidmodifiers-get",
        domain="bidding",
        description="Получить корректировки ставок",
        params_model=BidModifiersGetParams,
        api_method="bidmodifiers_get",
        keywords=["корректировки", "bidmodifiers", "get", "ставки"],
    ),
    Action(
        id="bidmodifiers-add",
        domain="bidding",
        description="Добавить корректировки ставок",
        params_model=BidModifiersAddParams,
        api_method="bidmodifiers_add",
        keywords=["корректировки", "bidmodifiers", "add", "ставки", "добавить"],
    ),
    Action(
        id="bidmodifiers-delete",
        domain="bidding",
        description="Удалить корректировки ставок",
        params_model=BidModifiersDeleteParams,
        api_method="bidmodifiers_delete",
        is_destructive=True,
        keywords=["корректировки", "bidmodifiers", "delete", "удалить"],
    ),
    Action(
        id="bidmodifiers-set",
        domain="bidding",
        description="Установить корректировки ставок",
        params_model=BidModifiersSetParams,
        api_method="bidmodifiers_set",
        keywords=["корректировки", "bidmodifiers", "set", "установить"],
    ),

    # ── Sitelinks ──────────────────────────────────────────────────────────
    Action(
        id="sitelinks-get",
        domain="assets",
        description="Получить наборы быстрых ссылок",
        params_model=SitelinksGetParams,
        api_method="sitelinks_get",
        keywords=["быстрые ссылки", "sitelinks", "get"],
    ),
    Action(
        id="sitelinks-add",
        domain="assets",
        description="Создать наборы быстрых ссылок",
        params_model=SitelinksAddParams,
        api_method="sitelinks_add",
        keywords=["быстрые ссылки", "sitelinks", "add", "создать"],
    ),
    Action(
        id="sitelinks-delete",
        domain="assets",
        description="Удалить наборы быстрых ссылок",
        params_model=SitelinksDeleteParams,
        api_method="sitelinks_delete",
        is_destructive=True,
        keywords=["быстрые ссылки", "sitelinks", "delete", "удалить"],
    ),

    # ── AdImages ───────────────────────────────────────────────────────────
    Action(
        id="adimages-get",
        domain="assets",
        description="Получить изображения для объявлений",
        params_model=AdImagesGetParams,
        api_method="adimages_get",
        keywords=["изображения", "adimages", "get", "картинки"],
    ),
    Action(
        id="adimages-add",
        domain="assets",
        description="Загрузить изображения для объявлений",
        params_model=AdImagesAddParams,
        api_method="adimages_add",
        keywords=["изображения", "adimages", "add", "загрузить", "картинки"],
    ),
    Action(
        id="adimages-delete",
        domain="assets",
        description="Удалить изображения для объявлений",
        params_model=AdImagesDeleteParams,
        api_method="adimages_delete",
        is_destructive=True,
        keywords=["изображения", "adimages", "delete", "удалить"],
    ),

    # ── AdVideos ───────────────────────────────────────────────────────────
    Action(
        id="advideos-get",
        domain="assets",
        description="Получить видео для объявлений",
        params_model=AdVideosGetParams,
        api_method="advideos_get",
        keywords=["видео", "advideos", "get"],
    ),
    Action(
        id="advideos-add",
        domain="assets",
        description="Загрузить видео для объявлений",
        params_model=AdVideosAddParams,
        api_method="advideos_add",
        keywords=["видео", "advideos", "add", "загрузить"],
    ),

    # ── AdExtensions ───────────────────────────────────────────────────────
    Action(
        id="adextensions-get",
        domain="assets",
        description="Получить расширения объявлений (уточнения, цены)",
        params_model=AdExtensionsGetParams,
        api_method="adextensions_get",
        keywords=["расширения", "adextensions", "get", "уточнения"],
    ),
    Action(
        id="adextensions-add",
        domain="assets",
        description="Добавить расширения объявлений",
        params_model=AdExtensionsAddParams,
        api_method="adextensions_add",
        keywords=["расширения", "adextensions", "add", "уточнения"],
    ),
    Action(
        id="adextensions-delete",
        domain="assets",
        description="Удалить расширения объявлений",
        params_model=AdExtensionsDeleteParams,
        api_method="adextensions_delete",
        is_destructive=True,
        keywords=["расширения", "adextensions", "delete", "удалить"],
    ),

    # ── AudienceTargets ────────────────────────────────────────────────────
    Action(
        id="audiencetargets-get",
        domain="audience",
        description="Получить условия нацеливания на аудиторию",
        params_model=AudienceTargetsGetParams,
        api_method="audiencetargets_get",
        keywords=["аудитория", "audiencetargets", "get", "нацеливание"],
    ),
    Action(
        id="audiencetargets-add",
        domain="audience",
        description="Добавить условия нацеливания на аудиторию",
        params_model=AudienceTargetsAddParams,
        api_method="audiencetargets_add",
        keywords=["аудитория", "audiencetargets", "add", "нацеливание"],
    ),
    Action(
        id="audiencetargets-delete",
        domain="audience",
        description="Удалить условия нацеливания на аудиторию",
        params_model=AudienceTargetsDeleteParams,
        api_method="audiencetargets_delete",
        is_destructive=True,
        keywords=["аудитория", "audiencetargets", "delete", "удалить"],
    ),
    Action(
        id="audiencetargets-suspend",
        domain="audience",
        description="Остановить условия нацеливания на аудиторию",
        params_model=AudienceTargetsActionParams,
        api_method="audiencetargets_suspend",
        keywords=["аудитория", "audiencetargets", "suspend", "остановить"],
    ),
    Action(
        id="audiencetargets-resume",
        domain="audience",
        description="Возобновить условия нацеливания на аудиторию",
        params_model=AudienceTargetsActionParams,
        api_method="audiencetargets_resume",
        keywords=["аудитория", "audiencetargets", "resume", "возобновить"],
    ),
    Action(
        id="audiencetargets-set-bids",
        domain="audience",
        description="Установить ставки для условий нацеливания на аудиторию",
        params_model=AudienceTargetsSetBidsParams,
        api_method="audiencetargets_set_bids",
        keywords=["аудитория", "audiencetargets", "ставки", "bids"],
    ),

    # ── RetargetingLists ───────────────────────────────────────────────────
    Action(
        id="retargetinglists-get",
        domain="audience",
        description="Получить списки ретаргетинга и аудиторий",
        params_model=RetargetingListsGetParams,
        api_method="retargetinglists_get",
        keywords=["ретаргетинг", "retargetinglists", "get", "аудитории"],
    ),
    Action(
        id="retargetinglists-add",
        domain="audience",
        description="Создать списки ретаргетинга и аудиторий",
        params_model=RetargetingListsAddParams,
        api_method="retargetinglists_add",
        keywords=["ретаргетинг", "retargetinglists", "add", "создать"],
    ),
    Action(
        id="retargetinglists-update",
        domain="audience",
        description="Обновить списки ретаргетинга и аудиторий",
        params_model=RetargetingListsUpdateParams,
        api_method="retargetinglists_update",
        keywords=["ретаргетинг", "retargetinglists", "update", "обновить"],
    ),
    Action(
        id="retargetinglists-delete",
        domain="audience",
        description="Удалить списки ретаргетинга и аудиторий",
        params_model=RetargetingListsDeleteParams,
        api_method="retargetinglists_delete",
        is_destructive=True,
        keywords=["ретаргетинг", "retargetinglists", "delete", "удалить"],
    ),

    # ── NegativeKeywordSharedSets ──────────────────────────────────────────
    Action(
        id="negkeywordsets-get",
        domain="negkeywords",
        description="Получить общие списки минус-слов",
        params_model=NegativeKeywordSharedSetsGetParams,
        api_method="negkeywordsets_get",
        keywords=["минус слова", "negkeywords", "get", "минус-слова"],
    ),
    Action(
        id="negkeywordsets-add",
        domain="negkeywords",
        description="Создать общие списки минус-слов",
        params_model=NegativeKeywordSharedSetsAddParams,
        api_method="negkeywordsets_add",
        keywords=["минус слова", "negkeywords", "add", "создать"],
    ),
    Action(
        id="negkeywordsets-update",
        domain="negkeywords",
        description="Обновить общие списки минус-слов",
        params_model=NegativeKeywordSharedSetsUpdateParams,
        api_method="negkeywordsets_update",
        keywords=["минус слова", "negkeywords", "update", "обновить"],
    ),
    Action(
        id="negkeywordsets-delete",
        domain="negkeywords",
        description="Удалить общие списки минус-слов",
        params_model=NegativeKeywordSharedSetsDeleteParams,
        api_method="negkeywordsets_delete",
        is_destructive=True,
        keywords=["минус слова", "negkeywords", "delete", "удалить"],
    ),

    # ── Feeds ──────────────────────────────────────────────────────────────
    Action(
        id="feeds-get",
        domain="feeds",
        description="Получить фиды (товарные фиды для динамических объявлений)",
        params_model=FeedsGetParams,
        api_method="feeds_get",
        keywords=["фиды", "feeds", "get", "товарные", "динамические"],
    ),
    Action(
        id="feeds-add",
        domain="feeds",
        description="Создать фиды",
        params_model=FeedsAddParams,
        api_method="feeds_add",
        keywords=["фиды", "feeds", "add", "создать"],
    ),
    Action(
        id="feeds-update",
        domain="feeds",
        description="Обновить фиды",
        params_model=FeedsUpdateParams,
        api_method="feeds_update",
        keywords=["фиды", "feeds", "update", "обновить"],
    ),
    Action(
        id="feeds-delete",
        domain="feeds",
        description="Удалить фиды",
        params_model=FeedsDeleteParams,
        api_method="feeds_delete",
        is_destructive=True,
        keywords=["фиды", "feeds", "delete", "удалить"],
    ),

    # ── Creatives ──────────────────────────────────────────────────────────
    Action(
        id="creatives-get",
        domain="creatives",
        description="Получить креативы для медийных объявлений",
        params_model=CreativesGetParams,
        api_method="creatives_get",
        keywords=["креативы", "creatives", "get", "медийные"],
    ),
    Action(
        id="creatives-add",
        domain="creatives",
        description="Создать креативы для медийных объявлений",
        params_model=CreativesAddParams,
        api_method="creatives_add",
        keywords=["креативы", "creatives", "add", "создать", "медийные"],
    ),

    # ── KeywordsResearch ───────────────────────────────────────────────────
    Action(
        id="keywordsresearch-deduplicate",
        domain="research",
        description="Дедуплицировать ключевые слова (убрать дубликаты)",
        params_model=DeduplicateParams,
        api_method="keywordsresearch_deduplicate",
        keywords=["дедупликация", "keywordsresearch", "deduplicate", "дубликаты"],
    ),
    Action(
        id="keywordsresearch-has-search-volume",
        domain="research",
        description="Проверить наличие поискового спроса для ключевых слов",
        params_model=HasSearchVolumeParams,
        api_method="keywordsresearch_has_search_volume",
        keywords=["спрос", "keywordsresearch", "search volume", "ключевые слова"],
    ),

    # ── Leads ──────────────────────────────────────────────────────────────
    Action(
        id="leads-get",
        domain="leads",
        description="Получить лиды из форм лидогенерации",
        params_model=LeadsGetParams,
        api_method="leads_get",
        keywords=["лиды", "leads", "get", "лидогенерация"],
    ),

    # ── Changes ────────────────────────────────────────────────────────────
    Action(
        id="changes-check",
        domain="changes",
        description="Проверить изменения в объектах аккаунта",
        params_model=ChangesCheckParams,
        api_method="changes_check",
        keywords=["изменения", "changes", "check"],
    ),
    Action(
        id="changes-check-dictionaries",
        domain="changes",
        description="Проверить изменения в справочниках Яндекс Директа",
        params_model=None,
        api_method="changes_check_dictionaries",
        keywords=["изменения", "changes", "справочники", "dictionaries"],
    ),
    Action(
        id="changes-check-campaigns",
        domain="changes",
        description="Проверить изменения в кампаниях",
        params_model=ChangesCheckCampaignsParams,
        api_method="changes_check_campaigns",
        keywords=["изменения", "changes", "кампании", "campaigns"],
    ),

    # ── Dictionaries ───────────────────────────────────────────────────────
    Action(
        id="dictionaries-get",
        domain="account",
        description="Получить справочники Яндекс Директа (валюты, регионы, временные зоны и др.)",
        params_model=DictionariesGetParams,
        api_method="dictionaries_get",
        keywords=["справочники", "dictionaries", "get", "валюты", "регионы"],
    ),

    # ── Clients ────────────────────────────────────────────────────────────
    Action(
        id="clients-get",
        domain="account",
        description="Получить параметры клиентского аккаунта",
        params_model=ClientsGetParams,
        api_method="clients_get",
        keywords=["клиент", "clients", "get", "аккаунт"],
    ),
    Action(
        id="clients-update",
        domain="account",
        description="Обновить параметры клиентского аккаунта",
        params_model=ClientsUpdateParams,
        api_method="clients_update",
        keywords=["клиент", "clients", "update", "аккаунт", "обновить"],
    ),

    # ── AgencyClients ──────────────────────────────────────────────────────
    Action(
        id="agencyclients-get",
        domain="account",
        description="Получить список клиентов агентства",
        params_model=AgencyClientsGetParams,
        api_method="agencyclients_get",
        keywords=["агентство", "agencyclients", "get", "клиенты"],
    ),
    Action(
        id="agencyclients-add",
        domain="account",
        description="Создать клиентов агентства",
        params_model=AgencyClientsAddParams,
        api_method="agencyclients_add",
        keywords=["агентство", "agencyclients", "add", "клиенты", "создать"],
    ),
    Action(
        id="agencyclients-update",
        domain="account",
        description="Обновить параметры клиентов агентства",
        params_model=AgencyClientsUpdateParams,
        api_method="agencyclients_update",
        keywords=["агентство", "agencyclients", "update", "клиенты", "обновить"],
    ),

    # ── TurboPages ─────────────────────────────────────────────────────────
    Action(
        id="turbopages-get",
        domain="turbopages",
        description="Получить Турбо-страницы",
        params_model=TurboPagesGetParams,
        api_method="turbopages_get",
        keywords=["турбо", "turbopages", "get", "страницы"],
    ),

    # ── Reports ────────────────────────────────────────────────────────────
    Action(
        id="reports-get",
        domain="reports",
        description="Получить отчёт Яндекс Директа (TSV/CSV) по заданным полям и критериям",
        params_model=ReportsGetBody,
        api_method="reports_get",
        keywords=["отчёт", "отчет", "reports", "get", "статистика", "TSV", "CSV"],
    ),
]

# Dict for O(1) lookup by action ID
ACTIONS: dict[str, Action] = {a.id: a for a in _ACTIONS_LIST}
