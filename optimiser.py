import numpy as np
from scipy.optimize import minimize
from portfolio import Portfolio


class Optimiser:

    """
    Optimises a given portfolio to maximise the Sharpe ratio (minimise negative Sharpe ratio).
    """
    def __init__(self, portfolio: Portfolio, risk_free_rate: float =0.0, allow_short: bool = True):
        """
        Initialises the Optimiser with a portfolio and risk-free rate.

        Parameters:
        portfolio (Portfolio): The portfolio to optimise.
        risk_free_rate (float): The risk-free rate, default is 0.0.
        allow_short (bool): Flag indicating whether short selling is allowed, default is True.
        """
        self.portfolio = portfolio
        self.risk_free_rate = risk_free_rate
        self.allow_short = allow_short
        self.num_assets = self.portfolio.get_num_assets()
        self.results = None

    def portfolio_performance(self, weights: np.ndarray):
        """
        Calculates the portfolio performance.

        Parameters:
        weights (np.ndarray): Asset weights in the portfolio.

        Returns:
        tuple: Standard deviation and returns of the portfolio.
        """
        returns = np.sum(self.portfolio.get_mean_returns() * weights) * 252
        std = np.sqrt(np.dot(weights.T, np.dot(self.portfolio.get_cov_matrix(), weights))) * np.sqrt(252)
        return std, returns

    def neg_sharpe_ratio(self, weights: np.ndarray):
        """
        Calculates the negative Sharpe ratio of the portfolio.

        Parameters:
        weights (np.ndarray): Asset weights in the portfolio.

        Returns:
        float: Negative Sharpe ratio.
        """
        std, returns = self.portfolio_performance(weights)
        return -(returns - self.risk_free_rate) / std

    def optimise(self):
        """
        Optimises the portfolio to maximize the Sharpe ratio.

        Returns:
        OptimizeResult: The result of the optimization.
        """
        constraints = ({'type': 'eq', 'fun': lambda x: np.sum(x) - 1})
        bounds = tuple(((-np.inf, np.inf) if self.allow_short else (0, 1)) for _ in range(self.num_assets))
        initial_weights = self.num_assets * [1. / self.num_assets]

        opts = minimize(self.neg_sharpe_ratio, initial_weights, method='SLSQP', bounds=bounds, constraints=constraints)

        self.results = opts
        return opts

    def get_optimised_weights(self):
        """
        Returns the optimised asset weights.

        Returns:
        np.ndarray: Optimised asset weights.

        Raises:
        ValueError: If the optimiser has not been run yet.
        """
        if self.results is None:
            raise ValueError("Optimiser has not been run yet.")
        return self.results.x

    def get_optimised_performance(self):
        """
        Returns the performance of the optimised portfolio.

        Returns:
        tuple: Standard deviation, returns, and Sharpe ratio of the optimised portfolio.

        Raises:
        ValueError: If the optimiser has not been run yet.
        """
        if self.results is None:
            raise ValueError("Optimiser has not been run yet.")
        std, returns = self.portfolio_performance(self.results.x)
        sharpe_ratio = (returns - self.risk_free_rate) / std
        return std, returns, sharpe_ratio
