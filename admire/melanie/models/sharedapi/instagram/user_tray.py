# generated by datamodel-codegen:
#   timestamp: 2023-03-26T06:49:33+00:00


from __future__ import annotations

from typing import Any

from melanie import BaseModel, Field, str

from .instagram_post2 import InstagramPostResponse, InstagramUserResponse  # noqa


class FanClubInfo(BaseModel):
    fan_club_id: Any | None
    fan_club_name: Any | None
    is_fan_club_referral_eligible: Any | None
    fan_consideration_page_revamp_eligiblity: Any | None
    is_fan_club_gifting_eligible: Any | None


class FirstFrame(BaseModel):
    width: int | None
    height: int | None
    url: str | None


class SharingFrictionInfo(BaseModel):
    should_have_sharing_friction: bool | None
    bloks_app_url: Any | None
    sharing_friction_payload: Any | None


class AchievementsInfo(BaseModel):
    show_achievements: bool | None
    num_earned_achievements: Any | None


class AudioReattributionInfo(BaseModel):
    should_allow_restore: bool | None


class AudioRankingInfo(BaseModel):
    best_audio_cluster_id: str | None


class BrandedContentTagInfo(BaseModel):
    can_add_tag: bool | None


class ContentAppreciationInfo(BaseModel):
    enabled: bool | None
    entry_point_container: Any | None


class MashupInfo(BaseModel):
    mashups_allowed: bool | None
    can_toggle_mashups_allowed: bool | None
    has_been_mashed_up: bool | None
    formatted_mashups_count: Any | None
    original_media: Any | None
    privacy_filtered_mashups_media_count: Any | None
    non_privacy_filtered_mashups_media_count: Any | None
    mashup_type: Any | None
    is_creator_requesting_mashup: bool | None
    has_nonmimicable_additional_audio: bool | None


class ConsumptionInfo(BaseModel):
    is_bookmarked: bool | None
    should_mute_audio_reason: str | None
    is_trending_in_clips: bool | None
    should_mute_audio_reason_type: Any | None
    display_media_id: Any | None


class CommentInformTreatment(BaseModel):
    should_have_inform_treatment: bool | None
    text: str | None
    url: Any | None
    action_type: Any | None


class UserElement(BaseModel):
    pk: str | None
    pk_id: str | None
    username: str | None
    full_name: str | None
    is_private: bool | None
    is_verified: bool | None
    profile_pic_id: str | None
    profile_pic_url: str | None
    profile_grid_display_type: str | None
    fbid_v2: str | None


class AdditionalCandidates(BaseModel):
    igtv_first_frame: FirstFrame | None
    first_frame: FirstFrame | None
    smart_frame: Any | None


class SquareCrop(BaseModel):
    crop_left: float | None
    crop_right: float | None
    crop_top: float | None
    crop_bottom: float | None


class MusicMetadata(BaseModel):
    music_canonical_id: int | None
    audio_type: Any | None
    music_info: Any | None
    original_sound_info: Any | None
    pinned_media_ids: Any | None


class VideoVersion(BaseModel):
    type: int | None
    width: int | None
    height: int | None
    url: str | None
    id: str | None


class CaptionUser(BaseModel):
    has_anonymous_profile_picture: bool | None
    fan_club_info: FanClubInfo | None
    transparency_product_enabled: bool | None
    is_favorite: bool | None
    is_unpublished: bool | None
    pk: str | None
    pk_id: str | None
    strong_id__: str | None
    username: str | None
    full_name: str | None
    is_private: bool | None
    is_verified: bool | None
    profile_pic_id: str | None
    profile_pic_url: str | None
    account_badges: list | None
    latest_reel_media: int | None


class CarouselMediaImageVersions2(BaseModel):
    candidates: list[FirstFrame] | None


class In(BaseModel):
    user: UserElement | None
    position: list[float] | None
    start_time_in_video_in_sec: Any | None
    duration_in_video_in_sec: Any | None


class AdditionalAudioInfo(BaseModel):
    additional_audio_username: Any | None
    audio_reattribution_info: AudioReattributionInfo | None


class OriginalSoundInfo(BaseModel):
    audio_asset_id: str | None
    music_canonical_id: Any | None
    progressive_download_url: str | None
    duration_in_ms: int | None
    dash_manifest: str | None
    ig_artist: UserElement | None
    should_mute_audio: bool | None
    hide_remixing: bool | None
    original_media_id: str | None
    time_created: int | None
    original_audio_title: str | None
    consumption_info: ConsumptionInfo | None
    can_remix_be_shared_to_fb: bool | None
    formatted_clips_media_count: Any | None
    allow_creator_to_rename: bool | None
    audio_parts: list | None
    is_explicit: bool | None
    original_audio_subtype: str | None
    is_audio_automatically_attributed: bool | None
    is_reuse_disabled: bool | None
    is_xpost_from_fb: bool | None
    xpost_fb_creator_info: Any | None
    nft_info: Any | None


class Comment(BaseModel):
    pk: str | None
    user_id: str | None
    text: str | None
    type: int | None
    created_at: int | None
    created_at_utc: int | None
    content_type: str | None
    status: str | None
    bit_flags: int | None
    did_report_as_spam: bool | None
    share_enabled: bool | None
    user: UserElement | None
    is_covered: bool | None
    is_ranked_comment: bool | None
    media_id: str | None
    has_liked_comment: bool | None
    comment_like_count: int | None
    private_reply_status: int | None
    parent_comment_id: str | None


class ItemImageVersions2(BaseModel):
    candidates: list[FirstFrame] | None
    additional_candidates: AdditionalCandidates | None
    smart_thumbnail_enabled: bool | None


class MediaCroppingInfo(BaseModel):
    square_crop: SquareCrop | None


class Caption(BaseModel):
    pk: str | None
    user_id: str | None
    text: str | None
    type: int | None
    created_at: int | None
    created_at_utc: int | None
    content_type: str | None
    status: str | None
    bit_flags: int | None
    did_report_as_spam: bool | None
    share_enabled: bool | None
    user: CaptionUser | None
    is_covered: bool | None
    is_ranked_comment: bool | None
    media_id: str | None
    private_reply_status: int | None


class Usertags(BaseModel):
    in_: list[In] | None = Field(None, alias="in")


class ClipsMetadata(BaseModel):
    music_info: Any | None
    original_sound_info: OriginalSoundInfo | None
    audio_type: str | None
    music_canonical_id: str | None
    featured_label: Any | None
    mashup_info: MashupInfo | None
    reusable_text_info: Any | None
    nux_info: Any | None
    viewer_interaction_settings: Any | None
    branded_content_tag_info: BrandedContentTagInfo | None
    shopping_info: Any | None
    additional_audio_info: AdditionalAudioInfo | None
    is_shared_to_fb: bool | None
    breaking_content_info: Any | None
    challenge_info: Any | None
    reels_on_the_rise_info: Any | None
    breaking_creator_info: Any | None
    asset_recommendation_info: Any | None
    contextual_highlight_info: Any | None
    clips_creation_entry_point: str | None
    audio_ranking_info: AudioRankingInfo | None
    template_info: Any | None
    is_fan_club_promo_video: bool | None
    disable_use_in_clips_client_cache: bool | None
    content_appreciation_info: ContentAppreciationInfo | None
    achievements_info: AchievementsInfo | None
    show_achievements: bool | None
    show_tips: bool | None
    merchandising_pill_info: Any | None
    is_public_chat_welcome_video: bool | None
    professional_clips_upsell_type: int | None


class CarouselMedia(BaseModel):
    id: str | None
    media_type: int | None
    product_type: str | None
    image_versions2: CarouselMediaImageVersions2 | None
    video_versions: list[VideoVersion] | None
    original_width: int | None
    original_height: int | None
    accessibility_caption: str | None
    pk: str | None
    carousel_parent_id: str | None
    usertags: Usertags | None
    commerciality_status: str | None
    sharing_friction_info: SharingFrictionInfo | None


class Item(BaseModel):
    taken_at: int | None
    pk: str | None
    id: str | None
    device_timestamp: int | None
    media_type: int | None
    code: str | None
    client_cache_key: str | None
    filter_type: int | None
    accessibility_caption: str | None
    is_unified_video: bool | None
    should_request_ads: bool | None
    original_media_has_visual_reply_media: bool | None
    like_and_view_counts_disabled: bool | None
    commerciality_status: str | None
    is_paid_partnership: bool | None
    is_visual_reply_commenter_notice_enabled: bool | None
    clips_tab_pinned_user_ids: list | None
    has_delayed_metadata: bool | None
    comment_likes_enabled: bool | None
    comment_threading_enabled: bool | None
    max_num_visible_preview_comments: int | None
    has_more_comments: bool | None
    preview_comments: list[Comment] | None
    comments: list[Comment] | None
    comment_count: int | None
    can_view_more_preview_comments: bool | None
    hide_view_all_comment_entrypoint: bool | None
    inline_composer_display_condition: str | None
    photo_of_you: bool | None
    is_organic_product_tagging_eligible: bool | None
    can_see_insights_as_brand: bool | None
    user: CaptionUser | None
    can_viewer_reshare: bool | None
    like_count: int | None
    has_liked: bool | None
    top_likers: list[str] | None
    facepile_top_likers: list[UserElement] | None
    likers: list[UserElement] | None
    is_comments_gif_composer_enabled: bool | None
    image_versions2: ItemImageVersions2 | None
    original_width: int | None
    original_height: int | None
    caption: Caption | None
    caption_is_edited: bool | None
    comment_inform_treatment: CommentInformTreatment | None
    sharing_friction_info: SharingFrictionInfo | None
    can_viewer_save: bool | None
    is_in_profile_grid: bool | None
    profile_grid_control_enabled: bool | None
    organic_tracking_token: str | None
    has_shared_to_fb: int | None
    product_type: str | None
    show_shop_entrypoint: bool | None
    deleted_reason: int | None
    integrity_review_decision: str | None
    commerce_integrity_review_decision: Any | None
    music_metadata: MusicMetadata | None
    is_artist_pick: bool | None
    ig_media_sharing_disabled: bool | None
    next_max_id: str | None
    carousel_media_count: int | None
    carousel_media: list[CarouselMedia] | None
    usertags: Usertags | None
    video_subtitles_confidence: float | None
    video_subtitles_uri: str | None
    is_dash_eligible: int | None
    video_dash_manifest: str | None
    video_codec: str | None
    number_of_qualities: int | None
    video_versions: list[VideoVersion] | None
    has_audio: bool | None
    video_duration: float | None
    play_count: int | None
    third_party_downloads_enabled: bool | None
    clips_metadata: ClipsMetadata | None
    media_cropping_info: MediaCroppingInfo | None


class InstagramUserTrayRaw(BaseModel):
    items: list[Item] | None
    num_results: int | None
    more_available: bool | None
    next_max_id: str | None
    user: UserElement | None
    auto_load_more_enabled: bool | None
    status: str | None


class InstagramUserTrayResponse(BaseModel):
    user: InstagramUserResponse | None
    items: list[InstagramPostResponse] | None = []
