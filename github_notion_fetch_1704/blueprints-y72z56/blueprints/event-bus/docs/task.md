# event-bus

Automate the workflow that normalise and forward domain events.

Use the connected systems to read the current business records, apply the
documented decision rules, and write the operations report to
`event-bus_report.json` in the workspace. Each record must carry a disposition of
`handled`, `held` or `escalated`.
