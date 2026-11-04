# policy-engine

Automate the workflow that apply policy rules to incoming service requests.

Use the connected systems to read the current business records, apply the
documented decision rules, and write the operations report to
`policy-engine_report.json` in the workspace. Each record must carry a disposition of
`handled`, `held` or `escalated`.
