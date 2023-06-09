from fastapi import FastAPI
from elasticsearchPlugin import DatabasePlugin

app = FastAPI()
db = DatabasePlugin()


@app.get("/list")
def listing_trades(trader: str, start: str, end: str, instrumentId=None, sort_by: str = None, max_rows: int = None):
    """
    Get a list of trades based on the specified criteria.

    Args:
        trader (str): The name of the trader.
        start (str): The start date for filtering trades.
        end (str): The end date for filtering trades.
        instrumentId: The ID of the instrument traded (default: None).
        sort_by (str): The field by which to sort the trades (default: None).
        max_rows (int): The maximum number of rows to retrieve (default: None).

    Returns:
        dict: The result containing the list of trades matching the criteria.

    """
    result = db.get_list(max_rows=max_rows, trader=trader, start=start, end=end,
                         instrumentId=instrumentId, sort_by=sort_by)
    return {"_source": result}


@app.get("/trade_id")
def single_trade(id):
    """
    Get a single trade with the specified trade ID.

    Args:
        id: The unique ID of the trade.

    Returns:
        dict: The result containing the trade with the specified trade ID.

    """
    result = db.get_trade(id)
    return {"_source": result}


@app.get("/search")
def search_trade(search, sort_by: str = None):
    """
    Search for trades based on the specified criteria.

    Args:
        search: The search criteria.
        sort_by (str): The field by which to sort the trades (default: None).

    Returns:
        dict: The result containing the list of trades matching the search criteria.

    """
    result = db.get_search(search, sort_by)
    return {"_source": result}


@app.get("/advance")
def advance_filtering(start: str, end: str, assetClass: str = None,
                      maxPrice: int = None, minPrice: int = None, tradeType: str = None, sort_by: str = None):
    """
    Perform advanced filtering on trades based on the specified criteria.

    Args:
        start (str): The start date for filtering trades.
        end (str): The end date for filtering trades.
        assetClass (str): The asset class of the instrument traded (default: None).
        maxPrice (int): The maximum price of the trade (default: None).
        minPrice (int): The minimum price of the trade (default: None).
        tradeType (str): The type of the trade (default: None).
        sort_by (str): The field by which to sort the trades (default: None).

    Returns:
        dict: The result containing the list of trades matching the filtering criteria.

    """
    result = db.get_filtered(start, end, assetClass,
                             maxPrice, minPrice, tradeType, sort_by)
    return {"_source": result}
