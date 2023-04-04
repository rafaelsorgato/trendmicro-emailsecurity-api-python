# trendmicro emailsecurity api python
how to get trend micro email security (tmes) API data with python, these code takes all logs that trigger inbound policies

<br>
<h3> 1) first step - get your emailsecurity username:</h3>
<img src="https://github.com/rafaelsorgato/trendmicro-emailsecurity-api-python/blob/main/images/emailsecurity.png">

<br><br><br>
<h3> 2) second step - get your emailsecurity api:</h3>
<img src="https://github.com/rafaelsorgato/trendmicro-emailsecurity-api-python/blob/main/images/emailsecurityapi.png">

<br><br><br>
<h3> 3) third step - get your region :</h3>
choose the url based on the location of your trend micro service and put in the variable "localization"
<br>
North America, Latin America and Asia Pacific = api.tmes.trendmicro.com<br>
Europe, the Middle East and Africa = api.tmes.trendmicro.eu<br>
Australia and New Zealand = api.tmes-anz.trendmicro.com<br>
Japan = api.tmems-jp.trendmicro.com<br>
Singapore = api.tmes-sg.trendmicro.com<br>
India = api.tmes-in.trendmicro.com<br>
I'm from Latin America, so I'll have to choose: api.tmes.trendmicro.com in the localization variable
<br><br>
<h3> 4) last step, take the data acquired in steps 1, 2 and 3 and put them in the code below (localization, username, api)</h3>
<br><br>


```
import requests
import datetime
import base64

##### PUT HERE THE DATA THAT YOU ACQUIRED IN STEPS 1,2,3 #####
localization="api.tmes.trendmicro.com" #change the url based on the location of your trend micro service
username= "test" #put the username of the account  
api="acxhxsa68423=qsdqras55468adcbba" #put you api code
##### PUT HERE THE DATA THAT YOU ACQUIRED IN STEPS 1,2,3 #####


apiusername=username+":"+api
apiusername = apiusername.encode('ascii')
finalapi = base64.b64encode(apiusername)
finalapi=str(finalapi,'utf-8')

if __name__ == '__main__':
  

  #get the current day
  currentdate = datetime.datetime.now() + datetime.timedelta(days=+1)
  currentdate = currentdate.strftime('%Y-%m-%d')

  #get the current date and subtract it by 3 days 
  olddate = datetime.datetime.now() + datetime.timedelta(days=-3)

  #get the times of the current date
  hours = olddate.strftime('%H:%M:%S')

  # transform the date into an api-readable format
  olddate = olddate.strftime('%Y-%m-%d')

  # transform the dates into a string to be able to put them in the url
  olddate = str(olddate)
  hours=str(hours)

  # http request headers
  headers = {
    'Authorization': 'Basic {}'.format(finalapi)
  }

  # emailsecurity trend api url
  url ="https://{}/api/v1/log/policyeventlog?start={}T00:00:00Z&end={}T{}Z".format(localization,olddate, currentdate, hours)

  # make the request to the API
  r = requests.get(url, headers=headers)

  # send the request data to a list of dictionaries
  list = r.json().get("logs")

  #these list have all the data, to see, only print the list
  print(list)


```


