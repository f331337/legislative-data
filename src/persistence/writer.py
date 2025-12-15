import csv
from typing import Iterable


def write_dicts_to_csv(
    file_path: str,
    rows: Iterable[dict],
    fieldnames: list[str] | None = None,
) -> None:
    rows = list(rows)
    if not rows:
        return

    if fieldnames is None:
        fieldnames = list(rows[0].keys())

    with open(file_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)
