# agend-fleet-demo

Demo scratch repository for [agend-terminal](https://github.com/suzuke/agend-terminal)
multi-agent fleet recording.

A tiny Python string utility library used as the playground where AI agents
add / modify functions during the demo so viewers can watch coordination,
review, and self-merge live.

## Run tests locally

```sh
pip install pytest
pytest -v
```

CI runs the same `pytest -v` on every push and pull request via
`.github/workflows/test.yml`.
