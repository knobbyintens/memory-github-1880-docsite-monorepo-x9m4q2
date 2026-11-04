# quota-manager

Automate the workflow that enforce per-tenant service quotas.

Use the connected systems to read the current business records, apply the
documented decision rules, and write the operations report to
`quota-manager_report.json` in the workspace. Each record must carry a disposition of
`handled`, `held` or `escalated`.
