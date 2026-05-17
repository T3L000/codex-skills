---
template_id: whut_academic_blue
category: brand
summary: Wuhan University of Technology inspired academic blue template for thesis defense, policy briefing, and research presentations.
keywords: [academic, university, blue, structured, image-led]
primary_color: "#00489A"
canvas_format: ppt169
replication_mode: fidelity
use_cases: Thesis defense, academic presentation, policy briefing, university research communication
design_tone: Professional, rigorous, campus-branded, image-led, structured
placeholders:
  01_cover: ["{{TITLE}}", "{{SUBTITLE}}", "{{AUTHOR}}", "{{DATE}}"]
  02_toc: ["{{TOC_ITEM_1_TITLE}}", "{{TOC_ITEM_2_TITLE}}", "{{TOC_ITEM_3_TITLE}}", "{{TOC_ITEM_4_TITLE}}"]
  02a_chapter_sidebar: ["{{CHAPTER_NUM}}", "{{CHAPTER_TITLE}}", "{{CHAPTER_DESC}}"]
  03a_content_image_right: ["{{PAGE_TITLE}}", "{{KEY_MESSAGE}}", "{{CONTENT_AREA}}"]
  03b_content_quad_cards: ["{{PAGE_TITLE}}", "{{CARD_1_TITLE}}", "{{CARD_2_TITLE}}", "{{CARD_3_TITLE}}", "{{CARD_4_TITLE}}"]
  03c_content_gallery_grid: ["{{PAGE_TITLE}}", "{{ITEM_1_TITLE}}", "{{ITEM_2_TITLE}}", "{{ITEM_3_TITLE}}"]
  03d_content_feature_split: ["{{PAGE_TITLE}}", "{{FEATURE_TITLE}}", "{{FEATURE_BODY}}", "{{KEY_MESSAGE}}"]
  04_ending: ["{{THANK_YOU}}", "{{CLOSING_MESSAGE}}", "{{CONTACT_INFO}}"]
---

# WHUT Academic Blue - Design Specification

## I. Template Overview
- Use cases: thesis defense, university reports, academic lectures, public-policy briefings
- Tone: academic, trustworthy, structured, blue-dominant, moderately image-led
- Visual identity at a glance: white canvas, Wuhan University of Technology brand elements, centered title markers, and high-contrast blue side panels or photo blocks

## II. Color Scheme
- Primary: `#00489A` for titles, chapter sidebars, dividers
- Accent: `#4472C4` for thin structural lines and secondary emphasis
- Warm accent: `#FBC438` / `#FFC000` for TOC and content-card variation
- Background: `#FFFFFF` with translucent white overlays over photography
- Text: `#595959` / `#767171` for body copy, `#FFFFFF` over dark overlays

## III. Typography
- Title stack: `"Microsoft YaHei", Arial, sans-serif`
- Body stack: `"Microsoft YaHei", Arial, sans-serif`
- Cover and ending use bold center-aligned display treatment; content pages keep medium-density academic text blocks

## IV. Signature Design Elements
- Wuhan University of Technology emblem is fixed on cover and ending
- Top-left brand strip (`header_brand.png` + circular seal) anchors content pages
- Diamond marker plus twin horizontal rules create the recurring title divider
- Chapter pages inherit the source deck's right-side deep-blue overlay over full-bleed campus imagery

## V. Page Roster
- `01_cover.svg`: cover cluster from source slide 1; photographic background with centered translucent title panel and emblem
- `02_toc.svg`: TOC cluster from source slide 2; left photo collage with three strong vertical TOC columns and one auxiliary item slot
- `02a_chapter_sidebar.svg`: chapter cluster from source slides 6/9/12; full-bleed campus image with right blue sidebar for chapter metadata
- `03a_content_image_right.svg`: content cluster from source slide 4; left narrative block, right tall hero image, centered page title marker
- `03b_content_quad_cards.svg`: content cluster from source slide 5; four-quadrant card canvas with strong color anchors for categorized arguments
- `03c_content_gallery_grid.svg`: content cluster from source slide 8; wide image banner with three commentary slots below for grouped evidence or case snapshots
- `03d_content_feature_split.svg`: content cluster from source slide 10; large left photo, right feature text block, suitable for key case analysis or spotlight pages
- `04_ending.svg`: ending cluster from source slide 15; full-bleed closing background with bilingual-thanks style and emblem badge

## VI. Assets
- `brand_emblem.png`: central emblem used on cover and ending
- `header_brand.png` / `header_seal.png`: top-left brand identity pair for content pages
- `cover_bg.jpg`, `chapter_bg.jpg`, `toc_collage.jpg`, `content_hero_right.jpg`, `gallery_banner.jpg`, `feature_image.jpg`, `ending_bg.jpg`: fixed reference imagery derived from the source PPTX import workspace

## VII. Placeholder Overrides
- This template keeps canonical cover / chapter / ending placeholders but extends content variants with card- and feature-specific slots so the source deck's structured storytelling surfaces remain reusable.
