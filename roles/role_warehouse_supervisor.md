---
id: role_warehouse_supervisor
type: role
name: "Warehouse & Fulfillment Supervisor"
department: "Supply Chain & Logistics Fulfillment"
approval_limit_usd: 0.0
---
# Role Definition: Warehouse & Fulfillment Supervisor

- **Role ID**: `role_warehouse_supervisor`
- **Department**: Supply Chain & Logistics Fulfillment
- **Reports To**: VP Supply Chain Operations
- **Internal / External**: Internal

## Key Responsibilities
- Supervise warehouse wave picking, packing, staging, and dispatch operations.
- Ensure strict compliance with shipping SLAs, palletizing standards, and hazardous material rules.
- Confirm outbound delivery orders, generate Bills of Lading (BOL), and trigger ERP goods issue.
- Resolve fulfillment discrepancies, stock shortages, and carrier detention exceptions.

## Decision Rights & Financial Approval Limits
- **Inventory Adjustment Sign-off**: Discrepancies up to $10,000 USD.
- **Expedited Freight Approval**: Up to $2,500 USD per dispatch event.

## Required IT Systems Access
- `asset_wms_system` (Role: Warehouse Operations Supervisor)
- `asset_erp_system` (Role: Outbound Delivery Processor)
