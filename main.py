import yfinance
' some text '.strip

a = "AB"
print(a.lower)

asx_value = 7111.4
date = "2021-01-25"
units = 1
currency = "AUD"
print(f"The closing value of {units} unit of the All Ordinaries on {date} was {asx_value} {currency}.")

# Downloads Qantas share price beginning 1 January 2020

tic = "QAN.AX"
start = '2020-01-01'
end = None
df = yfinance.download(tic, start, end)
print(df)
df.to_csv('qan_stk_prc.csv')