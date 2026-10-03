# ADR-0004: uv and pyproject.toml for Python

- Status: Accepted
- Date: 2026-10-03

## Context

Learners often use corporate laptops without admin rights. Traditional installs (python.org installer, pip, conda) cause PATH and permission problems and inconsistent environments.

## Decision

Teach uv exclusively for installing Python, creating projects, and managing dependencies via pyproject.toml and uv.lock. Pin the Python version per project. Choose the exact Python version at M1 based on library support.

## Consequences

One consistent workflow; no admin rights needed; reproducible environments. pip, conda, and poetry are mentioned only in Going deeper boxes.
