# 07 - Open questions and risks

## Open questions

### Resolved

| #   | Question                         | Decision                                                                                                                                                                               |
| --- | -------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Q1  | Title                            | Automation & AI for Business Users: What They Never Taught You / Automatización e IA para profesionales: lo que nunca te enseñaron (ADR-0012)                                          |
| Q2  | Subdomain                        | learn.dompe.space, multi-course catalog (ADR-0002, ADR-0013)                                                                                                                           |
| Q3  | Repo                             | Personal account `ddompe`, repo `learn` → `github.com/ddompe/learn`                                                                                                                    |
| Q4  | GitHub Sponsors                  | Already set up on `ddompe`                                                                                                                                                             |
| Q5  | Employer policy                  | No concerns                                                                                                                                                                            |
| Q6  | Machine-translated Spanish pages | Publish with a visible notice (05-i18n.md)                                                                                                                                             |
| Q7  | Copilot plan                     | Recommend Copilot Free; upgrade to Pro only if the learner hits the limits                                                                                                             |
| Q8  | Notebooks                        | Jupyter notebooks inside VS Code as the main path; explain the classic Jupyter web UI and cloud notebooks (Google Colab) because learners will meet them; marimo as a bonus (ADR-0014) |
| Q10 | In-browser Python                | Later milestone (M12)                                                                                                                                                                  |
| Q12 | Root URL                         | Detect browser language, remember the learner's choice (03-architecture.md)                                                                                                            |
| Q13 | Site name                        | Let's learn together / Aprendamos juntos                                                                                                                                               |
| Q11 | Analytics                        | GoatCounter, script tag via Starlight `head`, no cookies                                                                                                                               |
| Q9  | LLM SDK for Part 10              | GitHub Copilot SDK (ADR-0015); revisit if it causes trouble                                                                                                                            |
| Q14 | Author bio                       | Short and generic, no employer named (about-author.md)                                                                                                                                 |

### Still open

None. New questions are added here as chapters are briefed.

### Q9 background: why the Copilot SDK

The Copilot SDK exposes the agent runtime behind Copilot CLI and has a Python package
(`github-copilot-sdk`).

For:

- Learners already have a Copilot account from Part 3, so Part 10 needs no new vendor
  account, credit card, or API key. This is a major simplification for this audience.
- It supports custom tools and agents, which fits lessons 10.5 and 10.6.
- It also supports bring-your-own-key, so learners with a company OpenAI or Anthropic key
  can use the same code.

Against:

- It is in preview and may change in breaking ways; it would be the most volatile part
  of the course.
- Each prompt counts against the Copilot premium request quota, which is small on the Free
  plan. Batch classification of hundreds of comments (10.3) may push learners to Pro.
- It requires the Copilot CLI installed alongside it, and its API is asynchronous,
  agent-oriented, and event-driven, which is more to explain than a single
  request/response call.

Proposal: use the Copilot SDK as the primary path for Part 10. Add a short side-by-side
in 10.1 showing the same request through a direct vendor SDK, so learners understand what
a plain API call looks like and can transfer the skill. Re-evaluate at M11 when the SDK may
be out of preview.

### Q11 background: why GoatCounter

Requirements: simple setup on a static site, page views per page and per locale, referrers,
no cookies (so no consent banner for European visitors), free or cheap.

| Tool                         | Cost                                            | Notes                                                                                               |
| ---------------------------- | ----------------------------------------------- | --------------------------------------------------------------------------------------------------- |
| **GoatCounter**              | Free for non-commercial use (donations welcome) | One script tag, no cookies, open source, simple dashboard, supports custom events. **Recommended.** |
| Cloudflare Web Analytics     | Free                                            | One script tag, no cookies; very basic reports. Good fallback.                                      |
| Umami (cloud or self-hosted) | Free hobby tier / self-host                     | Nicer dashboards; self-hosting is more maintenance.                                                 |
| Plausible                    | Paid (self-host possible)                       | Polished, but a monthly cost for a free course.                                                     |

Verify current plans and terms at M0. Implementation: add the script via Starlight's
`head` config so every page in every locale is tracked.

## Risks

| Risk                                         | Impact                                 | Mitigation                                                                            |
| -------------------------------------------- | -------------------------------------- | ------------------------------------------------------------------------------------- |
| Scope is large (~90 lessons)                 | Course never ships                     | Pilot Parts 0–2, publish part by part, learn from pilot learners                      |
| Fast-changing AI content goes stale          | Credibility loss                       | Isolate volatile facts, `lastVerified`, 6-month review cadence                        |
| Corporate laptop restrictions block installs | Learners drop out at Part 3/4          | uv (no admin), dedicated troubleshooting page, test on a locked-down Windows machine  |
| AI-generated lesson drafts are generic       | Course looks like every other tutorial | Chapter briefs specify real pitfalls and the case study; human review on every lesson |
| Translation lags behind English              | Spanish site always incomplete         | Translate per part; staleness checker                                                 |
| Tool versions change (uv, Starlight, pandas) | Broken instructions                    | Pinned versions, CI runs all examples, scheduled dependency updates                   |
