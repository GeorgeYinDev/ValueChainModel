# ADR-0005: Human Capital Operations (Hire-to-Retire) Taxonomy and Boundaries

## Status
Accepted

## Context
As the Enterprise Value Chain Modeling Engine expands beyond supply chain (S2P) and core financials (R2R), it is necessary to integrate human capital workflows. Labor constitutes a significant portion of operating expense and is a primary driver of capacity constraints. Furthermore, the payroll cycle directly feeds into the financial ledger, making the Hire-to-Retire (H2R) lifecycle a critical component of the broader enterprise architecture. We need to define the boundaries, milestones, and integration points for H2R.

## Decision
We will establish the `H2R` (Hire to Retire) lifecycle with the following boundaries and integration touchpoints:
- **Starting Point**: A job requisition is posted (headcount need identified).
- **Ending Point**: The employee separates from the organization and final offboarding settlements are processed.
- **Process Steps (Milestones)**:
  1. `h2r_001_job_requisition_posting`
  2. `h2r_002_candidate_screening_interview`
  3. `h2r_003_offer_letter_onboarding`
  4. `h2r_004_payroll_benefits_enrollment`
  5. `h2r_005_performance_compensation_review`
  6. `h2r_006_separation_offboarding_settlement`
- **Integration Points**:
  - `h2r_004_payroll_benefits_enrollment` will generate recurring payroll expense and tax liabilities, directly feeding into `r2r_001_journal_entry_recording`.

## Consequences
- Requires new enterprise assets (`asset_hcm_platform`, `asset_payroll_engine`) to be defined.
- Requires HR and Payroll roles to be added with standard frontmatter schema (Phase 6 compliance).
- Provides a foundation for modeling organizational capacity (FTE counts) dynamically in future simulation updates.
