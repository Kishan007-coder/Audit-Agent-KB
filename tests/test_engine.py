from __future__ import annotations

import argparse
import json

from audit_agent.engine import AuditEngine


def main() -> None:
    parser = argparse.ArgumentParser(description="Service Request Audit Agent")
    parser.add_argument("csv_path", help="Path to the ServiceNow CSV export to audit")
    parser.add_argument("--format", choices=["json", "pretty"], default="json", help="Output format")
    args = parser.parse_args()

    engine = AuditEngine()
    result = engine.audit_csv(args.csv_path)

    if args.format == "json":
        print(json.dumps(result, indent=2, ensure_ascii=False))
    else:
        for ticket in result["tickets"]:
            print(f"Ticket: {ticket['ticket_id']}")
            for control in ticket["controls"]:
                print(f"  Control {control['control_id']}: {control['result']} | {control['remark']}")


if __name__ == "__main__":
    main()
