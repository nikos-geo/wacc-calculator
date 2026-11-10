import yfinance as yf
import math

while True:
    symbol = input("Please enter a valid ticker symbol to get a WACC estimate: ").upper()
    ticker = yf.Ticker(symbol)

    # Get financial statements and ticker information
    bs = ticker.get_balance_sheet()
    income_st = ticker.get_income_stmt()
    tick_info = ticker.info

    # Get interest expense
    try:
        int_exp = abs(float(income_st.loc["InterestExpense"].iloc[0]))
    except (KeyError, ValueError, TypeError, IndexError):
        int_exp = 0
    if math.isnan(int_exp):
        int_exp = 0

    # Get total debt
    try:
        total_debt = float(bs.loc["TotalDebt"].iloc[0])
    except (KeyError, ValueError, TypeError):
        raise ValueError("No debt data found")
    if math.isnan(total_debt):
        raise ValueError("No debt data found")

    #Get cost of debt
    if math.isnan(int_exp) or math.isnan(total_debt):
        cost_of_debt = 0
    elif total_debt == 0:
        cost_of_debt = 0
    else:
        cost_of_debt = int_exp / total_debt

    # Get beta
    beta = tick_info.get("beta")

    # Get risk free rate
    rf = yf.Ticker("^TNX").history(period="5d")["Close"].iloc[-1] / 100

    # Get market risk premium 
    mrp = 0.0446  # Assuming a market risk premium of 4.46% according to Aswath Damodaran's data (Update January 2026 as of 10/11/2026)


    # Get cost of equity using CAPM
    if beta is None or math.isnan(beta):
        raise ValueError("No beta found")
    else:   
        cost_of_equity = rf + beta * (mrp)  

    # Get market value of equity
        market_cap = tick_info.get("marketCap")
    if market_cap is None:
        raise ValueError("No market cap found")

    # Get firm value
    firm_value = market_cap + total_debt

    # Get tax rate
    try:
        tax_rate = float(income_st.loc["TaxRateForCalcs"].iloc[0])
    except (KeyError, TypeError, ValueError):
        raise ValueError("No tax rate found.")
    if math.isnan(tax_rate):
        raise ValueError("No tax rate found.")
    if tax_rate >= 1 or tax_rate < 0:
        raise ValueError("Something went wrong with the tax rate")

    wacc = (((market_cap / firm_value) * cost_of_equity) + ((total_debt / firm_value) * (cost_of_debt*(1 - tax_rate))))
    print(f"For the company {symbol}: ") 
    print(f"WACC: {wacc:.2%}")
    print(f"Market capitalization: {market_cap:.2f}")
    print(f"Total debt: {total_debt:.2f}")
    print(f"Firm value: {firm_value:.2f}")
    print(f"Cost of equity: {cost_of_equity:.2%}")
    print(f"Cost of debt: {cost_of_debt:.2%}")
    print(f"Tax rate: {tax_rate:.2%}")

    answer = input("Would you like to see the estimated WACC of another company? (y/n) ")
    if answer == "n":
        break
