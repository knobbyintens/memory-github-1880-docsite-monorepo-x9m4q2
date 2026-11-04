# feature-flags

Automate the workflow that roll out feature flags with staged cohorts.

Use the connected systems to read the current business records, apply the
documented decision rules, and write the operations report to
`feature-flags_report.json` in the workspace. Each record must carry a disposition of
`handled`, `held` or `escalated`.
