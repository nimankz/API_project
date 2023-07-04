
#============================================libraries======================================
import datetime
from selenium import webdriver
import pickle
#============================================libraries======================================
#============================================class==========================================
class crypto:
    def __init__(self):
        self.url="https://coinmarketcap.com"
        self.browser=webdriver.Chrome()
        self.browser.get(self.url)
        self.universal_dict={}

    def fristOpen(self):
        try:
            mydict = {}
            for item in range(1,11):
                stritem=str(item)
                name = self.browser.find_element("xpath",
                    f'//*[@id="__next"]/div/div[1]/div[2]/div/div[1]/div[4]/table/tbody/tr[{stritem}]/td[3]/div/a/div/div/p').text
                price = self.browser.find_element("xpath",
                    f'//*[@id="__next"]/div/div[1]/div[2]/div/div[1]/div[4]/table/tbody/tr[{stritem}]/td[4]/div/a/span').text
                symbol=self.browser.find_element("xpath",f'//*[@id="__next"]/div[2]/div[1]/div[2]/div/div[1]/div[4]/table/tbody/tr[{stritem}]/td[3]/div/a/div/div/div/p').text
                oneHprofit=self.browser.find_element("xpath",f'//*[@id="__next"]/div[2]/div[1]/div[2]/div/div[1]/div[4]/table/tbody/tr[{stritem}]/td[5]/span').text
                if "..." in price:
                    price = "too much numbers"
                    # try to find a way to fix this problem!
                mydict[symbol] = {"rate": stritem, "price": price,"name":name}
            mydict["time"]=str(datetime.datetime.now())
            myfile=open(r'lastInfo.txt',"wb")
            pickle.dump(mydict,myfile)
            myfile.close()
            self.universal_dict=mydict

            return mydict
        except:
            myfile=open(r'lastInfo.txt',"rb")
            mydict=pickle.load(myfile)
            myfile.close()
            self.universal_dict=mydict
            return [f"Sorry there was a problem in fetching uptaded data, here is prices in {mydict['time']}",mydict]

    def convert(self,crypto1,num1:int,crypto2):
        answer=(int(self.universal_dict[crypto1]["price"][1:])*num1)/(int(self.universal_dict[crypto2]["price"][1:]))
        return answer

    def findHarderOne(self,name):
        pass

    def goToPage(self,name: str):
        try:
            self.browser.find_element("xpath",
                '//*[@id="__next"]/div/div[1]/div[2]/div/div[1]/div[4]/table/tbody/tr[' + self.universal_dict[name]["rate"] +
                ']/td[3]/div/a').click()
            self.tempurl=str(self.browser.current_url)
            return self.tempurl
        except:
            return ["Unfortunately there was some problem in fetching data but we guess you are looking for this url:"
                    ,str(self.url)+f"/currencies/{(self.universal_dict[name]['name']).lower()}/"]
#============================================class==========================================
#============================================defs==========================================
