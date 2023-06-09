from fastapi import FastAPI
from elasticsearchPlugin import DatabasePlugin

app = FastAPI()
db = DatabasePlugin()


@app.get("/list")
def listing_trades(trader: str, start: str, end: str, instrumentId=None, sort_by: str = None, max_rows: int = None):
    result = db.get_list(max_rows=max_rows, trader=trader, start=start, end=end,
                         instrumentId=instrumentId, sort_by=sort_by)
    return {"_source": result}


@app.get("/trade_id")
def single_trade(id):
    result = db.get_trade(id)
    return {"_source": result}


@app.get("/search")
def search_trade(search, sort_by: str = None):
    result = db.get_search(search, sort_by)
    return {"_source": result}


@app.get("/advance")
def advance_filtering(start: str, end: str, assetClass: str = None,
              maxPrice: int = None, minPrice: int = None, tradeType: str = None, sort_by: str = None):
    result = db.get_filtered(start, end, assetClass,
                             maxPrice, minPrice, tradeType, sort_by)
    return {"_source": result}
