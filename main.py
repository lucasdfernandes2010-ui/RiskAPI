
from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn
from typing import List
from util import metrics as m


class MetricsInput(BaseModel):
    returns: List[float]
    risk_free_rate: float = 0.0

class MetricsOutput(BaseModel):
    volatility: float
    cagr: float
    max_drawdown: float
    sharpe: float
    total_return: float


app = FastAPI()

@app.get("/")
def home():
    return {"message": "Welcome to the Risk Analytics API. Use /metrics to get portfolio metrics."}

@app.post("/metrics", response_model=MetricsOutput)
def metrics(data: MetricsInput):
    returns = data.returns
    rf = data.risk_free_rate
    return MetricsOutput(
        volatility=m.volatility(returns),
        cagr=m.cagr(returns),
        max_drawdown=m.max_drawdown(returns),
        sharpe=m.sharpe(returns, rf),
        total_return=m.total_returns(returns)
    )

@app.get("/info")
def info():
    return {
      "volatility": "Volatility measures how much returns fluctuate and shows the overall risk of the asset.",
      "max_drawdown": "Max drawdown represents the largest peak-to-trough loss during the period.",
      "sharpe_ratio": "Sharpe ratio shows how much excess return you earn per unit of volatility.",
      "cagr": "CAGR is the average annual growth rate of the investment assuming smooth compounding.",
      "total_return": "Total return is the overall percentage gain or loss over the entire period."
    }