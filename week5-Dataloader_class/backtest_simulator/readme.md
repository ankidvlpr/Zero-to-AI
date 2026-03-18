# BTC Strategy Simulator

A simple Python backtest engine to test an SMA-based BTC trading strategy on historical data before risking real money.

Built with core Python (`csv` module only) as a learning project.

## Overview

This project simulates trading on old BTC OHLCV data.
It helps answer one question: if this strategy was used in the past, would it make or lose money?

Strategy logic:

- `BUY` when `Close > SMA(period)`
- `SELL` when `Close < SMA(period)`
- `HOLD` when `Close == SMA(period)`
- `No signal yet` for candles before SMA warm-up is complete

## What Is OHLCV?

Each CSV row contains:

| Column | Meaning |
| --- | --- |
| `Open` | Price at start of candle |
| `High` | Highest price in candle |
| `Low` | Lowest price in candle |
| `Close` | Price at end of candle |
| `Volume` | Amount traded |

This simulator uses only the `Close` column.

## What Is SMA?

SMA (Simple Moving Average) is the average of the last `N` closing prices.

Example:

```text
closes = [9640, 9657, 9651, 9647, 9636]
SMA(3) = (9651 + 9647 + 9636) / 3 = 9644.67
```

Smaller SMA periods react faster and produce more signals.
Larger SMA periods react slower and produce fewer signals.

## Project Structure

```text
backtest_engine.py   # main simulator class
sample_prices.csv    # historical BTC OHLCV data
readme.md            # this file
```

## Requirements

- Python 3.x
- No third-party packages

## Run

From this folder:

```bash
python backtest_engine.py
```

## Usage Examples

### Basic Backtest

```python
from backtest_engine import StrategySimulator

sim = StrategySimulator()
sim.load("sample_prices.csv")
sim.backtest(5)
print(sim.stats())
```

### Check SMA Values

```python
from backtest_engine import StrategySimulator

sim = StrategySimulator()
sim.load("sample_prices.csv")
sma_values = sim.sma(5)
print(sma_values[:10])
```

### Check Signals

```python
signals = sim.generate_signals(5)
print(signals[:20])
print(signals.count("BUY"))
print(signals.count("SELL"))
```

### Compare SMA Periods

```python
from backtest_engine import StrategySimulator

for period in [3, 5, 10, 20]:
    sim2 = StrategySimulator()
    sim2.load("sample_prices.csv")
    sim2.backtest(period)
    result = sim2.stats()
    print(
        f"Period {period:>2} | "
        f"Return: {result['total return']:>7.2f}% | "
        f"Trades: {result['totaltrades']}"
    )
```

## Class Methods

| Method | Purpose |
| --- | --- |
| `load(path)` | Reads CSV and stores close prices |
| `sma(period)` | Computes rolling SMA values |
| `generate_signals(period)` | Creates BUY/SELL/HOLD signals |
| `backtest(period)` | Simulates all-in/all-out trades |
| `stats()` | Returns return %, trade count, win rate, final cash |

## Backtest Rules

- Starting cash: `10000`
- One position at a time (`position = 0` or `1`)
- On `BUY`: convert all cash to BTC
- On `SELL`: convert all BTC to cash

## Notes

- This is a learning simulator, not production trading software.
- It does not include fees, slippage, partial position sizing, or risk management.
- Results can change significantly with different SMA periods and datasets.

## Data Sources (Optional)

You can test with your own CSV from:

- Yahoo Finance (`BTC-USD` historical data)
- Binance data portal
- CryptoDataDownload

Make sure the CSV includes a `Close` column.
