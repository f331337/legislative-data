from persistence.readers import load_csv


class ProcessorData:
    def __init__(self):
        self.legislators: dict[int, str] = {}
        self.votes: dict[int, int] = {}
        self.bills: dict[int, dict] = {}
        self.vote_results: list[dict] = []

    def get_legislators(self, file_path: str) -> None:
        raw_data = load_csv(file_path)
        self.legislators = {int(row["id"]): row["name"] for row in raw_data}

    def get_votes(self, file_path: str) -> None:
        raw_data = load_csv(file_path)
        self.votes = {int(row["id"]): int(row["bill_id"]) for row in raw_data}

    def get_bills(self, file_path: str) -> None:
        raw_data = load_csv(file_path)
        self.bills = {
            int(row["id"]): {
                "title": row["title"],
                "primary_sponsor": int(row["primary_sponsor"])
                if row.get("primary_sponsor") and row["primary_sponsor"].isdigit()
                else None,
            }
            for row in raw_data
        }

    def get_vote_results(self, file_path: str) -> None:
        self.vote_results = load_csv(file_path)

    def compute_legislator_stats(self) -> dict[int, dict]:
        stats = {lid: {"supported": 0, "opposed": 0} for lid in self.legislators}

        for row in self.vote_results:
            legislator_id = int(row["legislator_id"])
            vote_type = int(row["vote_type"])

            if vote_type == 1:
                stats[legislator_id]["supported"] += 1
            elif vote_type == 2:
                stats[legislator_id]["opposed"] += 1

        return stats

    def compute_bill_stats(self) -> dict[int, dict]:
        stats = {bid: {"supporters": 0, "opposers": 0} for bid in self.bills}

        for row in self.vote_results:
            vote_id = int(row["vote_id"])
            vote_type = int(row["vote_type"])

            bill_id = self.votes.get(vote_id)
            if bill_id is None:
                continue

            if vote_type == 1:
                stats[bill_id]["supporters"] += 1
            elif vote_type == 2:
                stats[bill_id]["opposers"] += 1

        return stats
