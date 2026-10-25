# Enterprise Value Chain Diagrams Summary [ALL]

Auto-generated visualization pack compiled from validated knowledge graph index.

---

## 1. End-to-End Value Chain Process Flowchart
```mermaid
flowchart TD
  %% Style Classes
  classDef processStep fill:#0f172a,stroke:#38bdf8,stroke-width:2px,color:#f8fafc,rx:8,ry:8;
  classDef controlPolicy fill:#1e1b4b,stroke:#a855f7,stroke-width:2px,stroke-dasharray: 4 4,color:#f3e8ff,rx:4,ry:4;
  classDef valueStream fill:#064e3b,stroke:#34d399,stroke-width:2px,color:#ecfdf5,rx:12,ry:12;

  subgraph Subgraph_ValueStreams ["<b>Enterprise Value Streams</b>"]
    client_onboarding_kyc_stream[["<b>Stream: Institutional Client Onboarding &amp; KYC/AML Compliance Value Stream</b><br/><small>client_onboarding_kyc_stream</small>"]]:::valueStream
    commercial_lending_servicing_stream[["<b>Stream: Commercial Loan Origination, Underwriting &amp; Servicing Value Stream</b><br/><small>commercial_lending_servicing_stream</small>"]]:::valueStream
    financial_close_reporting_stream[["<b>Stream: Financial Close, Consolidation &amp; Regulatory Reporting Stream</b><br/><small>financial_close_reporting_stream</small>"]]:::valueStream
    procure_to_pay_stream[["<b>Stream: Procure to Pay (P2P) Operational Value Stream</b><br/><small>procure_to_pay_stream</small>"]]:::valueStream
    strategic_sourcing_stream[["<b>Stream: Strategic Sourcing &amp; Contracting Value Stream</b><br/><small>strategic_sourcing_stream</small>"]]:::valueStream
  end

  subgraph Subgraph_H2R_talent_acquisition ["<b>Talent Acquisition & Onboarding Phase</b>"]
    h2r_001_job_requisition_posting["<b>Job Requisition Definition &amp; Posting</b><br/><small>ID: h2r_001_job_requisition_posting</small><br/>⏱ 48.0h | 💰 $120.0 | ⚡ 10% auto"]:::processStep
    h2r_002_candidate_screening_interview["<b>Candidate Screening &amp; Interview Execution</b><br/><small>ID: h2r_002_candidate_screening_interview</small><br/>⏱ 168.0h | 💰 $800.0 | ⚡ 30% auto"]:::processStep
    h2r_003_offer_letter_onboarding["<b>Offer Letter Generation &amp; Employee Onboarding</b><br/><small>ID: h2r_003_offer_letter_onboarding</small><br/>⏱ 48.0h | 💰 $150.0 | ⚡ 70% auto"]:::processStep
  end

  subgraph Subgraph_H2R_talent_management_payroll ["<b>Payroll, Performance & Offboarding Phase</b>"]
    h2r_004_payroll_benefits_enrollment["<b>Payroll &amp; Benefits Enrollment Processing</b><br/><small>ID: h2r_004_payroll_benefits_enrollment</small><br/>⏱ 24.0h | 💰 $45.0 | ⚡ 85% auto"]:::processStep
    h2r_005_performance_compensation_review["<b>Performance &amp; Compensation Review</b><br/><small>ID: h2r_005_performance_compensation_review</small><br/>⏱ 120.0h | 💰 $200.0 | ⚡ 40% auto"]:::processStep
    h2r_006_separation_offboarding_settlement["<b>Separation, Offboarding &amp; Final Settlement</b><br/><small>ID: h2r_006_separation_offboarding_settlement</small><br/>⏱ 48.0h | 💰 $300.0 | ⚡ 50% auto"]:::processStep
  end

  subgraph Subgraph_R2R_subledger_reconciliation ["<b>Subledger Ingestion & Substantiation Phase</b>"]
    r2r_001_journal_entry_recording["<b>General Ledger Journal Recording &amp; Subledger Ingestion</b><br/><small>ID: r2r_001_journal_entry_recording</small><br/>⏱ 8.0h | 💰 $18.0 | ⚡ 82% auto"]:::processStep
    r2r_002_intercompany_reconciliation["<b>Intercompany Transaction Matching &amp; Elimination</b><br/><small>ID: r2r_002_intercompany_reconciliation</small><br/>⏱ 12.0h | 💰 $35.0 | ⚡ 75% auto"]:::processStep
    r2r_003_balance_sheet_substantiation["<b>Balance Sheet Account Substantiation &amp; Reconciliation</b><br/><small>ID: r2r_003_balance_sheet_substantiation</small><br/>⏱ 16.0h | 💰 $45.0 | ⚡ 70% auto"]:::processStep
  end

  subgraph Subgraph_R2R_close_reporting ["<b>Financial Close & Group Reporting Phase</b>"]
    r2r_004_financial_close_consolidation["<b>Financial Close Orchestration &amp; Group Consolidation</b><br/><small>ID: r2r_004_financial_close_consolidation</small><br/>⏱ 20.0h | 💰 $65.0 | ⚡ 80% auto"]:::processStep
    r2r_005_statutory_financial_reporting["<b>Statutory, Tax &amp; Management Financial Reporting</b><br/><small>ID: r2r_005_statutory_financial_reporting</small><br/>⏱ 14.0h | 💰 $50.0 | ⚡ 65% auto"]:::processStep
  end

  subgraph Subgraph_S2P_sourcing ["<b>Strategic Sourcing & Contracting Phase</b>"]
    s2p_001_spend_analysis_need_id["<b>Spend Analysis &amp; Need Identification</b><br/><small>ID: s2p_001_spend_analysis_need_id</small><br/>⏱ 12.0h | 💰 $45.0 | ⚡ 70% auto"]:::processStep
    s2p_002_supplier_discovery_qualification["<b>Supplier Discovery &amp; Qualification</b><br/><small>ID: s2p_002_supplier_discovery_qualification</small><br/>⏱ 48.0h | 💰 $120.0 | ⚡ 50% auto"]:::processStep
    s2p_003_sourcing_rfx_auction["<b>Strategic Sourcing &amp; RFx Execution</b><br/><small>ID: s2p_003_sourcing_rfx_auction</small><br/>⏱ 96.0h | 💰 $250.0 | ⚡ 65% auto"]:::processStep
    s2p_004_contracting_sla_negotiation["<b>Contracting &amp; SLA Negotiation</b><br/><small>ID: s2p_004_contracting_sla_negotiation</small><br/>⏱ 72.0h | 💰 $300.0 | ⚡ 40% auto"]:::processStep
  end

  subgraph Subgraph_S2P_procure_to_pay ["<b>Procure-to-Pay (P2P) Phase</b>"]
    s2p_005_purchase_requisition_po["<b>Purchase Requisition &amp; PO Issuance</b><br/><small>ID: s2p_005_purchase_requisition_po</small><br/>⏱ 8.0h | 💰 $18.0 | ⚡ 90% auto"]:::processStep
    s2p_006_goods_services_receipt["<b>Goods &amp; Services Receipt Verification</b><br/><small>ID: s2p_006_goods_services_receipt</small><br/>⏱ 6.0h | 💰 $12.5 | ⚡ 80% auto"]:::processStep
    s2p_007_invoice_verification_matching["<b>Invoice 3-Way Matching &amp; Exception Handling</b><br/><small>ID: s2p_007_invoice_verification_matching</small><br/>⏱ 16.0h | 💰 $22.0 | ⚡ 75% auto"]:::processStep
    s2p_008_payment_settlement_disbursement["<b>Payment Settlement &amp; Disbursement</b><br/><small>ID: s2p_008_payment_settlement_disbursement</small><br/>⏱ 4.0h | 💰 $8.5 | ⚡ 95% auto"]:::processStep
  end

  subgraph Subgraph_C2A_intake_verification ["<b>Client Intake & Identity Verification Phase</b>"]
    c2a_001_prospect_application_intake["<b>Prospect Application &amp; Entity Intake</b><br/><small>ID: c2a_001_prospect_application_intake</small><br/>⏱ 2.0h | 💰 $85.0 | ⚡ 75% auto"]:::processStep
    c2a_002_kyc_cip_identity_verification["<b>KYC/CIP Identity &amp; UBO Verification</b><br/><small>ID: c2a_002_kyc_cip_identity_verification</small><br/>⏱ 6.0h | 💰 $160.0 | ⚡ 65% auto"]:::processStep
  end

  subgraph Subgraph_C2A_fincrime_activation ["<b>Financial Crime Due Diligence & Account Activation Phase</b>"]
    c2a_003_aml_sanctions_pep_screening["<b>AML Sanctions, PEP &amp; Adverse Media Screening</b><br/><small>ID: c2a_003_aml_sanctions_pep_screening</small><br/>⏱ 4.0h | 💰 $120.0 | ⚡ 80% auto"]:::processStep
    c2a_004_enhanced_due_diligence_compliance["<b>Enhanced Due Diligence (EDD) &amp; BSA Approval</b><br/><small>ID: c2a_004_enhanced_due_diligence_compliance</small><br/>⏱ 16.0h | 💰 $450.0 | ⚡ 35% auto"]:::processStep
    c2a_005_account_provisioning_core_activation["<b>Core Account Provisioning &amp; Treasury Activation</b><br/><small>ID: c2a_005_account_provisioning_core_activation</small><br/>⏱ 3.0h | 💰 $95.0 | ⚡ 85% auto"]:::processStep
  end

  subgraph Subgraph_L2S_origination_underwriting ["<b>Credit Origination & Underwriting Phase</b>"]
    l2s_001_loan_application_credit_packaging["<b>Loan Application &amp; Credit Packaging</b><br/><small>ID: l2s_001_loan_application_credit_packaging</small><br/>⏱ 12.0h | 💰 $380.0 | ⚡ 55% auto"]:::processStep
    l2s_002_credit_underwriting_risk_rating["<b>Credit Underwriting &amp; PD/LGD Risk Rating</b><br/><small>ID: l2s_002_credit_underwriting_risk_rating</small><br/>⏱ 24.0h | 💰 $820.0 | ⚡ 45% auto"]:::processStep
  end

  subgraph Subgraph_L2S_closing_funding ["<b>Collateral Closing & Facility Funding Phase</b>"]
    l2s_003_collateral_valuation_lien_perfection["<b>Collateral Valuation &amp; Lien Perfection</b><br/><small>ID: l2s_003_collateral_valuation_lien_perfection</small><br/>⏱ 18.0h | 💰 $540.0 | ⚡ 50% auto"]:::processStep
    l2s_004_loan_booking_funding_disbursement["<b>Loan Booking &amp; Principal Funding Disbursement</b><br/><small>ID: l2s_004_loan_booking_funding_disbursement</small><br/>⏱ 4.0h | 💰 $150.0 | ⚡ 85% auto"]:::processStep
  end

  subgraph Subgraph_L2S_servicing_settlement ["<b>Portfolio Servicing, Workout & GL Settlement Phase</b>"]
    l2s_005_repayment_servicing_covenant_monitoring["<b>Repayment Servicing &amp; Covenant Monitoring</b><br/><small>ID: l2s_005_repayment_servicing_covenant_monitoring</small><br/>⏱ 6.0h | 💰 $190.0 | ⚡ 80% auto"]:::processStep
    l2s_006_delinquency_workout_ledger_settlement["<b>Delinquency Workout &amp; Subledger Reconciliation</b><br/><small>ID: l2s_006_delinquency_workout_ledger_settlement</small><br/>⏱ 10.0h | 💰 $310.0 | ⚡ 70% auto"]:::processStep
  end

  subgraph Subgraph_Governance ["<b>Governance & Control Policies</b>"]
    basel_credit_risk_underwriting_policy(["<b>Policy: Basel III Credit Risk Underwriting, Concentration &amp; CECL Policy</b><br/><small>basel_credit_risk_underwriting_policy</small>"]):::controlPolicy
    bsa_aml_kyc_compliance_policy(["<b>Policy: BSA/AML, USA PATRIOT Act CIP &amp; OFAC Sanctions Governance Policy</b><br/><small>bsa_aml_kyc_compliance_policy</small>"]):::controlPolicy
    sod_spending_limits_policy(["<b>Policy: Segregation of Duties &amp; Financial Authority Policy</b><br/><small>sod_spending_limits_policy</small>"]):::controlPolicy
    sox_financial_reporting_controls_policy(["<b>Policy: SOX 404 Financial Reporting Internal Controls &amp; Materiality Thresholds Policy</b><br/><small>sox_financial_reporting_controls_policy</small>"]):::controlPolicy
  end

  %% Process Flows & Policy Linkages
  data_journal_entry -. triggers .-> r2r_002_intercompany_reconciliation
  financial_close_reporting_stream -. governed by .-> sox_financial_reporting_controls_policy
  h2r_001_job_requisition_posting --> h2r_002_candidate_screening_interview
  h2r_002_candidate_screening_interview --> h2r_003_offer_letter_onboarding
  h2r_002_candidate_screening_interview -. exception_to .-> h2r_001_job_requisition_posting
  h2r_003_offer_letter_onboarding --> h2r_004_payroll_benefits_enrollment
  h2r_003_offer_letter_onboarding -. exception_to .-> h2r_002_candidate_screening_interview
  h2r_004_payroll_benefits_enrollment --> h2r_005_performance_compensation_review
  h2r_004_payroll_benefits_enrollment --> r2r_001_journal_entry_recording
  h2r_005_performance_compensation_review --> h2r_006_separation_offboarding_settlement
  h2r_006_separation_offboarding_settlement --> r2r_001_journal_entry_recording
  procure_to_pay_stream -. governed by .-> sod_spending_limits_policy
  r2r_001_journal_entry_recording --> r2r_002_intercompany_reconciliation
  r2r_001_journal_entry_recording -. governed by .-> sox_financial_reporting_controls_policy
  r2r_001_journal_entry_recording -. produces_artifact .-> data_journal_entry
  r2r_002_intercompany_reconciliation --> r2r_003_balance_sheet_substantiation
  r2r_002_intercompany_reconciliation -. governed by .-> sox_financial_reporting_controls_policy
  r2r_003_balance_sheet_substantiation --> r2r_004_financial_close_consolidation
  r2r_003_balance_sheet_substantiation -. governed by .-> sox_financial_reporting_controls_policy
  r2r_004_financial_close_consolidation --> r2r_005_statutory_financial_reporting
  r2r_004_financial_close_consolidation -. governed by .-> sox_financial_reporting_controls_policy
  r2r_005_statutory_financial_reporting -. governed by .-> sox_financial_reporting_controls_policy
  s2p_001_spend_analysis_need_id --> s2p_002_supplier_discovery_qualification
  s2p_001_spend_analysis_need_id -. governed by .-> sod_spending_limits_policy
  s2p_002_supplier_discovery_qualification --> s2p_003_sourcing_rfx_auction
  s2p_002_supplier_discovery_qualification -. governed by .-> sod_spending_limits_policy
  s2p_003_sourcing_rfx_auction --> s2p_004_contracting_sla_negotiation
  s2p_004_contracting_sla_negotiation --> s2p_005_purchase_requisition_po
  s2p_004_contracting_sla_negotiation -. governed by .-> sod_spending_limits_policy
  s2p_004_contracting_sla_negotiation --> l2s_003_collateral_valuation_lien_perfection
  s2p_005_purchase_requisition_po --> s2p_006_goods_services_receipt
  s2p_005_purchase_requisition_po -. governed by .-> sod_spending_limits_policy
  s2p_006_goods_services_receipt --> s2p_007_invoice_verification_matching
  s2p_007_invoice_verification_matching --> s2p_008_payment_settlement_disbursement
  s2p_007_invoice_verification_matching -. exception_to .-> s2p_006_goods_services_receipt
  s2p_007_invoice_verification_matching -. governed by .-> sod_spending_limits_policy
  s2p_008_payment_settlement_disbursement --> r2r_001_journal_entry_recording
  s2p_008_payment_settlement_disbursement -. governed by .-> sod_spending_limits_policy
  strategic_sourcing_stream --> procure_to_pay_stream
  data_credit_facility_agreement -. triggers .-> l2s_004_loan_booking_funding_disbursement
  data_kyc_cdd_dossier -. triggers .-> c2a_005_account_provisioning_core_activation
  kpi_kyc_onboarding_time_to_yes -. impacted_by .-> c2a_004_enhanced_due_diligence_compliance
  kpi_kyc_onboarding_time_to_yes -. impacted_by .-> c2a_005_account_provisioning_core_activation
  kpi_net_interest_margin -. impacted_by .-> l2s_004_loan_booking_funding_disbursement
  kpi_net_interest_margin -. impacted_by .-> l2s_005_repayment_servicing_covenant_monitoring
  kpi_non_performing_loan_ratio -. impacted_by .-> l2s_002_credit_underwriting_risk_rating
  kpi_non_performing_loan_ratio -. impacted_by .-> l2s_006_delinquency_workout_ledger_settlement
  c2a_001_prospect_application_intake --> c2a_002_kyc_cip_identity_verification
  c2a_001_prospect_application_intake -. governed by .-> bsa_aml_kyc_compliance_policy
  c2a_002_kyc_cip_identity_verification --> c2a_003_aml_sanctions_pep_screening
  c2a_002_kyc_cip_identity_verification -. governed by .-> bsa_aml_kyc_compliance_policy
  c2a_003_aml_sanctions_pep_screening --> c2a_004_enhanced_due_diligence_compliance
  c2a_003_aml_sanctions_pep_screening -. governed by .-> bsa_aml_kyc_compliance_policy
  c2a_004_enhanced_due_diligence_compliance --> c2a_005_account_provisioning_core_activation
  c2a_004_enhanced_due_diligence_compliance -. produces_artifact .-> data_kyc_cdd_dossier
  c2a_004_enhanced_due_diligence_compliance -. governed by .-> bsa_aml_kyc_compliance_policy
  c2a_004_enhanced_due_diligence_compliance -. exception_to .-> c2a_002_kyc_cip_identity_verification
  c2a_005_account_provisioning_core_activation --> l2s_001_loan_application_credit_packaging
  c2a_005_account_provisioning_core_activation -. governed by .-> bsa_aml_kyc_compliance_policy
  l2s_001_loan_application_credit_packaging --> l2s_002_credit_underwriting_risk_rating
  l2s_001_loan_application_credit_packaging -. governed by .-> basel_credit_risk_underwriting_policy
  l2s_002_credit_underwriting_risk_rating --> l2s_003_collateral_valuation_lien_perfection
  l2s_002_credit_underwriting_risk_rating -. governed by .-> basel_credit_risk_underwriting_policy
  l2s_002_credit_underwriting_risk_rating -. exception_to .-> l2s_001_loan_application_credit_packaging
  l2s_003_collateral_valuation_lien_perfection --> l2s_004_loan_booking_funding_disbursement
  l2s_003_collateral_valuation_lien_perfection -. produces_artifact .-> data_credit_facility_agreement
  l2s_003_collateral_valuation_lien_perfection -. governed by .-> basel_credit_risk_underwriting_policy
  l2s_004_loan_booking_funding_disbursement --> l2s_005_repayment_servicing_covenant_monitoring
  l2s_004_loan_booking_funding_disbursement -. governed by .-> basel_credit_risk_underwriting_policy
  l2s_004_loan_booking_funding_disbursement -. governed by .-> bsa_aml_kyc_compliance_policy
  l2s_005_repayment_servicing_covenant_monitoring --> l2s_006_delinquency_workout_ledger_settlement
  l2s_005_repayment_servicing_covenant_monitoring -. governed by .-> basel_credit_risk_underwriting_policy
  l2s_006_delinquency_workout_ledger_settlement --> r2r_001_journal_entry_recording
  l2s_006_delinquency_workout_ledger_settlement -. governed by .-> basel_credit_risk_underwriting_policy
  client_onboarding_kyc_stream -. governed by .-> bsa_aml_kyc_compliance_policy
  client_onboarding_kyc_stream --> commercial_lending_servicing_stream
  commercial_lending_servicing_stream -. governed by .-> basel_credit_risk_underwriting_policy
  commercial_lending_servicing_stream --> financial_close_reporting_stream
```

---

## 2. RACI Role Handoff & Swimlane Sequence
```mermaid
flowchart LR
  %% RACI Swimlanes Styling
  classDef roleLane fill:#0f172a,stroke:#64748b,stroke-width:1px,color:#cbd5e1;
  classDef rNode fill:#1e3a8a,stroke:#60a5fa,stroke-width:2px,color:#eff6ff,rx:6,ry:6;
  classDef aNode fill:#701a75,stroke:#f472b6,stroke-width:2px,color:#fdf2f8,rx:6,ry:6;

  subgraph Sub_role_accounts_payable_clerk ["<b>Accounts Payable Clerk</b>"]
    s2p_007_invoice_verification_matching__R["<b>Invoice 3-Way Matching &amp; Exception Handling</b><br/>Role: <b>Responsible (R)</b>"]:::rNode
    s2p_008_payment_settlement_disbursement__R["<b>Payment Settlement &amp; Disbursement</b><br/>Role: <b>Responsible (R)</b>"]:::rNode
  end

  subgraph Sub_role_bsa_compliance_officer ["<b>BSA / AML Chief Compliance Officer</b>"]
    c2a_001_prospect_application_intake__A["<b>Prospect Application &amp; Entity Intake</b><br/>Role: <b>Accountable (A)</b>"]:::aNode
    c2a_002_kyc_cip_identity_verification__A["<b>KYC/CIP Identity &amp; UBO Verification</b><br/>Role: <b>Accountable (A)</b>"]:::aNode
    c2a_003_aml_sanctions_pep_screening__A["<b>AML Sanctions, PEP &amp; Adverse Media Screening</b><br/>Role: <b>Accountable (A)</b>"]:::aNode
    c2a_004_enhanced_due_diligence_compliance__A["<b>Enhanced Due Diligence (EDD) &amp; BSA Approval</b><br/>Role: <b>Accountable (A)</b>"]:::aNode
  end

  subgraph Sub_role_category_manager ["<b>Category Manager</b>"]
    s2p_004_contracting_sla_negotiation__R["<b>Contracting &amp; SLA Negotiation</b><br/>Role: <b>Responsible (R)</b>"]:::rNode
    s2p_001_spend_analysis_need_id__A["<b>Spend Analysis &amp; Need Identification</b><br/>Role: <b>Accountable (A)</b>"]:::aNode
    s2p_002_supplier_discovery_qualification__A["<b>Supplier Discovery &amp; Qualification</b><br/>Role: <b>Accountable (A)</b>"]:::aNode
    s2p_003_sourcing_rfx_auction__A["<b>Strategic Sourcing &amp; RFx Execution</b><br/>Role: <b>Accountable (A)</b>"]:::aNode
    s2p_004_contracting_sla_negotiation__A["<b>Contracting &amp; SLA Negotiation</b><br/>Role: <b>Accountable (A)</b>"]:::aNode
    s2p_005_purchase_requisition_po__A["<b>Purchase Requisition &amp; PO Issuance</b><br/>Role: <b>Accountable (A)</b>"]:::aNode
    s2p_006_goods_services_receipt__A["<b>Goods &amp; Services Receipt Verification</b><br/>Role: <b>Accountable (A)</b>"]:::aNode
  end

  subgraph Sub_role_chief_credit_officer ["<b>Chief Credit Officer (CCO)</b>"]
    l2s_002_credit_underwriting_risk_rating__A["<b>Credit Underwriting &amp; PD/LGD Risk Rating</b><br/>Role: <b>Accountable (A)</b>"]:::aNode
    l2s_003_collateral_valuation_lien_perfection__A["<b>Collateral Valuation &amp; Lien Perfection</b><br/>Role: <b>Accountable (A)</b>"]:::aNode
    l2s_005_repayment_servicing_covenant_monitoring__A["<b>Repayment Servicing &amp; Covenant Monitoring</b><br/>Role: <b>Accountable (A)</b>"]:::aNode
  end

  subgraph Sub_role_consolidation_specialist ["<b>Financial Consolidation Specialist</b>"]
    r2r_002_intercompany_reconciliation__R["<b>Intercompany Transaction Matching &amp; Elimination</b><br/>Role: <b>Responsible (R)</b>"]:::rNode
    r2r_004_financial_close_consolidation__R["<b>Financial Close Orchestration &amp; Group Consolidation</b><br/>Role: <b>Responsible (R)</b>"]:::rNode
    r2r_005_statutory_financial_reporting__R["<b>Statutory, Tax &amp; Management Financial Reporting</b><br/>Role: <b>Responsible (R)</b>"]:::rNode
  end

  subgraph Sub_role_credit_underwriter ["<b>Commercial Credit Underwriter</b>"]
    l2s_002_credit_underwriting_risk_rating__R["<b>Credit Underwriting &amp; PD/LGD Risk Rating</b><br/>Role: <b>Responsible (R)</b>"]:::rNode
    l2s_005_repayment_servicing_covenant_monitoring__R["<b>Repayment Servicing &amp; Covenant Monitoring</b><br/>Role: <b>Responsible (R)</b>"]:::rNode
    l2s_001_loan_application_credit_packaging__A["<b>Loan Application &amp; Credit Packaging</b><br/>Role: <b>Accountable (A)</b>"]:::aNode
  end

  subgraph Sub_role_finance_controller ["<b>Finance Controller</b>"]
    r2r_001_journal_entry_recording__A["<b>General Ledger Journal Recording &amp; Subledger Ingestion</b><br/>Role: <b>Accountable (A)</b>"]:::aNode
    r2r_002_intercompany_reconciliation__A["<b>Intercompany Transaction Matching &amp; Elimination</b><br/>Role: <b>Accountable (A)</b>"]:::aNode
    r2r_003_balance_sheet_substantiation__A["<b>Balance Sheet Account Substantiation &amp; Reconciliation</b><br/>Role: <b>Accountable (A)</b>"]:::aNode
    r2r_004_financial_close_consolidation__A["<b>Financial Close Orchestration &amp; Group Consolidation</b><br/>Role: <b>Accountable (A)</b>"]:::aNode
    r2r_005_statutory_financial_reporting__A["<b>Statutory, Tax &amp; Management Financial Reporting</b><br/>Role: <b>Accountable (A)</b>"]:::aNode
    l2s_006_delinquency_workout_ledger_settlement__A["<b>Delinquency Workout &amp; Subledger Reconciliation</b><br/>Role: <b>Accountable (A)</b>"]:::aNode
    s2p_007_invoice_verification_matching__A["<b>Invoice 3-Way Matching &amp; Exception Handling</b><br/>Role: <b>Accountable (A)</b>"]:::aNode
    s2p_008_payment_settlement_disbursement__A["<b>Payment Settlement &amp; Disbursement</b><br/>Role: <b>Accountable (A)</b>"]:::aNode
  end

  subgraph Sub_role_general_ledger_accountant ["<b>General Ledger Accountant</b>"]
    r2r_001_journal_entry_recording__R["<b>General Ledger Journal Recording &amp; Subledger Ingestion</b><br/>Role: <b>Responsible (R)</b>"]:::rNode
    r2r_003_balance_sheet_substantiation__R["<b>Balance Sheet Account Substantiation &amp; Reconciliation</b><br/>Role: <b>Responsible (R)</b>"]:::rNode
  end

  subgraph Sub_role_hiring_manager ["<b>Hiring Manager</b>"]
    h2r_001_job_requisition_posting__R["<b>Job Requisition Definition &amp; Posting</b><br/>Role: <b>Responsible (R)</b>"]:::rNode
    h2r_005_performance_compensation_review__R["<b>Performance &amp; Compensation Review</b><br/>Role: <b>Responsible (R)</b>"]:::rNode
    h2r_001_job_requisition_posting__A["<b>Job Requisition Definition &amp; Posting</b><br/>Role: <b>Accountable (A)</b>"]:::aNode
    h2r_002_candidate_screening_interview__A["<b>Candidate Screening &amp; Interview Execution</b><br/>Role: <b>Accountable (A)</b>"]:::aNode
    h2r_003_offer_letter_onboarding__A["<b>Offer Letter Generation &amp; Employee Onboarding</b><br/>Role: <b>Accountable (A)</b>"]:::aNode
    h2r_005_performance_compensation_review__A["<b>Performance &amp; Compensation Review</b><br/>Role: <b>Accountable (A)</b>"]:::aNode
  end

  subgraph Sub_role_hr_business_partner ["<b>HR Business Partner</b>"]
    h2r_006_separation_offboarding_settlement__R["<b>Separation, Offboarding &amp; Final Settlement</b><br/>Role: <b>Responsible (R)</b>"]:::rNode
    h2r_006_separation_offboarding_settlement__A["<b>Separation, Offboarding &amp; Final Settlement</b><br/>Role: <b>Accountable (A)</b>"]:::aNode
  end

  subgraph Sub_role_kyc_aml_analyst ["<b>KYC &amp; AML Compliance Analyst</b>"]
    c2a_002_kyc_cip_identity_verification__R["<b>KYC/CIP Identity &amp; UBO Verification</b><br/>Role: <b>Responsible (R)</b>"]:::rNode
    c2a_003_aml_sanctions_pep_screening__R["<b>AML Sanctions, PEP &amp; Adverse Media Screening</b><br/>Role: <b>Responsible (R)</b>"]:::rNode
    c2a_004_enhanced_due_diligence_compliance__R["<b>Enhanced Due Diligence (EDD) &amp; BSA Approval</b><br/>Role: <b>Responsible (R)</b>"]:::rNode
  end

  subgraph Sub_role_loan_servicing_specialist ["<b>Loan Closing &amp; Servicing Specialist</b>"]
    l2s_003_collateral_valuation_lien_perfection__R["<b>Collateral Valuation &amp; Lien Perfection</b><br/>Role: <b>Responsible (R)</b>"]:::rNode
    l2s_004_loan_booking_funding_disbursement__R["<b>Loan Booking &amp; Principal Funding Disbursement</b><br/>Role: <b>Responsible (R)</b>"]:::rNode
    c2a_005_account_provisioning_core_activation__R["<b>Core Account Provisioning &amp; Treasury Activation</b><br/>Role: <b>Responsible (R)</b>"]:::rNode
    l2s_005_repayment_servicing_covenant_monitoring__R["<b>Repayment Servicing &amp; Covenant Monitoring</b><br/>Role: <b>Responsible (R)</b>"]:::rNode
    l2s_006_delinquency_workout_ledger_settlement__R["<b>Delinquency Workout &amp; Subledger Reconciliation</b><br/>Role: <b>Responsible (R)</b>"]:::rNode
  end

  subgraph Sub_role_payroll_specialist ["<b>Payroll Specialist</b>"]
    h2r_004_payroll_benefits_enrollment__R["<b>Payroll &amp; Benefits Enrollment Processing</b><br/>Role: <b>Responsible (R)</b>"]:::rNode
    h2r_004_payroll_benefits_enrollment__A["<b>Payroll &amp; Benefits Enrollment Processing</b><br/>Role: <b>Accountable (A)</b>"]:::aNode
  end

  subgraph Sub_role_procurement_specialist ["<b>Procurement Specialist</b>"]
    s2p_001_spend_analysis_need_id__R["<b>Spend Analysis &amp; Need Identification</b><br/>Role: <b>Responsible (R)</b>"]:::rNode
    s2p_002_supplier_discovery_qualification__R["<b>Supplier Discovery &amp; Qualification</b><br/>Role: <b>Responsible (R)</b>"]:::rNode
    s2p_003_sourcing_rfx_auction__R["<b>Strategic Sourcing &amp; RFx Execution</b><br/>Role: <b>Responsible (R)</b>"]:::rNode
    s2p_005_purchase_requisition_po__R["<b>Purchase Requisition &amp; PO Issuance</b><br/>Role: <b>Responsible (R)</b>"]:::rNode
    s2p_006_goods_services_receipt__R["<b>Goods &amp; Services Receipt Verification</b><br/>Role: <b>Responsible (R)</b>"]:::rNode
  end

  subgraph Sub_role_relationship_manager ["<b>Commercial Relationship Manager</b>"]
    c2a_001_prospect_application_intake__R["<b>Prospect Application &amp; Entity Intake</b><br/>Role: <b>Responsible (R)</b>"]:::rNode
    l2s_001_loan_application_credit_packaging__R["<b>Loan Application &amp; Credit Packaging</b><br/>Role: <b>Responsible (R)</b>"]:::rNode
  end

  subgraph Sub_role_talent_acquisition_specialist ["<b>Talent Acquisition Specialist</b>"]
    h2r_002_candidate_screening_interview__R["<b>Candidate Screening &amp; Interview Execution</b><br/>Role: <b>Responsible (R)</b>"]:::rNode
    h2r_003_offer_letter_onboarding__R["<b>Offer Letter Generation &amp; Employee Onboarding</b><br/>Role: <b>Responsible (R)</b>"]:::rNode
  end

  subgraph Sub_role_treasury_operations_officer ["<b>Treasury &amp; Settlement Operations Officer</b>"]
    l2s_004_loan_booking_funding_disbursement__A["<b>Loan Booking &amp; Principal Funding Disbursement</b><br/>Role: <b>Accountable (A)</b>"]:::aNode
    c2a_005_account_provisioning_core_activation__A["<b>Core Account Provisioning &amp; Treasury Activation</b><br/>Role: <b>Accountable (A)</b>"]:::aNode
  end

  h2r_001_job_requisition_posting__R --> h2r_002_candidate_screening_interview__R
  h2r_002_candidate_screening_interview__R --> h2r_003_offer_letter_onboarding__R
  h2r_003_offer_letter_onboarding__R --> h2r_004_payroll_benefits_enrollment__R
  h2r_004_payroll_benefits_enrollment__R --> h2r_005_performance_compensation_review__R
  h2r_004_payroll_benefits_enrollment__R --> r2r_001_journal_entry_recording__R
  h2r_005_performance_compensation_review__R --> h2r_006_separation_offboarding_settlement__R
  h2r_006_separation_offboarding_settlement__R --> r2r_001_journal_entry_recording__R
  r2r_001_journal_entry_recording__R --> r2r_002_intercompany_reconciliation__R
  r2r_002_intercompany_reconciliation__R --> r2r_003_balance_sheet_substantiation__R
  r2r_003_balance_sheet_substantiation__R --> r2r_004_financial_close_consolidation__R
  r2r_004_financial_close_consolidation__R --> r2r_005_statutory_financial_reporting__R
  s2p_001_spend_analysis_need_id__R --> s2p_002_supplier_discovery_qualification__R
  s2p_002_supplier_discovery_qualification__R --> s2p_003_sourcing_rfx_auction__R
  s2p_003_sourcing_rfx_auction__R --> s2p_004_contracting_sla_negotiation__R
  s2p_004_contracting_sla_negotiation__R --> s2p_005_purchase_requisition_po__R
  s2p_004_contracting_sla_negotiation__R --> l2s_003_collateral_valuation_lien_perfection__R
  s2p_005_purchase_requisition_po__R --> s2p_006_goods_services_receipt__R
  s2p_006_goods_services_receipt__R --> s2p_007_invoice_verification_matching__R
  s2p_007_invoice_verification_matching__R --> s2p_008_payment_settlement_disbursement__R
  s2p_008_payment_settlement_disbursement__R --> r2r_001_journal_entry_recording__R
  c2a_001_prospect_application_intake__R --> c2a_002_kyc_cip_identity_verification__R
  c2a_002_kyc_cip_identity_verification__R --> c2a_003_aml_sanctions_pep_screening__R
  c2a_003_aml_sanctions_pep_screening__R --> c2a_004_enhanced_due_diligence_compliance__R
  c2a_004_enhanced_due_diligence_compliance__R --> c2a_005_account_provisioning_core_activation__R
  c2a_005_account_provisioning_core_activation__R --> l2s_001_loan_application_credit_packaging__R
  l2s_001_loan_application_credit_packaging__R --> l2s_002_credit_underwriting_risk_rating__R
  l2s_002_credit_underwriting_risk_rating__R --> l2s_003_collateral_valuation_lien_perfection__R
  l2s_003_collateral_valuation_lien_perfection__R --> l2s_004_loan_booking_funding_disbursement__R
  l2s_004_loan_booking_funding_disbursement__R --> l2s_005_repayment_servicing_covenant_monitoring__R
  l2s_005_repayment_servicing_covenant_monitoring__R --> l2s_006_delinquency_workout_ledger_settlement__R
  l2s_006_delinquency_workout_ledger_settlement__R --> r2r_001_journal_entry_recording__R
```

---

## 3. Enterprise IT Asset & Infrastructure Topology
```mermaid
flowchart TD
  %% Systems & Assets Styling
  classDef coreAsset fill:#14532d,stroke:#4ade80,stroke-width:2px,color:#f0fdf4,rx:8,ry:8;
  classDef subAsset fill:#064e3b,stroke:#2dd4bf,stroke-width:2px,color:#f0fdfa,rx:6,ry:6;
  classDef stepDep fill:#1e293b,stroke:#94a3b8,stroke-width:1px,color:#e2e8f0,rx:4,ry:4;

  subgraph Subgraph_EnterpriseSystems ["<b>Enterprise Core IT Systems & Assets</b>"]
    asset_erp_system["<b>Enterprise Core ERP (SAP S/4HANA)</b><br/><small>Type: it_application | SLA: 99.95% | Max TPS: 2500</small>"]:::coreAsset
    asset_hcm_platform["<b>Human Capital Management (HCM) Platform</b><br/><small>Type: it_application | SLA: 99.95% | Max TPS: 0</small>"]:::coreAsset
    asset_payroll_engine["<b>Enterprise Payroll &amp; Tax Engine</b><br/><small>Type: it_application | SLA: 99.99% | Max TPS: 0</small>"]:::coreAsset
    asset_aml_kyc_screening_engine["<b>AML/KYC Client Lifecycle &amp; Sanctions Screening Engine</b><br/><small>Type: it_application | SLA: 99.9% | Max TPS: 0</small>"]:::coreAsset
    asset_core_banking_platform["<b>Core Banking &amp; Subledger Platform</b><br/><small>Type: it_application | SLA: 99.9% | Max TPS: 0</small>"]:::coreAsset
    asset_loan_origination_system["<b>Commercial Loan Origination &amp; Risk Rating System (LOS)</b><br/><small>Type: it_application | SLA: 99.9% | Max TPS: 0</small>"]:::coreAsset
    asset_crm_system["<b>Enterprise Cloud CRM &amp; CPQ Platform (Salesforce)</b><br/><small>Type: it_application | SLA: 99.9% | Max TPS: 1200</small>"]:::subAsset
    asset_erp_system ==>|integrates with| asset_crm_system
    asset_eprocurement_portal["<b>Cloud e-Procurement &amp; Supplier Network Portal</b><br/><small>Type: it_application | SLA: 99.9% | Max TPS: 800</small>"]:::subAsset
    asset_erp_system ==>|integrates with| asset_eprocurement_portal
    asset_financial_consolidation_system["<b>Enterprise Financial Consolidation &amp; Reporting System (SAP Group Reporting / OneStream)</b><br/><small>Type: it_application | SLA: 99.9% | Max TPS: 500</small>"]:::subAsset
    asset_erp_system ==>|integrates with| asset_financial_consolidation_system
    asset_payment_gateway["<b>Corporate Banking Payment Gateway &amp; ISO 20022 Router</b><br/><small>Type: api_gateway | SLA: 99.99% | Max TPS: 1500</small>"]:::subAsset
    asset_erp_system ==>|integrates with| asset_payment_gateway
  end

  subgraph Subgraph_ProcessBindings ["<b>Value Chain Process Workloads</b>"]
    proc_c2a_001_prospect_application_intake_asset_crm_system["Prospect Application &amp; Entity Intake"]:::stepDep
    proc_c2a_001_prospect_application_intake_asset_crm_system -. runs on .-> asset_crm_system
    proc_l2s_001_loan_application_credit_packaging_asset_crm_system["Loan Application &amp; Credit Packaging"]:::stepDep
    proc_l2s_001_loan_application_credit_packaging_asset_crm_system -. runs on .-> asset_crm_system
    proc_s2p_001_spend_analysis_need_id_asset_eprocurement_portal["Spend Analysis &amp; Need Identification"]:::stepDep
    proc_s2p_001_spend_analysis_need_id_asset_eprocurement_portal -. runs on .-> asset_eprocurement_portal
    proc_s2p_002_supplier_discovery_qualification_asset_eprocurement_portal["Supplier Discovery &amp; Qualification"]:::stepDep
    proc_s2p_002_supplier_discovery_qualification_asset_eprocurement_portal -. runs on .-> asset_eprocurement_portal
    proc_s2p_003_sourcing_rfx_auction_asset_eprocurement_portal["Strategic Sourcing &amp; RFx Execution"]:::stepDep
    proc_s2p_003_sourcing_rfx_auction_asset_eprocurement_portal -. runs on .-> asset_eprocurement_portal
    proc_s2p_004_contracting_sla_negotiation_asset_eprocurement_portal["Contracting &amp; SLA Negotiation"]:::stepDep
    proc_s2p_004_contracting_sla_negotiation_asset_eprocurement_portal -. runs on .-> asset_eprocurement_portal
    proc_s2p_005_purchase_requisition_po_asset_eprocurement_portal["Purchase Requisition &amp; PO Issuance"]:::stepDep
    proc_s2p_005_purchase_requisition_po_asset_eprocurement_portal -. runs on .-> asset_eprocurement_portal
    proc_s2p_007_invoice_verification_matching_asset_eprocurement_portal["Invoice 3-Way Matching &amp; Exception Handling"]:::stepDep
    proc_s2p_007_invoice_verification_matching_asset_eprocurement_portal -. runs on .-> asset_eprocurement_portal
    proc_r2r_001_journal_entry_recording_asset_erp_system["General Ledger Journal Recording &amp; Subledger Ingestion"]:::stepDep
    proc_r2r_001_journal_entry_recording_asset_erp_system -. runs on .-> asset_erp_system
    proc_r2r_002_intercompany_reconciliation_asset_erp_system["Intercompany Transaction Matching &amp; Elimination"]:::stepDep
    proc_r2r_002_intercompany_reconciliation_asset_erp_system -. runs on .-> asset_erp_system
    proc_r2r_003_balance_sheet_substantiation_asset_erp_system["Balance Sheet Account Substantiation &amp; Reconciliation"]:::stepDep
    proc_r2r_003_balance_sheet_substantiation_asset_erp_system -. runs on .-> asset_erp_system
    proc_r2r_004_financial_close_consolidation_asset_erp_system["Financial Close Orchestration &amp; Group Consolidation"]:::stepDep
    proc_r2r_004_financial_close_consolidation_asset_erp_system -. runs on .-> asset_erp_system
    proc_s2p_001_spend_analysis_need_id_asset_erp_system["Spend Analysis &amp; Need Identification"]:::stepDep
    proc_s2p_001_spend_analysis_need_id_asset_erp_system -. runs on .-> asset_erp_system
    proc_s2p_004_contracting_sla_negotiation_asset_erp_system["Contracting &amp; SLA Negotiation"]:::stepDep
    proc_s2p_004_contracting_sla_negotiation_asset_erp_system -. runs on .-> asset_erp_system
    proc_s2p_005_purchase_requisition_po_asset_erp_system["Purchase Requisition &amp; PO Issuance"]:::stepDep
    proc_s2p_005_purchase_requisition_po_asset_erp_system -. runs on .-> asset_erp_system
    proc_s2p_006_goods_services_receipt_asset_erp_system["Goods &amp; Services Receipt Verification"]:::stepDep
    proc_s2p_006_goods_services_receipt_asset_erp_system -. runs on .-> asset_erp_system
    proc_s2p_007_invoice_verification_matching_asset_erp_system["Invoice 3-Way Matching &amp; Exception Handling"]:::stepDep
    proc_s2p_007_invoice_verification_matching_asset_erp_system -. runs on .-> asset_erp_system
    proc_s2p_008_payment_settlement_disbursement_asset_erp_system["Payment Settlement &amp; Disbursement"]:::stepDep
    proc_s2p_008_payment_settlement_disbursement_asset_erp_system -. runs on .-> asset_erp_system
    proc_l2s_006_delinquency_workout_ledger_settlement_asset_erp_system["Delinquency Workout &amp; Subledger Reconciliation"]:::stepDep
    proc_l2s_006_delinquency_workout_ledger_settlement_asset_erp_system -. runs on .-> asset_erp_system
    proc_r2r_002_intercompany_reconciliation_asset_financial_consolidation_system["Intercompany Transaction Matching &amp; Elimination"]:::stepDep
    proc_r2r_002_intercompany_reconciliation_asset_financial_consolidation_system -. runs on .-> asset_financial_consolidation_system
    proc_r2r_003_balance_sheet_substantiation_asset_financial_consolidation_system["Balance Sheet Account Substantiation &amp; Reconciliation"]:::stepDep
    proc_r2r_003_balance_sheet_substantiation_asset_financial_consolidation_system -. runs on .-> asset_financial_consolidation_system
    proc_r2r_004_financial_close_consolidation_asset_financial_consolidation_system["Financial Close Orchestration &amp; Group Consolidation"]:::stepDep
    proc_r2r_004_financial_close_consolidation_asset_financial_consolidation_system -. runs on .-> asset_financial_consolidation_system
    proc_r2r_005_statutory_financial_reporting_asset_financial_consolidation_system["Statutory, Tax &amp; Management Financial Reporting"]:::stepDep
    proc_r2r_005_statutory_financial_reporting_asset_financial_consolidation_system -. runs on .-> asset_financial_consolidation_system
    proc_h2r_001_job_requisition_posting_asset_hcm_platform["Job Requisition Definition &amp; Posting"]:::stepDep
    proc_h2r_001_job_requisition_posting_asset_hcm_platform -. runs on .-> asset_hcm_platform
    proc_h2r_002_candidate_screening_interview_asset_hcm_platform["Candidate Screening &amp; Interview Execution"]:::stepDep
    proc_h2r_002_candidate_screening_interview_asset_hcm_platform -. runs on .-> asset_hcm_platform
    proc_h2r_003_offer_letter_onboarding_asset_hcm_platform["Offer Letter Generation &amp; Employee Onboarding"]:::stepDep
    proc_h2r_003_offer_letter_onboarding_asset_hcm_platform -. runs on .-> asset_hcm_platform
    proc_h2r_004_payroll_benefits_enrollment_asset_hcm_platform["Payroll &amp; Benefits Enrollment Processing"]:::stepDep
    proc_h2r_004_payroll_benefits_enrollment_asset_hcm_platform -. runs on .-> asset_hcm_platform
    proc_h2r_005_performance_compensation_review_asset_hcm_platform["Performance &amp; Compensation Review"]:::stepDep
    proc_h2r_005_performance_compensation_review_asset_hcm_platform -. runs on .-> asset_hcm_platform
    proc_h2r_006_separation_offboarding_settlement_asset_hcm_platform["Separation, Offboarding &amp; Final Settlement"]:::stepDep
    proc_h2r_006_separation_offboarding_settlement_asset_hcm_platform -. runs on .-> asset_hcm_platform
    proc_s2p_008_payment_settlement_disbursement_asset_payment_gateway["Payment Settlement &amp; Disbursement"]:::stepDep
    proc_s2p_008_payment_settlement_disbursement_asset_payment_gateway -. runs on .-> asset_payment_gateway
    proc_c2a_005_account_provisioning_core_activation_asset_payment_gateway["Core Account Provisioning &amp; Treasury Activation"]:::stepDep
    proc_c2a_005_account_provisioning_core_activation_asset_payment_gateway -. runs on .-> asset_payment_gateway
    proc_l2s_004_loan_booking_funding_disbursement_asset_payment_gateway["Loan Booking &amp; Principal Funding Disbursement"]:::stepDep
    proc_l2s_004_loan_booking_funding_disbursement_asset_payment_gateway -. runs on .-> asset_payment_gateway
    proc_h2r_004_payroll_benefits_enrollment_asset_payroll_engine["Payroll &amp; Benefits Enrollment Processing"]:::stepDep
    proc_h2r_004_payroll_benefits_enrollment_asset_payroll_engine -. runs on .-> asset_payroll_engine
    proc_h2r_006_separation_offboarding_settlement_asset_payroll_engine["Separation, Offboarding &amp; Final Settlement"]:::stepDep
    proc_h2r_006_separation_offboarding_settlement_asset_payroll_engine -. runs on .-> asset_payroll_engine
    proc_c2a_001_prospect_application_intake_asset_aml_kyc_screening_engine["Prospect Application &amp; Entity Intake"]:::stepDep
    proc_c2a_001_prospect_application_intake_asset_aml_kyc_screening_engine -. runs on .-> asset_aml_kyc_screening_engine
    proc_c2a_002_kyc_cip_identity_verification_asset_aml_kyc_screening_engine["KYC/CIP Identity &amp; UBO Verification"]:::stepDep
    proc_c2a_002_kyc_cip_identity_verification_asset_aml_kyc_screening_engine -. runs on .-> asset_aml_kyc_screening_engine
    proc_c2a_003_aml_sanctions_pep_screening_asset_aml_kyc_screening_engine["AML Sanctions, PEP &amp; Adverse Media Screening"]:::stepDep
    proc_c2a_003_aml_sanctions_pep_screening_asset_aml_kyc_screening_engine -. runs on .-> asset_aml_kyc_screening_engine
    proc_c2a_004_enhanced_due_diligence_compliance_asset_aml_kyc_screening_engine["Enhanced Due Diligence (EDD) &amp; BSA Approval"]:::stepDep
    proc_c2a_004_enhanced_due_diligence_compliance_asset_aml_kyc_screening_engine -. runs on .-> asset_aml_kyc_screening_engine
    proc_c2a_005_account_provisioning_core_activation_asset_core_banking_platform["Core Account Provisioning &amp; Treasury Activation"]:::stepDep
    proc_c2a_005_account_provisioning_core_activation_asset_core_banking_platform -. runs on .-> asset_core_banking_platform
    proc_l2s_004_loan_booking_funding_disbursement_asset_core_banking_platform["Loan Booking &amp; Principal Funding Disbursement"]:::stepDep
    proc_l2s_004_loan_booking_funding_disbursement_asset_core_banking_platform -. runs on .-> asset_core_banking_platform
    proc_l2s_005_repayment_servicing_covenant_monitoring_asset_core_banking_platform["Repayment Servicing &amp; Covenant Monitoring"]:::stepDep
    proc_l2s_005_repayment_servicing_covenant_monitoring_asset_core_banking_platform -. runs on .-> asset_core_banking_platform
    proc_l2s_006_delinquency_workout_ledger_settlement_asset_core_banking_platform["Delinquency Workout &amp; Subledger Reconciliation"]:::stepDep
    proc_l2s_006_delinquency_workout_ledger_settlement_asset_core_banking_platform -. runs on .-> asset_core_banking_platform
    proc_l2s_001_loan_application_credit_packaging_asset_loan_origination_system["Loan Application &amp; Credit Packaging"]:::stepDep
    proc_l2s_001_loan_application_credit_packaging_asset_loan_origination_system -. runs on .-> asset_loan_origination_system
    proc_l2s_002_credit_underwriting_risk_rating_asset_loan_origination_system["Credit Underwriting &amp; PD/LGD Risk Rating"]:::stepDep
    proc_l2s_002_credit_underwriting_risk_rating_asset_loan_origination_system -. runs on .-> asset_loan_origination_system
    proc_l2s_003_collateral_valuation_lien_perfection_asset_loan_origination_system["Collateral Valuation &amp; Lien Perfection"]:::stepDep
    proc_l2s_003_collateral_valuation_lien_perfection_asset_loan_origination_system -. runs on .-> asset_loan_origination_system
    proc_l2s_005_repayment_servicing_covenant_monitoring_asset_loan_origination_system["Repayment Servicing &amp; Covenant Monitoring"]:::stepDep
    proc_l2s_005_repayment_servicing_covenant_monitoring_asset_loan_origination_system -. runs on .-> asset_loan_origination_system
  end

```

---

## 4. RACI Governance & Operational Execution Grid
# Enterprise RACI Governance Matrix [ALL]

> **RACI Legend**: **R** = Responsible (Executes) | **A** = Accountable (Approves) | **C** = Consulted (Inputs) | **I** = Informed (Notified)

## 1. Value Chain Process RACI Grid

| Step ID | Process Step Name | Accounts Payable Clerk | Billing & Accounts Receivable Specialist | BSA / AML Chief Compliance Officer | Category Manager | Chief Credit Officer (CCO) | Compensation Analyst | Financial Consolidation Specialist | Credit & Risk Manager | Commercial Credit Underwriter | Enterprise Customer | Finance Controller | General Ledger Accountant | Hiring Manager | HR Business Partner | Internal Auditor | KYC & AML Compliance Analyst | Loan Closing & Servicing Specialist | Payroll Specialist | Procurement Specialist | Commercial Relationship Manager | Sales Operations Specialist | Supplier / Vendor | Talent Acquisition Specialist | Treasury & Settlement Operations Officer |
| :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `c2a_001_prospect_application_intake` | **Prospect Application & Entity Intake** | - | - | **A** | - | - | - | - | - | - | C | - | - | - | - | - | I | - | - | - | **R** | - | - | - | - |
| `c2a_002_kyc_cip_identity_verification` | **KYC/CIP Identity & UBO Verification** | - | - | **A** | - | - | - | - | - | - | C | - | - | - | - | - | **R** | - | - | - | C | - | - | - | I |
| `c2a_003_aml_sanctions_pep_screening` | **AML Sanctions, PEP & Adverse Media Screening** | - | - | **A** | - | - | - | - | - | - | - | - | - | - | - | C | **R** | - | - | - | I | - | - | - | - |
| `c2a_004_enhanced_due_diligence_compliance` | **Enhanced Due Diligence (EDD) & BSA Approval** | - | - | **A** | - | - | - | - | - | - | - | - | - | - | - | I | **R** | - | - | - | C | - | - | - | - |
| `c2a_005_account_provisioning_core_activation` | **Core Account Provisioning & Treasury Activation** | - | - | - | - | - | - | - | - | - | I | - | - | - | - | - | C | **R** | - | - | I | - | - | - | **A** |
| `h2r_001_job_requisition_posting` | **Job Requisition Definition & Posting** | - | - | - | - | - | C | - | - | - | - | - | - | **R**, **A** | C | - | - | - | - | - | - | - | - | I | - |
| `h2r_002_candidate_screening_interview` | **Candidate Screening & Interview Execution** | - | - | - | - | - | - | - | - | - | - | - | - | **A** | C | - | - | - | - | - | - | - | - | **R** | - |
| `h2r_003_offer_letter_onboarding` | **Offer Letter Generation & Employee Onboarding** | - | - | - | - | - | C | - | - | - | - | - | - | **A** | - | - | - | - | I | - | - | - | - | **R** | - |
| `h2r_004_payroll_benefits_enrollment` | **Payroll & Benefits Enrollment Processing** | - | - | - | - | - | - | - | - | - | - | I | - | - | C | - | - | - | **R**, **A** | - | - | - | - | - | - |
| `h2r_005_performance_compensation_review` | **Performance & Compensation Review** | - | - | - | - | - | C | - | - | - | - | - | - | **R**, **A** | C | - | - | - | I | - | - | - | - | - | - |
| `h2r_006_separation_offboarding_settlement` | **Separation, Offboarding & Final Settlement** | - | - | - | - | - | - | - | - | - | - | - | - | C | **R**, **A** | - | - | - | I | - | - | - | - | - | - |
| `l2s_001_loan_application_credit_packaging` | **Loan Application & Credit Packaging** | - | - | - | - | I | - | - | - | **A** | C | - | - | - | - | - | - | - | - | - | **R** | - | - | - | - |
| `l2s_002_credit_underwriting_risk_rating` | **Credit Underwriting & PD/LGD Risk Rating** | - | - | - | - | **A** | - | - | C | **R** | I | - | - | - | - | - | - | - | - | - | C | - | - | - | - |
| `l2s_003_collateral_valuation_lien_perfection` | **Collateral Valuation & Lien Perfection** | - | - | - | - | **A** | - | - | - | C | C | - | - | - | - | - | - | **R** | - | - | - | - | - | - | I |
| `l2s_004_loan_booking_funding_disbursement` | **Loan Booking & Principal Funding Disbursement** | - | - | - | - | - | - | - | - | C | I | - | - | - | - | - | - | **R** | - | - | I | - | - | - | **A** |
| `l2s_005_repayment_servicing_covenant_monitoring` | **Repayment Servicing & Covenant Monitoring** | - | - | - | - | **A** | - | - | - | **R** | I | I | - | - | - | - | - | **R** | - | - | C | - | - | - | - |
| `l2s_006_delinquency_workout_ledger_settlement` | **Delinquency Workout & Subledger Reconciliation** | - | - | - | - | C | - | - | - | - | - | **A** | I | - | - | I | - | **R** | - | - | - | - | - | - | C |
| `r2r_001_journal_entry_recording` | **General Ledger Journal Recording & Subledger Ingestion** | C | C | - | - | - | - | - | - | - | - | **A** | **R** | - | - | I | - | - | - | - | - | - | - | - | - |
| `r2r_002_intercompany_reconciliation` | **Intercompany Transaction Matching & Elimination** | - | - | - | - | - | - | **R** | - | - | - | **A** | C | - | - | I | - | - | - | - | - | - | - | - | - |
| `r2r_003_balance_sheet_substantiation` | **Balance Sheet Account Substantiation & Reconciliation** | - | - | - | - | - | - | C | - | - | - | **A** | **R** | - | - | I | - | - | - | - | - | - | - | - | - |
| `r2r_004_financial_close_consolidation` | **Financial Close Orchestration & Group Consolidation** | - | - | - | - | - | - | **R** | - | - | - | **A** | C | - | - | I | - | - | - | - | - | - | - | - | - |
| `r2r_005_statutory_financial_reporting` | **Statutory, Tax & Management Financial Reporting** | - | - | - | - | - | - | **R** | - | - | - | **A** | I | - | - | C | - | - | - | - | - | - | - | - | - |
| `s2p_001_spend_analysis_need_id` | **Spend Analysis & Need Identification** | - | - | - | **A** | - | - | - | - | - | - | C | - | - | - | - | - | - | - | **R** | - | - | I | - | - |
| `s2p_002_supplier_discovery_qualification` | **Supplier Discovery & Qualification** | - | - | - | **A** | - | - | - | - | - | - | C | - | - | - | - | - | - | - | **R** | - | - | I | - | - |
| `s2p_003_sourcing_rfx_auction` | **Strategic Sourcing & RFx Execution** | - | - | - | **A** | - | - | - | - | - | - | C | - | - | - | - | - | - | - | **R** | - | - | I | - | - |
| `s2p_004_contracting_sla_negotiation` | **Contracting & SLA Negotiation** | - | - | - | **R**, **A** | - | - | - | - | - | - | C | - | - | - | - | - | - | - | - | - | - | I | - | - |
| `s2p_005_purchase_requisition_po` | **Purchase Requisition & PO Issuance** | - | - | - | **A** | - | - | - | - | - | - | C | - | - | - | - | - | - | - | **R** | - | - | I | - | - |
| `s2p_006_goods_services_receipt` | **Goods & Services Receipt Verification** | C | - | - | **A** | - | - | - | - | - | - | - | - | - | - | - | - | - | - | **R** | - | - | I | - | - |
| `s2p_007_invoice_verification_matching` | **Invoice 3-Way Matching & Exception Handling** | **R** | - | - | - | - | - | - | - | - | - | **A** | - | - | - | - | - | - | - | C | - | - | I | - | - |
| `s2p_008_payment_settlement_disbursement` | **Payment Settlement & Disbursement** | **R** | - | - | C | - | - | - | - | - | - | **A** | - | - | - | - | - | - | - | - | - | - | I | - | - |

---

## 2. Role Workload & Touchpoint Distribution

| Enterprise Role | Responsible (R) | Accountable (A) | Consulted (C) | Informed (I) | Total Touchpoints | Operational Load |
| :--- | :---: | :---: | :---: | :---: | :---: | :--- |
| **Accounts Payable Clerk** (`role_accounts_payable_clerk`) | 2 | 0 | 2 | 0 | **4** | 🟡 Moderate |
| **Billing & Accounts Receivable Specialist** (`role_billing_specialist`) | 0 | 0 | 1 | 0 | **1** | 🟢 Low |
| **BSA / AML Chief Compliance Officer** (`role_bsa_compliance_officer`) | 0 | 4 | 0 | 0 | **4** | 🟡 Moderate |
| **Category Manager** (`role_category_manager`) | 1 | 6 | 1 | 0 | **8** | 🔴 High (Key Dependency) |
| **Chief Credit Officer (CCO)** (`role_chief_credit_officer`) | 0 | 3 | 1 | 1 | **5** | 🟡 Moderate |
| **Compensation Analyst** (`role_compensation_analyst`) | 0 | 0 | 3 | 0 | **3** | 🟢 Low |
| **Financial Consolidation Specialist** (`role_consolidation_specialist`) | 3 | 0 | 1 | 0 | **4** | 🔴 High (Key Dependency) |
| **Credit & Risk Manager** (`role_credit_manager`) | 0 | 0 | 1 | 0 | **1** | 🟢 Low |
| **Commercial Credit Underwriter** (`role_credit_underwriter`) | 2 | 1 | 2 | 0 | **5** | 🟡 Moderate |
| **Enterprise Customer** (`role_customer`) | 0 | 0 | 4 | 4 | **8** | 🔴 High (Key Dependency) |
| **Finance Controller** (`role_finance_controller`) | 0 | 8 | 5 | 2 | **15** | 🔴 High (Key Dependency) |
| **General Ledger Accountant** (`role_general_ledger_accountant`) | 2 | 0 | 2 | 2 | **6** | 🔴 High (Key Dependency) |
| **Hiring Manager** (`role_hiring_manager`) | 2 | 4 | 1 | 0 | **7** | 🔴 High (Key Dependency) |
| **HR Business Partner** (`role_hr_business_partner`) | 1 | 1 | 4 | 0 | **6** | 🔴 High (Key Dependency) |
| **Internal Auditor** (`role_internal_auditor`) | 0 | 0 | 2 | 6 | **8** | 🔴 High (Key Dependency) |
| **KYC & AML Compliance Analyst** (`role_kyc_aml_analyst`) | 3 | 0 | 1 | 1 | **5** | 🔴 High (Key Dependency) |
| **Loan Closing & Servicing Specialist** (`role_loan_servicing_specialist`) | 5 | 0 | 0 | 0 | **5** | 🔴 High (Key Dependency) |
| **Payroll Specialist** (`role_payroll_specialist`) | 1 | 1 | 0 | 3 | **5** | 🟡 Moderate |
| **Procurement Specialist** (`role_procurement_specialist`) | 5 | 0 | 1 | 0 | **6** | 🔴 High (Key Dependency) |
| **Commercial Relationship Manager** (`role_relationship_manager`) | 2 | 0 | 4 | 3 | **9** | 🔴 High (Key Dependency) |
| **Sales Operations Specialist** (`role_sales_ops_specialist`) | 0 | 0 | 0 | 0 | **0** | 🟢 Low |
| **Supplier / Vendor** (`role_supplier`) | 0 | 0 | 0 | 8 | **8** | 🔴 High (Key Dependency) |
| **Talent Acquisition Specialist** (`role_talent_acquisition_specialist`) | 2 | 0 | 0 | 1 | **3** | 🟡 Moderate |
| **Treasury & Settlement Operations Officer** (`role_treasury_operations_officer`) | 0 | 2 | 1 | 2 | **5** | 🟡 Moderate |

---

## 3. Segregation of Duties (SoD) & Conflict Analysis

⚠️ **Potential Segregation of Duties (SoD) Overlaps Detected:**

- **Step `h2r_001_job_requisition_posting` (Job Requisition Definition & Posting)**: Role `role_hiring_manager` is listed as both Responsible and Accountable.
- **Step `h2r_004_payroll_benefits_enrollment` (Payroll & Benefits Enrollment Processing)**: Role `role_payroll_specialist` is listed as both Responsible and Accountable.
- **Step `h2r_005_performance_compensation_review` (Performance & Compensation Review)**: Role `role_hiring_manager` is listed as both Responsible and Accountable.
- **Step `h2r_006_separation_offboarding_settlement` (Separation, Offboarding & Final Settlement)**: Role `role_hr_business_partner` is listed as both Responsible and Accountable.
- **Step `s2p_004_contracting_sla_negotiation` (Contracting & SLA Negotiation)**: Role `role_category_manager` is listed as both Responsible and Accountable.

---

## 5. DACI Decision Authority Grid
# Enterprise DACI Decision Governance Matrix [ALL]

> **DACI Legend**: **D** = Driver (Orchestrates/Leads) | **A** = Approver (Sole Sign-off/Veto) | **C** = Contributor (Advises/Consulted) | **I** = Informed (Notified)

## 1. Value Chain Process DACI Grid

| Step ID | Process Step Name | Accounts Payable Clerk | Billing & Accounts Receivable Specialist | BSA / AML Chief Compliance Officer | Category Manager | Chief Credit Officer (CCO) | Compensation Analyst | Financial Consolidation Specialist | Credit & Risk Manager | Commercial Credit Underwriter | Enterprise Customer | Finance Controller | General Ledger Accountant | Hiring Manager | HR Business Partner | Internal Auditor | KYC & AML Compliance Analyst | Loan Closing & Servicing Specialist | Payroll Specialist | Procurement Specialist | Commercial Relationship Manager | Sales Operations Specialist | Supplier / Vendor | Talent Acquisition Specialist | Treasury & Settlement Operations Officer |
| :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `c2a_001_prospect_application_intake` | **Prospect Application & Entity Intake** | - | - | **A** | - | - | - | - | - | - | C | - | - | - | - | - | I | - | - | - | **D** | - | - | - | - |
| `c2a_002_kyc_cip_identity_verification` | **KYC/CIP Identity & UBO Verification** | - | - | **A** | - | - | - | - | - | - | C | - | - | - | - | - | **D** | - | - | - | C | - | - | - | I |
| `c2a_003_aml_sanctions_pep_screening` | **AML Sanctions, PEP & Adverse Media Screening** | - | - | **A** | - | - | - | - | - | - | - | - | - | - | - | C | **D** | - | - | - | I | - | - | - | - |
| `c2a_004_enhanced_due_diligence_compliance` | **Enhanced Due Diligence (EDD) & BSA Approval** | - | - | **A** | - | - | - | - | - | - | - | - | - | - | - | I | **D** | - | - | - | C | - | - | - | - |
| `c2a_005_account_provisioning_core_activation` | **Core Account Provisioning & Treasury Activation** | - | - | - | - | - | - | - | - | - | I | - | - | - | - | - | C | **D** | - | - | I | - | - | - | **A** |
| `h2r_001_job_requisition_posting` | **Job Requisition Definition & Posting** | - | - | - | - | - | C | - | - | - | - | - | - | **D**, **A** | C | - | - | - | - | - | - | - | - | I | - |
| `h2r_002_candidate_screening_interview` | **Candidate Screening & Interview Execution** | - | - | - | - | - | - | - | - | - | - | - | - | **A** | C | - | - | - | - | - | - | - | - | **D** | - |
| `h2r_003_offer_letter_onboarding` | **Offer Letter Generation & Employee Onboarding** | - | - | - | - | - | C | - | - | - | - | - | - | **A** | - | - | - | - | I | - | - | - | - | **D** | - |
| `h2r_004_payroll_benefits_enrollment` | **Payroll & Benefits Enrollment Processing** | - | - | - | - | - | - | - | - | - | - | I | - | - | C | - | - | - | **D**, **A** | - | - | - | - | - | - |
| `h2r_005_performance_compensation_review` | **Performance & Compensation Review** | - | - | - | - | - | C | - | - | - | - | - | - | **D**, **A** | C | - | - | - | I | - | - | - | - | - | - |
| `h2r_006_separation_offboarding_settlement` | **Separation, Offboarding & Final Settlement** | - | - | - | - | - | - | - | - | - | - | - | - | C | **D**, **A** | - | - | - | I | - | - | - | - | - | - |
| `l2s_001_loan_application_credit_packaging` | **Loan Application & Credit Packaging** | - | - | - | - | I | - | - | - | **A** | C | - | - | - | - | - | - | - | - | - | **D** | - | - | - | - |
| `l2s_002_credit_underwriting_risk_rating` | **Credit Underwriting & PD/LGD Risk Rating** | - | - | - | - | **A** | - | - | C | **D** | I | - | - | - | - | - | - | - | - | - | C | - | - | - | - |
| `l2s_003_collateral_valuation_lien_perfection` | **Collateral Valuation & Lien Perfection** | - | - | - | - | **A** | - | - | - | C | C | - | - | - | - | - | - | **D** | - | - | - | - | - | - | I |
| `l2s_004_loan_booking_funding_disbursement` | **Loan Booking & Principal Funding Disbursement** | - | - | - | - | - | - | - | - | C | I | - | - | - | - | - | - | **D** | - | - | I | - | - | - | **A** |
| `l2s_005_repayment_servicing_covenant_monitoring` | **Repayment Servicing & Covenant Monitoring** | - | - | - | - | **A** | - | - | - | C | I | I | - | - | - | - | - | **D** | - | - | C | - | - | - | - |
| `l2s_006_delinquency_workout_ledger_settlement` | **Delinquency Workout & Subledger Reconciliation** | - | - | - | - | C | - | - | - | - | - | **A** | I | - | - | I | - | **D** | - | - | - | - | - | - | C |
| `r2r_001_journal_entry_recording` | **General Ledger Journal Recording & Subledger Ingestion** | C | C | - | - | - | - | - | - | - | - | **A** | **D** | - | - | I | - | - | - | - | - | - | - | - | - |
| `r2r_002_intercompany_reconciliation` | **Intercompany Transaction Matching & Elimination** | - | - | - | - | - | - | **D** | - | - | - | **A** | C | - | - | I | - | - | - | - | - | - | - | - | - |
| `r2r_003_balance_sheet_substantiation` | **Balance Sheet Account Substantiation & Reconciliation** | - | - | - | - | - | - | C | - | - | - | **A** | **D** | - | - | I | - | - | - | - | - | - | - | - | - |
| `r2r_004_financial_close_consolidation` | **Financial Close Orchestration & Group Consolidation** | - | - | - | - | - | - | **D** | - | - | - | **A** | C | - | - | I | - | - | - | - | - | - | - | - | - |
| `r2r_005_statutory_financial_reporting` | **Statutory, Tax & Management Financial Reporting** | - | - | - | - | - | - | **D** | - | - | - | **A** | I | - | - | C | - | - | - | - | - | - | - | - | - |
| `s2p_001_spend_analysis_need_id` | **Spend Analysis & Need Identification** | - | - | - | **A** | - | - | - | - | - | - | C | - | - | - | - | - | - | - | **D** | - | - | I | - | - |
| `s2p_002_supplier_discovery_qualification` | **Supplier Discovery & Qualification** | - | - | - | **A** | - | - | - | - | - | - | C | - | - | - | - | - | - | - | **D** | - | - | I | - | - |
| `s2p_003_sourcing_rfx_auction` | **Strategic Sourcing & RFx Execution** | - | - | - | **A** | - | - | - | - | - | - | C | - | - | - | - | - | - | - | **D** | - | - | I | - | - |
| `s2p_004_contracting_sla_negotiation` | **Contracting & SLA Negotiation** | - | - | - | **D**, **A** | - | - | - | - | - | - | C | - | - | - | - | - | - | - | - | - | - | I | - | - |
| `s2p_005_purchase_requisition_po` | **Purchase Requisition & PO Issuance** | - | - | - | **A** | - | - | - | - | - | - | C | - | - | - | - | - | - | - | **D** | - | - | I | - | - |
| `s2p_006_goods_services_receipt` | **Goods & Services Receipt Verification** | C | - | - | **A** | - | - | - | - | - | - | - | - | - | - | - | - | - | - | **D** | - | - | I | - | - |
| `s2p_007_invoice_verification_matching` | **Invoice 3-Way Matching & Exception Handling** | **D** | - | - | - | - | - | - | - | - | - | **A** | - | - | - | - | - | - | - | C | - | - | I | - | - |
| `s2p_008_payment_settlement_disbursement` | **Payment Settlement & Disbursement** | **D** | - | - | C | - | - | - | - | - | - | **A** | - | - | - | - | - | - | - | - | - | - | I | - | - |

---

## 2. Decision Authority & Driver Distribution

| Enterprise Role | Driver (D) | Approver (A) | Contributor (C) | Informed (I) | Total Decision Touchpoints | Governance Weight |
| :--- | :---: | :---: | :---: | :---: | :---: | :--- |
| **Accounts Payable Clerk** (`role_accounts_payable_clerk`) | 2 | 0 | 2 | 0 | **4** | 🟡 Operational Authority |
| **Billing & Accounts Receivable Specialist** (`role_billing_specialist`) | 0 | 0 | 1 | 0 | **1** | 🟢 Advisory |
| **BSA / AML Chief Compliance Officer** (`role_bsa_compliance_officer`) | 0 | 4 | 0 | 0 | **4** | 🔴 Strategic Approver |
| **Category Manager** (`role_category_manager`) | 1 | 6 | 1 | 0 | **8** | 🚨 Key-Person Risk (Concentrated Approver) |
| **Chief Credit Officer (CCO)** (`role_chief_credit_officer`) | 0 | 3 | 1 | 1 | **5** | 🔴 Strategic Approver |
| **Compensation Analyst** (`role_compensation_analyst`) | 0 | 0 | 3 | 0 | **3** | 🟢 Advisory |
| **Financial Consolidation Specialist** (`role_consolidation_specialist`) | 3 | 0 | 1 | 0 | **4** | 🔵 Primary Driver |
| **Credit & Risk Manager** (`role_credit_manager`) | 0 | 0 | 1 | 0 | **1** | 🟢 Advisory |
| **Commercial Credit Underwriter** (`role_credit_underwriter`) | 1 | 1 | 3 | 0 | **5** | 🟡 Operational Authority |
| **Enterprise Customer** (`role_customer`) | 0 | 0 | 4 | 4 | **8** | 🟢 Advisory |
| **Finance Controller** (`role_finance_controller`) | 0 | 8 | 5 | 2 | **15** | 🚨 Key-Person Risk (Concentrated Approver) |
| **General Ledger Accountant** (`role_general_ledger_accountant`) | 2 | 0 | 2 | 2 | **6** | 🟡 Operational Authority |
| **Hiring Manager** (`role_hiring_manager`) | 2 | 4 | 1 | 0 | **7** | 🔴 Strategic Approver |
| **HR Business Partner** (`role_hr_business_partner`) | 1 | 1 | 4 | 0 | **6** | 🟡 Operational Authority |
| **Internal Auditor** (`role_internal_auditor`) | 0 | 0 | 2 | 6 | **8** | 🟢 Advisory |
| **KYC & AML Compliance Analyst** (`role_kyc_aml_analyst`) | 3 | 0 | 1 | 1 | **5** | 🔵 Primary Driver |
| **Loan Closing & Servicing Specialist** (`role_loan_servicing_specialist`) | 5 | 0 | 0 | 0 | **5** | 🔵 Primary Driver |
| **Payroll Specialist** (`role_payroll_specialist`) | 1 | 1 | 0 | 3 | **5** | 🟡 Operational Authority |
| **Procurement Specialist** (`role_procurement_specialist`) | 5 | 0 | 1 | 0 | **6** | 🔵 Primary Driver |
| **Commercial Relationship Manager** (`role_relationship_manager`) | 2 | 0 | 4 | 3 | **9** | 🟡 Operational Authority |
| **Sales Operations Specialist** (`role_sales_ops_specialist`) | 0 | 0 | 0 | 0 | **0** | 🟢 Advisory |
| **Supplier / Vendor** (`role_supplier`) | 0 | 0 | 0 | 8 | **8** | 🟢 Advisory |
| **Talent Acquisition Specialist** (`role_talent_acquisition_specialist`) | 2 | 0 | 0 | 1 | **3** | 🟡 Operational Authority |
| **Treasury & Settlement Operations Officer** (`role_treasury_operations_officer`) | 0 | 2 | 1 | 2 | **5** | 🟡 Operational Authority |

---

## 3. Decision Governance & Single-Approver Rule Analysis

✅ **Single Approver Rule Upheld!**
Every decision milestone has exactly one designated Approver (A), preventing consensus deadlock.

