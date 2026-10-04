# ADR 0004: Record-to-Report (R2R) Lifecycle Taxonomy and Boundary Design

- **Status**: Approved
- **Date**: 2026-10-03
- **Authors**: Enterprise Architecture Team / Antigravity AI

## Context
Following the implementation of the Source-to-Pay (S2P, ADR-0002) and Order-to-Cash (O2C, ADR-0003) lifecycles, the enterprise value chain requires the third foundational pillar: **Record-to-Report (R2R)**. 

R2R represents the core general ledger and financial accounting engine of the enterprise. It ingests transactional feeds from procurement (AP subledger) and commercial sales (AR subledger), performs intercompany matching and eliminations, enforces balance sheet substantiation, orchestrates multi-entity close consolidation, and produces certified statutory and regulatory disclosures.

## Decision
We define the Record-to-Report (R2R) lifecycle as a 5-step milestone-driven accounting value chain:
1. `r2r_001_journal_entry_recording`: Ingestion of operational subledgers (AP disbursements from `s2p_008`, AR clearing from `o2c_005`), validation of manual journal vouchers, and posting to general ledger.
2. `r2r_002_intercompany_reconciliation`: Automated reciprocal transaction matching across global subsidiaries, bilateral dispute resolution, and cross-border elimination.
3. `r2r_003_balance_sheet_substantiation`: Account-level substantiation against bank statements, inventory counts, and aging schedules under SOX 404 guidelines.
4. `r2r_004_financial_close_consolidation`: Multi-currency translation, period-end ledger locking, top-side adjustments, and group consolidation.
5. `r2r_005_statutory_financial_reporting`: Assembly of external financial statements (SEC 10-K/10-Q under US GAAP/IFRS), footnotes, and board reporting packs.

### Enterprise Roles Included
- General Ledger Accountant (`role_general_ledger_accountant`): Operational preparer of journals and account substantiations.
- Financial Consolidation Specialist (`role_consolidation_specialist`): Lead driver for intercompany matching, currency translation, and consolidation roll-ups.
- Internal Auditor (`role_internal_auditor`): Independent reviewer evaluating SOX 404 controls, SoD profiles, and journal sampling.
- Finance Controller (`role_finance_controller`): Single designated approver holding ultimate sign-off authority across all close milestones.
- Accounts Payable Clerk (`role_accounts_payable_clerk`): Consulted on subledger AP feeds.
- Billing & AR Specialist (`role_billing_specialist`): Consulted on subledger AR feeds.

### Core Assets Included
- Enterprise Core ERP (`asset_erp_system`): System of record for transactional general ledgers.
- Financial Consolidation & Reporting System (`asset_financial_consolidation_system`): Dedicated platform for group eliminations, currency translations, and disclosure management (child asset of `asset_erp_system`).

### Governance & Value Stream
- Control Policy: `sox_financial_reporting_controls_policy` (mandates dual sign-offs for entries >= $50,000 USD, strict SoD, and T+3 substantiation deadlines).
- Value Stream: `financial_close_reporting_stream` (aggregates end-to-end close and reporting velocity).

## Consequences
- **Financial Triad Completed**: Unifies S2P, O2C, and R2R into a cohesive, bi-directionally linked enterprise knowledge graph.
- **Strict SoD & Single Approver Rule**: Zero Segregation of Duties conflicts between execution and approval, with `role_finance_controller` functioning as the authoritative Approver (A) across all close decisions.
- **Stress-Testing Ready**: Quantitative simulation via `scenario_close_period_crunch.json` models year-end close bottlenecks and manual adjustment spikes.
