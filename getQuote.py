import requests
def getQuotes():
    catergories = ["inspire",
            "management",
            "life",
            "funny",
            "art"]
    baseUrl = 'https://quotes.rest/qod'
    quotes = []
    for catergory in catergories:
        quotes.append(requests.get(baseUrl+"?category="+catergory).json()['contents']['quotes'][0]['quote'])
    return quotes