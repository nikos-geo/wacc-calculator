# wacc-calculator
A small python script that estimates the WACC for any publicly traded US company with data from Yahoo finance.

How it works
Input	Source / method
1) Market cap, beta 	are derived from Yahoo Finance (yfinance)
2) Total debt, interest expense, tax rate	are derived from the latest annual balance sheet and income statement
3) Risk-free rate	is the US 10-year Treasury yield (^TNX)
4) Market risk premium	is fixed at 4.46% (Damodaran, January 2026 updated)

Formulas:
Cost of equity (CAPM) = risk-free rate + beta × market risk premium
Cost of debt = interest expense / total debt
WACC = E/(D+E) × cost of equity + D/(D+E) × cost of debt × (1 − tax rate)

How to use it: Enter a ticker symbol when prompted (e.g. JBL). The script prints the WACC along with its inputs:
1) For the company JBL:
2) WACC: X.XX%
3) Market capitalization: ...
4) Total debt: ...
5) Firm value: ...
6) Cost of equity: X.XX%
7) Cost of debt: X.XX%
8) Tax rate: X.XX%

Limitations:
1) The data is unofficial. Yahoo finance data comes from the yfinance library which is not an official API. Fields may be missing or
   change without warning.
2) US assumptions. The risk free rate and market risk premium are US-based and companies reporting in other currencies will make the script
   give inconsistent or wrong results.
3) Rough estimate of cost of debt. Interest expense divided by total debt is an estimation and Yahoo's total debt may also include lease obligations.
4) Yahoo's tax rate is a calculated rate and may differ from the statutory rate.
5) Update the market risk premium in the code when a new estimate is published.

Important disclaimer: 
This script may be used for educational purposes and is no way financial advise.
