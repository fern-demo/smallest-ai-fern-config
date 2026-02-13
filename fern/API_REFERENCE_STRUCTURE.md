# API Reference Navigation Structure

This document explains how the API Reference tab in the Fern-generated docs is organized, and how the two navigation structures (MDX pages and auto-generated API reference) relate to each other.

## Two Navigation Structures

The API Reference tab contains two types of content that appear together in the sidebar:

### 1. MDX Pages (Manual Documentation)

These are hand-written markdown pages located in `fern/products/waves/pages/<version>/api-references/`. They provide detailed guides, code examples, and explanations for each endpoint.

In the version config files (`fern/products/waves/versions/<version>.yml`), MDX pages are organized into named sections:

```yaml
- tab: api-reference
  layout:
    - section: Lightning v2
      contents:
        - page: Lightning v2
          path: ../pages/v2.2.0/api-references/lightning-v2.mdx
        - page: Lightning v2 Stream
          path: ../pages/v2.2.0/api-references/lightning-v2-stream.mdx
```

### 2. Auto-Generated API Reference (From OpenAPI/AsyncAPI Specs)

These are interactive endpoint pages generated automatically from the API specs in `fern/apis/waves/openapi/` and `fern/apis/waves/asyncapi/`. They include request/response schemas, parameter details, and try-it-out functionality.

In the version config, the auto-generated API reference is declared with:

```yaml
- api: API Reference
  api-name: waves
  flattened: true
  layout:
    - Lightning v2:
        title: Lightning v2
    - Lightning Large:
        title: Lightning Large
```

## How They Connect

### OpenAPI Tags Control Grouping

Each OpenAPI endpoint has a `tags` field that determines which group (subpackage) it belongs to. For example, in `waves-api-overrides.yaml`:

```yaml
/api/v1/lightning-v2/get_speech:
  post:
    tags:
      - Lightning v2
```

The tag name ("Lightning v2") becomes the subpackage name in the auto-generated API reference.

### The Layout Controls Order and Visibility

The `layout` property under the `api:` section in the version config controls:
1. **Which subpackages appear** - only listed subpackages are shown
2. **The order they appear in** - follows the list order

### `flattened: true` Merges Into Navigation

When `flattened: true` is set, the auto-generated API sections are merged directly into the sidebar alongside the MDX page sections, rather than appearing under a separate collapsible "API Reference" heading.

## Keeping the Two Structures Aligned

The MDX pages and auto-generated API reference should use the same organizational structure so the navigation feels consistent. This means:

1. **OpenAPI tag names should match MDX section names** - If MDX pages are grouped under "Lightning v2", the OpenAPI endpoints should also be tagged "Lightning v2" (not a generic "Text to Speech").

2. **Layout order should match MDX section order** - The `layout` list in the `api:` block should follow the same order as the MDX `section` entries above it.

### Example: v2.2.0

MDX sections appear in this order:
- API References (Authentication, WebSocket)
- Lightning v2
- Lightning Large
- Lightning
- Voices
- Voice Cloning

The auto-generated API layout matches:
```yaml
layout:
  - Lightning v2:
      title: Lightning v2
  - Lightning Large:
      title: Lightning Large
  - Lightning:
      title: Lightning
  - Voices:
      title: Voices
  - Voice Cloning:
      title: Voice Cloning
```

## File Locations

| Purpose | Path |
|---------|------|
| Version configs (navigation) | `fern/products/waves/versions/*.yml` |
| MDX pages | `fern/products/waves/pages/<version>/api-references/*.mdx` |
| OpenAPI specs | `fern/apis/waves/openapi/*.yaml` |
| OpenAPI overrides (tag changes) | `fern/apis/waves/openapi/*-overrides.yaml` |
| AsyncAPI specs | `fern/apis/waves/asyncapi/*.yml` |
| API definition config | `fern/apis/waves/generators.yml` |

## Modifying the Structure

To reorder or reorganize the API reference:

1. **To change endpoint grouping**: Update the `tags` in the relevant `*-overrides.yaml` file
2. **To change section order**: Update the `layout` list in the version config `.yml` file
3. **To add/remove sections**: Update both the override tags AND the layout list
4. **Keep all versions consistent**: Changes to override files affect all versions since they share the same API specs. Update each version's layout accordingly.
