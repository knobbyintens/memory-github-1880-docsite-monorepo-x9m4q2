# legacy-export

Automate the workflow that nightly export of legacy reporting extracts.

Use the connected systems to read the current business records, apply the
documented decision rules, and write the operations report to
`legacy-export_report.json` in the workspace. Each record must carry a disposition of
`handled`, `held` or `escalated`.
