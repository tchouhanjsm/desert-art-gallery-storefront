# 12 — Merchant Operations

## Purpose
Design the public storefront with realistic owner/admin operations in mind. Do not build a complex admin system prematurely.

## Operating capabilities to understand
- Product creation and editing.
- Product identifiers/SKUs and variants.
- Product status: draft, published, unavailable, archived.
- Price and enquiry status.
- Category and collection assignment.
- Product descriptions/specifications.
- Image selection, ordering, rights and approval.
- Inventory and one-of-a-kind handling.
- Order review and fulfilment.
- Customer enquiries.
- Shipping and tracking updates.
- Returns/refunds when policy is approved.
- Content and journal publishing.
- Customer-service workflow.
- Audit trail and permissions.

## Product publishing workflow
A proposed workflow:
1. Product record created.
2. Facts and specifications verified.
3. Price/commercial status confirmed.
4. Images matched and rights checked.
5. Copy reviewed.
6. Owner approves publication.
7. Product is published.
8. Updates and unpublishing are auditable.

This is a proposal, not an approved process. Validate it with the owner.

## Operational safeguards
- Never expose internal notes or draft/test products to customers.
- Separate development/CI fixtures from production catalogue data.
- Enforce role-based access for owner/admin actions.
- Keep pricing, inventory and order changes auditable.
- Never allow client-side values to be authoritative for financial or stock operations.
- Protect personal and order data.
- Plan backups and test restoration.

## Future design requirement
The admin workflow should be efficient for a small merchant team. Do not create a feature merely because enterprise platforms include it. Validate the actual operating need first.


## Draft catalogue intake controls

The proposed [catalogue intake standard](20-CATALOGUE-INTAKE-AND-FACT-VERIFICATION.md) separates product identity, factual evidence, public approval and image rights/publication approval. The local validator checks structure and cross-file references; it does not verify truth or approve records. Treat these statuses as draft intake conventions until the owner confirms the workflow.
