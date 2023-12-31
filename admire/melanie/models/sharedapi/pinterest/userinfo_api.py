# generated by datamodel-codegen:
#   timestamp: 2023-04-08T01:58:01+00:00

from __future__ import annotations

from typing import Any

from melanie import BaseModel


class ActiveExperiments(BaseModel):
    pass


class AnalysisUa(BaseModel):
    app_type: int | None
    browser_name: str | None
    browser_version: str | None
    device_type: Any | None
    device: str | None
    os_name: str | None
    os_version: str | None


class User(BaseModel):
    verified_identity: ActiveExperiments | None
    image_small_url: str | None
    last_name: str | None
    verified_user_websites: list | None
    gender: str | None
    country: str | None
    can_enable_mfa: bool | None
    has_password: bool | None
    image_xlarge_url: str | None
    image_medium_url: str | None
    twitter_publish_enabled: bool | None
    connected_to_etsy: bool | None
    is_partner: bool | None
    allow_personalization_cookies: Any | None
    phone_country: Any | None
    facebook_timeline_enabled: bool | None
    connected_to_microsoft: bool | None
    personalize_from_offsite_browsing: bool | None
    nags: list | None
    is_any_website_verified: bool | None
    is_candidate_for_parental_control_passcode: bool | None
    is_parental_control_passcode_enabled: bool | None
    phone_number: Any | None
    should_show_messaging: bool | None
    username: str | None
    ip_country: str | None
    unverified_phone_country: Any | None
    twitter_url: Any | None
    website_url: Any | None
    connected_to_google: bool | None
    ip_region: str | None
    allow_marketing_cookies: Any | None
    push_package_user_id: str | None
    phone_number_end: str | None
    is_matured_new_user: bool | None
    is_under_16: bool | None
    unverified_phone_number_without_country: str | None
    created_at: str | None
    connected_to_dropbox: bool | None
    is_high_risk: bool | None
    resurrection_info: Any | None
    third_party_marketing_tracking_enabled: bool | None
    domain_verified: bool | None
    facebook_publish_stream_enabled: bool | None
    connected_to_instagram: bool | None
    is_private_profile: bool | None
    profile_discovered_public: Any | None
    email: str | None
    full_name: str | None
    listed_website_url: Any | None
    connected_to_facebook: bool | None
    connected_to_youtube: bool | None
    age_in_years: int | None
    is_ads_only_profile: bool | None
    epik: str | None
    first_name: str | None
    ads_only_profile_site: Any | None
    unverified_phone_number: Any | None
    parental_control_anonymized_email: Any | None
    domain_url: Any | None
    type: str | None
    allow_analytic_cookies: Any | None
    is_employee: bool | None
    is_write_banned: bool | None
    gplus_url: str | None
    id: str | None
    login_state: int | None
    image_large_url: str | None
    verified_domains: list | None
    facebook_id: str | None
    has_mfa_enabled: bool | None
    custom_gender: Any | None


class Options(BaseModel):
    bookmarks: list[str] | None
    username: str | None
    field_set_key: str | None


class EligibleProfileTab(BaseModel):
    id: str | None
    type: str | None
    tab_type: int | None
    name: str | None
    is_default: bool | None


class ProfileCover(BaseModel):
    id: str | None


class RepinsFrom(BaseModel):
    repins_from: list | None
    image_medium_url: str | None
    username: str | None
    full_name: str | None
    id: str | None
    image_small_url: str | None


class ClientContext(BaseModel):
    active_experiments: ActiveExperiments | None
    analysis_ua: AnalysisUa | None
    app_type_detailed: int | None
    app_version: str | None
    batch_exp: bool | None
    browser_locale: str | None
    browser_name: str | None
    browser_type: int | None
    browser_version: str | None
    country: str | None
    country_from_hostname: str | None
    country_from_ip: str | None
    csp_nonce: str | None
    current_url: str | None
    debug: bool | None
    deep_link: str | None
    enabled_advertiser_countries: list[str] | None
    experiment_hash: str | None
    facebook_token: Any | None
    full_path: str | None
    http_referrer: str | None
    impersonator_user_id: Any | None
    invite_code: str | None
    invite_sender_id: str | None
    is_authenticated: bool | None
    is_bot: str | None
    is_internal_ip: bool | None
    is_full_page: bool | None
    is_managed_advertiser: bool | None
    is_mobile_agent: bool | None
    is_shop_the_pin_campaign_whitelisted: bool | None
    is_sterling_on_steroids: bool | None
    is_tablet_agent: bool | None
    language: str | None
    locale: str | None
    origin: str | None
    path: str | None
    placed_experiences: Any | None
    referrer: Any | None
    region_from_ip: str | None
    request_host: str | None
    request_identifier: str | None
    social_bot: str | None
    stage: str | None
    sterling_on_steroids_ldap: Any | None
    sterling_on_steroids_user_type: Any | None
    triggerable_experiments: dict[str, str] | None
    unauth_id: str | None
    seo_debug: bool | None
    user_agent_can_use_native_app: bool | None
    user_agent_platform: str | None
    user_agent_platform_version: Any | None
    user_agent: str | None
    user: User | None
    utm_campaign: Any | None
    visible_url: str | None


class Resource(BaseModel):
    name: str | None
    options: Options | None


class Data(BaseModel):
    blocked_by_me: bool | None
    board_count: int | None
    is_tastemaker: bool | None
    native_pin_count: int | None
    storefront_search_enabled: bool | None
    explicitly_followed_by_me: bool | None
    pins_done_count: int | None
    show_creator_profile: bool | None
    show_engagement_tab: bool | None
    listed_website_url: str | None
    pronouns: list | None
    has_showcase: bool | None
    story_pin_count: int | None
    is_ads_only_profile: bool | None
    should_show_messaging: bool | None
    is_partner: bool | None
    profile_reach: int | None
    group_board_count: int | None
    profile_cover: ProfileCover | None
    website_url: str | None
    is_inspirational_merchant: bool | None
    profile_discovered_public: Any | None
    image_small_url: str | None
    interest_following_count: int | None
    show_impressum: bool | None
    full_name: str | None
    video_pin_count: int | None
    has_published_pins: bool | None
    is_verified_merchant: bool | None
    last_pin_save_time: str | None
    has_catalog: bool | None
    impressum_url: Any | None
    username: str | None
    eligible_profile_tabs: list[EligibleProfileTab] | None
    profile_views: int | None
    ads_only_profile_site: Any | None
    storefront_management_enabled: bool | None
    has_shopping_showcase: bool | None
    following_count: int | None
    image_medium_url: str | None
    show_discovered_feed: Any | None
    explicit_user_following_count: int | None
    partner: Any | None
    first_name: str | None
    about: str | None
    indexed: bool | None
    follower_count: int | None
    has_custom_board_sorting_order: bool | None
    joined_communities_count: int | None
    last_name: str | None
    pin_count: int | None
    type: str | None
    image_large_url: str | None
    is_primary_website_verified: bool | None
    image_xlarge_url: str | None
    verified_identity: ActiveExperiments | None
    domain_url: Any | None
    id: str | None
    should_default_comments_off: bool | None
    domain_verified: bool | None
    repins_from: list[RepinsFrom] | None
    has_board: bool | None


class ResourceResponse(BaseModel):
    status: str | None
    code: int | None
    message: str | None
    endpoint_name: str | None
    data: Data | None
    x_pinterest_sli_endpoint_name: str | None
    http_status: int | None


class PinterestUserinfoAPIResponse(BaseModel):
    resource_response: ResourceResponse | None
    client_context: ClientContext | None
    resource: Resource | None
    request_identifier: str | None
