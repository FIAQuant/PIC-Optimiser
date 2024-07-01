# PIC-Optimiser

Example code for portfolio optimiser

Portfolio Optimiser is a Python package designed to optimise investment portfolios using historical stock data from Yahoo Finance. It provides a simple tool for fetching data, calculating portfolio metrics, and optimising asset allocations based on modern portfolio theory.

## Features

- **Data Fetching**: Fetch historical stock data from Yahoo Finance for specified tickers and date range.
- **Portfolio Metrics**: Calculate mean returns, covariance matrix, and Sharpe ratio for portfolio evaluation.
- **Optimisation Algorithms**: Implement optimisation algorithms to find optimal asset allocations by maximising the Sharpe ratio.

## Installation

Clone the repository:
```bash
git clone https://github.com/FIAQuant/PIC-Optimiser.git
pip install -r requirements.txt
```

## Usage Example

```python
from portfolio_optimiser.main
import Main

if __name__ == "__main__":
    tickers = ['AAPL', 'MSFT', 'GOOG', 'AMZN', 'NVDA']
    start_date = '2000-01-01'
    end_date = '2024-01-01'
    main = Main(tickers, start_date, end_date)
    main.run_optimisation()
```

### Input
- **Tickers**: List of stock tickers (e.g., `['AAPL', 'MSFT', 'GOOG', 'AMZN', 'NVDA']`).
- **Start Date**: Start date for historical data (e.g., `'2000-01-01'`).
- **End Date**: End date for historical data (e.g., `'2024-01-01'`).

### Output
- **Optimised Weights**: Allocation percentages for each stock.
- **Optimised Performance**: Standard deviation, returns, and Sharpe ratio of the optimised portfolio.

## Contributing

Contributions are welcome! Please feel free to fork the repository and submit pull requests or open issues for bugs or feature requests.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

This package utilises `yfinance`, `numpy`, `scipy`, and `pandas`. 
Inspiration for portfolio optimisation techniques comes from modern portfolio theory.

## Contact

Azim Patel  
GitHub: [FIAQuant](https://github.com/FIAQuant)  
Email: N/A

