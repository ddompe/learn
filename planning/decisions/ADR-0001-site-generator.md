# ADR-0001: Astro Starlight as site generator

- Status: Accepted
- Date: 2026-10-03

## Context

We need a static site on GitHub Pages with first-class multi-language support, good search, and a documentation-style UX. Candidates: Quarto (weak i18n), Docusaurus (heavier React stack), Material for MkDocs (scheduled for end of life on 2026-11-05), Zensical (young), Jupyter Book 2 (i18n not first-class).

## Decision

Use Astro with the Starlight theme. The npm toolchain is acceptable.

## Consequences

Built-in locale routing, language picker, UI translations, English fallback, and Pagefind search. Python outputs are not executed by the site generator, so we need our own example pipeline (ADR-0011). MDX allows custom components such as PromptExample.
