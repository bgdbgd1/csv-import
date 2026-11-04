"""
CSV import job entry point.

Receives the path to a CSV file and figures out which processor to use
from the filename — no --table argument needed.

  In:  --file argument + DB_DSN environment variable
  Out: exit code 0 (success) or 1 (failure)

Usage:
    python import_csv.py --file /data/incoming/orders.csv
    python import_csv.py --file /data/incoming/orders_20261104.csv
"""
from __future__ import annotations

import argparse
import os
import sys

from processors import get_processor


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--file", required=True, help="Path to the CSV file inside the pod")
    args = parser.parse_args()

    dsn = os.environ.get("DB_DSN")
    if not dsn:
        print("ERROR: DB_DSN environment variable is not set", file=sys.stderr)
        sys.exit(1)

    try:
        processor = get_processor(args.file)
    except ValueError as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        sys.exit(1)

    try:
        inserted = processor.run(args.file, dsn)
    except FileNotFoundError:
        print(f"ERROR: file not found: {args.file}", file=sys.stderr)
        sys.exit(1)
    except Exception as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        sys.exit(1)

    print(f"OK: inserted {inserted} rows")


if __name__ == "__main__":
    main()