"""Command-line interface."""

import argparse


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="DocPipeline Test App")
    sub = parser.add_subparsers(dest="command")

    # serve
    serve = sub.add_parser("serve", help="Run the server")
    serve.add_argument("--port", type=int, default=8000, help="Port number")
    serve.add_argument("--host", default="0.0.0.0", help="Host address")
    serve.add_argument("--workers", type=int, default=1, help="Number of workers")
    serve.add_argument("--reload", action="store_true", help="Enable auto-reload")
    serve.add_argument("--auth-secret", default="", help="Auth signing secret")

    # process
    proc = sub.add_parser("process", help="Process data")
    proc.add_argument("--input", required=True, help="Input file path")
    proc.add_argument("--output", default="-", help="Output file path")
    proc.add_argument("--normalize", action="store_true", help="Normalize input")
    proc.add_argument("--strict", action="store_true", help="Enable strict validation")
    proc.add_argument("--batch", action="store_true", help="Batch mode (one item per line)")

    # auth (new subcommand)
    auth = sub.add_parser("auth", help="Authentication utilities")
    auth.add_argument("--create-token", metavar="USER_ID", help="Create auth token for user")
    auth.add_argument("--verify-token", metavar="TOKEN", help="Verify an auth token")
    auth.add_argument("--secret", required=True, help="Signing secret")

    return parser


def main():
    parser = build_parser()
    args = parser.parse_args()
    print(f"Running command: {args.command}")


if __name__ == "__main__":
    main()
