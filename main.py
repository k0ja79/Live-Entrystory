import requests, json
from bs4 import BeautifulSoup as bs
import graphql

pre_id, id='', ''

with requests.Session() as s:
    loginPage = s.get('https://playentry.org/signin')
    soup = bs(loginPage.text, 'html.parser')
    csrf = soup.find('meta', {'name': 'csrf-token'})
    login_headers={'CSRF-Token': csrf['content'], "Content-Type": "application/json"}
    s.post('https://playentry.org/graphql', headers=login_headers, json={'query':graphql.login, 'variables':{"username":"tnghks8","password":"xldpsqht0179"}})
    headers={'X-Token': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZG5vIjoiZDk3ZDg0YzAtYTJjZC0xMWVjLTgyZmUtMjQ2ZTk2NDg3MDljIiwiZXhwIjoxNjc2NTQ0ODI5LCJpYXQiOjE2NzUzMzUyMjl9.WebyF8msvtcvbGi0fhdTq5uYUtq-y5-_T01JPAgazNw', 'x-client-type': 'Client', 'CSRF-Token': csrf['content'], "Content-Type": "application/json"}
    print('Live Entrystory 작동 시작')
    f=open('project.json', 'r', encoding='utf8')
    projValue=f.read()
    projValue=json.loads(projValue)
    f.close()
    while True:
        req=s.post('https://playentry.org/graphql', headers=headers, json={'query':graphql.loadStory, "variables":{"category":"free","searchType":"scroll","term":"all","discussType":"entrystory","pageParam":{"display":1,"sort":"created"}}})
        story=req.text
        story=json.loads(story)
        id=story['data']['discussList']['list'][0]['id']
        text=story['data']['discussList']['list'][0]['content']
        time=story['data']['discussList']['list'][0]['created']
        comments=story['data']['discussList']['list'][0]['commentsLength']
        likes=story['data']['discussList']['list'][0]['likesLength']
        nick=story['data']['discussList']['list'][0]['user']['nickname']
        projValue['variables'][0]['value']=text
        projValue['variables'][1]['value']=comments
        projValue['variables'][2]['value']=likes
        projValue['variables'][3]['value']=time
        projValue['variables'][4]['value']=nick
        if id!=pre_id:
            print(text)
            req=s.post('https://playentry.org/graphql', headers=headers, json={'query':graphql.project, "variables":projValue})
            pre_id=id