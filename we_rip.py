from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options as OptChrome
from selenium.webdriver.firefox.options import Options as OptFirefox
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import selenium
import os
import time
import re

def write_addresses():
    content = driver.page_source
    str_ban = 'Too many requests. If you need to process'
    if str_ban in content:
        log_file.write('[*] Error, sleeping, url: ' + str(driver.current_url))
        time.sleep(60)
        driver.refresh()
    time.sleep(3)
    for word in content.split():
        regex_add = re.search(btc_pattern, word)
        if regex_add:
            print(regex_add.group())
            output_file.write(regex_add.group() + '\n')
            log_file.write(driver.current_url)
            
def status_check():
    read_time = open('time_check.txt', 'r').read()
    if time.time() - float(read_time) > 900:
        write_file = open('time_check.txt', 'w')
        write_file.write(str(time.time()))
        write_file.close()
        output_file.close()  
        output_file = open("out.txt", "a")    
        print('Sleeping for 60 seconds...')
        time.sleep(60)
    
            
if os.path.exists('out.txt'):
    os.remove('out.txt')

exchanges_list = ["Huobi.com-2", "Bittrex.com", "Luno.com", "Poloniex.com", "Kraken.com", 'Kraken.com-old', "BTC-e.com", "BitZlato.com", "Bitstamp.net", "LocalBitcoins.com", "MercadoBitcoin.com.br", "Cryptsy.com", "Binance.com", "Bitcoin.de", "Cex.io", "BtcTrade.com", "YoBit.net", "OKCoin.com", "CoinSpot.com.au", "BTCC.com", "BX.in.th", "HitBtc.com", "MaiCoin.com", "Bter.com", "Hashnest.com", "AnxPro.com", "BitBay.net", "Bleutrade.com", "Bitfinex.com", "CoinHako.com", "Matbea.com", "CoinMotion.com", "Bit-x.com", "VirWoX.com", "Paxful.com", "BitBargain.co.uk", "SpectroCoin.com", "Cavirtex.com", "C-Cex.com", "TheRockTrading.com", "FoxBit.com.br", "Vircurex.com", "BitVC.com", "Exmo.com", "Btc38.com", "Igot.com", "BlockTrades.us", "SimpleCoin.cz", "FYBSG.com", "CampBX.com", "CoinTrader.net", "Bitcurex.com", "Coinmate.io", "Korbit.co.kr", "Vaultoro.com", "Exchanging.ir", "796.com", "HappyCoins.com", "BtcMarkets.net", "ChBtc.com", "Coins-e.com", "LiteBit.eu", "CoinCafe.com", "UrduBit.com-c", "BTradeAustralia.com", "MeXBT.com", "Coinomat.com", "OrderBook.net", "LakeBTC.com", "BitKonan.com", "QuadrigaCX.com", "Banx.io", "CleverCoin.com", "Gatecoin.com", "Indacoin.com", "CoinArch.com", "BitcoinVietnam.com.vn", "CoinChimp.com", "Cryptonit.net", "Coingi.com", "Exchange-Credit.ru", "Bitso.com", "Coinimal.com", "EmpoEX.com", "Ccedk.com", "UseCryptos.com", "Coinbroker.io", "BTC-e.com-output", "BTC-e.com-old", "Bitstamp.net-old", "LocalBitcoins.com-old", "Cryptsy.com-old", "Binance.com-old", "Bitcoin.de-old", "OKCoin.com-2", "BTCC.com-old", "BTCC.com-old2", "HitBtc.com-old", "Bter.com-old", "Bter.com-old2", "Bter.com-old3", "Bter.com-cold", "Bitfinex.com-old", "Bitfinex.com-old2", "C-Cex.com-old", "TheRockTrading.com-old", "FoxBit.com.br-2", "FoxBit.com.br-cold", "FoxBit.com.br-cold-old", "SimpleCoin.cz-old", "SimpleCoin.cz-old2", "SimpleCoin.cz-old3", "SimpleCoin.cz-old4", "SimpleCoin.cz-old5", "CampBX.com-old", "BTradeAustralia.com-incoming", "Banx.io-old", "Banx.io-old2", "Gatecoin.com-2", "Cryptonit.net-old"]

#completed_list = []



btc_pattern = '(bc1|[13])[a-zA-HJ-NP-Z0-9]{25,39}'

output_file = open("out.txt", "a")
log_file = open('log.txt', 'a')

if os.path.exists('C:\Program Files\Google\Chrome Beta\Application\chrome.exe1'):
    options = OptChrome()
    options.binary_location = r'C:\Program Files\Google\Chrome Beta\Application\chrome.exe'
    #options.add_argument('headless')
    driver = webdriver.Chrome("chromedriver", options=options)

else:
    options = OptFirefox()
    options.binary_location = r'C:\Program Files\Mozilla Firefox\firefox.exe'
    #options.add_argument('--headless')
    driver = webdriver.Firefox("", options = options)    

for exchange in exchanges_list:
    try:
        output_file.write('Exchange: ' + exchange)
        output_file.write('\n')
        driver.get('https://walletexplorer.com/wallet/' + exchange + '/addresses')
        write_addresses()    
        while True:
            try:
                driver.find_element(By.LINK_TEXT, 'Next…').click()
                write_addresses()
            except selenium.common.exceptions.NoSuchElementException:    
                driver.find_element(By.LINK_TEXT, 'Last').click()
                write_addresses() 
                output_file.write('\n')
                break
    except selenium.common.exceptions.NoSuchElementException:
        continue

output_file.close()   
log_file.close() 
input('Press \'ENTER\' key to exit...')



