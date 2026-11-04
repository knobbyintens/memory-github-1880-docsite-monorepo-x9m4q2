# alert-fanout

Automate the workflow that deduplicate and route operational alerts.

Use the connected systems to read the current business records, apply the
documented decision rules, and write the operations report to
`alert-fanout_report.json` in the workspace. Each record must carry a disposition of
`handled`, `held` or `escalated`.
