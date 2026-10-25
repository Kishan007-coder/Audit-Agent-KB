# Service Request Audit Agent

This repository contains a starter audit agent built from the KB in `TQA_Audit_SR_KB_3.md`.

It reads a ServiceNow-style CSV export, consolidates rows by ticket, validates duplicate/missing identifiers, and produces an audit report for the first major controls from the KB:

- Control 1 — Customer Approval
- Control 2 — Approved Implementation Window
- Control 3 — Required Documentation Templates
- Control 4 — Pre/Post Doer-Checker Notes

## Quick start

```bash
python -m audit_agent.cli samples/sample_service_requests.csv --format json
```

## Example output

```json
{
  "validated_unique_ticket_count": 2,
  "total_rows": 4,
  "duplicate_rows_removed": 1,
  "tickets": [
    {
      "ticket_id": "SR-1001",
      "controls": [
        {
          "control_id": 1,
          "question": "Was the activity approved by the customer?",
          "result": "YES",
          "remark": "Customer approval was documented ..."
        }
      ]
    }
  ]
}
```

## Notes

- This is an implementation starter, not a full production-grade legal or policy engine.
- The audit logic follows the KB guidance and applies conservative reasoning when evidence is missing.
- For a production deployment, add richer parsing for all KB controls and a stronger ticket-normalization layer.
