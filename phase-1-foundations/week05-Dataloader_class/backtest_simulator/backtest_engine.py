import csv

class StrategySimulator:
    
    def __init__(self):
        self.data = []               # will be filled by load()
        self.trade = []              # will be filled by backtest()
        self.closes = []             # just the close prices

    def load(self, path):
        with open(path) as file:
            reader = csv.DictReader(file)
            self.data = list(reader)

            for line in self.data:
                self.closes.append(float(line["Close"]))

        print(f"Loaded {len(self.closes)} rows!")


    def sma(self, period):
        result = []
        for i in range(len(self.closes)):
            if i < period - 1:
                result.append(None)
            else:
                window = self.closes[i - period + 1 : i + 1]
                result.append(sum(window) / period)
        return result


    def generate_signals(self, period):
        result = []
        sma_list = self.sma(period)
        for i in range(len(self.closes)):
            
            if sma_list[i] == None:
                result.append("No signal yet")
                
            elif self.closes[i] > sma_list[i]:
                result.append("BUY")
            elif self.closes[i] < sma_list[i]:
                result.append("SELL")
            elif self.closes[i] == sma_list[i]:
                result.append("HOLD")

        return result


    def backtest(self, period):
        test_signal = self.generate_signals(period)

        cash = 10000
        position = 0
        btc_balance = 0

        for i in range(len(self.closes)):
            price = self.closes[i]
            if test_signal[i] == "BUY":
                if position == 0:
                    btc_balance = cash/price
                    cash = 0
                    position = 1
                    self.trade.append({"action" : "BUY", "price" : price, "btc" : btc_balance})

            elif test_signal[i] == "SELL":
                if position == 1:
                    cash = btc_balance * price
                    btc_balance = 0
                    position = 0
                    self.trade.append({"action" : "SELL", "price" : price, "cash" : cash})

        self.starting_cash = 10000
        self.final_cash = cash
        return round(cash, 2)
        
        

    def stats(self):
        final_cash = self.final_cash
        starting_cash = self.starting_cash
        trade_data = self.trade

        total_return = ((final_cash - starting_cash) / starting_cash) * 100

        total_trade = len(self.trade)

        wining_trades = 0
        total_sells = 0
        for trade in trade_data:
            if trade["action"] == "SELL":
                if trade["cash"] > 10000:
                    wining_trades += 1
                total_sells += 1
        
        if total_sells == 0:
            winrate = 0
        else:
            winrate = (wining_trades / total_sells) * 100

        return {"total return" : total_return, 
                "totaltrades" : total_trade,
                "win rate" : winrate,
                "final cash" : final_cash
        }
                



sim = StrategySimulator()
sim.load("sample_prices.csv")



# sim_values = sim.sma(3)
# print(sim_values[:10])
# print(sim.closes[:5])  # just check the first 5

signals = sim.generate_signals(3)
# print(signals[:15])

sim.backtest(5)
print(sim.stats())

