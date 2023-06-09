from datagenerator import DataGenerator
import random


class Elasticsearch(DataGenerator):
    def match(self, trader: str, start: str, end: str, instrumentId=None, max_rows: int = None):
        """
        Generate a list of trades that match the specified criteria.

        Args:
            trader (str): The name of the trader.
            start (str): The start date for generating trade data.
            end (str): The end date for generating trade data.
            instrumentId: The ID of the instrument traded (default: None).
            max_rows (int): The maximum number of rows to generate (default: None).

        Returns:
            list: A list of Trade objects matching the criteria.

        """
        return [self.gen_trades(trader=trader, start=start, end=end, instrumentId=instrumentId) for i in
                range(max_rows if max_rows else random.randint(5, 20))]

    def get(self, trade_id):
        """
        Generate a single trade with the specified trade ID.

        Args:
            trade_id (int): The unique ID of the trade.

        Returns:
            Trade: A Trade object with the specified trade ID.

        """
        return self.gen_trades(tradeId=trade_id)

    def multi_match(self, search):
        """
        Generate a list of trades that match the specified search criteria.

        Args:
            search: The search criteria.

        Returns:
            list: A list of Trade objects matching the search criteria.

        """
        ran = {random.choice(["counterparty",
                              "instrumentId",
                              "instrumentName",
                              "trader"]): search}

        return [self.gen_trades(**ran) for i in range(random.randint(1, 10))]

    def advance_match(self, start: str, end: str, assetClass: str = None,
                      maxPrice: int = None, minPrice: int = None, tradeType: str = None):
        """
        Generate a list of trades with advanced matching criteria.

        Args:
            start (str): The start date for generating trade data.
            end (str): The end date for generating trade data.
            assetClass (str): The asset class of the instrument traded (default: None).
            maxPrice (int): The maximum price of the trade (default: None).
            minPrice (int): The minimum price of the trade (default: None).
            tradeType (str): The type of the trade (default: None).

        Returns:
            list: A list of Trade objects matching the advanced criteria.

        """
        return [self.gen_trades(start=start, end=end, assetClass=assetClass,
                                maxPrice=maxPrice, minPrice=minPrice, tradeType=tradeType) for i in
                range(random.randint(5, 20))]
