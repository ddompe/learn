# ADR-0005: GitHub Copilot in VS Code as the primary AI assistant; LLM APIs deferred

- Status: Accepted
- Date: 2026-10-03

## Context

The first goal is learners who are proficient in an IDE and use an AI assistant to help them work. Calling LLM APIs from code adds secrets, cost, and complexity too early.

## Decision

From Part 3 onward, learners use GitHub Copilot in VS Code. LLM API usage is taught only in Part 10 (Advanced).

## Consequences

The core path needs no API keys or paid accounts beyond what Copilot requires. Copilot features change fast, so lesson 3.3 is marked fast-changing.
