# API Reference

## Functions

### `health() -> dict`

Returns service health status.

**Returns:** `{"status": "ok"}`

### `process(data: str) -> dict`

Processes input data by converting to uppercase.

**Parameters:**
- `data` (str): Input string to process.

**Returns:** `{"result": "<uppercase>", "length": <int>}`

## Data Models

### ProcessRequest

| Field | Type   | Description       |
|-------|--------|-------------------|
| data  | string | Input to process  |

### ProcessResponse

| Field  | Type   | Description         |
|--------|--------|---------------------|
| result | string | Processed output    |
| length | int    | Length of input     |
