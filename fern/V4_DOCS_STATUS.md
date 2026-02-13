# V4 Docs: Status & Remaining Issues

## How We Solved Version-Specific Summaries

v4.0.0 needed different endpoint summaries/categories than v2.2.0/v3.0.1 (e.g. "Lightning v3.1" vs "Generate speech (Lightning v3.1)"). Since all versions shared one API definition (`waves`), summaries were identical across versions.

**Solution:** Created a separate API definition `waves-v4` (`fern/apis/waves-v4/`) that:
- References the same base OpenAPI/AsyncAPI specs as `waves`
- Has its own override files with v4-specific summaries and tag organization
- Has NO `groups` section in `generators.yml` — zero SDK generation impact
- Uses `x-fern-audiences: [v4docs]` to control endpoint visibility
- Is referenced only by `v4.0.0.yml` via `api-name: waves-v4`

Old Lightning/Lightning Large endpoints are excluded from v4 by tagging them with `x-fern-audiences: [exclude]` in the v4 overrides.

## Remaining Issue: Lightning v2 WebSocket Missing in v4

The Lightning v2 WebSocket (`wss://waves-api.smallest.ai/api/v1/lightning-v2/get_speech/stream`) does not appear in v4.0.0 docs. The Lightning v3.1 WebSocket shows fine.

**Root cause:** When two AsyncAPI specs included in the same API definition have operations with the same name (`ttsRequest`/`ttsResponse`), only one endpoint renders. The second spec's operations appear to overwrite the first during Fern's API processing. This is a **naming collision bug in Fern's AsyncAPI handling**.

**What was tried:**
1. Renaming operations/messages in the override to unique names (`lightningV2TtsRequest`) — didn't work because the override merges with the base spec (doesn't fully replace the operations section), so the original `ttsRequest` key still exists
2. Creating a fully self-contained AsyncAPI spec with unique operation names (no override, no shared base) — also didn't render the endpoint

**What's needed:** A fix in fern-platform for how multiple AsyncAPI specs with overlapping operation names are processed within a single API definition. The operations should be namespaced per-spec or per-channel to avoid collisions.
