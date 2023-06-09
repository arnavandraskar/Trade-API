from elasticsearchDB import Elasticsearch
from typing import List, Optional
from lib.utils import Trade


class DatabasePlugin(Elasticsearch):
    def get_sorted(self, lst: List[Trade], sort_by: str):
        try:
            lst.sort(key=lambda trade: getattr(trade, sort_by))
        except AttributeError:
            return {"error": "Invalid field for sorting"}

        return lst

    def get_list(self, trader: str, start: str, end: str, instrumentId=None, max_rows: int = None, sort_by: str = None):
        result = self.match(max_rows=max_rows, trader=trader, start=start, end=end, instrumentId=instrumentId)
        if sort_by:
            return self.get_sorted(result, sort_by=sort_by)
        return result

    def get_trade(self, id):
        return self.get(trade_id=id)

    def get_search(self, search, sort_by: str = None):
        result = self.multi_match(search)
        if sort_by:
            return self.get_sorted(result, sort_by=sort_by)
        return result

    def get_filtered(self, start: str, end: str, assetClass: str = None,
                     maxPrice: int = None, minPrice: int = None, tradeType: str = None, sort_by: str = None):
        result = self.advance_match(start=start, end=end, assetClass=assetClass, maxPrice=maxPrice,
                                    minPrice=minPrice, tradeType=tradeType)
        if sort_by:
            return self.get_sorted(result, sort_by=sort_by)
        return result
