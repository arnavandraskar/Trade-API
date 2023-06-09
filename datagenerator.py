from lib.utils import Trade, TradeDetails
import datetime
import random


class DataGenerator:
    def get_random_dates(self, start_date_str="2023-06-01", end_date_str="2023-06-15", limit=1):
        """
        Generate a list of random dates within a specified range.

        Args:
            start_date_str (str): The start date in the format "YYYY-MM-DD".
            end_date_str (str): The end date in the format "YYYY-MM-DD".
            limit (int): The number of random dates to generate (default: 1).

        Returns:
            list: A list of random datetime objects.

        """
        start_date = datetime.datetime.strptime(start_date_str, "%Y-%m-%d")
        end_date = datetime.datetime.strptime(end_date_str, "%Y-%m-%d")

        dates = []
        delta = end_date - start_date

        for _ in range(limit):
            random_days = random.randint(0, delta.days)
            random_date = start_date + datetime.timedelta(days=random_days)
            dates.append(random_date)

        return dates

    def gen_trades(self, start: str = None, end: str = None, assetClass: str = None,
                   maxPrice: int = None, minPrice: int = None, tradeType: str = None, tradeId: int = None,
                   trader: str = None, instrumentId=None, counterparty=None, instrumentName: str = None):
        """
        Generate mock trade data.

        Args:
            start (str): The start date for generating trade data.
            end (str): The end date for generating trade data.
            assetClass (str): The asset class of the instrument traded (default: None).
            maxPrice (int): The maximum price of the trade (default: None).
            minPrice (int): The minimum price of the trade (default: None).
            tradeType (str): The type of the trade (default: None).
            tradeId (int): The unique ID of the trade (default: None).
            trader (str): The name of the trader (default: None).
            instrumentId: The ID of the instrument traded (default: None).
            counterparty: The counterparty the trade was executed with (default: None).
            instrumentName (str): The name of the instrument traded (default: None).

        Returns:
            Trade: A Trade object generated with the provided parameters.

        """
        td = {
            "buySellIndicator": None,
            "price": None,
            "quantity": None
        }

        t = {
            "assetClass": None,
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
