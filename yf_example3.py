"""yf_example3 -> """

import os
import toolkit_config as cfg
import yf_example2

def qan_prc_to_csv(year):
    """Download Qantas stock prices for a given year into a CSV file"""
    StartYr = f"{year}-01-01"
    EndYr = f"{year}-12-31"
    print(StartYr)
    pth = os.path.join(cfg.DATADIR, f"qan_prc_{year}.csv")
    yf_example2.yf_prc_to_csv('QAN.AX', pth, start = StartYr, end = EndYr)


if __name__ == "__main__":
    qan_prc_to_csv(2020)