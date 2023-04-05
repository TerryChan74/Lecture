from bs4 import BeautifulSoup
import requests
import csv

file = open("market_indices_1.csv", "w")
writer = csv.writer(file)
writer.writerow(["INDICES", "LAST_PRICE"])

page_to_scrape = requests.get("http://www.aastocks.com/tc/stocks/market/index/hk-index-con.aspx")
soup = BeautifulSoup(page_to_scrape.text, "html.parser")

HSI = soup.find("div", class_ = "hkidx-last txt_r")
print(HSI.text)
writer.writerow(["HSI", HSI.text])

page_to_scrape = requests.get("https://www.marketwatch.com/investing/future/brn00?countrycode=uk")
soup = BeautifulSoup(page_to_scrape.text, "html.parser")


BRENT_OIL = soup.find("span", class_ = "value")
print(BRENT_OIL.text)
writer.writerow(["BrentOil", BRENT_OIL.text])

file.close()

def mk_csv_name(tic):
    tic = tic.lower()
    tic_base = tic.split('.')[0]
    csv_name = f'{tic_base}_stk_prc.csv'
    return csv_name

print(mk_csv_name("ABC"))

number = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 20, 22, 23, 25, 29, 30, 31]
def check_number1(list):
    a = 0
    even_num =[]
    for number[a] in list:
        check_num = number[a]
        if (check_num % 2 == 0):
            even_num.append(check_num)
        a += 1
    print(even_num)
check_number1(number)

lst = [2, 3, 10, 14, 20, 21, 25, 13, 15]
new_lst=[x**2 for x in lst if x**2 > 150]
print(new_lst)

number = [0, 1, 1, 2, 5, 6, 8, 2, 4, 6, 8]
final = [i for i in set(number) if i % 2 == 0]
final.sort()
print(final)
new_set = {x for x in number if x % 2 == 0}
final_lst = [x for x in new_set]
print(final_lst)

f_suburbs = dict()
f_suburbs["Fairfield"] = 18081
f_suburbs["Fairfield East"] = 5273
f_suburbs["Fairfield Heights"] = 7517
f_suburbs["Fairfield West"] = 11575
f_suburbs["Fairlight"] = 5840
f_suburbs["Fiddletown"] = 233
f_suburbs["Five Dock"] = 9356
f_suburbs["Flemington"] = None
f_suburbs["Forest Glen"] = None
f_suburbs["Forest Lodge"] = 4583
f_suburbs["Forestville"] = 8329
f_suburbs["Freemans Reach"] = 1973
f_suburbs["Frenchs Forest"] = 13473
f_suburbs["Freshwater"] = 8866

for key, value in f_suburbs.items():
    print(key, value)

    if key[0:6] != "Forest" and value is not None:
        print(f"[key]: [value]")

for i in range(0:100):
    if i % 3 == 0 and i % 5 != 0:
        print(f"{i}: Fizz")
    elif not(i % 3 == 0) and i % 5 == 0:
        print(f"{i}: Buzz")
    elif i % 15 == 0:
        print(f"{i}: FIZZ BUZZ")
    else:
        print(i)


def my_function(y):
    y = y + 1
    return y

def my_function(y):
    y = y + x
    x = 2
    y = y + x
    return y

x = 3
y = 10
y = my_function(y)

prc_dic = {
    '3000-01-15': 7.0400,
    '2020-01-14': 7.1100,
    '2020-01-13': 7.0200,
    '2020-01-02': 7.1600,
    '2020-01-03': 7.1900,
    '2020-01-06': 7.0000,
    '2020-01-07': 7.1000,
    '2020-01-08': 6.8600,
    '2020-01-09': 6.9500,
    '2020-01-10': 7.0000,
}

# replace '???' with the correct expression
sorted_keys = sorted(list(prc_dic.keys()), key = lambda x:x.split("-")[2])
prc_dic["2020-01-15"] = prc_dic["3000-01-15"]
print(prc_dic)




