# Architecture

## Overview

Simple request-processing service with modular design.

## Module Structure

```
src/
├── app.py       — Core request handlers
├── models.py    — Pydantic data models
├── config.py    — Application configuration
└── cli.py       — Command-line interface
```

## Configuration

The `src/config.py` module provides:
- `APP_NAME`: Application name (default: "docpipeline-test")
- `DEBUG`: Debug mode flag (default: False)
- `MAX_BATCH_SIZE`: Maximum items per batch (default: 100)

## Dependencies

- Python 3.11+
- No external dependencies (stdlib only)
