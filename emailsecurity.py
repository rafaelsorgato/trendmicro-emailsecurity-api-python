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

