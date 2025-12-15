from pathlib import Path

from src.persistence.writer import write_dicts_to_csv
from src.processor import ProcessorData


def main() -> None:
    base_dir = Path(__file__).resolve().parent
    data_dir = base_dir / "data"
    output_dir = base_dir / "output"
    output_dir.mkdir(parents=True, exist_ok=True)

    processor = ProcessorData()
    processor.get_legislators(str(data_dir / "legislators.csv"))
    processor.get_votes(str(data_dir / "votes.csv"))
    processor.get_bills(str(data_dir / "bills.csv"))
    processor.get_vote_results(str(data_dir / "vote_results.csv"))

    legislator_stats = processor.compute_legislator_stats()
    bill_stats = processor.compute_bill_stats()


if __name__ == "__main__":
    main()
