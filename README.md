# Trade API Documentation

This documentation provides an overview and usage details of the Trade API, which serves trade data from a mocked database. The API is built using FastAPI, a Python web framework, and utilizes Elasticsearch-like functions to fetch and manipulate trade data.

## Introduction

At SteelEye, FastAPI is used as the primary client-facing API layer. FastAPI's usage of Pydantic for expressing data types aligns well with the schema models used at SteelEye, which also utilize Pydantic.

The objective of this exercise is to build a REST API with endpoints that allow users to retrieve a list of trades, retrieve a single trade by ID, search for trades, and filter trades based on various parameters.

## API Endpoints

The Trade API provides the following endpoints:

### 1. List Trades

**Endpoint:** `/list`

**Method:** GET

**Parameters:**
- `trader` (required): The name of the trader.
- `start` (required): The start date (YYYY-MM-DD) for filtering trades.
- `end` (required): The end date (YYYY-MM-DD) for filtering trades.
- `instrumentId` (optional): The ID of the instrument to filter trades.
- `sort_by` (optional): The field name to sort the trades. (e.g., "assetClass", "tradeDateTime")

**Response:** Returns a list of trades matching the provided criteria.

### 2. Get Single Trade by ID

**Endpoint:** `/trade_id`

**Method:** GET

**Parameters:**
- `id` (required): The ID of the trade to retrieve.

**Response:** Returns the trade with the specified ID.

### 3. Search Trades

**Endpoint:** `/search`

**Method:** GET

**Parameters:**
- `search` (required): The search query to find trades.
- `sort_by` (optional): The field name to sort the search results. (e.g., "assetClass", "tradeDateTime")

**Response:** Returns a list of trades matching the search query.

### 4. Advanced Filtering of Trades

**Endpoint:** `/advance`

**Method:** GET

**Parameters:**
- `start` (required): The start date (YYYY-MM-DD) for filtering trades.
- `end` (required): The end date (YYYY-MM-DD) for filtering trades.
- `assetClass` (optional): The asset class of the instrument traded.
- `maxPrice` (optional): The maximum price for filtering trades.
- `minPrice` (optional): The minimum price for filtering trades.
- `tradeType` (optional): The type of trade (e.g., "BUY", "SELL").
- `sort_by` (optional): The field name to sort the filtered trades. (e.g., "assetClass", "tradeDateTime")

**Response:** Returns a list of trades filtered based on the provided criteria.

## Data Models

The Trade API uses the following data models:

### Trade

```python
class Trade(BaseModel):
    assetClass: Optional[str] = Field(alias="assetClass", default=None, description="The asset class of the instrument traded. E.g. Bond, Equity, FX...etc")
    counterparty: Optional[str] = Field(default=None, description="The counterparty the trade was executed with")
    instrumentId: str = Field(alias="instrumentId", description="The ISIN/ID of the instrument traded. E.g. TSLA, AAPL, AMZN...etc")
    instrumentName: str = Field(alias="instrumentName", description="The name of the instrument traded.")
    tradeDateTime: datetime.datetime = Field(alias="tradeDateTime", description="The date-time the Trade was executed")
    tradeDetails: TradeDetails = Field(alias="tradeDetails", description="The details of the trade, i.e. price, quantity")
    tradeId: str = Field(alias="tradeId", default=None, description="The unique ID of the trade")
    trader: str = Field(description="The name of the Trader")
  ```    
    
    
### Trade Details

```python
class TradeDetails(BaseModel):
    buySellIndicator: str = Field(description="A value of BUY for buys, SELL for sells.")
    price: float = Field(description="The price of the Trade.")
    quantity: int = Field(description="The amount of units traded.")
```

## Mock Database Scripts

To simulate the interaction with Elasticsearch, the following scripts are used:

### lib/utils.py
This script contains the data models Trade and TradeDetails used by the API.

### datagenerator.py
This script is responsible for generating random data for trades. It includes the DataGenerator class with methods to generate random dates and mock Elasticsearch query results.

### elasticsearchDB.py
This script implements a mock database using the Elasticsearch class, which extends the DataGenerator class. It includes methods to perform mock database operations such as matching trades, retrieving trades by ID, multi-matching searches, and advanced filtering.

### elasticsearchPlugin.py
This script provides the DatabasePlugin class, which acts as a plugin for the API. It extends the Elasticsearch class and includes methods to sort trades, fetch a list of trades, retrieve a single trade, search trades, and apply advanced filtering.

### main.py
This script serves as the entry point for the Trade API. It creates a FastAPI instance, initializes the DatabasePlugin as the database plugin, and defines the API endpoints using FastAPI decorators.

## Getting Started

To get started with the Trade API, follow these steps:

### Prerequisites

Make sure you have the following dependencies installed:

- Python (version 3.7 or higher)
- FastAPI (installed via pip)

```shell
$ pip install fastapi
```
- Uvicorn (installed via pip)

```shell
$ pip install uvicorn
```
## Running the API

To run the Trade API, use the following command:

```shell
$ uvicorn main:app --reload
```
This command starts the API using Uvicorn as the web server. The main:app parameter specifies the entry point of the application, where main refers to the main.py file and app is the instance of the FastAPI application.

The --reload flag enables automatic reloading of the server whenever the source code changes, making it convenient for development.

Once the API is running, you can access it at http://localhost:8000 in your web browser or use tools like cURL or Postman to interact with the endpoints.

Make sure to provide the required parameters in the API calls as per the defined endpoints and data models.


