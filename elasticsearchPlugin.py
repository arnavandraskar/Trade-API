from elasticsearchDB import Elasticsearch
from typing import List, Optional
from lib.utils import Trade


class DatabasePlugin(Elasticsearch):
    def get_sorted(self, lst: List[Trade], sort_by: str):
        """
        Sort the list of trades based on the specified field.

        Args:
            lst (List[Trade]): The list of Trade objects to be sorted.
            sort_by (str): The field by which to sort the trades.

        Returns:
            Union[List[Trade], Dict[str, str]]: The sorted list of trades if the sort field is valid,
            otherwise a dictionary with an error message.

        """
        try:
            lst.sort(key=lambda trade: getattr(trade, sort_by))
        except AttributeError:
            return {"error": "Invalid field for sorting"}

        return lst

    def get_list(self, trader: str, start: str, end: str, instrumentId=None, max_rows: int = None,
                 sort_by: str = None):
        """
        Get a list of trades matching the specified criteria.

        Args:
            trader (str): The name of the trader.
            start (str): The start date for generating trade data.
            end (str): The end date for generating trade data.
            instrumentId: The ID of the instrument traded (default: None).
            max_rows (int): The maximum number of rows to generate (default: None).
            sort_by (str): The field by which to sort the trades (default: None).

        Returns:
            Union[List[Trade], Dict[str, str]]: The list of trades matching the criteria if successful,
            otherwise a dictionary with an error message.

        """
        result = self.match(max_rows=max_rows, trader=trader, start=start, end=end, instrumentId=instrumentId)
        if sort_by:
            return self.get_sorted(result, sort_by=sort_by)
        return result

    def get_trade(self, id):
        """
        Get a trade with the specified trade ID.

        Args:
            id: The unique ID of the trade.

        Returns:
            Trade: The Trade object with the specified trade ID.

        """
        return self.get(trade_id=id)

    def get_search(self, search, sort_by: str = None):
        """
        Get a list of trades matching the specified search criteria.

        Args:
            search: The search criteria.
            sort_by (str): The field by which to sort the trades (default: None).

        Returns:
            Union[List[Trade], Dict[str, str]]: The list of trades matching the search criteria if successful,
            otherwise a dictionary with an error message.

        """
        result = self.multi_match(search)
        if sort_by:
            return self.get_sorted(result, sort_by=sort_by)
        return result

    def get_filtered(self, start: str, end: str, assetClass: str = None,
                     maxPrice: int = None, minPrice: int = None, tradeType: str = None, sort_by: str = None):
        """
        Get a list of trades matching the specified filtering criteria.

        Args:
            start (str): The start date for generating trade data.
            end (str): The end date for generating trade data.
            assetClass (str): The asset class of the instrument traded (default: None).
            maxPrice (int): The maximum price of the trade (default: None).
            minPrice (int): The minimum price of the trade (default: None).
            tradeType (str): The type of the trade (default: None).
            sort_by (str): The field by which to sort the trades (default: None).

        Returns:
            Union[List[Trade], Dict[str, str]]: The list of trades matching the filtering criteria if successful,
            otherwise a dictionary with an error message.

        """
        result = self.advance_match(start=start, end=end, assetClass=assetClass, maxPrice=maxPrice,
                                    minPrice=minPrice, tradeType=tradeType)
        if sort_by:
            return self.get_sorted(result, sort_by=sort_by)
        return result
