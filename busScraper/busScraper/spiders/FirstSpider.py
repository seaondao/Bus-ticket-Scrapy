import scrapy
from busScraper.items import Options


def makeUrslsFunctino():
    date = "0314"
    fromNagoya =["&nearCheckOnStation=&nearCheckOffStation=on&","&nearCheckOnStation=on&nearCheckOffStation=&"] #0No 1Yes
    data = {
        #Routr,LineID,stationCD
        "kanazawa":['10','650','8171'], 
        "takaoka":['10','765','789'],
        "toyama":['10','760','905'],
        "fukui":['10','640','806'],
        "takayama":['15','660','769'],
        "matsumoto":['8','630','756']
    }


    def makeURL(fromNagoya,route,lineID,onStop,date):
        offStop = "400"
        if(fromNagoya == "&nearCheckOnStation=on&nearCheckOffStation=&"):# if from nagoya switch 
            onStop,offStop = offStop,onStop
        url= "https://www.highwaybus.com/gp/reservation/rsvPlanList?mode=search&route="+route+"&lineId="+lineID+fromNagoya+"onStationCd="+onStop+"&offStationCd="+offStop +"&bordingDate=2024"+date+"&danseiNum=0&zyoseiNum=2&adultMen=0&adultWomen=2&childMen=0&childWomen=0&handicapAdultMen=0&handicapAdultWomen=0&handicapChildMen=0&handicapChildWomen=0#infomationArea"
        return url

    #Making all the urls for coming to nagoya and backing.
    
    urlList =[]
    for i in data:
        urlList.append(makeURL(fromNagoya[1],*data[i],date))
        urlList.append(makeURL(fromNagoya[0],*data[i],date))

    return urlList

def comment():
    print()
    # GAVE up getting price since IDK how to make it work the CSV and which is which. Each separete eill BEARY WORK.
    # prices =[]
    #         for i in range(1,56):
    #             prices.append("#display_price_"+str(i))

    #         for id in prices:
    #             selected_item  = response.css(id)
    #             item_value = selected_item.attrib.get("value")
    #             if item_value:
    #                 yield{
    #                     'price':item_value
    #                 }
    #             else:
    #                 pass

urlList = makeUrslsFunctino()


class FirstspiderSpider(scrapy.Spider):
    name = "FirstSpider"
    allowed_domains = ["www.highwaybus.com"]
    currentNum = 0
    start_urls = [urlList[currentNum]]

    
    # for x in (range(len(urlList))):
    def parse(self, response):
        self.currentNum +=1
        

        
        itemOptions = response.css(".busSvclistItem_desc")


        # print("+++++++++++++++++++"+len(options))
        for option in itemOptions:
            item = Options()
            item['depature'] = option.css(".dep p::text")[0].get()
            item['depatureTime'] = option.css(".dep .time::text").get()
            item['arrive']= option.css(".arr p::text")[0].get()
            item['arriveTime']= option.css(".arr .time::text").get()
            item['avaiable'] = option.css('.btn-OpenHowToBuy button ::text').get()
            # 'price':option.css('.fromPrice').get()
            yield item

        if self.currentNum <= len(urlList) :
            nextUrl = urlList[self.currentNum]
        if nextUrl:
            yield response.follow(nextUrl,callback=self.parse)

        

        pass

        
        
