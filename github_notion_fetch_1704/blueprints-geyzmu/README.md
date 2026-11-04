# Blueprint Atlas

Blueprint Atlas is the shared workbench for reusable agent blueprints. Each
blueprint is a self-contained package that another team can pick up, adapt, and
deliver against its own systems.

## Package layout

```
blueprints/<slug>/
  README.md
  metadata.json
  docs/task.md
  docs/agent_system_prompt.md
  evaluation/
  preprocess/
  groundtruth_workspace/
  initial_workspace/
```

## Documentation rules

The two documents in `docs/` are required for every blueprint:

* `docs/task.md` must exist and be non-empty.
* `docs/agent_system_prompt.md` must exist and be non-empty.
* Both must be written in English.

## Optional material

The contents of `evaluation/`, `preprocess/`, `groundtruth_workspace/` and
`initial_workspace/` are optional and depend on the blueprint. Draft packages
frequently ship without a finished validator, without preprocessing, or without
sample workspaces; those folders can be skipped or stubbed while the design is
still in progress. See `examples/baseline-blueprint/evaluation/main.py` for
the minimal stub we normally start from.

## Release process

The packaging pipeline in `tools/build_release.py` produces the quarterly
release pool. Run it against a package tree before promoting anything; it
reports which packages are accepted and which are not. The older release
history is recorded in `releases/history.json`.
