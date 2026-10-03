# ADR-0013: learn.dompe.space as a multi-course site

- Status: Accepted
- Date: 2026-10-03

## Context

More courses may follow this one. They should share the domain, branding, components,
sponsor link, and author page, and the landing page should list them.

## Decision

One Astro Starlight site in one repository hosts all courses.

- The locale catalog pages (`/en/`, `/es/`) list the courses, generated from each
  course's `courses/<slug>/course.yml`.
- Each course lives under `/<locale>/<course-slug>/` with its own sidebar.
- This course's slug is `automation-ai`.
- Components, i18n strings, the About page, and CI are shared. Examples and datasets are
  per course.

Alternative considered: one repository per course served under the same domain. Rejected
because a GitHub Pages custom domain maps to a single repository unless the user-site repo
is used, and shared components would have to be duplicated or packaged.

## Consequences

The repository is named for the site, not the course. Adding a course means adding a
content directory, a `courses/<slug>/` directory, and a sidebar entry. A single build
deploys all courses, which is acceptable at this scale.
