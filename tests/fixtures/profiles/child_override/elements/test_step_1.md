---
id: test_step_1
overrides: base
type: process_step
name: Overridden Test Step 1
version: 1.1.0
lifecycles: [TEST_LC]
lod_support: [tier_1]
tags: [overridden]
raci:
  responsible: [role_test_actor]
  accountable: [role_test_actor]
compensating_control: "Self-tested unit fixture"
attributes:
  cycle_time_hours: 15.0
  cost_per_transaction_usd: 7.0
  error_rate: 0.02
  automation_percentage: 0.85
---
# Overridden Test Step 1
Overridden version of step 1.
