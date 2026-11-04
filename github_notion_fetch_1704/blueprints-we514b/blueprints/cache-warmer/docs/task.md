# cache-warmer

Automate the workflow that pre-warm regional cache tiers.

Use the connected systems to read the current business records, apply the
documented decision rules, and write the operations report to
`cache-warmer_report.json` in the workspace. Each record must carry a disposition of
`handled`, `held` or `escalated`.
