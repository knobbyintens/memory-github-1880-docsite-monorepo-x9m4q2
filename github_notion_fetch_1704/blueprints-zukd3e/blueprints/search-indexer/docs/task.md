# search-indexer

Automate the workflow that refresh the internal document search index.

Use the connected systems to read the current business records, apply the
documented decision rules, and write the operations report to
`search-indexer_report.json` in the workspace. Each record must carry a disposition of
`handled`, `held` or `escalated`.
