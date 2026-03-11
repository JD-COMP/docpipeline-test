# CLI Usage

## Commands

### Run Server

```bash
python -m src.cli serve --port 8000
```

**Options:**
- `--port` (int): Port number (default: 8000)
- `--host` (str): Host address (default: "0.0.0.0")

### Process Data

```bash
python -m src.cli process --input data.txt
```

**Options:**
- `--input` (str): Input file path
- `--output` (str): Output file path (default: stdout)
