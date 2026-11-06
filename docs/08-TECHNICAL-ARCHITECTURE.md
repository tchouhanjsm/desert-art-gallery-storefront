# 08 — Technical Architecture

## Status
No application stack is approved. This document defines how to choose one; it does not declare that the project uses a particular framework.

## Discovery required
Document:
- Catalogue size and data shape.
- Product variants and inventory model.
- Admin and content editing needs.
- Direct purchase versus enquiry workflow.
- Checkout and order requirements.
- Payment-provider availability for confirmed seller jurisdiction and target markets.
- Shipping and tax integration.
- Authentication and customer-account needs.
- Search and filtering.
- Image storage, transformation and delivery.
- Traffic, availability and operational support.
- Hosting skills, cost constraints and deployment requirements.
- Selective migration needs from the legacy repository.

## Principles
- Prefer the simplest architecture that meets demonstrated needs.
- Avoid premature microservices.
- Keep authoritative pricing, tax, inventory and order rules on trusted server-side boundaries.
- Validate sensitive operations on the server.
- Use stable product identifiers.
- Keep media separate from source control.
- Use environment configuration and secret management.
- Plan backups, restore testing, observability and recovery.
- Avoid vendor commitments before requirements and costs are understood.

## Legacy engineering assessment
For each proposed reuse from the old repository, document:
- Source file/system.
- Purpose and actual behaviour.
- Evidence it works.
- Security and data implications.
- Compatibility.
- Migration cost and tests.
- Decision: reuse, adapt, replace or reject.

Never copy legacy frontend code as a shortcut.

## Architecture decision records
For significant choices, document context, options, trade-offs, decision, consequences and date. Link the ADR in `docs/DECISIONS.md`.
