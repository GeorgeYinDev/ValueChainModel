# Role Definition: Internal Auditor

- **Role ID**: `role_internal_auditor`
- **Department**: Internal Audit & Corporate Governance
- **Reports To**: Audit Committee of Board of Directors / Chief Audit Executive
- **Internal / External**: Internal

## Key Responsibilities
- Independently test and validate internal controls over financial reporting (ICFR) under Sarbanes-Oxley (SOX 404).
- Audit Segregation of Duties (SoD) profiles across ERP, consolidation systems, and banking gateways.
- Perform stratified sampling and forensics on manual journal entries, management overrides, and post-close adjustments.
- Issue formal audit deficiency findings, control gap remediation tracking, and governance assurance opinions.

## Decision Rights & Financial Approval Limits
- **Audit Access Rights**: Read-only enterprise-wide query and extraction authority across all financial ledgers and consolidation engines.
- **Control Issue Escalation**: Direct reporting line to the Board Audit Committee for material weaknesses and significant deficiencies.
- **Operational Authority**: Strictly non-operational (zero transaction posting or approval rights to ensure complete audit independence).

## Required IT Systems Access
- `asset_erp_system` (Role: Internal Audit Read-Only Inspector)
- `asset_financial_consolidation_system` (Role: Internal Audit Read-Only Inspector)
