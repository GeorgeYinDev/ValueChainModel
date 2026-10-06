---
id: test_step_2
type: process_step
name: Test Step 2
version: 1.0.0
lifecycles: [TEST_LC]
lod_support: [tier_1]
tags: [child]
raci:
  responsible: [role_test_actor]
  accountable: [role_test_actor]
compensating_control: "Self-tested unit fixture"
graph_relations:
  - relation: feeds_into
    target: test_step_1
attributes:
  cycle_time_hours: 5.0
  cost_per_transaction_usd: 2.0
  error_rate: 0.01
  automation_percentage: 0.9
---
# Test Step 2
Second process step in child fixture.
