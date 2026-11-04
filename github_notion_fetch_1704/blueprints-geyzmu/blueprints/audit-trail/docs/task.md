# audit-trail

Automate the workflow that assemble immutable audit trails for regulated changes.

Use the connected systems to read the current business records, apply the
documented decision rules, and write the operations report to
`audit-trail_report.json` in the workspace. Each record must carry a disposition of
`handled`, `held` or `escalated`.
