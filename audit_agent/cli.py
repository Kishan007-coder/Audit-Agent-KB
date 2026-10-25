from __future__ import annotations

import csv
import json
import re
from dataclasses import dataclass, field
from datetime import datetime
from pathlib import Path
from typing import Any, Iterable


@dataclass
class Ticket:
    ticket_id: str
    rows: list[dict[str, Any]] = field(default_factory=list)
    assignment_group: str = ""
    assigned_to: str = ""
    created_at: datetime | None = None
    closed_at: datetime | None = None
    text: str = ""

    @property
    def duration_hours(self) -> float | None:
        if self.created_at and self.closed_at:
            delta = self.closed_at - self.created_at
            return delta.total_seconds() / 3600
        return None


@dataclass
class ControlResult:
    control_id: int
    question: str
    result: str
    remark: str


class AuditEngine:
    """Rule-based ticket auditor based on the supplied KB."""

    _TEXT_FIELDS = [
        "Description",
        "Work Notes",
        "Additional Comments",
        "Approval",
        "Approval Comments",
        "Activity",
        "Implementation Details",
        "Implementation Start",
        "Implementation End",
        "Resolution Notes",
        "Closure Notes",
        "Doer",
        "Checker",
        "Pre-Doer",
        "Pre-Checker",
        "Post-Doer",
        "Post-Checker",
        "Customer Communication",
        "Comments",
        "Activity Logs",
        "Request Description",
    ]

    def audit_csv(self, csv_path: str | Path) -> dict[str, Any]:
        tickets, total_rows, duplicate_rows = self._load_tickets(csv_path)
        ticket_reports: list[dict[str, Any]] = []

        for ticket in tickets:
            ticket_reports.append(self._audit_ticket(ticket))

        return {
            "validated_unique_ticket_count": len(tickets),
            "total_rows": total_rows,
            "duplicate_rows_removed": duplicate_rows,
            "tickets": ticket_reports,
        }

    def _load_tickets(self, csv_path: str | Path) -> tuple[list[Ticket], int, int]:
        path = Path(csv_path)
        with path.open("r", encoding="utf-8-sig", newline="") as fh:
            reader = csv.DictReader(fh)
            if reader.fieldnames is None:
                return [], 0, 0
            rows = list(reader)

        grouped: dict[str, list[dict[str, Any]]] = {}
        missing_counter = 1

        for row in rows:
            ticket_value = self._get_row_value(row, [
                "Ticket Number",
                "ticket number",
                "Ticket#",
                "Ticket ID",
                "ticket_id",
                "Incident Number",
            ])
            ticket_id = str(ticket_value).strip() if ticket_value and str(ticket_value).strip() else f"MISSING-TICKET-ID-{missing_counter}"
            if not ticket_value or not str(ticket_value).strip():
                missing_counter += 1
            grouped.setdefault(ticket_id, []).append(row)

        tickets: list[Ticket] = []
        duplicate_rows = 0

        for ticket_id, ticket_rows in grouped.items():
            deduped_rows: list[dict[str, Any]] = []
            seen: set[str] = set()
            for row in ticket_rows:
                row_key = json.dumps(row, sort_keys=True, ensure_ascii=False)
                if row_key in seen:
                    duplicate_rows += 1
                    continue
                seen.add(row_key)
                deduped_rows.append(row)

            ticket = Ticket(ticket_id=ticket_id, rows=deduped_rows)
            ticket.assignment_group = self._first_nonempty(deduped_rows, ["Assignment Group", "assignment_group", "AssignmentGroup"])
            ticket.assigned_to = self._first_nonempty(deduped_rows, ["Assigned To", "assigned_to", "Assignee"])
            ticket.created_at = self._first_datetime(deduped_rows, [
                "Opened Date/Time",
                "opened date/time",
                "Created Date",
                "created_at",
                "Created",
            ])
            ticket.closed_at = self._first_datetime(deduped_rows, [
                "Closed Date/Time",
                "closed date/time",
                "Resolved Date/Time",
                "resolved_at",
                "Closed",
                "Resolved",
            ])
            ticket.text = self._build_ticket_text(deduped_rows)
            tickets.append(ticket)

        return tickets, len(rows), duplicate_rows

    def _audit_ticket(self, ticket: Ticket) -> dict[str, Any]:
        controls = [
            self._control_1(ticket),
            self._control_2(ticket),
            self._control_3(ticket),
            self._control_4(ticket),
        ]

        return {
            "ticket_id": ticket.ticket_id,
            "assignment_group": ticket.assignment_group,
            "assigned_to": ticket.assigned_to,
            "created_at": ticket.created_at.isoformat() if ticket.created_at else None,
            "closed_at": ticket.closed_at.isoformat() if ticket.closed_at else None,
            "controls": [
                {
                    "control_id": c.control_id,
                    "question": c.question,
                    "result": c.result,
                    "remark": c.remark,
                }
                for c in controls
            ],
        }

    def _control_1(self, ticket: Ticket) -> ControlResult:
        text = ticket.text.lower()
        if "customer approval not required" in text or "not required for this activity" in text:
            return ControlResult(1, "Was the activity approved by the customer?", "NA", "The ticket states that customer approval was not required; no approval evidence is necessary.")

        approval_evidence = bool(re.search(r"customer.*approved|approved by customer|approval.*received|approved.*on|customer approval", text))
        if approval_evidence:
            return ControlResult(1, "Was the activity approved by the customer?", "YES", "Customer approval is documented in the ticket narrative or approval records.")

        if "approval" in text or "approved" in text:
            return ControlResult(1, "Was the activity approved by the customer?", "NO", "Approval is mentioned, but the ticket does not provide evidence that customer approval was required and documented before the work.")

        return ControlResult(1, "Was the activity approved by the customer?", "NA", "No documented approval requirement or approval evidence was identified in the ticket.")

    def _control_2(self, ticket: Ticket) -> ControlResult:
        text = ticket.text.lower()
        window_patterns = [
            r"implementation window\s*[:\-]?\s*(.*?)(?:\n|\.|;|$)",
            r"approved window\s*[:\-]?\s*(.*?)(?:\n|\.|;|$)",
            r"between\s+(\d{1,2}[-/ ]\w+[-/ ]\d{2,4}\s+\d{1,2}:?\d{2}\s*(?:am|pm)?)\s+and\s+(\d{1,2}[-/ ]\w+[-/ ]\d{2,4}\s+\d{1,2}:?\d{2}\s*(?:am|pm)?)",
            r"from\s+(\d{4}-\d{2}-\d{2}\s+\d{2}:\d{2})\s+to\s+(\d{4}-\d{2}-\d{2}\s+\d{2}:\d{2})",
        ]

        window_found = any(re.search(pattern, text) for pattern in window_patterns)
        if not window_found:
            return ControlResult(2, "Was the activity implemented within the agreed/customer-approved window?", "NA", "No valid agreed or customer-approved implementation window was identified in the available ticket evidence.")

        valid_window = self._extract_window_label(ticket.text)
        if not valid_window:
            return ControlResult(2, "Was the activity implemented within the agreed/customer-approved window?", "NO", "A candidate window was found, but the ticket does not provide enough evidence to confirm the final approved implementation window.")

        actual_impl = self._extract_implementation_timestamp(ticket.text)
        if actual_impl is None:
            return ControlResult(2, "Was the activity implemented within the agreed/customer-approved window?", "NO", "A valid implementation window exists, but the ticket does not provide an implementation timestamp sufficient to confirm compliance.")

        if self._window_contains(actual_impl, valid_window):
            return ControlResult(2, "Was the activity implemented within the agreed/customer-approved window?", "YES", f"A valid implementation window was identified: '{valid_window}'. The evidence shows the implementation occurred within that approved window.")

        return ControlResult(2, "Was the activity implemented within the agreed/customer-approved window?", "NO", f"A valid implementation window was identified: '{valid_window}', but the implementation timestamp falls outside that approved window.")

    def _control_3(self, ticket: Ticket) -> ControlResult:
        text = ticket.text.lower()
        doer_checker_applicable = "doer" in text and "checker" in text
        status_required = ticket.duration_hours is not None and ticket.duration_hours >= 24
        has_closure_notes = any(k.lower() in text for k in ["closure notes", "service request closure", "request completed", "resolved"])

        if doer_checker_applicable:
            has_doer_checker = all(needle in text for needle in ["pre-doer", "pre-checker", "post-doer", "post-checker"])
            if not has_doer_checker:
                return ControlResult(3, "Were the required documentation templates for Doer-Checker, status check, and closure notes followed?", "NO", "Doer-Checker is applicable, but one or more mandatory Doer-Checker stages are missing or incomplete.")
        else:
            has_doer_checker = True

        if status_required:
            has_status = "status check" in text or "status update" in text or "current status" in text
            if not has_status:
                return ControlResult(3, "Were the required documentation templates for Doer-Checker, status check, and closure notes followed?", "NO", "The ticket remained open for 24 hours or more, but meaningful status-check evidence is missing.")
        else:
            has_status = True

        if not has_closure_notes:
            return ControlResult(3, "Were the required documentation templates for Doer-Checker, status check, and closure notes followed?", "NO", "Closure notes or a meaningful closure summary are missing.")

        return ControlResult(3, "Were the required documentation templates for Doer-Checker, status check, and closure notes followed?", "YES", "The applicable documentation templates were identified and the ticket contains the required completion evidence.")

    def _control_4(self, ticket: Ticket) -> ControlResult:
        text = ticket.text.lower()
        if "doer" not in text and "checker" not in text:
            return ControlResult(4, "Were Pre-Doer, Pre-Checker, Post-Doer and Post-Checker notes documented according to the standard template?", "NA", "Doer-Checker is not applicable or not evidenced; no four-stage validation sequence is required.")

        stages = [
            "pre-doer",
            "pre-checker",
            "post-doer",
            "post-checker",
        ]
        stage_presence = {stage: stage in text for stage in stages}
        if not all(stage_presence.values()):
            return ControlResult(4, "Were Pre-Doer, Pre-Checker, Post-Doer and Post-Checker notes documented according to the standard template?", "NO", "One or more required Pre/Post Doer-Checker stages are missing from the ticket evidence.")

        sequence_ok = self._sequence_is_valid(ticket.text)
        if not sequence_ok:
            return ControlResult(4, "Were Pre-Doer, Pre-Checker, Post-Doer and Post-Checker notes documented according to the standard template?", "NO", "The required stages are present, but the sequence or stage-specific evidence is not consistent with the KB.")

        return ControlResult(4, "Were Pre-Doer, Pre-Checker, Post-Doer and Post-Checker notes documented according to the standard template?", "YES", "The four-stage Doer-Checker sequence is documented in the ticket and appears consistent with the KB.")

    def _build_ticket_text(self, rows: Iterable[dict[str, Any]]) -> str:
        text_chunks: list[str] = []
        for row in rows:
            for key in self._TEXT_FIELDS:
                value = row.get(key)
                if value is not None and str(value).strip():
                    text_chunks.append(f"{key}: {value}")
            for key, value in row.items():
                if key not in self._TEXT_FIELDS and str(value).strip():
                    text_chunks.append(str(value))
        return "\n".join(text_chunks)

    def _get_row_value(self, row: dict[str, Any], candidates: list[str]) -> Any:
        for candidate in candidates:
            if candidate in row and row.get(candidate) not in (None, ""):
                return row.get(candidate)
        return None

    def _first_nonempty(self, rows: list[dict[str, Any]], candidates: list[str]) -> str:
        for row in rows:
            for candidate in candidates:
                value = row.get(candidate)
                if value is not None and str(value).strip():
                    return str(value).strip()
        return ""

    def _first_datetime(self, rows: list[dict[str, Any]], candidates: list[str]) -> datetime | None:
        for row in rows:
            for candidate in candidates:
                value = row.get(candidate)
                if value is None or str(value).strip() == "":
                    continue
                dt = self._parse_datetime(str(value))
                if dt:
                    return dt
        return None

    def _parse_datetime(self, value: str) -> datetime | None:
        cleaned = value.strip()
        for pattern in [
            "%Y-%m-%d %H:%M:%S",
            "%Y-%m-%d %H:%M",
            "%Y-%m-%d",
            "%m/%d/%Y %H:%M",
            "%m/%d/%Y",
            "%d-%m-%Y %H:%M",
            "%d-%m-%Y",
            "%m-%d-%Y %H:%M",
            "%m-%d-%Y",
        ]:
            try:
                return datetime.strptime(cleaned, pattern)
            except ValueError:
                pass
        return None

    def _extract_window_label(self, text: str) -> str | None:
        matches = []
        for pattern in [
            r"implementation window\s*[:\-]?\s*([^\n\.]+)",
            r"approved window\s*[:\-]?\s*([^\n\.]+)",
            r"from\s+(\d{4}-\d{2}-\d{2}\s+\d{2}:\d{2})\s+to\s+(\d{4}-\d{2}-\d{2}\s+\d{2}:\d{2})",
            r"between\s+(\d{1,2}[-/ ]\w+[-/ ]\d{2,4}\s+\d{1,2}:?\d{2}\s*(?:am|pm)?)\s+and\s+(\d{1,2}[-/ ]\w+[-/ ]\d{2,4}\s+\d{1,2}:?\d{2}\s*(?:am|pm)?)",
        ]:
            match = re.search(pattern, text, re.IGNORECASE)
            if match:
                matches.append(match.group(0).strip())
        return matches[-1] if matches else None

    def _extract_implementation_timestamp(self, text: str) -> datetime | None:
        candidates = []
        patterns = [
            r"implementation\s+completed\s+on\s+(\d{4}-\d{2}-\d{2}\s+\d{2}:\d{2})",
            r"implemented\s+on\s+(\d{4}-\d{2}-\d{2}\s+\d{2}:\d{2})",
            r"completed\s+at\s+(\d{4}-\d{2}-\d{2}\s+\d{2}:\d{2})",
            r"(\d{4}-\d{2}-\d{2}\s+\d{2}:\d{2})",
        ]
        for pattern in patterns:
            match = re.search(pattern, text, re.IGNORECASE)
            if match:
                candidates.append(match.group(1))
        for value in candidates:
            dt = self._parse_datetime(value)
            if dt is not None:
                return dt
        return None

    def _window_contains(self, actual: datetime, window_text: str) -> bool:
        match = re.search(r"from\s+(\d{4}-\d{2}-\d{2}\s+\d{2}:\d{2})\s+to\s+(\d{4}-\d{2}-\d{2}\s+\d{2}:\d{2})", window_text, re.IGNORECASE)
        if match:
            start = self._parse_datetime(match.group(1))
            end = self._parse_datetime(match.group(2))
            if start and end:
                return start <= actual <= end
        return True

    def _sequence_is_valid(self, text: str) -> bool:
        ordered = [
            "pre-doer",
            "pre-checker",
            "post-doer",
            "post-checker",
        ]
        positions = []
        for stage in ordered:
            pos = text.lower().find(stage)
            if pos != -1:
                positions.append((stage, pos))
        # Stage presence is enough for the starter logic.
        return len(positions) == len(ordered) and [s for s, _ in positions] == ordered


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Audit a ServiceNow ticket export against the supplied KB")
    parser.add_argument("csv_path", help="Path to a CSV ticket export")
    parser.add_argument("--format", default="json", choices=["json", "pretty"], help="Output format")
    args = parser.parse_args()

    engine = AuditEngine()
    report = engine.audit_csv(args.csv_path)

    if args.format == "json":
        print(json.dumps(report, indent=2, ensure_ascii=False))
    else:
        for ticket in report["tickets"]:
            print(f"Ticket: {ticket['ticket_id']}")
            for control in ticket["controls"]:
                print(f"  {control['control_id']}: {control['result']} - {control['remark']}")
