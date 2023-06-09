from lib.utils import Trade, TradeDetails
import datetime
import random


class DataGenerator:
    def get_random_dates(self, start_date_str="2023-06-01", end_date_str="2023-06-15", limit=1):
        start_date = datetime.datetime.strptime(start_date_str, "%Y-%m-%d")
        end_date = datetime.datetime.strptime(end_date_str, "%Y-%m-%d")

        dates = []
        delta = end_date - start_date

        for _ in range(limit):
            random_days = random.randint(0, delta.days)
            random_date = start_date + datetime.timedelta(days=random_days)
            dates.append(random_date)

        return dates

    # Mock the elasticsearch query
    def gen_trades(self, start: str = None, end: str = None, assetClass: str = None,
                     maxPrice: int = None, minPrice: int = None, tradeType: str = None, tradeId: int = None,
                     trader: str = None, instrumentId=None, counterparty=None, instrumentName: str = None
                     ):
        td = {
            "buySellIndicator": None,
            "price": None,
            "quantity": None
        }

        t = {"assetClass": None,
             "counterparty": None,
             "instrumentId": None,
             "instrumentName": None,
             "tradeDateTime": None,
             "tradeDetails": None,
             "tradeId": None,
             "trader": None
             }

        instruments = {
            "AAPL": "Apple Inc.",
            "MSFT": "Microsoft Corporation",
            "AMZN": "Amazon.com, Inc.",
            "GOOGL": "Alphabet Inc. (Google)",
            "FB": "Facebook, Inc.",
            "NVDA": "NVIDIA Corporation",
            "TSLA": "Tesla, Inc.",
            "INTC": "Intel Corporation",
            "ADBE": "Adobe Inc.",
            "CRM": "Salesforce.com, Inc."
        }

        traders_name = [
            "John Smith",
            "Emily Johnson",
            "Michael Williams",
            "Sophia Brown",
            "Daniel Davis",
            "Olivia Miller",
            "William Wilson",
            "Ava Taylor",
            "James Anderson",
            "Isabella Martinez"
        ]

        td["buySellIndicator"] = tradeType if tradeType else random.choice(["BUY", "SELL"])
        td["price"] = random.randint(minPrice, maxPrice) if minPrice and maxPrice else random.randint(150, 2500)
        td["quantity"] = random.randint(5, 100)
        td = TradeDetails(**td)

        t["assetClass"] = assetClass if assetClass else random.choice(["Bond", "Equity", "Fixed"])
        t["counterparty"] = counterparty if counterparty else None
        t["instrumentId"] = instrumentId if instrumentId else random.choice(list(instruments.keys()))
        t["instrumentName"] = instrumentName if instrumentName else instruments[t["instrumentId"]] \
            if t["instrumentId"] in instruments.keys() else t["instrumentId"]
        t["tradeDateTime"] = self.get_random_dates(start, end)[0] if start and end else self.get_random_dates()[0]
        t["tradeDetails"] = td
        t["tradeId"] = tradeId if tradeId else random.randint(1000, 5000)
        t["trader"] = trader if trader else random.choice(traders_name)

        return Trade(**t)
