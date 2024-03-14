import requests

# URL of the website you want to scrape
url = 'https://www.highwaybus.com/gp/reservation/rsvPlanList?mode=search&route=2&lineId=650&nearCheckOnStation=on&nearCheckOffStation=&onStationCd=400&offStationCd=8171&bordingDate=20240316&danseiNum=2&zyoseiNum=0&adultMen=2&adultWomen=0&childMen=0&childWomen=0&handicapAdultMen=0&handicapAdultWomen=0&handicapChildMen=0&handicapChildWomen=0#infomationArea'

# Send a GET request to the URL
response = requests.get(url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # # Print the HTML content of the website
    # print(response.text)
     # Open a new file in write mode
    with open('output.html', 'w', encoding='utf-8') as f:
        # Write the HTML content to the file
        f.write(response.text)
    print('HTML content saved to output.html')
else:
    print('Failed to retrieve the webpage')
