import requests, time
from bs4 import BeautifulSoup as bs
from ua_parser import user_agent_parser
from rich import print

url=[]
class tracker:
    def __init__(self):
       self.c = requests.Session()
       self.url = "https://tracker.iplocation.net/ip_shortener"
       self.headers= {"User-Agent":"Mozilla/5.0 (Linux; Android 10; SM-M315F Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/80.0.3987.99 Mobile Safari/537.36"}

    def getTrackedUrl(self):
       data ={"source_url":"https://instagram.com"}
       response = self.c.post(self.url, data=data, headers=self.headers)
       soup = bs(response.text, "html.parser")
       find = soup.find("table",attrs={"class":"table table-hover table-striped"})
       urls = find.find_all("a")
       share_url = urls[0].text
       data_url = urls[2].text
       #rpl = data_url.replace(" ","")
       url.append(data_url.replace(" ",""))
       print(share_url)

    def getData(self):
       # create dictionary
       data = {"time":"",
               "ip_address":"",
               "country":"",
               "region":"",
               "city":"",
               "language":"",
               "isp":"",
               "os":"",
               "proxy":"",
               "device":"",
               "battery_level":"",
               "battery_charge":""}
       while True:
         response = self.c.get(url[0], headers=self.headers)
         soup = bs(response.text, 'html.parser')
         find = soup.find("a",attrs={"class":"advanc-log"})
         if find==None:
           continue
           #x = f"{find}[italic red]=>data not found[/italic red]"
           #print(x,url)
         else:
           ua = find.get("data-user_agent")
           parsed = user_agent_parser.Parse(ua)
           device = parsed["device"]["family"]
           os = parsed["os"]["family"] + parsed["os"]["major"]
       #save the dict
           data["time"]=find.get("data-date")
           data["ip_address"]=find.get("data-ip_address")
           data["country"]=find.get("data-country")
           data["region"]=find.get("data-region")
           data["city"]=find.get("data-city")
           data["language"]=find.get("data-language")
           data["isp"]=find.get("data-isp")
           data["os"]=os
           data["proxy"]=find.get("data-proxy")
           data["device"]=device
           data["battery_level"]=find.get("data-battery_level")
           data["battery_charge"]=find.get("data-battery_charge")
           print(data)

           usr_action = input("Press enter to show data")
           time.sleep(2)

run=tracker()
run.getTrackedUrl()
run.getData()
#3xyrun.showDetailsData()
