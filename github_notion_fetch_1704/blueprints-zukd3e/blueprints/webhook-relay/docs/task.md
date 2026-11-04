# webhook-relay

Automate the workflow that fan out partner webhooks with retry semantics.

Use the connected systems to read the current business records, apply the
documented decision rules, and write the operations report to
`webhook-relay_report.json` in the workspace. Each record must carry a disposition of
`handled`, `held` or `escalated`.
