import pandas as pd


class Portfolio:
    """ Represents a portfolio of assets. """

    def __init__(self, returns: pd.DataFrame):
        """
        Initializes the Portfolio with the given returns data.

        Parameters:
        returns (pd.DataFrame): DataFrame containing the asset returns.
        """
        self.returns = returns
        self.mean_returns = returns.mean()
        self.cov_matrix = returns.cov()

    def get_num_assets(self):
        """
        Returns the number of assets in the portfolio.

        Returns:
        int: Number of assets.
        """
        return len(self.mean_returns)

    def get_mean_returns(self):
        """
        Returns the mean returns of the assets.

        Returns:
        pd.Series: Mean returns.
        """
        return self.mean_returns

    def get_cov_matrix(self):
        """
        Returns the covariance matrix of the asset returns.

        Returns:
        pd.DataFrame: Covariance matrix.
        """
        return self.cov_matrix