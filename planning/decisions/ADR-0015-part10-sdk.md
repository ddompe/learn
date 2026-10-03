# ADR-0015: GitHub Copilot SDK for Part 10

- Status: Accepted
- Date: 2026-10-03

## Context

Part 10 teaches calling LLMs from Python. Learners already use GitHub Copilot in VS Code
from Part 3. Requiring a separate vendor account, billing, and API key adds friction for
this audience.

## Decision

Use the GitHub Copilot SDK (`github-copilot-sdk`) as the primary path in Part 10.
Lesson 10.1 includes a short side-by-side with a direct vendor SDK so learners understand
a plain API call and can transfer the skill.

## Consequences

- No new account or key for learners who already have Copilot; BYOK lets learners with a
  company key reuse the same code.
- The SDK is in preview and may change in breaking ways; Part 10 pages are marked ⏱ and
  examples pin the SDK version.
- Prompts consume Copilot premium requests; lesson 10.3 (batch processing) must keep
  datasets small on the Free plan and explain when Pro is needed.
- The SDK requires the Copilot CLI and uses an async, event-driven API; lesson 10.1 must
  introduce async at a practical level.
- Revisit at M11, or earlier if the SDK becomes a source of trouble. Switching to a direct
  vendor SDK affects only Part 10.
