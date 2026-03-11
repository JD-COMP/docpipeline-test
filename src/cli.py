"""Command-line interface."""

import argparse


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="DocPipeline Test App")
    sub = parser.add_subparsers(dest="command")

    # serve
    serve = sub.add_parser("serve", help="Run the server")
    serve.add_argument("--port", type=int, default=8000, help="Port number")
    serve.add_argument("--host", default="0.0.0.0", help="Host address")

    # process
    proc = sub.add_parser("process", help="Process data")
    proc.add_argument("--input", required=True, help="Input file path")
    proc.add_argument("--output", default="-", help="Output file path")

    return parser


def main():
    parser = build_parser()
    args = parser.parse_args()
    print(f"Running command: {args.command}")


if __name__ == "__main__":
    main()
