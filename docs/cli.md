# CLI Usage

## Commands

### Run Server

```bash
python -m src.cli serve --port 8000
```

**Options:**
- `--port` (int): Port number (default: 8000)
- `--host` (str): Host address (default: "0.0.0.0")
- `--workers` (int): Number of workers (default: 1)
- `--reload` (flag): Enable auto-reload
- `--auth-secret` (str): Auth signing secret (default: "")

### Process Data

```bash
python -m src.cli process --input data.txt
```

**Options:**
- `--input` (str): Input file path
- `--output` (str): Output file path (default: stdout)
- `--normalize` (flag): Normalize input
- `--strict` (flag): Enable strict validation
- `--batch` (flag): Batch mode (one item per line)

### Authentication Utilities

```bash
python -m src.cli auth --secret mysecret --create-token user123
```

**Options:**
- `--create-token` (str): Create auth token for user
- `--verify-token` (str): Verify an auth token
- `--secret` (str): Signing secret (required)