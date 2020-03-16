

import pandas as pd
import yfinance as yf

tker_lst = ['WMT', 'BBY', 'BBBY', 'HD', 'LOW',
            'ODP', 'AMZN', 'CONN', 'CVS', 'RAD',
            'WBA', 'KR', 'WSM', 'BGI', 'BKS',
            'AAPL', 'CMG', 'COST', 'DUK', 'FB',
            'IBB', 'LUV', 'NVDA', 'PENN', 'SNAP',
            'SQ', 'FDO', 'IBUY', 'KMX', 'ADC']

def get_prices(tker_lst=list)
    '''
    Function returns a dataframe with one month of historical prices 
    for all stock tickers in tourney. Daily percent change is calucated.

    Paramaters
    -----------
    tker_lst (list): List of stock ticker symbols to scrape


    Returns
    -----------
    Pandas dataframe with month's worth of open/close and daily percent change

    '''

    def _daily_pct_gain(open_price, close_price):
        '''
        '''

        gain = (close_price / open_price) - 1

        return gain

    tker = pd.DataFrame()

    for tk in tker_lst:

        tiker_obj = yf.Ticker(tk)
        tker_tmp = tiker_obj.history(period="1mo")

        tker_tmp = tker_tmp.reset_index()
        tker_tmp.columns = [x.lower() for x in tker_tmp.columns]
        tker_tmp['ticker'] = tk
        tker_tmp = tker_tmp[['ticker', 'date', 'open', 'close']]

        tker = tker.append(tker_tmp).reset_index(drop=True)

        print(tk)

    tker['gain_pct'] = [_daily_pct_gain(x, y)
                        for x, y in zip(tker['open'], tker['close'])]
    
    return tker




