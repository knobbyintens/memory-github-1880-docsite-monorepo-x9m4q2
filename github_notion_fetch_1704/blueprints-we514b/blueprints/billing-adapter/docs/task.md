# billing-adapter

Automate the workflow that legacy billing gateway adapter.

Use the connected systems to read the current business records, apply the
documented decision rules, and write the operations report to
`billing-adapter_report.json` in the workspace. Each record must carry a disposition of
`handled`, `held` or `escalated`.
