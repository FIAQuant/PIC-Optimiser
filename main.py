import yfinance as yf
from portfolio import Portfolio
from optimiser import Optimiser


class Main:
    """
    Main class for fetching data and running portfolio optimisation.
    """

    def __init__(self, tickers: list, start_date: str, end_date: str, risk_free_rate=0.0, allow_short=True):
        """
        Initialise the Main object.

        Parameters:
        tickers : list
            List of ticker symbols for assets.
        start_date : str
            Start date for fetching historical data.
        end_date : str
            End date for fetching historical data.
        risk_free_rate : float, optional
            Risk-free rate for calculating Sharpe ratio, default is 0.0.
        allow_short : bool, optional
            Flag indicating whether short selling is allowed, default is True.
        """
        self.tickers = tickers
        self.start_date = start_date
        self.end_date = end_date
        self.risk_free_rate = risk_free_rate
        self.data = self.fetch_data()
        self.portfolio = Portfolio(self.data)
        self.optimiser = Optimiser(self.portfolio, risk_free_rate, allow_short)

    def fetch_data(self):
        """
        Fetches historical adjusted close prices from Yahoo Finance.

        Returns:
        pd.DataFrame
            Historical adjusted close prices of the assets.
        """
        return yf.download(self.tickers, start=self.start_date, end=self.end_date)['Adj Close'].pct_change().dropna()

    def run_optimisation(self):
        """
        Runs portfolio optimisation and prints results.
        """
        self.optimiser.optimise()
        weights = self.optimiser.get_optimised_weights()
        performance = self.optimiser.get_optimised_performance()

        print("Optimised Weights:", weights)
        print("Optimised Performance (Std, Returns, Sharpe Ratio):", performance)


# Example usage:
if __name__ == "__main__":
    tickers = ['AAPL', 'MSFT', 'GOOG', 'AMZN', 'NVDA']
    start_date = '1990-01-01'
    end_date = '2024-01-01'

    main = Main(tickers, start_date, end_date, allow_short=True)
    main.run_optimisation()
