import numpy as np

compounded = []

def volatility(data):
	return float(np.std(data, ddof=1))

def total_returns(data):
	c = 1
	for r in data:
		c *= (1 + r)

	returns = c - 1
	return returns

def cagr(data):
	c = 1
	for r in data:
		c *= (1 + r)
		compounded.append(c)

	yr = len(data) / 252
	cagr = compounded[-1] ** (1 / yr) - 1
	return cagr

def max_drawdown(data):
	peak = data[0]
	mdd = 0

	for x in data:
		peak = max(peak, x)
		dd = (x - peak) / peak   
		mdd = min(mdd, dd)

	return abs(mdd)  

def sharpe(data, risk_free_rate):
	m = float(np.mean(data))
	sd = float(np.std(data, ddof=1))
	sharpe = (m - risk_free_rate) / sd
	return sharpe
