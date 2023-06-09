from datagenerator import DataGenerator
import random


class Elasticsearch(DataGenerator):

    def match(self, trader: str, start: str, end: str, instrumentId=None, max_rows: int = None):
        return [self.gen_trades(trader=trader, start=start, end=end, instrumentId=instrumentId) for i in
                range(max_rows if max_rows else random.randint(5, 20))]

    def get(self, trade_id):
        return self.gen_trades(tradeId=trade_id)

    def multi_match(self, search):
        ran = {random.choice(["counterparty",
                              "instrumentId",
                              "instrumentName",
                              "trader"]): search}

        return [self.gen_trades(**ran) for i in range(random.randint(1, 10))]

    def advance_match(self, start: str, end: str, assetClass: str = None,
                      maxPrice: int = None, minPrice: int = None, tradeType: str = None):
        return [self.gen_trades(start=start, end=end, assetClass=assetClass,
                                maxPrice=maxPrice, minPrice=minPrice, tradeType=tradeType) for i in
                range(random.randint(5, 20))]
