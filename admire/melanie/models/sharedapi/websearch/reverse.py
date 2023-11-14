# generated by datamodel-codegen:
#   timestamp: 2023-02-09T00:13:49+00:00


from __future__ import annotations

from melanie import BaseModel


class ImageResult(BaseModel):
    position: int | None
    title: str | None
    link: str | None
    displayed_link: str | None
    snippet: str | None
    snippet_highlighted_words: list[str] | None
    cached_page_link: str | None
    related_pages_link: str | None
    thumbnail: str | None
    image_resolution: str | None
    displayed_results: str | None
    date: str | None


class ImageSize(BaseModel):
    title: str | None
    link: str | None
    serpapi_link: str | None


class InlineImage(BaseModel):
    link: str | None
    source: str | None
    thumbnail: str | None


class Link(BaseModel):
    text: str | None
    link: str | None


class HeaderImage(BaseModel):
    image: str | None
    source: str | None


class Profile(BaseModel):
    name: str | None
    link: str | None
    source: str | None
    image: str | None


class Source(BaseModel):
    name: str | None
    link: str | None


class SearchInformation(BaseModel):
    organic_results_state: str | None
    query_displayed: str | None
    total_results: int | None
    time_taken_displayed: float | None


class SearchMetadata(BaseModel):
    id: str | None
    status: str | None
    json_endpoint: str | None
    created_at: str | None
    processed_at: str | None
    google_reverse_image_url: str | None
    raw_html_file: str | None
    total_time_taken: float | None


class SearchParameters(BaseModel):
    engine: str | None
    image_url: str | None
    google_domain: str | None
    device: str | None


class KnowledgeGraph(BaseModel):
    title: str | None
    type: str | None
    kgmid: str | None
    knowledge_graph_search_link: str | None
    serpapi_knowledge_graph_search_link: str | None
    header_images: list[HeaderImage] | None
    image: str | None
    website: str | None
    description: str | None
    source: Source | None
    born: str | None
    born_links: list[Link] | None
    marriage_location: str | None
    marriage_location_links: list[Link] | None
    organization_founded: str | None
    organization_founded_links: list[Link] | None
    production_company: str | None
    production_company_links: list[Link] | None
    awards: str | None
    awards_links: list[Link] | None
    nominations: str | None
    nominations_links: list[Link] | None
    books: str | None
    books_links: list[Link] | None
    profiles: list[Profile] | None


class ReverseSearchImageResultRaw(BaseModel):
    search_metadata: SearchMetadata | None
    search_parameters: SearchParameters | None
    search_information: SearchInformation | None
    image_sizes: list[ImageSize] | None
    inline_images: list[InlineImage] | None
    inline_images_link: str | None
    image_results: list[ImageResult] | None


###


class ReverseImageSearchItem(BaseModel):
    position: int | None
    title: str | None
    link: str | None
    snippet: str | None
    thumbnail: str | None
    image_resolution: str | None
    displayed_results: str | None
    date: str | None


class ReverseImageSearchResponse(BaseModel):
    reverse_search_google_link: str | None
    image_url: str | None
    query_text: str | None
    items: list[ReverseImageSearchItem] | None = []