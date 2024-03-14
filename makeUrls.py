date = "0306"
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

# print(makeURL(fromNagoya[1],*data["kanazawa"],date))


#Making all the urls for coming to nagoya and backing.
def makeNextPages(date="0310"):
    urlList =[]
    for i in data:

        urlList.append(makeURL(fromNagoya[1],*data[i],date))
        urlList.append(makeURL(fromNagoya[0],*data[i],date))
    return urlList