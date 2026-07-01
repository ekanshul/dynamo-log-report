# dynamo/log-report

A fixed Terminal-Bench 2 (Harbor) task. The task parses an Apache-style access log
(`/app/access.log`) into a small JSON summary report at `/app/report.json` with three
fields: `total_requests`, `unique_ips`, and `top_path`.

## Layout

```
log-report/
  task.toml                 # TB2 Harbor task config (artifacts, metadata, env)
  instruction.md            # Agent brief with numbered success criteria
  environment/
    Dockerfile              # Approved base pinned by @sha256; verifier deps baked in
    access.log              # Input log
  solution/
    solve.sh                # Oracle entrypoint
    solve.py                # Reference solution
  tests/
    test.sh                 # Runs pytest; writes reward.txt + ctrf.json to /logs/verifier/
    test_outputs.py         # Value-level assertions, 1:1 with instruction criteria
```

## Run

```bash
harbor run -p log-report -a oracle    # reference solution -> reward 1
harbor run -p log-report --agent nop  # no-op agent        -> reward 0
```

## Verified results

- `-a oracle`: reward `1.0`, ctrf `4 passed / 0 failed`, artifact
  `{"total_requests": 6, "unique_ips": 3, "top_path": "/index.html"}`.
- `--agent nop`: reward `0.0`, ctrf `0 passed / 4 failed`.
