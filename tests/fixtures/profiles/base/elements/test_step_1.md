---
id: test_step_1
type: process_step
name: Test Step 1
version: 1.0.0
lifecycles: [TEST_LC]
lod_support: [tier_1]
tags: [test]
raci:
  responsible: [role_test_actor]
  accountable: [role_test_actor]
compensating_control: "Self-tested unit fixture"
asset_dependencies: [asset_test_system]
attributes:
  cycle_time_hours: 10.0
  cost_per_transaction_usd: 5.0
  error_rate: 0.05
  automation_percentage: 0.8
---
# Test Step 1
First process step in base fixture.
