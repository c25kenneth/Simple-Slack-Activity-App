import requests

def getRandomActivity(): 
    response = requests.get("https://www.boredapi.com/api/activity")
    
    return response.json()
