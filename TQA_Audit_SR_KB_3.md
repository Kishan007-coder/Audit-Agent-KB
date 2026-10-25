> TQA SERVICE REQUEST AUDIT AGENT

##################### AUTHORITATIVE KNOWLEDGE BASE

> **Version:** 9.2
>
> **Purpose:** This document contains detailed business rules, control definitions, evidence requirements, applicability rules, examples, scoring logic, validation rules, and Excel/reporting specifications that should remain outside the Copilot Agent Instructions.

########### 1. Agent Purpose and Scope

> The agent audits ServiceNow Service Request tickets only. The audit covers documentation quality, process compliance, authorization, implementation/execution, communication, evidence, backup evidence, OEM/vendor documentation, and Doer-Checker compliance.
>
> The agent must not use Incident controls, Change controls, legacy controls, or any undefined audit parameters.
>
> The submitted source is normally an Excel or CSV ServiceNow export. One ticket may occupy multiple rows because of activity/history records. All rows belonging to the same ticket must be consolidated chronologically before auditing.

########### 2. Input Fields and Evidence Sources

> Potential fields include:

- Ticket Number

- Assigned To

- Assignment Group

- Opened Date/Time

- Updated Date/Time

- Resolved Date/Time

- Closed Date/Time

- State/Status

- Description

- Work Notes

- Additional Comments

- Configuration Item (CI)

- Approval information/comments/timestamps

- Implementation details

- Activity/history records

- Doer-Checker information

- Pre-Doer

- Pre-Checker

- Post-Doer

- Post-Checker

- Activity timestamps

- Customer communication

- Attachment metadata

- Backup evidence

- OEM/vendor information

- Vendor ticket number

- Audit Track

- Reporting Month

- Timezone(PST)

> Use only fields actually present. Do not require a field if it is irrelevant to the specific control.

########### 3. Ticket Identification and Validation

> Before auditing:

- Count all input rows/records.

- Identify every unique Ticket Number.

- Consolidate all rows for the same ticket chronologically.

- Audit each unique ticket exactly once.

- Do not combine evidence across different tickets.

- Preserve Ticket Number, Assignment Group, and Assigned To exactly as supplied.

- Report exact duplicates in Validation Summary.

- Never omit an incomplete ticket.

> If Ticket Number is missing, assign a temporary identifier: MISSING-TICKET-ID-001, MISSING-TICKET-ID-002, etc. Do not fabricate a ServiceNow ticket number. Include the record and flag the missing identifier.
>
> The final audited ticket count must equal the validated unique-ticket count, except that duplicate rows of the same ticket are consolidated and audited once.

########### 4. Evidence Decision Standard

> Every control result must be supported by evidence belonging to the ticket being audited.
>
> **YES:** Use Yes only when the complete requirement is clearly supported by available evidence.
>
> **NO:** Use No when:

- the requirement is not met;

- required evidence is missing;

- evidence is incomplete;

- evidence is contradictory;

- compliance cannot be established under the control's applicable rule;

- only partial compliance is demonstrated.

> **NA:** Use NA only when the specific control allows NA and the evidence confirms that the control genuinely does not apply.
>
> **Never:**

- infer approval;

- infer customer communication;

- infer implementation;

- infer evidence;

- treat missing information as automatically compliant;

- use another ticket as evidence;

- convert partial compliance to Yes;

- use NA simply because information is missing when the control requires a Yes/No decision.

> Every control must have a meaningful audit remark.

########### 5. Audit Controls

##################### Control 1 — Customer Approval

**Question: Was the activity approved by the customer?**

**Review:**  
• Work notes  
• Customer communication  
• Approval records  
• Ticket description/documentation

**Decision Logic:**  
The work notes and/or supporting documentation must explicitly indicate that customer approval was required for the activity. If no documented approval requirement is identified, customer approval cannot be considered mandatory. Customer closure confirmation is **not** customer approval.

**YES:** Customer approval was required and documented before the activity was performed.

**NO:** Customer approval was required, but approval is missing, undocumented.

**NA:** The work notes or documentation do not indicate that customer approval was required or explicitly state that customer approval was not required.

**Remark:** Must state the evidence showing whether approval was required, the approval source (for YES), or the missing approval evidence (for NO).

##################### Control 2 — Approved Implementation Window

> **Question: Was the activity implemented within the agreed/customer-approved window?**
>
> **Review:**

- Mentioned implementation window.

- Approval timestamp.

- Work notes.

- Activity logs.

- Implementation of the timestamps.

- Request description, customer comments, communication records, resolution notes, and other available CSV fields that may contain implementation-window information.

- Review all available written comments and notes to determine whether the initially mentioned implementation window was later changed, cancelled, corrected, or superseded.

> **YES:** A specific and valid implementation window is documented, and the available timestamps confirm that the activity was implemented within that window.
>
> **Remark:** Must identify:

- The agreed or customer-approved implementation window.

- Where the implementation window was documented.

- The actual implementation date and time.

- Confirmation that the activity was completed within the valid implementation window.

> **NO:** A specific and valid implementation window is documented, but:

- The activity was implemented outside the agreed window, or

- The applicable evidence establishes that the timing requirement was not followed, or

- The implementation timestamps are missing or insufficient to confirm that the activity was completed within the agreed window.

> **Remark:** Must identify:

- The valid implementation window.

- Where the window was documented.

- The available implementation timestamp, if present.

- How the activity occurred outside the window, or which timestamp evidence is missing and prevents compliance from being established.

> **NA:** No valid implementation window is mentioned or required in the ticket. Since this control applies to a Service Request, an implementation window is not mandatory unless one is specifically agreed, approved, or documented.
>
> **Remark:** Must state that no valid agreed or customer-approved implementation window was identified in the request description, work notes, customer comments, activity records, communication records, or other available ticket fields.
>
> If a valid implementation window exists but the timestamps are insufficient to establish compliance, do not invent, estimate, or assume the implementation time. Treat the result as **NO** because compliance cannot be established for an applicable control, and clearly explain the missing timestamp evidence.
>
> **Auditor Guidance**
>
> The audit agent must first determine whether a valid implementation window exists. An implementation window is not compulsory for every Service Request. Therefore, the agent must not mark the control as **NO** only because no implementation window is mentioned.
>
> If no valid agreed or customer-approved implementation window is identified after reviewing all available ticket information, select **NA**.
>
> If an implementation window is mentioned, the agent must validate whether it represents the final and applicable window before comparing it with the implementation timestamp.
>
> The agent must review the complete sequence of work notes, comments, descriptions, customer communications, and ticket updates. This review must identify whether an earlier implementation window was:

- Changed to a new window.

- Cancelled.

- Postponed or rescheduled.

- Entered incorrectly.

- Added by mistake.

- Rejected by the customer.

- Replaced by a later agreed window.

- Explicitly marked as invalid or no longer applicable.

> Instructions such as the following indicate that an earlier window may no longer be valid:

- “Please ignore the previous comment.”

- “Ignore the below implementation window.”

- “The previously mentioned window was incorrect.”

- “Please consider the revised window.”

- “The activity has been rescheduled.”

- “The previous schedule has been cancelled.”

- “Please use the updated date and time.”

- Any equivalent statement showing that an earlier window was withdrawn, corrected, or replaced.

> When such instructions are present, the agent must ignore the cancelled, incorrect, or superseded window and use only the latest valid agreed or customer-approved implementation window.
>
> A date or time mentioned in the ticket must not automatically be treated as an approved implementation window. The agent must verify that the date and time clearly relate to the planned, agreed, or customer-approved implementation of the activity. Generic dates, target dates, due dates, ticket creation times, assignment times, response times, resolution times, SLA times, or casually mentioned dates must not be treated as implementation windows.
>
> When reviewing CSV-based data, attachments may not be available. The agent must rely on the available written content in fields such as:

- Request Description.

- Work Notes.

- Customer Comments.

- Approval Records.

- Activity Logs.

- Resolution Notes.

- Communication Records.

- Implementation Start and End Timestamps.

- Any other exported ticket fields.

> The absence of an attachment must not automatically result in **NO**. The agent must first read and assess all available written information in the CSV.
>
> Apply the result as follows:

- Select **YES** when a valid implementation window exists and the activity was implemented within that window.

- Select **NO** when a valid implementation window exists and the activity was implemented outside that window.

- Select **NO** when a valid implementation window exists but the implementation timestamp is missing or insufficient to establish compliance.

- Select **NA** when no valid agreed or customer-approved implementation window exists.

- Select **NA** when a window was entered mistakenly and was later clearly withdrawn, with no replacement window provided.

- If multiple windows are mentioned, use the latest valid window that was agreed or approved and ignore any earlier window that was cancelled, corrected, or superseded.

> The agent must not invent an implementation window, assume approval, or use an outdated or invalid window to determine the result.

##################### Control 3 — Required Documentation Templates

> **Question: Were the required documentation templates for Doer-Checker, status check, and closure notes followed?**
>
> **Review:**

- Doer-Checker documentation, only when Doer-Checker is applicable.

- Status-check documentation, only when the ticket remained open for 24 hours or more.

- Service Request closure notes.

- Request description.

- Work notes.

- Resolution notes.

- Activity logs and comments.

- Ticket creation date and time.

- Ticket completion or closure date and time.

- Assignment group or team details.

- Team weekly-off or non-working-day information.

- Ticket status and closure information.

- “Closed by” details.

- Applicable template rules, requirements, and examples provided in the KB.

- Any other available CSV fields containing Doer-Checker, status-check, closure, or timestamp information.

> The agent must first determine which templates are applicable to the Service Request. The agent must check only the templates that are applicable according to the rules and examples provided in the KB.
>
> The agent must evaluate each applicable template separately. The presence of one correctly completed template must not be used to assume that the other applicable templates were also completed.
>
> **Control 3 — Mandatory Exclusion Rule**
>
> **Daily ticket-update compliance must not be evaluated under Control 3. Missing daily updates, missing updates on applicable working days, 24-hour update gaps, ticket lifecycle dates, weekly offs, holidays, and team working schedules must not affect the Control 3 result or remark.**
>
> **Do not mark Control 3 NO because daily status updates are missing. Control 3 must only verify whether the applicable Doer-Checker, status-check, and closure-notes templates follow the required KB format.**
>
> **If a status-check entry is available, review only whether its content follows the applicable status-check template. Do not evaluate how frequently the status check was added or whether an update was recorded on every applicable working day.**
>
> **Daily ticket-update frequency and 24-hour update compliance must be evaluated exclusively under Control 14 — 24-Hour Ticket Updates.**
>
> **Prohibited Control 3 Finding: Do not include remarks such as “daily status updates are missing,” “working-day updates are missing,” “24-hour update gaps were identified,” or any equivalent finding under Control 3. These findings belong only to Control 14.**
>
>  
>
> **YES**
>
> Required applicable templates are present and followed.
>
> Select **YES** only when all the following requirements are satisfied:

- The Doer-Checker template is present and correctly completed, when Doer-Checker is applicable.

- If Doer-Checker is not applicable according to the KB rules, the Doer-Checker check is skipped.

- If the ticket remained open for 24 hours or more, a meaningful status check is documented for every applicable working day after the ticket reached 24 hours.

- The team’s confirmed weekly off or non-working days are excluded from the daily status-check requirement.

- If the ticket was completed or closed within 24 hours of creation, the status-check template is not required.

- The Service Request closure-notes template is present and correctly completed.

- All mandatory sections required by the applicable KB templates are documented.

- The documented information relates to the ticket being reviewed.

- The information is complete, meaningful, and consistent with the activity performed.

- Any section marked “NA,” “N/A,” or “Not Applicable” contains a valid reason when an explanation is required by the KB.

> If Doer-Checker or status-check documentation is not applicable, the agent must skip that specific check and continue reviewing the remaining applicable templates.
>
> **Remark:** Must identify:

- Each applicable template reviewed.

- Where each applicable template was found.

- Whether each applicable template was complete and correctly followed.

- Any template determined to be not applicable and the reason.

- For status checks, the ticket creation time, completion or closure time, applicable working days, excluded weekly-off days, and status updates reviewed.

- Confirmation that all required applicable templates were followed.

>  
>
> **NO**
>
> A required applicable template is missing, incomplete, or incorrectly documented.
>
> Select **NO** when one or more of the following conditions apply:

- Doer-Checker is applicable, but the required Doer-Checker template is missing.

- Doer-Checker is applicable, but its documentation is incomplete or incorrect.

- The ticket remained open for 24 hours or more, but no status check was documented.

- The ticket remained open for 24 hours or more, but a meaningful status update is missing for one or more applicable working days.

- A working day was incorrectly excluded without evidence that it was the assigned team’s weekly off or non-working day.

- A status update contains only generic or placeholder wording without meaningful information.

- The required Service Request closure notes are missing, incomplete, or incorrectly documented.

- A mandatory section or required field in an applicable template is missing.

- An applicable template was not completed according to the KB requirements.

- The information documented in the template is generic, unclear, unrelated, or not meaningful for the ticket.

- A section is marked “NA,” “N/A,” or “Not Applicable” without a valid reason when the KB requires an explanation.

- The documentation contains only template headings without the required details.

- The closure notes do not clearly document the request and actions completed.

- One applicable template is correctly completed, but another required applicable template is missing or incomplete.

- The agent cannot validate a required applicable template from the available CSV data.

> The agent must **not** select **NO** only because:

- Doer-Checker documentation is missing when Doer-Checker is not applicable.

- Status-check documentation is missing when the ticket was completed or closed within 24 hours.

- A status check is missing on a confirmed weekly off or non-working day of the team handling the ticket.

- Attachments are unavailable, but sufficient evidence is available in other CSV fields.

> **Remark:** Must identify:

- The specific applicable template that is missing, incomplete, or incorrectly documented.

- The specific required section, daily status update, or information that is missing or incorrect.

- Where the agent checked for the documentation.

- The applicable KB requirement or template example used for comparison.

- Why the available documentation does not meet the requirement.

- For missing status checks, the specific applicable working date or dates on which a meaningful status update was required but not found.

>  
>
> **NA**
>
> Only when the ticket was closed by Requester, as defined by the source rule.
>
> Select **NA** only when:

- The available ticket evidence clearly confirms that the ticket was closed by the requester; and

- The applicable source rule states that this control is not applicable when the ticket is closed by the requester.

> The agent must not select **NA** merely because:

- Doer-Checker is not applicable.

- Status-check documentation is not applicable.

- The ticket was completed within 24 hours.

- A required template is missing.

- Documentation is incomplete.

- Closure notes are unavailable.

- The CSV contains limited information.

- Attachments are unavailable.

- The agent cannot locate a required applicable template.

- The ticket was closed by a resolver, analyst, engineer, system, or support-team member.

- The “Closed by” information is missing, blank, or unclear.

> If Doer-Checker is not applicable, skip the Doer-Checker check and continue reviewing the other applicable templates.
>
> If the status-check template is not applicable because the ticket was completed within 24 hours, skip the status-check review and continue reviewing the closure-notes template and Doer-Checker documentation, when applicable.
>
> The non-applicability of an individual template does not make the entire control **NA**.
>
> **Remark:** Must identify:

- The evidence confirming that the requester closed the ticket.

- The ticket field or record containing the requester-closure evidence.

- Confirmation that the applicable source rule permits **NA** for a requester-closed ticket.

>  
>
> **Doer-Checker Applicability and Validation**
>
> The agent must first determine whether Doer-Checker is applicable by using the rules and examples provided in the KB.
>
> **When Doer-Checker Is Applicable**
>
> When Doer-Checker is applicable:

- The agent must locate the required Doer-Checker documentation.

- The agent must compare it with the applicable KB template.

- The agent must confirm that all mandatory sections are completed.

- The agent must verify that the documented Doer and Checker information relates to the actual ticket.

- If required Doer-Checker documentation is missing, incomplete, or incorrect, select **NO**.

> **When Doer-Checker Is Not Applicable**
>
> When Doer-Checker is not applicable:

- Skip the Doer-Checker template review.

- Do not search for or require a Doer-Checker template.

- Do not select **NO** because Doer-Checker documentation is absent.

- Do not select **NA** for the entire control only because Doer-Checker is not applicable.

- Continue reviewing the status-check and closure-notes templates.

> If the ticket states that Doer-Checker is not applicable, the agent must validate the statement against the applicable KB rule. The words “NA,” “N/A,” or “Not Applicable” must not be accepted automatically if the KB requires a reason or if the ticket activity indicates that Doer-Checker should apply.
>
>  
>
> **Status-Check Applicability and Validation**
>
> The agent must determine whether status-check documentation is required by comparing:

- Ticket creation date and time.

- Ticket completion or closure date and time.

- Work-note and activity timestamps.

- Applicable working days.

- Confirmed weekly-off or non-working days of the team handling the ticket.

> **When the Status Check Is Applicable**
>
> The status-check template is required when the ticket was completed or closed **24 hours or more after it was created**.
>
> This includes tickets that remained open for:

- Exactly 24 hours.

- Between 24 and 48 hours.

- More than 48 hours.

- Multiple working days.

> Once the ticket reaches 24 hours from its creation time, the agent must check for a meaningful status update on every applicable working day until the ticket is completed or closed.
>
> **When the Status Check Is Not Applicable**
>
> The status-check template is not required when:

- The ticket was completed or closed in less than 24 hours from its creation; or

- A specific day was a confirmed weekly off or non-working day for the team responsible for the ticket.

> A missing status check must not result in **NO** when the ticket was completed or closed in less than 24 hours.
>
> Status-check non-applicability does not make the entire control **NA**. The agent must continue checking Doer-Checker, when applicable, and the closure-notes template.
>
>  
>
> **Daily Status-Check Requirement**
>
> For a ticket that remained open for 24 hours or more, a meaningful status update must be documented on every applicable working day after the ticket reached 24 hours and until it was completed or closed.
>
> A meaningful status update may include:

- Current progress.

- Actions completed.

- Actions pending.

- Current ticket position.

- Reason for delay.

- Dependency or blocker.

- Waiting for requester or customer information.

- Waiting for approval.

- Waiting for another team.

- Troubleshooting or investigation details.

- Planned next action.

- Expected completion time, if available.

> Generic entries such as the following must not be accepted as complete status checks unless the KB specifically permits them:

- “WIP.”

- “In progress.”

- “Work ongoing.”

- “Pending.”

- “Checking.”

- “Under observation.”

- “Will update.”

- “No update.”

> A status entry must provide enough meaningful information to show the ticket’s progress, current situation, pending action, dependency, or next step.
>
> The status update does not need to match the wording or formatting of the KB example exactly. However, it must contain the mandatory information required by the applicable status-check template.
>
>  
>
> **Team Weekly-Off Exception**
>
> A status check is not required on a confirmed weekly off or non-working day of the team responsible for the ticket.
>
> The agent must:

- Identify the team responsible for the ticket during the relevant period.

- Identify that team’s weekly off or non-working day using the information or rules provided in the KB or available ticket data.

- Exclude the confirmed weekly-off or non-working day from the daily status-check requirement.

- Resume checking for status updates on the next working day if the ticket remains open.

- Not select **NO** only because a status update is missing on the team’s confirmed weekly off.

> The agent must not automatically assume that Saturday, Sunday, or any other day is a weekly off. The day must be established using the team calendar, shift information, weekly-off information, or applicable rules provided in the KB.
>
> If the ticket was reassigned from one team to another, use the working schedule of the team responsible for the ticket on each applicable day, where that information is available.
>
> If the available data does not establish the team’s weekly off, the agent must not invent or assume a weekly-off day.
>
>  
>
> **Service Request Closure-Notes Validation**
>
> The Service Request closure-notes template must be reviewed for every ticket unless the entire control is **NA** because the ticket was closed by the requester under the applicable source rule.
>
> The agent must compare the closure notes with the applicable template and examples provided in the KB.
>
> The wording and formatting do not need to match the KB example exactly. However, all mandatory information required by the closure-notes template must be clearly documented.
>
> The agent must verify that:

- The Service Request or requested activity is described.

- The actions completed are documented.

- The information relates to the actual ticket.

- **Mandatory closure sections are completed.**

- Doer-Checker information is included only when required by the applicable template and rules.

- User validation, SLA, or other sections are documented when required by the KB.

- Any section marked as not applicable contains a valid explanation when required.

- The closure notes contain meaningful information and not only template headings or placeholder text.  
    
   

> **Reference Sample — Service Request Closure Notes**
>
>  
>
> Service Request Description:
>
> Request to reset Active Directory password.
>
>  
>
> Actions Completed:
>
> \- Verified user identity
>
> \- Password reset performed
>
> \- User informed of temporary password
>
>  
>
> Doer & Checker:
>
> Not Applicable — Standard request with automated validation.
>
>  
>
> User Validation:
>
> User confirmed successful login post password reset.
>
>  
>
> SLA:
>
> Met.
>
>  
>
> **Auditor Guidance**
>
> The agent must complete the assessment in the following order.
>
> **Step 1: Check Whether the Ticket Was Closed by the Requester**
>
> Review the “Closed by” field and other available closure evidence.

- If the ticket was closed by the requester and the source rule permits it, select **NA** for the entire control.

- If requester closure cannot be clearly established, do not select **NA**.

- Continue reviewing all applicable templates.

> **Step 2: Determine Whether Doer-Checker Is Applicable**
>
> Use the applicable rules and examples provided in the KB.

- If applicable, validate the Doer-Checker template.

- If not applicable, skip the Doer-Checker check.

- Do not select **NO** because Doer-Checker documentation is missing when Doer-Checker is not applicable.

> **Step 3: Determine Whether the Status Check Is Applicable**
>
> Calculate the time between ticket creation and completion or closure.

- If the duration is less than 24 hours, skip the status-check review.

- If the duration is 24 hours or more, review daily status-check documentation.

- Check every applicable working day after the ticket reached 24 hours.

- Exclude only confirmed weekly-off or non-working days of the responsible team.

- Resume the status-check requirement on the next working day if the ticket remains open.

> The agent must use available timestamps and must not estimate, invent, or assume missing dates or times.
>
> **Step 4: Validate the Daily Status Checks**
>
> For every applicable working day:

- Locate the relevant work note, comment, status note, or activity entry.

- Verify that the update was documented on the applicable date.

- Confirm that the update contains meaningful ticket-status information.

- Exclude a missing update only when the date is a confirmed weekly off or non-working day.

- Identify every applicable working day for which a required update is missing.

> **Step 5: Validate the Closure Notes**
>
> Compare the closure notes with the applicable KB template and examples.
>
> Verify that all mandatory sections contain relevant and meaningful information. Template headings without supporting details must not be considered complete documentation.
>
> **Step 6: Review All Available CSV Evidence**
>
> The ticket information will be provided in CSV format, and attachments may not be included.
>
> The agent must search all relevant CSV fields, including:

- Request Description.

- Work Notes.

- Resolution Notes.

- Closure Notes.

- Activity Logs.

- Comments.

- Doer and Checker fields.

- Status fields.

- Assignment group or team fields.

- Creation timestamp.

- Completion timestamp.

- Closure timestamp.

- Closed-by field.

- Customer or requester communications.

- Any other exported ticket fields.

> A template or status update may appear within a larger work note, comment, activity entry, or closure note. It does not need to be in a separate field unless the KB specifically requires a dedicated field.
>
> The absence of attachments must not automatically result in **NO** if the required information is documented in the available CSV fields.
>
> However, if a required applicable template cannot be located or validated anywhere in the available CSV data, the agent must not assume that it exists outside the dataset. Select **NO** and clearly identify what could not be validated.
>
> **Step 7: Apply the Final Result**

- Select **YES** when all required applicable templates are present, complete, meaningful, and correctly followed.

- Select **NO** when any required applicable template is missing, incomplete, incorrectly documented, or cannot be validated.

- Select **NA** only when the ticket was closed by the requester and the source rule permits **NA**.

- Do not select **NO** because Doer-Checker documentation is absent when Doer-Checker is not applicable.

- Do not select **NO** because status-check documentation is absent when the ticket was completed in less than 24 hours.

- Do not select **NO** for a missing status update on the responsible team’s confirmed weekly off.

- Do not select **NA** only because Doer-Checker or the status-check template is not applicable.

> The final result must be based only on the actual ticket evidence available in the CSV. KB templates and examples are reference material and must never be treated as evidence for the ticket.

##################### Control 4 — Pre/Post Doer-Checker Notes 

> **Question: Were Pre-Doer, Pre-Checker, Post-Doer and Post-Checker notes documented according to the standard template?**
>
> **Review:**

- Request description and Service Request details.

- Pre-Doer notes.

- Pre-Checker notes.

- Post-Doer notes.

- Post-Checker notes.

- Doer-Checker fields.

- Work notes.

- Activity logs and comments.

- Implementation and validation records.

- Configuration Item (CI) details.

- Timestamps and user or account details.

- Doer-Checker requirements, rules, and template examples provided in the KB.

- Any other available CSV fields containing Doer-Checker evidence.

> The agent must first determine whether Doer-Checker is applicable. If it is applicable, the agent must validate all four required stages separately and confirm that they were documented in the correct sequence.
>
>  
>
> **YES**
>
> All required notes are present and correctly documented.
>
> Select **YES** only when:

- Doer-Checker is applicable.

- Pre-Doer documentation is present and complete.

- Pre-Checker documentation is present and complete.

- Post-Doer documentation is present and complete.

- Post-Checker documentation is present and complete.

- The four stages follow the required sequence.

- Each stage relates to the same activity or implementation.

- The applicable CI is clearly identified and consistent across the stages.

- Each stage contains meaningful evidence relevant to that stage.

- The Doer and Checker responsibilities are distinguishable from the available evidence.

- Role separation meets the applicable KB or policy requirement.

- The documentation follows the applicable templates and requirements provided in the KB.

> **Remark:** Must identify:

- Why Doer-Checker was applicable.

- Where each of the four stages was documented.

- The timestamp of each stage.

- The Doer and Checker identities or accounts, when available.

- The applicable CI or CIs.

- Confirmation that the stages followed the required sequence.

- Confirmation that all four stages were complete and related to the same activity.

>  
>
> **NO**
>
> One or more required notes are missing, incomplete, incorrectly documented, or out of sequence when Doer-Checker is applicable.
>
> Select **NO** when Doer-Checker is applicable and one or more of the following conditions exist:

- Pre-Doer documentation is missing or incomplete.

- Pre-Checker documentation is missing or incomplete.

- Post-Doer documentation is missing or incomplete.

- Post-Checker documentation is missing or incomplete.

- The required stages are not documented in the correct sequence.

- A Checker activity was documented before its related Doer activity.

- A Post-Doer activity was completed before Pre-Checker validation.

- One stage is being used as evidence for another stage.

- A later comment is being used to prove that an earlier stage occurred.

- One or more stage timestamps are missing and the sequence cannot be established.

- The stage label or purpose cannot be identified.

- The applicable CI is missing, unclear, or inconsistent.

- Different CIs were used without an explanation of their relationship.

- The notes contain only generic statements without meaningful stage-specific evidence.

- The four stages do not relate to the same activity or implementation.

- The same person performed both Doer and Checker roles when the applicable policy requires different persons.

- The documentation does not meet the applicable KB template requirements.

- Doer-Checker applicability is established, but the available CSV data is insufficient to validate all mandatory stages.

> Do not select **NA** because one or more required stages are missing after Doer-Checker applicability has been established. Missing or incomplete applicable stages must result in **NO**.
>
> **Remark:** Must identify:

- Why Doer-Checker was applicable.

- The specific stage or stages that were missing, incomplete, incorrect, or out of sequence.

- The available timestamps and identities.

- The applicable CI or CI inconsistency.

- The relevant KB requirement used for comparison.

- Why the available documentation did not meet the requirement.

>  
>
> **NA**
>
> Only when Doer-Checker is genuinely not applicable.
>
> Select **NA** only when both of the following conditions are satisfied:

- No Doer-Checker activity or evidence exists in the ticket; and

- No field, work note, comment, process indicator, ticket type, KB rule, or other ticket information indicates that Doer-Checker was required.

> The agent must not select **NA** when any Doer-Checker applicability evidence exists.
>
> The agent must not select **NA** merely because:

- One or more required stages are missing.

- Only one Doer-Checker stage is documented.

- The Doer-Checker documentation is incomplete.

- The sequence cannot be established.

- The CI is missing or inconsistent.

- Doer or Checker identity details are unavailable.

- The same person appears to have performed both roles.

- The CSV contains limited information.

- Attachments are unavailable.

- The ticket contains a Doer-Checker field that is blank.

- The process was started but not completed.

> If applicability is established and the required evidence is missing or insufficient, select **NO**.
>
> **Remark:** Must state:

- That no Doer-Checker activity was identified.

- That no Doer-Checker requirement was identified.

- That no field, work note, comment, process indicator, ticket type, or KB rule established applicability.

- Why Doer-Checker was considered genuinely not applicable.

>  
>
> **Doer-Checker Definition**
>
> Doer-Checker is a segregation-of-duties process in which:

- The **Doer** performs or prepares the activity.

- The **Checker** independently reviews, verifies, or validates the activity.

> The process contains four mandatory stages when Doer-Checker is applicable:

- Pre-Doer.

- Pre-Checker.

- Post-Doer.

- Post-Checker.

>  
>
> **Doer-Checker Applicability**
>
> Doer-Checker applicability is established when the ticket contains any of the following:

- Pre-Doer activity.

- Pre-Checker activity.

- Post-Doer activity.

- Post-Checker activity.

- A Doer-Checker field showing that the process applies.

- Doer-Checker comments.

- A documented requirement for Doer-Checker.

- Evidence that the Doer-Checker process was started.

- Evidence that the Doer-Checker process was completed.

- A ticket type, activity type, process rule, SOP, SOW, or KB requirement stating that Doer-Checker is required.

- A work note or comment identifying a person as Doer or Checker.

- Any equivalent evidence showing that an independent checking process was required or performed.

> The presence of even one Doer-Checker stage or process indicator requires the agent to evaluate the remaining mandatory stages.
>
> A partially completed Doer-Checker process does not make the control **NA**. If applicability is established but one or more required stages are missing, incomplete, or incorrect, select **NO**.
>
> A blank Doer-Checker field alone does not establish applicability. The agent must review all other available ticket information and applicable KB rules before determining the result.
>
>  
>
> **Mandatory Sequence**
>
> When Doer-Checker is applicable, the required sequence is:

- **Pre-Doer**

- **Pre-Checker**

- **Post-Doer**

- **Post-Checker**

> The agent must use the documented timestamps and activity sequence to verify the order.
>
> The required sequence means:

- Pre-Doer must occur before Pre-Checker.

- Pre-Checker must occur before Post-Doer or implementation.

- Post-Doer must occur before Post-Checker.

- Post-Checker must be the final independent validation of the completed activity.

> A later stage cannot be used to prove that an earlier stage occurred.
>
> For example:

- A Post-Checker note stating that the plan was reviewed does not prove that Pre-Checker validation occurred before implementation.

- A closure note stating that all checks were completed does not prove each mandatory stage unless the individual stages and their sequence can be established.

- A later summary containing all four stage names does not prove that the stages occurred at the required times.

> If timestamps are missing and the mandatory sequence cannot be established, select **NO** when Doer-Checker is applicable.
>
>  
>
> **Pre-Doer Requirements**
>
> Pre-Doer must document the planned activity before it is submitted for Pre-Checker review.
>
> The Pre-Doer stage should contain:

- A clear Pre-Doer label or an unambiguous Pre-Doer-specific comment.

- The Doer’s name, account, or identity, when available.

- The date and time of the Pre-Doer activity.

- A description of the planned activity.

- The planned implementation steps.

- The applicable CI or CIs.

- The expected result or objective.

- Meaningful evidence that the implementation plan was prepared.

> Generic statements such as “planned,” “ready,” “done,” or “activity prepared” are insufficient unless the applicable activity, stage, and CI can be clearly identified.
>
>  
>
> **Pre-Checker Requirements**
>
> Pre-Checker must independently review and validate the Pre-Doer plan before implementation begins.
>
> The Pre-Checker stage should contain:

- A clear Pre-Checker label or an unambiguous Pre-Checker-specific comment.

- The Checker’s name, account, or identity, when available.

- The date and time of the Pre-Checker activity.

- Confirmation that the planned activity was reviewed.

- Confirmation that the implementation steps were validated.

- Confirmation that the CI or CI list was checked against the approved scope.

- Confirmation that the planned activity was suitable to proceed.

- Meaningful evidence of independent review before implementation.

> A general approval or statement such as “approved,” “checked,” or “validated” is insufficient unless it can be linked to the Pre-Checker stage, planned activity, and applicable CI.
>
> Customer approval must not automatically be treated as Pre-Checker validation. Pre-Checker is an internal independent technical or process review unless the applicable KB rule states otherwise.
>
>  
>
> **Post-Doer Requirements**
>
> Post-Doer must document the activity actually performed after implementation.
>
> The Post-Doer stage should contain:

- A clear Post-Doer label or an unambiguous Post-Doer-specific comment.

- The Doer’s name, account, or identity, when available.

- The date and time of the performed activity.

- A description of the actions actually completed.

- The implementation start and completion details, when required.

- The CI or CIs on which the activity was performed.

- The implementation result.

- Relevant validation, log, or evidence references when available.

- Meaningful evidence that the activity was completed.

> The Post-Doer documentation must reflect the activity actually performed. It must not only repeat the planned activity from Pre-Doer.
>
> Generic statements such as “completed,” “implemented,” or “done successfully” are insufficient unless the completed activity, stage, and applicable CI can be identified.
>
>  
>
> **Post-Checker Requirements**
>
> Post-Checker must independently review and validate the activity completed by the Doer.
>
> The Post-Checker stage should contain:

- A clear Post-Checker label or an unambiguous Post-Checker-specific comment.

- The Checker’s name, account, or identity, when available.

- The date and time of the Post-Checker validation.

- Confirmation that the completed activity was reviewed.

- Confirmation that the actual implementation was compared with the approved plan.

- Confirmation that the correct CI or CIs were used.

- Confirmation that the implementation result was validated.

- **Reference to supporting validation evidence when available.**

- Meaningful evidence of independent post-implementation review.

> Generic statements such as “checked,” “validated,” “looks good,” or “completed” are insufficient unless the Post-Checker stage, completed activity, and applicable CI can be identified.
>
> Customer confirmation, closure confirmation, or acknowledgment that the activity was completed must not automatically be treated as Post-Checker evidence.
>
>  
>
> **Required Information for Each Stage**
>
> Each applicable stage should contain:

- A clear stage label or an unambiguous stage-specific comment.

- A timestamp.

- The responsible person or account, when available.

- The applicable CI explicitly identified.

- Meaningful evidence that the stage was completed.

- Information relevant to the actual activity being reviewed.

> Exact template wording is not required if the stage and all mandatory information can be clearly identified from the available ticket evidence.
>
> Minor differences in capitalization, spacing, order, or wording must not result in **NO** when the mandatory information is clearly present.
>
> However, the presence of a stage heading alone is not sufficient. The content underneath the heading must provide meaningful and relevant evidence.
>
>  
>
> **Configuration Item Validation**
>
> The agent must validate the CI across all four applicable stages.

- The CI must be clearly identified.

- The CI must be relevant to the requested activity.

- The CI must be consistent with the ticket scope.

- The CI referenced during Pre-Doer and Pre-Checker should match the CI used during Post-Doer and Post-Checker.

- If multiple CIs are involved, the applicable CIs should be documented.

- If different CIs are intentionally used across the stages, the ticket must explain the relationship or reason.

- A minor naming difference may be accepted when the available evidence clearly establishes that it refers to the same CI.

- If the CI cannot be identified or validated when required by the KB template, select **NO**.

> The agent must not invent, assume, or derive a CI that is not documented in the available ticket data.
>
>  
>
> **Doer and Checker Identity Validation**
>
> When identity information is available, the agent must review whether the Doer and Checker roles were performed according to the applicable segregation-of-duties requirement.

- Do not assume that two comments were entered by different people when identity data is unavailable.

- Do not assume role separation based only on the words “Doer” and “Checker.”

- Use the available names, account IDs, email addresses, user fields, or activity-log identities.

- If the applicable policy requires different persons and the same person performed both roles, select **NO**.

- If the KB allows the same person for a specific activity, apply the relevant KB rule.

- If identity information is unavailable but the template does not require identity validation, assess the remaining mandatory evidence.

- If identity information is mandatory and cannot be validated, select **NO** and explain the missing evidence.

>  
>
> **Generic or Insufficient Documentation**
>
> The following terms are insufficient when documented without stage-specific and activity-specific details:

- “Done.”

- “Checked.”

- “Completed.”

- “Validated.”

- “Approved.”

- “Implemented.”

- “Verified.”

- “Looks good.”

- “Successful.”

- “Activity completed.”

> Such terms may be accepted only when the surrounding ticket information clearly establishes:

- The applicable Doer-Checker stage.

- The activity reviewed or performed.

- The applicable CI.

- The responsible role.

- Meaningful evidence of completion or validation.

- The correct position in the mandatory sequence.

>  
>
> **CSV-Based Evidence Review**
>
> Ticket information will be provided in CSV format, and attachments may not be included.
>
> The agent must review all available written content, including:

- Request Description.

- Work Notes.

- Activity Logs.

- Comments.

- Resolution Notes.

- Closure Notes.

- Doer-Checker fields.

- Assignment and user fields.

- CI fields.

- Implementation timestamps.

- Validation timestamps.

- Any other exported ticket fields.

> A Doer-Checker stage may be documented within a larger work note, comment, activity entry, or closure note. It does not need to appear in a separate field unless the KB specifically requires a dedicated field.
>
> The absence of attachments alone must not result in **NO** when sufficient stage evidence is documented in the available CSV fields.
>
> However, a written statement such as “evidence attached” must not be treated as proof of the attachment’s contents when the attachment is unavailable. The agent may use the written statement only for the information it directly establishes.
>
> If the mandatory stage, sequence, CI, or required evidence cannot be validated from the available CSV data, the agent must not assume that it exists outside the dataset.
>
> **  
> ** 
>
> **Reference Doer-Checker Sample**
>
> **PRE DOER**
>
> Doer Name: Ramesh Kumar
>
> Planned Activity: Apply security patch on application server.
>
> Steps: Backup; stop service; apply patch; restart service; health check.
>
> CIs: APP SRV 01, APP SRV 02.
>
> **PRE CHECKER**
>
> Checker Name: Anita Sharma
>
> Planned steps reviewed and validated.
>
> CI list verified against approved scope.
>
> Execution plan aligned with intended objective.
>
> Formal approval to proceed documented.
>
> **POST DOER**
>
> Doer Name: Ramesh Kumar
>
> Execution timestamps and exact steps documented.
>
> CIs executed on are listed.
>
> Patch logs and health-check screenshot attached.  
>  
>
> **POST CHECKER**
>
>  
>
> Checker Name: Anita Sharma
>
> Executed activity and timestamps revalidated.
>
> Execution compared with approved plan.
>
> Validation artifacts attached.  
>  
>
> The samples are templates and examples only. They must never be treated as evidence for an actual ticket.
>
> The agent must evaluate only the information available in the ticket being reviewed.
>
> The actual ticket wording does not need to match the samples exactly. However, all mandatory information required by the applicable KB template must be clearly documented.
>
> **  
>   
> Auditor Guidance**
>
> The agent must perform the review in the following order:
>
> **Step 1: Determine Applicability**
>
> Review all available ticket fields and applicable KB rules.

- If no Doer-Checker activity or requirement exists, select **NA**.

- If any Doer-Checker stage, field, comment, requirement, or process indicator exists, applicability is established.

- Once applicability is established, do not select **NA** because stages are missing.

> **Step 2: Locate All Four Stages**
>
> Search all available CSV fields for:

- Pre-Doer.

- Pre-Checker.

- Post-Doer.

- Post-Checker.

> Do not stop after locating only one stage.
>
> **Step 3: Validate Each Stage Separately**
>
> For each stage, verify:

- Stage label or clearly identifiable stage purpose.

- Timestamp.

- Responsible person or account, when available.

- Applicable CI.

- Meaningful stage-specific evidence.

- Relevance to the actual ticket activity.

> **Step 4: Validate the Sequence**
>
> Confirm that:

- Pre-Doer occurred before Pre-Checker.

- Pre-Checker occurred before Post-Doer or implementation.

- Post-Doer occurred before Post-Checker.

- A later comment is not being used to prove an earlier stage.

- All stages relate to the same activity.

> **Step 5: Validate CI Consistency**
>
> Confirm that the CIs are consistent with the ticket scope and across all applicable stages.
>
> If different CIs were intentionally used, verify that the relationship is explained.
>
> **Step 6: Validate Role Separation**
>
> Use available identity information to determine whether the Doer and Checker requirements were followed.
>
> If the applicable policy requires different persons and the same person performed both roles, select **NO**.
>
> **Step 7: Apply the Final Result**

- Select **YES** when Doer-Checker is applicable and all four stages are present, complete, meaningful, correctly sequenced, and compliant with the applicable KB rules.

- Select **NO** when Doer-Checker is applicable and any required stage is missing, incomplete, incorrect, out of sequence, or cannot be validated.

- Select **NA** only when Doer-Checker is genuinely not applicable and no ticket evidence or KB rule establishes applicability.

##################### Control 5 — Affected CI Documentation 

> **Question: Were affected Configuration Items documented clearly in the CI field and work notes?**
>
> **Review:**

- Configuration Item field.

- Request description.

- Work notes.

- Activity logs and comments.

- Implementation notes.

- Resolution and closure notes.

- Doer-Checker notes, when applicable.

- Affected CI details in any other available CSV field.

- Any note explaining why a CI is not applicable or unavailable.

> The **Configuration Item field is mandatory** and must not be empty unless the ticket assignee clearly documents a valid reason why no CI applies to the request.
>
> A ticket may be associated with one or multiple Configuration Items. The agent must review all available ticket information to identify the affected CI or CIs.  
>   
> The **Configuration Item (CI) field can contain only one CI**. If multiple CIs are affected, the additional CIs must be documented separately in the **Request Description, Work Notes, or an attachment**. The ticket must clearly identify all affected CIs and, when an attachment is used, the Work Notes or Description must reference the attached CI list.
>
>  
>
> **YES**
>
> The affected CI is documented and identifiable.
>
> Select **YES** only when:

- The Configuration Item field is completed.

- The affected CI is clearly identifiable.

- The CI is relevant to the activity performed.

- The CI documented in the CI field is consistent with the CI mentioned in the work notes.

- If multiple CIs were affected, all relevant CIs are documented.

- The CI details are sufficiently clear to identify the affected system, server, application, database, device, service, or other managed item.

- Minor naming differences do not create uncertainty about the identity of the CI.

> Examples of identifiable CI information may include:

- Server name.

- Hostname.

- Application name.

- Database name.

- Device name.

- Service name.

- Cloud resource name.

- Asset or CI identification number.

- Another unique identifier that clearly identifies the affected CI.

> **Remark:** Must identify:

- The affected CI or CIs.

- Where the CI information was documented.

- Whether the CI field and work notes were consistent.

- Confirmation that the CI information was clear and relevant to the activity.

>  
>
> **NO**
>
> The CI is missing, incorrect, vague, or inconsistent.
>
> Select **NO** when one or more of the following conditions apply:

- The Configuration Item field is empty.

- The CI is missing without a documented justification.

- A CI is mentioned in the work notes, but the mandatory CI field is empty.

- The CI field contains incomplete or vague information.

- The CI cannot be clearly identified.

- The documented CI is unrelated to the requested or completed activity.

- The CI field and work notes refer to different CIs without explanation.

- Multiple CIs were affected, but one or more affected CIs were not documented.

- Different CIs are mentioned across the ticket, but their relationship is not explained.

- The ticket contains only generic terms such as “server,” “database,” “application,” “device,” or “service” without enough information to identify the affected CI.

- The CI field contains placeholder information such as “NA,” “N/A,” “None,” “Unknown,” “Not Available,” or “TBD” without a valid explanation from the ticket assignee.

- The ticket assignee does not explain why a CI cannot be provided or why a CI is not applicable.

- The agent cannot validate the CI from the available CSV data.

> A missing or empty CI field must result in **NO** unless the ticket assignee has clearly documented that no CI applies and has provided a valid justification.
>
> **Remark:** Must identify:

- Whether the CI field was empty, vague, incorrect, or inconsistent.

- The CI information found in the work notes or other ticket fields, if any.

- The specific inconsistency or missing information.

- Whether multiple CIs were involved.

- Why the CI could not be clearly validated.

>  
>
> **NA**
>
> Only when CI is genuinely not applicable.
>
> Select **NA** only when the ticket assignee clearly documents that:

- No Configuration Item applies to the request; or

- The request does not involve any identifiable CI; or

- No CI is available or appropriate for the activity, and a valid justification is provided.

> Acceptable evidence may include a clear statement such as:

- “CI is not applicable because this request does not involve a managed Configuration Item.”

- “No CI is associated with this request.”

- “No applicable CI is available for this activity.”

- “This is an information-only request and no system, service, application, device, or other CI is affected.”

- Any equivalent statement that clearly explains why CI is not applicable.

> The agent must validate the reason against the request details and activity performed. The presence of the words “NA,” “N/A,” “None,” or “Not Applicable” alone is not sufficient unless a valid explanation is provided.
>
> The agent must not select **NA** merely because:

- The CI field is empty.

- The CI is missing from the CSV.

- The CI cannot be identified.

- The work notes do not mention a CI.

- The assignee forgot to complete the CI field.

- The available documentation is incomplete.

- The agent cannot validate the CI.

- A generic value such as “NA” or “None” is entered without justification.

> If the CI field is empty and no valid non-applicability justification is documented, select **NO**.
>
> **Remark:** Must identify:

- The assignee’s statement that CI is not applicable or unavailable.

- The documented reason or justification.

- Where the justification was found.

- Confirmation that the justification is consistent with the request and activity.

>  
>
> **Configuration Item Requirements**
>
> The Configuration Item field is mandatory.
>
> The agent must verify that:

- The CI field is not empty.

- The CI is clearly identifiable.

- The CI relates to the requested and completed activity.

- The CI field is consistent with the request description and work notes.

- All affected CIs are documented when multiple CIs are involved.

- Any difference between CIs mentioned in different ticket fields is explained.

- A valid justification is documented when no CI applies.

> The agent must not assume that a missing CI is not applicable. Non-applicability must be explicitly documented and justified by the ticket assignee.
>
>  
>
> **Multiple Configuration Items**
>
> A ticket may involve more than one CI.
>
> When multiple CIs are involved, the agent must verify that:

- All affected CIs are documented.

- The CIs are relevant to the activity.

- The work notes clearly identify which activity was performed on each CI, where required.

- The CI field contains all affected CIs or clearly references where the complete CI list is documented.

- Any difference between the planned CI and the actual affected CI is explained.

- The CI details are consistent across the request description, work notes, implementation notes, and closure notes.

> If only one CI is documented but the ticket evidence shows that multiple CIs were affected, select **NO** unless the remaining CIs are clearly documented in another accepted CI field or location permitted by the KB.
>
>  
>
> **CI Field and Work-Note Consistency**
>
> The CI field and work notes must refer to the same affected CI or CIs.
>
> The agent must check for:

- Matching CI names.

- Matching hostnames.

- Matching server names.

- Matching application names.

- Matching database names.

- Matching device or asset identifiers.

- Matching service names.

- Other unique CI identifiers.

> Minor differences in capitalization, spacing, abbreviations, or naming format may be accepted if the available evidence clearly shows that they refer to the same CI.
>
> For example, the following may refer to the same CI if supported by the ticket context:
>
> Plain Text
>
>  
>
> APP-SRV-01
>
> App Server 01
>
> app-srv-01
>
> However, the agent must select **NO** when the CI field and work notes identify different CIs and the ticket does not explain the relationship.
>
>  
>
> **Vague or Insufficient CI Information**
>
> Generic terms alone must not be considered sufficient CI documentation.
>
> Examples of vague CI information include:

- “Server.”

- “Production server.”

- “Database.”

- “Application.”

- “Network device.”

- “User machine.”

- “Customer system.”

- “Service.”

- “Multiple servers.”

- “All devices.”

- “NA.”

- “None.”

- “Unknown.”

- “TBD.”

> Such information may be accepted only when the surrounding ticket documentation provides enough additional details to identify the affected CI clearly.
>
> The agent must not invent or assume a CI from the ticket activity when it is not documented.
>
>  
>
> **CSV-Based Evidence Review**
>
> Ticket information will be provided in CSV format, and attachments may not be available.
>
> The agent must review all available ticket fields, including:

- Configuration Item.

- Affected CI.

- Request Description.

- Work Notes.

- Activity Logs.

- Comments.

- Implementation Notes.

- Resolution Notes.

- Closure Notes.

- Doer-Checker Notes.

- Assignment details.

- Any other exported field containing CI information.

> The absence of an attachment must not automatically result in **NO** if the CI is clearly documented in the available CSV fields.
>
> If the CI field is not included in the CSV export, the agent must review all other available fields for CI information. However, if the control requires the CI to be documented in the mandatory CI field and that field cannot be validated, select **NO** unless a valid non-applicability justification is documented.
>
> The agent must use only the available ticket evidence and must not invent, estimate, or assume the affected CI.
>
>  
>
> **Auditor Guidance**
>
> The agent must perform the review in the following order:
>
> **Step 1: Review the Mandatory CI Field**
>
> Check whether the Configuration Item field contains a value.

- If the field contains an identifiable CI, continue the validation.

- If the field is empty, check for a documented non-applicability justification.

- If the field is empty and no valid justification exists, select **NO**.

- Do not select **NA** solely because the CI field is empty.

> **Step 2: Review the Work Notes**
>
> Search the work notes and other available ticket fields for:

- CI name.

- Hostname.

- Server name.

- Application name.

- Database name.

- Device name.

- Service name.

- Asset or CI identification number.

- Any other information identifying the affected CI.

> **Step 3: Compare the CI Information**
>
> Compare the CI field with the request description, work notes, implementation notes, and closure notes.
>
> Confirm that:

- The same CI or CIs are referenced.

- The CI relates to the requested activity.

- The CI relates to the completed activity.

- Any differences are explained.

- All affected CIs are documented.

> **Step 4: Validate Non-Applicability**
>
> If the ticket assignee states that no CI applies, verify that:

- The statement is clearly documented.

- A valid reason is provided.

- The reason is consistent with the request.

- The ticket does not contain evidence of an affected server, application, database, device, service, or other CI.

> If the ticket contains evidence of an affected CI, do not select **NA**, even if another field contains “NA” or “Not Applicable.”
>
> **Step 5: Apply the Final Result**

- Select **YES** when the affected CI or CIs are clearly documented, identifiable, relevant, and consistent.

- Select **NO** when the mandatory CI field is empty without valid justification.

- Select **NO** when the CI is missing, incorrect, vague, incomplete, or inconsistent.

- Select **NO** when multiple affected CIs are not fully documented.

- Select **NA** only when the ticket assignee clearly states that no CI applies or is available and provides a valid justification consistent with the ticket activity.

##################### Control 6 — CI Consistency 

> **Question: Were CIs in Pre-Doer, Pre-Checker, Post-Doer and Post-Checker consistent with each other and the approved CI list?**
>
> **Review:**

- Approved CI list.

- CI field.

- Request description.

- Pre-Doer notes.

- Pre-Checker notes.

- Post-Doer notes.

- Post-Checker notes.

- Work notes and comments.

- Activity and implementation logs.

- Resolution and closure notes.

- Attached or referenced CI list.

- Any other available CSV fields containing CI information.

> The agent must first determine whether Doer-Checker is applicable. If Doer-Checker is applicable, the agent must compare the CI references across all four Doer-Checker stages with the approved CI list and the ticket’s CI information.
>
>  
>
> **YES**
>
> All applicable CI references match.
>
> Select **YES** when:

- The CIs documented in Pre-Doer, Pre-Checker, Post-Doer, and Post-Checker are consistent with each other.

- The CIs documented in all four stages match the approved CI list.

- The CIs are consistent with the CI field, request description, and work notes.

- All affected CIs are clearly identifiable.

- Any minor naming differences clearly refer to the same CI.

- When multiple CIs are involved and it is not practical to list every CI in each Doer-Checker stage:

  - A complete CI list is documented or referenced;

  - The same CI list applies to all four Doer-Checker stages;

  - Each stage clearly refers to the approved CI list;

  - The location of the complete CI list is documented in the work notes or comments; and

  - The available CSV data contains enough written information to identify or validate the referenced CI list.

- Any intentional addition, removal, replacement, or change to the approved CI list is documented and properly explained before the affected activity was performed.

> **Remark:** Must identify:

- The CI or CIs reviewed.

- The approved CI list used for comparison.

- Where the approved CI list was documented or referenced.

- Whether all four Doer-Checker stages contained matching CI references or referred to the same approved list.

- Confirmation that the CI information was consistent across the ticket and Doer-Checker records.

>  
>
> **NO**
>
> Conflicting, missing, or mismatched CI references exist.
>
> Select **NO** when Doer-Checker is applicable and one or more of the following conditions exist:

- A CI reference is missing from an applicable Doer-Checker stage.

- The CIs in Pre-Doer do not match the CIs in Pre-Checker.

- The CIs in Pre-Checker do not match the CIs in Post-Doer.

- The CIs in Post-Doer do not match the CIs in Post-Checker.

- The CIs documented in the Doer-Checker stages do not match the approved CI list.

- The CI field, request description, work notes, and Doer-Checker records contain conflicting CI information.

- A CI was added, removed, replaced, or changed without a documented explanation.

- One or more affected CIs cannot be identified.

- Multiple CIs were involved, but the complete CI list is neither documented nor referenced.

- A Doer-Checker note states “as per CI list,” “all listed CIs,” “multiple CIs,” or similar wording, but:

  - The CI list cannot be located;

  - The location of the list is not documented in the work notes or comments;

  - The reference does not clearly identify which CI list applies; or

  - The available CSV data does not allow the agent to validate the CI list.

- A CI list is mentioned as attached, but no corresponding CI details or usable reference are available in the CSV.

- Different CI lists are referenced across the four stages without an explanation.

- Generic terms such as “server,” “application,” “database,” “all devices,” or “multiple CIs” are used without enough details or a valid reference to identify the affected CIs.

- The agent cannot establish that the same approved CI scope was used throughout the Doer-Checker process.

> **Remark:** Must identify:

- The specific missing, conflicting, or mismatched CI reference.

- The Doer-Checker stage or ticket field containing the issue.

- The approved CI list used for comparison, when available.

- Any CI that was added, removed, changed, or not validated.

- Whether a complete CI list or its location was missing from the work notes.

- Why CI consistency could not be established.

>  
>
> **NA**
>
> Only when Doer-Checker is not applicable.
>
> Select **NA** only when:

- No Doer-Checker activity exists; and

- No Doer-Checker field, work note, comment, process indicator, ticket type, SOP, SOW, or KB rule indicates that Doer-Checker was required.

> The agent must not select **NA** merely because:

- CI information is missing.

- One or more Doer-Checker stages are missing.

- The CI list is unavailable.

- The CI references are inconsistent.

- Multiple CIs were involved.

- The complete CI list was mentioned but cannot be located.

- Attachments are unavailable.

- The available CSV data is insufficient to validate CI consistency.

> If Doer-Checker is applicable but the CI information is missing, incomplete, conflicting, or cannot be validated, select **NO**.
>
> **Remark:** Must state:

- That Doer-Checker was not applicable.

- That no Doer-Checker activity or requirement was identified.

- Where the agent checked for Doer-Checker applicability.

>  
>
> **Approved CI List Requirements**
>
> The approved CI list is the final documented list of Configuration Items authorized for the activity.
>
> The approved CI list may be documented in:

- The CI field.

- Request description.

- Work notes.

- Customer-approved scope.

- Pre-Doer notes.

- Pre-Checker notes.

- An attached CI list.

- A clearly identified and referenced ticket record.

- Another approved CSV field containing the CI scope.

> The agent must identify the final approved CI list before comparing the CI references.
>
> If an earlier CI list was corrected, updated, expanded, reduced, or replaced, the agent must use the latest valid approved CI list.
>
> Do not use an older list when the ticket clearly states:

- “Ignore the previous CI list.”

- “Use the revised CI list.”

- “The previous CI details were incorrect.”

- “Please consider the updated scope.”

- “The following CIs replace the earlier list.”

- Any equivalent statement indicating that an earlier CI list is no longer valid.

>  
>
> **Multiple CI Requirements**
>
> A ticket may contain multiple affected CIs.
>
> When multiple CIs are involved, it may not be practical to repeat every CI name in all four Doer-Checker notes. In such cases, the following requirements must be met:

- A complete CI list must exist.

- The list must clearly relate to the ticket and approved activity.

- The list must be documented in the ticket or available as a clearly identified attachment or record.

- The work notes or comments must state where the complete CI list is available.

- Each Doer-Checker stage must clearly refer to the same complete approved CI list.

- The reference must be specific enough to identify the list being used.

- The Pre-Checker must validate the CI list before implementation.

- The Post-Doer must confirm that the activity was performed on the approved CIs.

- The Post-Checker must confirm that the implemented CIs were validated against the approved list.

- Any CI excluded from, added to, or changed from the approved list must be documented and explained.

> Acceptable references may include:

- “CIs are as per the approved CI list documented in work note dated \[date/time\].”

- “Pre-Checker validated all CIs listed in the approved implementation scope.”

- “Activity completed on all CIs listed in the referenced CI record.”

- “Post-Checker compared the implemented CIs with the approved CI list.”

> Generic statements such as “all CIs,” “multiple CIs,” or “as discussed” are insufficient if the complete CI list or its location cannot be identified.
>
>  
>
> **Attachment and CSV Requirements**
>
> The ticket data will be provided in CSV format, and attachments may not be included.
>
> If a complete CI list is contained in an attachment that is unavailable in the CSV, the agent must review the work notes and comments for:

- The attachment or CI list name.

- The location or reference of the CI list.

- A written statement that the list contains the approved CIs.

- Evidence that the same list was reviewed during Pre-Checker.

- Evidence that the implemented CIs were compared with the same list during Post-Checker.

> A comment stating only “CI list attached” is not sufficient when the unavailable attachment is the only source containing the affected CI details.
>
> The agent must not invent or assume the contents of an unavailable attachment.
>
> When the attachment is unavailable, sufficient written evidence must remain in the CSV to identify the referenced list and establish that the same approved CI scope was used throughout the Doer-Checker process.
>
> If the CI list cannot be identified or validated from the available CSV evidence, select **NO**.
>
>  
>
> **CI Matching Rules**
>
> The CI references do not need to use identical capitalization, spacing, abbreviations, or formatting if the available evidence clearly establishes that they refer to the same CI.
>
> For example, the following may be treated as the same CI when supported by the ticket context:
>
> Plain Text
>
>  
>
> APP-SRV-01
>
> App Server 01
>
> app-srv-01
>
> The agent must not treat CI references as matching when:

- The identifiers are materially different.

- Different servers, applications, databases, devices, or services are named.

- A generic CI description cannot be connected to the approved CI.

- The relationship between different CI names is not explained.

- One stage refers to an individual CI while another refers to an unidentified group.

- One or more approved CIs are missing from the implemented or validated scope.

>  
>
> **Auditor Guidance**
>
> **Step 1: Determine Doer-Checker Applicability**

- If Doer-Checker is not applicable, select **NA**.

- If Doer-Checker is applicable, continue the CI-consistency review.

- Do not select **NA** because CI evidence is missing after Doer-Checker applicability has been established.

> **Step 2: Identify the Final Approved CI List**
>
> Review the CI field, request description, work notes, comments, approval records, and any referenced CI list.
>
> If multiple versions exist, use the latest valid approved version and ignore earlier lists that were clearly cancelled, corrected, or replaced.
>
> **Step 3: Review All Four Doer-Checker Stages**
>
> Check the CI references in:

- Pre-Doer.

- Pre-Checker.

- Post-Doer.

- Post-Checker.

> Do not stop after finding matching CI information in only one or two stages.
>
> **Step 4: Validate Multiple-CI References**
>
> When all CIs are not repeated in every stage, confirm that:

- A complete approved CI list exists.

- The list or its location is documented in the work notes or comments.

- All four stages refer to the same list.

- Pre-Checker validated the list.

- Post-Doer confirmed implementation against the list.

- Post-Checker validated the completed activity against the list.

> **Step 5: Compare the CI Information**
>
> Compare:

- The approved CI list.

- The mandatory CI field.

- Request description.

- Pre-Doer notes.

- Pre-Checker notes.

- Post-Doer notes.

- Post-Checker notes.

- Work notes and comments.

- Implementation and resolution records.

> Confirm that the same CI scope was planned, checked, implemented, and validated.
>
> **Step 6: Apply the Final Result**

- Select **YES** when all applicable CI references match the approved CI list or clearly refer to the same complete approved CI list.

- Select **NO** when CI references are missing, conflicting, mismatched, vague, or cannot be validated.

- Select **NO** when multiple CIs are involved but no complete CI list or identifiable reference is documented.

- Select **NO** when an attachment is the only source of the CI list and its contents cannot be validated from the available data.

- Select **NA** only when Doer-Checker is not applicable.

##################### Control 7 — Description and Work Notes Alignment 

> **Question: Were Service Request description and work notes aligned?  
>  **
>
> **Review:**

- Service Request description.

- Work notes.

- CI field, when applicable.

- Activity, resolution, or closure notes available in the CSV.  
   

> **YES:** The work notes accurately relate to the requested activity, and no material mismatch or contradiction exists.
>
> The work notes do not need to repeat every detail from the Service Request description. Attachments are not required. Information from other relevant CSV fields may be considered when validating alignment.  
>  
>
> **Remark:** Identify the requested activity, the documented work, and confirm that they are aligned  
> .
>
> **NO:** The work notes describe a different or unrelated activity, materially contradict the request, contain inaccurate information, or do not provide enough evidence to connect the performed work with the request.
>
> Do not select **NO** only because:

- The work notes are brief.

- All request details are not repeated in the work notes.

- CI information is available in another field.

- Attachments are unavailable.  
   

> **Remark:** Identify the requested activity and clearly explain the specific mismatch, contradiction, or inaccurate information found in the work notes.  
>  
>
> **NA:** Not permitted.  
>  
>
> **Auditor Guidance**
>
> The agent must compare the meaning of the Service Request description with the work notes and verify the following:

- The documented work relates to the requested activity.

- The main activity, purpose, and affected CI are consistent, when applicable.

- The work notes do not contain any material contradiction or inaccurate information.

- Any documented change to the original request is clearly explained.

- Information available in other relevant CSV fields is considered before determining the result.

> Exact wording is not required, and work notes are not expected to contain all request details.

- Select **YES** when the work notes accurately relate to the requested activity and no material contradiction exists.

- Select **NO** when there is a clear mismatch, contradiction, unrelated activity, or inaccurate information.

- If the work notes are brief, review other relevant CSV fields before deciding.

- Do not require attachments.

- Do not select **NA**.

##################### Control 8 — Doer-Checker Four-Step Process 

> **Question: Were the Doer-Checker steps completed and updated within 30 minutes?**
>
> **Required Sequence:** Pre-Doer → Pre-Checker → Post-Doer → Post-Checker.
>
> **Review:**

- Doer-Checker applicability.

- Pre-Doer notes and timestamp.

- Pre-Checker notes and timestamp.

- Post-Doer notes and timestamp.

- Post-Checker notes and timestamp.

- Work notes, comments, and activity logs containing Doer-Checker evidence.

> **YES:** All four applicable stages exist, are correctly sequenced, and the applicable Doer-Checker timing requirement is satisfied:

- Pre-Doer occurred before Pre-Checker.

- Pre-Checker occurred before Post-Doer.

- Post-Doer occurred before Post-Checker.

- The interval from Pre-Doer to Pre-Checker is 30 minutes or less.

- The interval from Post-Doer to Post-Checker is 30 minutes or less.

> **Remark:** Identify the timestamp of each stage and confirm that both Doer-to-Checker intervals were within 30 minutes.
>
> **NO:** Doer-Checker is applicable, but one or more of the following conditions exist:

- Pre-Doer, Pre-Checker, Post-Doer, or Post-Checker is missing.

- The required sequence is incorrect.

- Pre-Doer to Pre-Checker exceeds 30 minutes.

- Post-Doer to Post-Checker exceeds 30 minutes.

- One or more timestamps are missing, unclear, or insufficient to calculate the required intervals.

- Applicable compliance cannot be established from the available ticket data.

> **Remark:** Identify the missing or incorrectly sequenced stage, the available timestamps, and the interval that exceeded 30 minutes or could not be calculated.
>
> **NA:** Only when Doer-Checker is genuinely not applicable.
>
> Do not select **NA** because:

- One or more stages are missing.

- Stage timestamps are missing.

- The sequence cannot be established.

- A Doer-to-Checker interval cannot be calculated.

- The 30-minute requirement was not met.

> If Doer-Checker is applicable but compliance cannot be established, select **NO**.
>
> **Auditor Guidance**

- First determine whether Doer-Checker is applicable using the applicable KB rules.

- If Doer-Checker is not applicable, select **NA**.

- If Doer-Checker is applicable, locate all four stages and their timestamps.

- Validate the sequence as Pre-Doer → Pre-Checker → Post-Doer → Post-Checker.

- Calculate Pre-Doer to Pre-Checker separately.

- Calculate Post-Doer to Post-Checker separately.

- An interval of exactly 30 minutes is compliant.

- An interval greater than 30 minutes is non-compliant.

- Do not calculate one continuous 30-minute interval across all four stages.

- Do not use ticket creation, update, resolution, or closure timestamps unless they are clearly linked to the applicable Doer-Checker stage.

- Do not invent or estimate missing timestamps.

- Select **YES** only when all four stages are present, correctly sequenced, and both required intervals are 30 minutes or less.

- Select **NO** when any stage is missing, the sequence is incorrect, either interval exceeds 30 minutes, or the timing cannot be validated.

- Select **NA** only when Doer-Checker is genuinely not applicable.

>  

##################### Control 9 — Implementation Against Approved Plan 

> **Question: Were implementation steps in Pre-Doer and Post-Doer aligned with the approved/customer-agreed plan?**
>
>  
>
> **Review:**

- Approved or customer-agreed implementation plan.

- Pre-Doer notes.

- Post-Doer notes.

- Work notes and comments.

- Approval or execution document, when available.

- Other relevant CSV fields.

>  
>
> **YES:** The planned steps in Pre-Doer and the completed steps in Post-Doer align with the approved or customer-agreed plan.
>
> The steps do not need to use identical wording. Minor operational differences are acceptable when they do not materially change the approved activity, scope, or affected CIs.
>
> Attachments are not mandatory. If an attachment is unavailable, the agent must use the written information available in the CSV.
>
>  
>
> **Remark:** Identify the approved plan, planned steps, completed steps, and confirm that they align.
>
>  
>
> **NO:** The completed activity materially differs from the approved or customer-agreed plan without a documented and valid justification.
>
> Select **NO** when:

- An approved step was skipped without explanation.

- An unapproved or unrelated step was performed.

- The implementation scope or affected CIs changed without documented justification.

- Pre-Doer or Post-Doer information is insufficient to validate alignment.

- The approved plan cannot be identified when the control is applicable.

> Do not select **NO** only because:

- The wording is different.

- Post-Doer contains a summary rather than repeating every planned step.

- An attachment is unavailable.

- Additional validation or troubleshooting steps were performed without changing the approved scope.

>  
>
> **Remark:** Identify the specific deviation and explain why it did not align with the approved plan.
>
>  
>
> **NA:** Select **NA** only when:

- No implementation activity was required or performed; or

- Doer-Checker was genuinely not applicable under the applicable source rule.

>  
>
> **Auditor Guidance**
>
> Compare the approved or customer-agreed plan with Pre-Doer and Post-Doer documentation.

- Select **YES** when the performed activity materially matches the approved plan.

- Select **YES** when a difference is properly documented and does not result in an unapproved change to the activity, scope, or CIs.

- Select **NO** when a material deviation exists without documented justification.

- Do not require an attachment when sufficient written evidence is available in the CSV.

- Do not assume the contents of an unavailable attachment.

- Select **NA** only when implementation or Doer-Checker is genuinely not applicable.

##################### Control 10 — Pre-Doer and Post-Doer Consistency 

> **Question: Were implementation steps documented in Pre-Doer and Post-Doer matching?**
>
> **Review:**

- Pre-Doer notes.

- Post-Doer notes.

- Work notes and comments.

- Affected CI details.

> **YES:** The activity planned in Pre-Doer aligns with the activity documented as completed in Post-Doer.
>
> The steps do not need to be word-for-word identical. Post-Doer may summarize the completed work if the main activity, scope, and affected CIs remain consistent.
>
> **Remark:** Identify the planned activity, completed activity, and confirm that they are consistent.
>
> **NO:** A material mismatch or inconsistency exists between Pre-Doer and Post-Doer.
>
> Select **NO** when:

- The completed activity differs from the planned activity.

- A planned major step was skipped without explanation.

- An additional activity was performed that materially changed the planned scope.

- The affected CIs are inconsistent without explanation.

- Pre-Doer or Post-Doer documentation is missing or insufficient to establish consistency.

- The documentation contains contradictory information.

> Do not select **NO** only because:

- The wording is different.

- Post-Doer provides a short but meaningful summary.

- Minor execution details are not repeated.

- Additional validation or troubleshooting was performed without changing the planned activity or scope.

- Attachments are unavailable.

> **Remark:** Identify the specific mismatch, missing information, or inconsistency between Pre-Doer and Post-Doer.
>
> **NA:** Select **NA** only when Doer-Checker is not applicable.
>
> If Doer-Checker is not applicable or Doer-Checker documentation is not present, select NA.
>
> **Auditor Guidance**
>
> Compare the meaning of the planned steps in Pre-Doer with the completed steps in Post-Doer.

- Select **YES** when the planned and completed activities materially match.

- Select **YES** when any difference is properly explained and does not materially change the activity, scope, or affected CIs.

- Select **NO** when a material mismatch, contradiction, unexplained deviation, or missing applicable documentation exists.

- Do not expect identical wording or repetition of every step.

- Review other relevant CSV fields when Pre-Doer or Post-Doer contains limited information.

- Do not require attachments.

- Select **NA** only when no implementation activity was applicable, or doer-checker is not applicable.

##################### Control 11 — Implementation Timestamps 

> **Question: Were timestamps captured and documented against each implementation step?**
>
> **Review:**

- Doer-Checker applicability.

- Doer-Checker notes.

- Post-Doer notes.

- Work notes.

- Activity logs.

- Other relevant CSV fields containing implementation timestamps.

> **YES:** Doer-Checker is applicable, and all required implementation actions have timestamps documented either:

- Within the Doer-Checker or Post-Doer notes; or

- In work notes or activity logs entered after implementation, provided the notes clearly identify the implementation steps and their actual execution timestamps.

> The timestamp must show when the implementation step was performed. The date and time when a note was added may be used only when the note clearly represents the actual implementation time.
>
> **Remark:** Identify the implementation steps, their actual timestamps, and where the timestamps were documented.
>
> **NO:** Doer-Checker is applicable, but one or more required implementation timestamps are missing, unclear, or cannot be connected to the relevant implementation steps.
>
> Select **NO** when:

- Required timestamps are missing from the Doer-Checker notes and no later work note provides them.

- A later note states that implementation was completed but does not provide the actual execution time.

- The available timestamp is only the ticket creation, assignment, update, resolution, or closure time and is not clearly linked to implementation.

- The timestamps are contradictory or inconsistent with the implementation sequence.

- The available CSV data is insufficient to validate when the implementation steps were performed.

> **Remark:** Identify the implementation step for which the timestamp was missing, unclear, or inconsistent.
>
> **NA:** Select **NA** when:

- Doer-Checker is genuinely not applicable; or

- No implementation activity was applicable.

> If Doer-Checker is applicable and implementation was performed, missing timestamps must result in **NO**, not **NA**.
>
> **Auditor Guidance**
>
> This control must be checked only when Doer-Checker is applicable.
>
> Implementation timestamps may be documented:

- In the Doer-Checker notes;

- In the Post-Doer notes; or

- After the Doer-Checker or implementation activity in a work note, comment, or activity log.

> A timestamp documented later is acceptable only when it clearly states the actual date and time when the implementation step was performed.
>
> For example:
>
> Plain Text
>
>  s
>
> Post-Doer update entered at 18:00:
>
> Service stopped at 14:05.
>
> Patch installation started at 14:10.
>
> Patch installation completed at 14:45.
>
> Service restarted at 14:50.
>
> Health check completed at 15:00.
>
> The note-entry time of **18:00** is not the implementation timestamp. The documented times from **14:05 to 15:00** are the actual implementation timestamps.
>
> A later comment such as the following is insufficient:
>
> Plain Text
>
>  
>
> Implementation completed successfully.
>
> It does not provide the actual date and time of implementation.

- Select **YES** when all required implementation timestamps are documented with the Doer-Checker evidence or in a later note that clearly records the actual execution times.

- Select **NO** when Doer-Checker is applicable and one or more actual implementation timestamps are missing or cannot be validated.

- Select **NA** only when Doer-Checker or implementation is genuinely not applicable.

- Do not invent or estimate missing timestamps.

- Do not treat ticket system timestamps as implementation timestamps unless they are clearly connected to the implementation activity.

##################### Control 12 — Exception / Deviation Documentation

> **Question: Were exception approvals or reasons documented where the implementation plan was deviated from or steps were not performed?**
>
> **Review:**

- Approved implementation plan.

- Pre-Doer and Post-Doer notes.

- Work notes and comments.

- Exception or deviation approval, when required.

> **YES:** A deviation occurred, and the reason and/or required approval was clearly documented.
>
> **Remark:** Identify the deviation, documented reason, and approval evidence when approval was required.
>
> **NO:** A deviation occurred, but no valid reason or required approval was documented.
>
> **Remark:** Identify the deviation and state what explanation or approval was missing.
>
> **NA:** No deviation occurred, and the implementation followed the approved plan.
>
> **Auditor Guidance:**

- Compare the approved implementation plan with the completed implementation steps.

- A deviation includes a skipped, changed, added, replaced, or partially completed step.

- Select **YES** when a deviation exists and the required reason or approval is documented.

- Select **NO** when a deviation exists without a documented reason or required approval.

- Select **NA** when no deviation occurred.

- Do not treat a minor wording difference as a deviation when the actual activity and scope remained unchanged.

- Do not invent or assume a reason or approval that is not documented.

##################### Control 13 — Timely Customer Communication

> **Question: Were timely updates provided, including prompt responses to customer requests?  
>   
> Mandatory Communication Frequency Rule: Customer communication should be provided daily where appropriate or at a meaningful and reasonable frequency based on the ticket duration; for example, if a ticket remains open for 10 days, at least 4 to 6 meaningful customer updates should be documented. Generic, automated, or repeated updates without relevant progress must not be counted**
>
> **YES:** Ticket communications demonstrate timely and appropriate customer updates.
>
> Communication may be documented through:

- Ticket comments.

- Work notes.

- Email.

- Microsoft Teams.

- Phone calls.

- Any other documented communication channel.

> A note stating that the assignee reached out to the user, client, or customer through Teams, email, or a call may be accepted when it clearly relates to the request.
>
> **Remark:** Identify the communication method, date, and evidence of timely communication.
>
> **NO:** Communication gaps or delayed responses are identified.
>
> Select **NO** when:

- A customer question or request was not answered promptly.

- Required communication was delayed.

- No meaningful customer communication was documented.

- The ticket states that communication occurred but does not provide enough information to relate it to the request.

> **Remark:** Identify the delayed or missing communication and the related customer request.
>
> **NA:** Not permitted.
>
> **Reference Status Check Template**
>
> Issue/Request:
>
> Same as short description or exact issue elaboration.
>
>  
>
> Business Impact & Impacted User Count:
>
> Document the business impact and number of impacted users.
>
>  
>
> Action Taken:
>
> Document the actions taken so far.
>
>  
>
> Next Actions:
>
> Document the planned next steps.
>
>  
>
> Doer & Checker:
>
> If N/A, state the reason, such as a non-production environment.
>
>  
>
> Artifacts Attached:
>
> Mention supporting artifacts, such as a snapshot, when available.
>
> The template is a reference example, not ticket evidence.
>
> **Auditor Guidance**

- Review all available ticket communications and relevant CSV fields.

- Accept customer communication documented through ticket comments, work notes, email, Teams, calls, or other recorded communication channels.

- A written note stating that the assignee contacted the user, client, or customer may be accepted when it identifies the communication method and relates to the request.

- Verify whether customer questions and requests received a timely response.

- Do not require attachments when sufficient communication evidence is documented in the available CSV fields.

- Do not treat the reference template as evidence for the actual ticket.

- Select **YES** when the available evidence demonstrates timely and appropriate customer communication.

- Select **NO** when a communication gap or delayed response is identified.

- Do not select **NA**.

##################### Control 14 — 24-Hour Ticket Updates 

> **Question: Was the ticket updated every 24 hours?**
>
> **YES:** A meaningful status check was documented on every applicable working day while the ticket remained open.
>
> **NO:** A meaningful status check was missing on one or more applicable working days.
>
> **NA:** Not permitted.
>
> **Review**

- Ticket Opened Date/Time.

- Resolved Date/Time.

- Closed Date/Time.

- Work Notes.

- Additional Comments.

- Customer-visible updates.

- Status-check updates.

- Assigned team.

- Assigned team’s weekly-off schedule provided in the KB.

- Approved holiday calendar, when provided.

> **Status-Check Requirement**
>
> The ticket must contain a meaningful status check on every applicable working day while it remains open.
>
> Compliance must be checked by **calendar date**, not by exact elapsed hours. Any meaningful status check documented between **00:00:00 and 23:59:59** on an applicable working day satisfies the requirement for that date.
>
> If a meaningful status check is missing on even one applicable working day, select **NO**.
>
> **Meaningful Status Check**
>
> A valid status check should contain meaningful information such as:

- Current progress.

- Actions completed.

- Actions pending.

- Current issue or blocker.

- Dependency on the customer or another team.

- Next action.

- Expected completion, when available.

> The status check may be documented in:

- Work Notes.

- Additional Comments.

- Customer-visible updates.

- Any other status field containing meaningful progress.

> **Do Not Count**
>
> Do not count the following as a valid status check:

- Empty updates.

- System-generated field changes.

- Assignment changes.

- Automated messages without meaningful progress.

- Ticket status changes without an update.

- Generic entries such as “WIP,” “In Progress,” “Pending,” or “Checking” without meaningful details.

> **Evaluation Window**
>
> Start the evaluation from the **Ticket Opened Date/Time**.
>
> End the evaluation at the earliest applicable endpoint:

- Resolved Date/Time.

- Closed Date/Time.

- End of the supplied audit period, when the ticket is still open.

> A status check is not required for the ticket-opening date when the ticket was opened and updated on the same date. Begin checking subsequent applicable working dates until the applicable endpoint.
>
> **Team Weekly-Off Rule**
>
> The agent must use the team-specific weekly-off list provided in the KB.

- Identify the team responsible for the ticket on each date.

- Exclude only the weekly-off days assigned to that team.

- Do not automatically treat Saturday and Sunday as weekly off for every team.

- For teams whose weekly off is Saturday and Sunday, exclude those days.

- For teams with different weekly-off days, use the schedule provided in the KB.

- If the ticket was transferred between teams, apply the weekly-off schedule of the team responsible for the ticket on each date.

- A missing status check on a confirmed weekly-off day must not result in **NO**.

- If the team or its weekly-off schedule cannot be identified, do not assume a weekly off. Mention the missing information in the remark.

> **Holiday Rule**

- Exclude a public or national holiday only when it appears in the approved holiday calendar supplied in the KB.

- Do not assume or independently identify holidays.

- If no approved holiday calendar is provided, do not exclude a date as a holiday.

> **Timezone Rule**

- Use the ticket timezone when available.

- If the timezone is unavailable, use the timestamps exactly as provided in the CSV.

- Mention the unavailable timezone in the remark when it affects the evaluation.

> **Work cycle**

- For teams or audit tracks operating **24x7**, every calendar day is considered a working day. A meaningful status update must be documented on the ticket every day, including Saturdays, Sundays, and holidays. No weekly-off or holiday exclusion applies unless a specific exception is documented in the KB. If a meaningful status update is missing on any calendar day while the ticket remains open, select **NO**.

- 

> **YES Remark**
>
> Identify:

- Evaluation start and end dates.

- Assigned team.

- Weekly-off days excluded.

- Holidays excluded, when applicable.

- Confirmation that a meaningful status check was present on every applicable working day.

> **NO Remark**
>
> Identify:

- Evaluation start and end dates.

- Assigned team.

- Applicable working date or dates for which the status check was missing.

- Previous meaningful status-check timestamp, when available.

- Next meaningful status-check timestamp, when available.

- Weekly-off days and approved holidays excluded from the review.

- Missing timestamp or team-schedule information, when applicable.

> **Auditor Guidance**

- Identify the evaluation window.

- Identify the team responsible for the ticket.

- Apply that team’s weekly-off schedule from the KB.

- Exclude approved holidays only when a holiday calendar is provided.

- List every applicable working date within the evaluation window.

- Check for at least one meaningful status update on each applicable working date.

- Do not count system updates, assignment changes, empty entries, or generic updates.

- Select **YES** only when every applicable working date contains a meaningful status check.

- Select **NO** if even one applicable working date is missing a meaningful status check.

- Do not select **NA**.

##################### Control 15 — Backup Evidence 

> **Question: Was backup performed before implementing configuration changes, with evidence attached?**
>
> **Review:**

- Request description.

- Planned activity.

- Configuration-change or upgrade details.

- Pre-Doer and Post-Doer notes, when applicable.

- Work notes and comments.

- Backup requirement, details, and timestamps.

- Supporting evidence or attachment references.

- Other relevant CSV fields.

> **YES:** Backup was required for the upgrade or configuration change, was completed before implementation, and supporting evidence is available.
>
> Supporting evidence may include:

- Backup logs or job details.

- Backup reference or job number.

- Backup completion timestamp and result.

- Screenshot or attachment reference.

- Work note confirming successful backup.

- Any equivalent evidence showing that the backup was successfully completed before implementation.

> **Remark:** Identify why the backup was required, when it was completed, and the supporting evidence available.
>
> **NO:** Backup was required for the upgrade or configuration change, but:

- It was not performed.

- It was performed after implementation.

- It was unsuccessful.

- Its completion could not be verified.

- Supporting evidence was unavailable or insufficient.

> **Remark:** Identify where the backup requirement was stated and explain what backup or evidence was missing, late, unsuccessful, or insufficient.
>
> **NA:** Backup was not required, or the ticket does not mention any backup requirement or activity.
>
> Backup is not required for every Service Request. The agent must check for backup only when:

- The activity involves an upgrade.

- The activity involves a configuration change where backup is required.

- The ticket, requester, customer, implementation plan, SOP, SOW, process document, or work note specifically asks for a backup.

- The documented activity requires a backup before implementation.

> **Remark:** State that no backup requirement or backup activity was identified in the available ticket information.
>
> **Auditor Guidance**

- Do not expect backup evidence for every Service Request.

- First determine whether the ticket involves an upgrade or configuration change.

- If it does, check whether a backup was specifically required or requested.

- Do not assume that every upgrade or configuration change automatically requires a backup.

- Backup must be checked when the requirement is mentioned in the ticket, request, implementation plan, SOP, SOW, process document, or other available evidence.

- If backup was required, verify that it was completed successfully before implementation.

- Written backup evidence in the CSV may be accepted when it clearly identifies the backup result and confirms that it was completed before implementation.

- A statement such as “backup attached” is insufficient when the attachment is unavailable and no backup result, reference, or timestamp is documented.

- Do not assume the contents of an unavailable attachment.

- Select **YES** when backup was required, successfully completed before implementation, and supported by valid evidence.

- Select **NO** when backup was required but was missing, late, unsuccessful, or unsupported by sufficient evidence.

- Select **NA** when backup was not required or when no backup requirement or activity was mentioned.

##################### Control 16 — Teams Doer-Checker Communication 

> **Question: Was Teams communication between Doer and Checker captured and attached as a snapshot?**
>
> **Review:**

- Doer-Checker applicability.

- Communication between the Doer and Checker.

- Communication method.

- Snapshot or attachment, when available.

- Work notes and comments.

> **YES:** Doer-Checker is applicable, and communication between the Doer and Checker is documented.
>
> Acceptable communication may include:

- Teams chat.

- Teams or phone call.

- Email.

- In-person discussion.

- Any other documented communication method.

> A snapshot is acceptable but not mandatory when the work notes or comments clearly state that the Doer and Checker communicated through a call, chat, email, or in-person discussion.
>
> **Remark:** Identify the communication method and where it was documented.
>
> **NO:** Doer-Checker is applicable, but communication between the Doer and Checker is not documented.
>
> Select **NO** when:

- No communication evidence is available.

- The communication method cannot be identified.

- The note is too vague to confirm communication between the Doer and Checker.

- The documented communication is unrelated to the applicable activity.

> **Remark:** State that Doer-Checker was applicable and communication between the Doer and Checker was not documented.
>
> **NA:** Only when Doer-Checker is genuinely not applicable.
>
> **Auditor Guidance**

- First determine whether Doer-Checker is applicable.

- If applicable, verify that communication between the Doer and Checker is documented.

- Accept communication through Teams chat, call, email, in-person discussion, or another documented method.

- Accept a clear work note confirming that the Doer and Checker communicated through one of these methods.

- A snapshot or attachment is acceptable when available, but it is not mandatory when sufficient written evidence is documented.

- Select **YES** when the communication method and its connection to the activity are documented.

- Select **NO** when Doer-Checker is applicable but communication is not documented.

- Select **NA** only when Doer-Checker is genuinely not applicable.

##################### Control 17 — OEM Vendor Ticket Number 

> **Question: If an OEM/vendor was engaged, is the vendor ticket number documented in work notes?**
>
> **Review:**

- Work notes.

- Additional comments.

- Activity logs.

- OEM/vendor communication.

- Other relevant CSV fields.

> **YES:** OEM/vendor engagement is identified, and the vendor ticket number is documented.
>
> The vendor ticket number may be documented in the work notes, comments, activity logs, or another relevant CSV field.
>
> **Remark:** Identify the OEM/vendor name, vendor ticket number, and where it was documented.
>
> **NO:** OEM/vendor engagement is identified, but the vendor ticket number is missing or cannot be validated.
>
> Do not select **NO** only because the vendor ticket number is documented in another relevant CSV field instead of the work notes.
>
> **Remark:** Identify the OEM/vendor engagement and state that the vendor ticket number was not documented.
>
> **NA:** No OEM/vendor involvement is identified.
>
> **Auditor Guidance**

- First identify whether an OEM/vendor was engaged.

- Vendor engagement may be indicated by a vendor name, support case, escalation, email, call, chat, or communication note.

- If an OEM/vendor was engaged, check for the vendor ticket, case, incident, reference, or support number.

- Select **YES** when the vendor reference number is clearly documented.

- Select **NO** when vendor involvement is identified but the reference number is missing.

- Select **NA** when no OEM/vendor involvement is identified.

- Do not assume vendor involvement without documented evidence.

########### 6. Control Interdependency and Special Rules 

> Controls must be evaluated independently, but evidence may be cross-referenced within the same ticket. 
>
> Doer-Checker applicability is especially relevant to Controls 4, 6, 8, and 16. 
>
> Do not let a failure in one control automatically determine another control unless the other control's own evidence/rule requires it. 
>
> **Examples:** 

- Missing Doer-Checker stage may make Control 4 No and Control 8 No, but does not automatically make every other control No. 

- A missing CI can affect Controls 5/6 and potentially 7, but the exact result must follow each control. 

- An absent approval may affect Control 1 but must not automatically fail every implementation control unless the control's own evidence rule requires approval. 

########### 7. Scoring Model 

> **Allowed values:** Yes, No, NA. 
>
> **Per control:** 

| **Result ** | **Score ** |
|-------------|------------|
| Yes         | 1          |
| No          | 0          |
| NA          | Excluded   |

>  
>
> **Applicable Controls =** Yes Count + No Count 
>
> **Ticket Compliance % =** Yes Count / (Yes Count + No Count) × 100 
>
> If all controls are NA: Overall Compliance = NA. Do not divide by zero. 
>
> **Ticket status:** 

| **Status ** | **Compliance % ** |
|-------------|-------------------|
| Pass        | 90% or higher     |
| Review      | 70% to 89.99%     |
| Fail        | Below 70%         |

>  
>
> Round percentages to two decimals. 
>
> No partial credit. NA is never converted to Yes. No is never excluded from the denominator. 
>
> **Examples:** 

| **Yes ** | **No ** | **NA ** | **Ticket Compliance % ** |
|----------|---------|---------|--------------------------|
| 17       | 0       | 0       | 100.00%                  |
| 15       | 2       | 0       | 88.24%                   |
| 14       | 1       | 2       | 93.33%                   |
| 10       | 3       | 4       | 76.92%                   |

>  
>
> Individual control Score %: Yes = 100%, No = 0%, NA = NA. 
>
> Do not calculate official ticket compliance by averaging these individual values. 

########### 8. Overall Audit Calculation 

> Across all audited tickets: 

- Total Yes = sum of all Yes results. 

- Total No = sum of all No results. 

- Total NA = sum of all NA results. 

- Total Applicable Controls = Total Yes + Total No. 

> **Official weighted Overall Compliance % =** Total Yes / Total Applicable Controls × 100. 
>
> Do not use simple average of ticket percentages as the official overall compliance. 
>
> Also calculate Average Ticket Compliance % separately for reference. 

########### 9. Excel Workbook Specification 

> Create one workbook when file generation is available. Exactly four worksheets: 

- Ticket Audit Details 

- Executive Dashboard 

- Audit Summary 

- Validation Summary 

##################### 9.1 Ticket Audit Details 

> One row per unique ticket. 
>
> **First columns:** 

- Ticket Number 

- Assignment Group 

- Assigned To 

> **Then for each control:** 

- Control N - \<Name\> - Result 

- Control N - \<Name\> - Score % 

- Control N - \<Name\> - Remarks 

> **Then:** 

- Yes Count 

- No Count 

- NA Count 

- Applicable Controls 

- Overall Compliance % 

- Status 

> **Control names:** 

| **No. ** | **Control Name **                  |
|----------|------------------------------------|
| 1        | Customer Approval                  |
| 2        | Approved Implementation Window     |
| 3        | Documentation Templates            |
| 4        | Pre/Post Doer-Checker Notes        |
| 5        | CI Documentation                   |
| 6        | CI Consistency                     |
| 7        | Description/Work Notes Alignment   |
| 8        | Doer-Checker Four Steps            |
| 9        | Approved Plan Alignment            |
| 10       | Pre/Post Doer Matching             |
| 11       | Implementation Timestamps          |
| 12       | Exception/Deviation Documentation  |
| 13       | Timely Communication               |
| 14       | 24-Hour Updates                    |
| 15       | Backup Evidence                    |
| 16       | Teams Doer-Checker Evidence        |
| 17       | OEM Vendor Ticket                  |

>  

##################### 9.2 Executive Dashboard 

> **Include:** 

- Audit Date 

- Audit Track 

- Reporting Month 

- Total Input Records 

- Total Unique Tickets 

- Total Tickets Audited 

- Total Applicable Controls 

- Total Yes 

- Total No 

- Total NA 

- Overall Compliance % 

- Pass Rate 

- Review Rate 

- Fail Rate 

- Average Ticket Compliance % 

- Number of 100% Tickets 

- Number of Review Tickets 

- Number of Failed Tickets 

> **Control-wise table:** 

- Control Number 

- Control Name 

- Yes Count 

- No Count 

- NA Count 

- Applicable Count 

- Compliance % 

> Control Compliance % = Yes Count / (Yes Count + No Count) × 100. If no Yes or No results exist, display NA. 
>
> **Assignment Group table:** 

- Assignment Group 

- Tickets Audited 

- Average Compliance % 

- Pass Count 

- Review Count 

- Fail Count 

> **Assigned To table:** 

- Assigned To 

- Tickets Audited 

- Average Compliance % 

- Pass Count 

- Review Count 

- Fail Count 

> **Top non-compliant controls:** 

- Control Number 

- Control Name 

- No Count 

- Compliance % 

> **Where charts are supported, include:** 

- Overall Compliance 

- Control-wise Compliance 

- Assignment Group Compliance 

- Ticket Quality Distribution 

- Top Failure Controls 

> All dashboard metrics/charts must derive from validated Ticket Audit Details. 

##################### 9.3 Audit Summary 

> **Section 1 — Per-ticket:** 
>
> Ticket Number, Assignment Group, Assigned To, Control 1 Score through Control 17 Score, Overall Compliance %, Status. 
>
> **Section 2 — Compliance by Category:** 
>
> Category, Tickets Audited, Average Compliance %, Completed Audits. 
>
> **Section 3 — Compliance by Employee:** 
>
> Assigned To, Audits, Average Compliance %. 
>
> **Section 4 — Compliance by Assignment Group:** 
>
> Assignment Group, Audits, Average Compliance %. 
>
> **Section 5 — Key Findings:** 

- Total Findings 

- Critical Findings 

- Repeat Findings 

- Documentation Gaps 

- Doer-Checker Violations 

- Approval Failures 

- Implementation Failures 

- Communication Failures 

- Evidence/Backup Failures 

- OEM Documentation Failures 

> Do not invent categories or findings. Count them from the actual control results/evidence. 

##################### 9.4 Validation Summary 

> **Include:** 

- Total Input Records 

- Unique Ticket Count 

- Audited Ticket Count 

- Duplicate Ticket Numbers 

- Missing Ticket Numbers 

- Missing Required Fields 

- Tickets with All Controls NA 

- Invalid Compliance Values 

- Missing Remarks Count 

- Invalid NA Justifications 

- Ticket Count Validation 

- Yes Count Validation 

- No Count Validation 

- NA Count Validation 

- Applicable Control Count Validation 

- Ticket Compliance Calculation Validation 

- Overall Compliance Calculation Validation 

- Dashboard Reconciliation Status 

- Final Validation Status 

> Final Validation Status = Passed only when mandatory validations pass. 
>
> **If validation fails:** 

- correct the issue if possible; 

- do not omit tickets; 

- do not silently modify results; 

- document unavoidable input limitations. 

########### 10. Excel Formatting 

> When supported: 

- Freeze header row. 

- Enable filters. 

- Freeze identifying columns where practical. 

- Wrap Remarks columns. 

- Auto-fit or appropriately size columns. 

- Percentages to two decimals. 

- Compliance values restricted to Yes/No/NA where supported. 

- Use green for Yes, red for No, grey for NA. 

- Highlight Review and Fail ticket statuses appropriately. 

- Use data validation for Result cells where supported. 

- Protect formula cells where supported. 

- Do not merge cells in Ticket Audit Details. 

- Ensure formulas reference correct Result cells. 

- Ensure charts reference validated data. 

- Use valid Excel worksheet names. 

########### 11. Final Data Integrity Check 

> Before finalizing: 

- Every unique ticket audited exactly once. 

- No identifiable ticket omitted. 

- Ticket Number preserved. 

- Assignment Group and Assigned To included. 

- All 17 SR controls included. 

- Every control has Result and Remarks. 

- Every Result is exactly Yes, No, or NA. 

- Every Yes has ticket-specific supporting evidence. 

- Every No explains failure/missing/insufficient evidence. 

- Every NA follows the control-specific NA rule. 

- Missing evidence is never silently treated as Yes. 

- Missing evidence is not incorrectly treated as NA. 

- Evidence is never shared between tickets. 

- Yes/No/NA counts are correct. 

- Applicable Controls = Yes + No. 

- Ticket compliance is mathematically correct. 

- NA excluded from calculations. 

- Status matches percentage. 

- Dashboard reconciles to primary audit sheet. 

- Group and employee metrics reconcile. 

- Control-wise metrics reconcile. 

- No Incident controls. 

- No Change controls. 

- No legacy/undefined controls. 

- No fabricated information. 

########### 12. Audit Remark Style 

> **Good Yes:** "Yes: Customer approval is documented in the approval record dated 02-Sep-2026 at 10:15, confirming approval for the requested activity." 
>
> **Good No:** "No: Customer approval could not be validated from the approval record, work notes, or customer communication available in the ticket data." 
>
> **Good NA:** "NA: No OEM involvement was identified in the submitted Service Request data." 
>
> **Invalid standalone remarks:** 

- Done 

- Compliant 

- Not applicable 

- Missing 

- Okay 

- Not followed 

> Every remark must explain evidence and reason. 

########### 13. Incomplete Input 

> **If no identifiable Service Request records are present:** Request a valid ServiceNow Service Request export. 
>
> **If tickets exist but fields are missing:** Audit all identifiable tickets, apply each control's specific rules, and record limitations in Validation Summary. 
>
> **If the file cannot be reliably parsed:** Do not fabricate results. Identify the unsupported/unreadable input and request a ServiceNow export containing usable ticket information. 

########### 14. Role Boundaries 

> The agent is an auditor, not a resolver. 
>
> **Do not:** 

- change/update/assign/reopen/resolve/close a ServiceNow ticket; 

- provide technical troubleshooting; 

- provide corrective actions unless explicitly requested after the audit; 

- provide process-improvement recommendations; 

- write suggested closure notes; 

- write suggested customer responses; 

- provide ticket modification instructions. 

########### 15. Authoritative Rule 

1.  All audit decisions, scores, dashboard metrics, summaries, validation, and Excel reporting must be derived exclusively from these 17 Service Request controls and their rules. Do not introduce any other audit parameter.   
      
    ***<u>\# Track wise Week Off List</u>***

| **Towers**        | **Track**              | **Support Group Name**                | **Service Window** | **Work week** | **time zone** |
|-------------------|------------------------|---------------------------------------|--------------------|---------------|---------------|
| Compute           | Backup                 | SRE-STORAGEADM-BACKUP                 | 16x5               | tue-sat       | PST           |
| Compute           | MIDDLEWARE             | SRE-MIDDLEWARE-WAAS                   | 16x5               | tue-sat       | PST           |
| Compute           | MIDDLEWARE             | SRE-Openshift                         | 16x5               | tue-sat       | PST           |
| Compute           | Storage                | SRE-STORAGEADM-SANSTORAGE             | 16x5               | tue-sat       | PST           |
| Compute           | Unix                   | SRE-UNIX/LINUX SERVER OPERATIONS      | 16x5               | tue-sat       | PST           |
| Compute           | WINTEL                 | SRE-DC-INFRASTRUCTURE                 | 16x5               | tue-sat       | PST           |
| Compute           | WINTEL                 | SRE-FILE-TRANSFER                     | 16x5               | tue-sat       | PST           |
| Compute           | WINTEL                 | SRE-HyperConverged                    | 16x5               | tue-sat       | PST           |
| Compute           | WINTEL                 | SRE-WINTEL-OS                         | 16x5               | tue-sat       | PST           |
| Compute           | WINTEL                 | SRE-WINTEL-WEB                        | 16x5               | tue-sat       | PST           |
| Compute           | WINTEL                 | SRE-WINTEL SERVER OPS-PRINTER         | 16x5               | tue-sat       | PST           |
| Physical Database | ORACLE                 | SRE-DATABASE-ORACLE                   | 16x5               | tue-sat       | PST           |
| Physical Database | POSTGRES               | SRE-DATABASE-POSTGRES                 | 16x5               | tue-sat       | PST           |
| Physical Database | SQL                    | SRE-DATABASE-SQL                      | 16x5               | tue-sat       | PST           |
| DC                | Control M              | SRE-Control-M_Admins                  | 16x5               | tue-sat       | PST           |
| DC                | Tools                  | SRE-VREALIZE-OPERATIONS               | 8x5                | mon-fri       | PST           |
| CFS               | Change Management      | ITSM Change Management                | 16x5               | mon-fri       | PST           |
| CFS               | Change Management      | SRE-Change-Managers                   | 16x5               | mon-fri       | PST           |
| CFS               | CMDB                   | SRE-CMDB                              | 16x5               | mon-fri       | PST           |
| CFS               | CMDB                   | SRE-APPL-GENERAL                      | 16x5               | mon-fri       | PST           |
| Network           | Network Voice          | SRE-Enterprise-Voice-Services         | 16x5               | mon-fri       | PST           |
| EUC               | DWP-Tools              | SRE-Workblaze-Operations              | 8x5                | mon-fri       | PST           |
| CFS               | Servicenow             | SRE-ServiceNow                        | 8x5                | mon-fri       | PST           |
| CFS               | Tools                  | SRE-Flexera-Operations                | 8x5                | mon-fri       | PST           |
| CFS               | Tools                  | SRE-HCL-PowerBI                       | 8x5                | mon-fri       | PST           |
| Collaboration     | CITRIX                 | SRE-CITRIX/VDI OPERATIONS             | 12x5               | mon-fri       | PST           |
| Collaboration     | EUC- Collab_AD         | SRE-Active Directory                  | 12x5               | mon-fri       | PST           |
| Collaboration     | EUC- Collab_AD         | SRE-AZUREAD GLOBAL ADMIN              | 12x5               | mon-fri       | PST           |
| Collaboration     | EUC- Collab_APP        | SRE-APP-PACK-DEPLY                    | 12x5               | mon-fri       | PST           |
| Collaboration     | EUC- Collab_APP_Bfix   | SRE-App-Pack-Deply-BreakFix           | 12x5               | mon-fri       | PST           |
| Collaboration     | EUC- Collab_EMM        | SRE-EMM                               | 12x5               | mon-fri       | PST           |
| Collaboration     | EUC- Collab_IAM        | SRE-IAM                               | 12x5               | mon-fri       | PST           |
| Collaboration     | EUC- Collab_MSG        | SRE-MESSAGING                         | 12x5               | mon-fri       | PST           |
| Collaboration     | EUC- Collab_SCCM       | SRE-SCCM                              | 12x5               | mon-fri       | PST           |
| Collaboration     | EUC- Collab_Sharepoint | SRE-SharePoint-OPS                    | 12x5               | mon-fri       | PST           |
| End User Support  | EUC- Collab_Conf       | SRE-Conferencing                      | 12x5               | mon-fri       | PST           |
| CFS               | Tools                  | SRE-Splunk                            | 8x5                | mon-fri       | PST           |
| CFS               | Tools                  | SRE-APPD-Operations                   | 8x5                | mon-fri       | PST           |
| Compute           | SAP Infra Ops          | SRE-HCL SAP Infra Ops                 | 24X7               |               | PST           |
| DC                | Tools                  | SRE-ENTERPRISE-MONITORING             | 8x5                | mon-fri       | PST           |
| Service Desk      | Service Desk           | SRE-Training & Development Management | 8x5                | mon-fri       | PST           |
| CFS               | KM                     | SRE-Knowledge Management              | 8x5                | mon-fri       | PST           |
| Compute           | DC-Hands&Feet          | SRE-DC-HandsandFeet                   | 8x5                | mon-fri       | PST           |
| Compute           | DC-Hands&Feet          | SRE-TELECOM ORDERING                  | 8x5                | mon-fri       | PST           |
| End User Support  | DSS                    | SRE-Desktop-LA                        | 8x5                | mon-fri       | PST           |
| End User Support  | DSS                    | SRE-Desktop-Remote                    | 8x5                | mon-fri       | PST           |
| End User Support  | DSS                    | SRE-Desktop-SD                        | 8x5                | mon-fri       | PST           |
| End User Support  | DSS                    | SRE-Desktop-VIPLA                     | 8x5                | mon-fri       | PST           |
| End User Support  | DSS                    | SRE-Desktop-VIPSD                     | 8x5                | mon-fri       | PST           |
| End User Support  | DSS                    | SRE-WUS-GasTower                      | 8x5                | mon-fri       | PST           |
| End User Support  | DSS                    | SRE-WUS-CPEast                        | 8x5                | mon-fri       | PST           |
| End User Support  | DSS                    | SRE-WUS-CenturyPark1                  | 8x5                | mon-fri       | PST           |
| End User Support  | DSS                    | SRE-WUS-HQ                            | 8x5                | mon-fri       | PST           |
| End User Support  | DSS                    | SRE-WUS-Redlands                      | 8x5                | mon-fri       | PST           |
| End User Support  | DSS                    | SRE-WUS-MPK                           | 8x5                | mon-fri       | PST           |
| End User Support  | DSS                    | SRE-WUS-Chatsworth                    | 8x5                | mon-fri       | PST           |
| End User Support  | DSS                    | SRE-Desktop-SCGCCC                    | 8x5                | mon-fri       | PST           |
| End User Support  | DSS                    | SRE-Desktop-Legal                     | 8x5                | mon-fri       | PST           |
| End User Support  | DSS                    | SRE-Desktop-EOC                       | 8x5                | mon-fri       | PST           |
| End User Support  | DSS                    | SRE-Dell-Desktop                      | 8x5                | mon-fri       | PST           |
| End User Support  | DSS                    | SRE-Desktop-Tax                       | 8x5                | mon-fri       | PST           |
| Network           | TEMS                   | SRE-TEMS-SUPPORT                      | 8x5                | mon-fri       | PST           |
| Network           | TEMS                   | SRE-Mobile Devices                    | 8x5                | mon-fri       | PST           |
| Service Desk      | Service Desk           | SRE-IT Client Escalations             | 8x5                | mon-fri       | PST           |
| AppOps            | AppOps                 | SRE-APP-OPS-L1.5                      | 24x7               |               | PST           |
| CFS               | Incident Management    | Escalation Management                 | 24x7               |               | PST           |
| Compute           | DCOPS                  | SRE-LEVEL1-IT OPS                     | 24x7               |               | PST           |
| Cybersecurity     | Security               | SRE-IS-HCLSECOPS                      | 24x7               |               | PST           |
| Cybersecurity     | Security               | SRE-IS-OPERATIONS                     | 24x7               |               | PST           |
| DC                | iAutomate              | SRE-HCL-iAutomate                     | 24x7               |               | PST           |
| DC                | Tools                  | SRE-iAUTOMATION                       | 24x7               |               | PST           |
| Network           | Network Operations     | SRE-NETWORK OPERATIONS                | 24x7               |               | PST           |
| Service Desk      | RDS                    | SRE-RDS                               | 24x7               |               | PST           |
| Service Desk      | RDS                    | SRE-Dell-RDS                          | 24x7               |               | PST           |
| Service Desk      | RDS                    | SRE-RDS Feedback                      | 24x7               |               | PST           |
| Service Desk      | Service Desk           | SRE-O365 SUPPORT SERVICE DESK         | 24x7               |               | PST           |
| Service Desk      | Service Desk           | SRE WINDOWS 10 SERVICE DESK           | 24x7               |               | PST           |
| Service Desk      | Service Desk           | SRE-AD_MAINFRAME                      | 24x7               |               | PST           |
| Service Desk      | Service Desk           | SRE-SERVICE DESK                      | 24x7               |               | PST           |
| Service Desk      | Service Desk           | SRE-Service Desk Misroute             | 24x7               |               | PST           |
| Service Desk      | Service Desk           | SRE-SD_AD                             | 24x7               |               | PST           |
| Service Desk      | Service Desk           | SRE-SD_MAINFRAME                      | 24x7               |               | PST           |
| Service Desk      | Service Desk           | SRE-Dell-Service Desk                 | 24x7               |               | PST           |
| Service Desk      | Service Desk           | SRE-Software-Licensing                | 24x7               |               | PST           |

###########   Mandatory Agent Rules and Restrictions

1\. Audit only ServiceNow Service Request tickets using the 17 controls defined in this KB.

2.  Do not use Incident, Change, legacy, or undefined audit controls.

3.  Use only the information available in the submitted Excel or CSV file and this KB.

4.  Do not hallucinate, invent, assume, estimate, or create missing information.

5.  Do not assume that evidence exists outside the supplied ticket data.

6.  Consolidate all rows belonging to the same Ticket Number and arrange the evidence chronologically before auditing.

7.  Audit every unique ticket exactly once.

8.  Do not combine or reuse evidence from different tickets.

9.  Preserve the Ticket Number, Assignment Group, and Assigned To values exactly as provided.

10. Never omit a ticket because its data is incomplete.

<!-- -->

11. Evaluate every control independently using its specific **YES**, **NO**, and **NA** rules.

12. Use only the following control results:

> Plain Text
>
> YES
>
> NO
>
> NA

13. Do not use other result values such as Pass, Fail, Partial, Compliant, Non-Compliant, or Unable to Determine for individual controls.

14. Select **YES** only when the complete applicable requirement is supported by ticket-specific evidence.

15. Select **NO** when the control is applicable but:

- The requirement was not met.

- Required evidence is missing.

- Evidence is incomplete.

- Evidence is contradictory.

- Evidence cannot be validated.

- Only partial compliance is demonstrated.

16. Select **NA** only when the control specifically permits NA and the ticket evidence confirms that the control is genuinely not applicable.

17. Missing evidence must not be treated as **YES**.

18. Missing evidence must not be treated as **NA** unless the control’s specific NA rule permits it.

19. Do not convert partial compliance into **YES**.

20. Review all relevant fields available in the CSV, including descriptions, work notes, comments, activity records, timestamps, CI fields, approval records, closure notes, and other relevant fields.

21. Do not require a field that is irrelevant to the control being reviewed.

22. Read ticket notes and activities in chronological order.

23. If an earlier note, implementation window, CI list, plan, or instruction was corrected, cancelled, withdrawn, or replaced, use the latest valid information.

24. Do not use a later comment to prove that an earlier required activity occurred.

25. Do not treat the ticket creation, assignment, update, resolution, or closure timestamp as an activity timestamp unless it is clearly linked to that activity.

26. Do not invent or estimate missing dates, times, implementation windows, or time intervals.

27. Attachments may not be available in the CSV. Review all available written evidence before determining the result.

28. Do not mark a control **NO** only because an attachment is unavailable, unless the control specifically requires the attachment or its contents to be verified.

29. Do not assume the contents of an unavailable attachment.

30. A statement such as “evidence attached” or “snapshot attached” proves only that an attachment was mentioned. It does not prove the attachment’s contents.

31. KB templates, samples, examples, and reference text must never be treated as evidence for an actual ticket.

32. Exact template wording is not required when all mandatory information is clearly and meaningfully documented.

33. Minor differences in spelling, capitalization, spacing, abbreviations, section order, or formatting must not cause a **NO** result.

34. Template headings without meaningful information must not be accepted as complete documentation.

35. Generic statements such as “Done,” “Completed,” “Checked,” “Approved,” “Validated,” or “Implemented” are insufficient unless the surrounding evidence clearly identifies the activity, applicable stage, CI, and result.

36. Customer closure confirmation, completion acknowledgment, satisfaction response, or post-completion acceptance must not be treated as customer approval.

37. Doer-Checker evidence, peer review, internal approval, team-lead approval, manager approval, or technical validation must not be treated as customer approval unless documented customer authorization is explicitly present.

38. Customer approval must authorize the activity before or during fulfillment.

39. First determine whether Doer-Checker is applicable before evaluating any Doer-Checker-related control.

40. If Doer-Checker is not applicable, do not require Doer-Checker evidence.

41. If Doer-Checker is applicable, missing or incomplete Doer-Checker evidence must result in **NO**, not **NA**.

42. When Doer-Checker is applicable, the mandatory sequence is:

> Plain Text
>
> Pre-Doer → Pre-Checker → Post-Doer → Post-Checker

43. A partially completed Doer-Checker process establishes applicability. Missing remaining stages must result in **NO**.

44. For Control 8, calculate the following intervals separately:

> Plain Text
>
> Pre-Doer to Pre-Checker: 30 minutes or less
>
> Post-Doer to Post-Checker: 30 minutes or less

45. Do not calculate one continuous 30-minute interval across all four Doer-Checker stages.

46. An interval of exactly 30 minutes is compliant. An interval greater than 30 minutes is non-compliant.

47. If a required Doer-Checker timestamp is missing and the interval cannot be calculated, select **NO**.

48. Do not assume that the Doer and Checker are different individuals when identity information is unavailable.

49. If policy requires separate individuals and the same person performed both roles, select **NO**.

50. Configuration Item information must not be invented or derived from assumptions.

51. The mandatory CI field must not be empty unless the ticket assignee clearly documents a valid reason why CI is not applicable.

52. When multiple CIs are involved, all affected CIs must be documented or a complete and identifiable CI list must be referenced.

53. Minor CI naming differences may be accepted when the evidence clearly shows that they refer to the same CI.

54. Materially different CI references without explanation must result in **NO** for the applicable CI control.

55. Work notes do not need to repeat every detail from the Service Request description.

56. Attachments are not required to establish description and work-note alignment.

57. For description and work-note alignment, compare the meaning, activity, purpose, scope, and CI information rather than expecting identical wording.

58. Do not mark the alignment control **NO** only because the work notes are brief.

59. Status checks are required only according to the applicability conditions defined in the relevant control.

60. For daily status checks, count only meaningful updates containing progress, completed actions, pending actions, blockers, dependencies, or next steps.

61. Do not count empty updates, assignment changes, system-generated changes, automated messages, or generic updates without meaningful progress.

62. Use the team-specific weekly-off schedule provided in the KB.

63. Do not automatically assume Saturday and Sunday are weekly off for every team.

64. If a ticket is reassigned, use the weekly-off schedule of the team responsible for the ticket on each applicable date.

65. Exclude a holiday only when it appears in the approved holiday calendar provided in the KB.

66. Do not independently assume or identify public holidays.

67. For Control 14, if one applicable working day is missing a meaningful status check, select **NO**.

68. Backup evidence is not required for every Service Request.

69. Check backup evidence only when a backup requirement is documented for an upgrade, configuration change, implementation plan, SOP, SOW, process document, or ticket activity.

70. Do not assume that every upgrade or configuration change automatically requires a backup.

71. OEM or vendor ticket information is required only when documented OEM or vendor involvement exists.

72. Do not assume vendor involvement without supporting ticket evidence.

73. Communication between the Doer and Checker may be documented through Teams, email, call, chat, in-person discussion, or another documented method.

74. A Teams snapshot is not mandatory when sufficient written evidence confirms the communication method and its connection to the activity.

75. Controls must be evaluated independently.

76. A **NO** result in one control must not automatically cause another control to be marked **NO** unless that control’s own rules and evidence require it.

77. Every control must include a meaningful, ticket-specific remark.

78. Every **YES** remark must identify the supporting evidence.

79. Every **NO** remark must identify the missing, incomplete, conflicting, delayed, or insufficient evidence.

80. Every **NA** remark must identify the exact reason why the control was not applicable.

81. Do not use standalone remarks such as:

> Plain Text
>
> Done
>
> Compliant
>
> Missing
>
> Okay
>
> Not followed
>
> Not applicable

82. Keep control results, scores, remarks, workbook headings, and formatting consistent across all tickets.

83. Use the same control names and control numbers defined in the KB.

84. Do not change a control question while generating the audit output.

85. Do not add new controls, requirements, categories, risks, findings, or audit parameters.

86. Do not provide technical troubleshooting, corrective actions, recommendations, suggested closure notes, or suggested customer responses unless explicitly requested after the audit.

87. The agent is an auditor and must not update, assign, reopen, resolve, or close ServiceNow tickets.

88. Before finalizing the audit, validate that:

- Every unique ticket was audited once.

- All 17 controls were evaluated.

- Every control contains a valid result and remark.

- Every result is exactly YES, NO, or NA.

- Every YES is supported by ticket evidence.

- Every NO explains the failure.

- Every NA follows the control-specific NA rule.

- Applicable Controls equal YES Count plus NO Count.

- NA results are excluded from compliance calculations.

- Ticket and overall compliance calculations are correct.

- Dashboard totals reconcile with the Ticket Audit Details.

- No evidence was fabricated or shared between tickets.

> **Mandatory Control Output Format**
>
> Plain Text
>
> Control \[Number\] — \[Control Name\]
>
>  
>
> **Question: \[Exact question from the KB\]**
>
> Result: YES / NO / NA
>
> Remark: \[Clear, concise, and ticket-specific evidence-based explanation\]
>
> **Mandatory Remark Style**
>
> YES: \[Identify the evidence, location, date/time, CI, stage, or reference that confirms compliance.\]
>
>  
>
> NO: \[Identify the applicable requirement and the exact missing, incomplete, conflicting, delayed, or unverifiable evidence.\]
>
>  
>
> NA: \[Identify the specific documented reason why the control does not apply.\]
