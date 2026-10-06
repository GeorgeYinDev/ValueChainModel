---
id: data_journal_entry
type: data_entity
name: "General Ledger Journal Entry"
version: "1.0.0"
lifecycles: ["R2R"]
lod_support: ["tier_2", "tier_3"]
tags: ["data", "finance", "ledger"]

data_entity_details:
  system_of_record: "asset_erp_system"
  owner: "role_finance_controller"

graph_relations:
  - relation: triggers
    target: r2r_002_intercompany_reconciliation
    weight: 1.0
---

# Data Entity: General Ledger Journal Entry

The core transactional artifact for accounting ledgers. Contains the debits, credits, accounting date, Chart of Accounts segment string, and business justification for financial recording.
