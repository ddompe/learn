# ADR-0010: Café Central as the running case study

- Status: Accepted
- Date: 2026-10-03

## Context

Context-free examples (hello world, foo/bar) fail to motivate business learners.

## Decision

All lessons use Café Central S.A., a fictional Costa Rican coffee company, with a deliberately messy, reproducibly generated dataset.

## Consequences

Concepts accumulate across parts toward a capstone pipeline. The dataset generator becomes a core asset that must be versioned carefully, since changes ripple through all examples.
