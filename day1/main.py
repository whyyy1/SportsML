
from bs4 import BeautifulSoup
import requests
import pandas as pd 

site = 'https://www.pro-football-reference.com'
year = 2022

readSite = requests.get(site +'/years/' + str(year))
soup = BeautifulSoup(readSite.content, 'html.parser')
dataTables = soup.find_all('table')
# count = 0
# print(len(dataTables))
# teamOffense = dataTables[0]
# print(teamOffense
league = []
for j in dataTables:
    
    for i,row in enumerate(j.find_all('tr')[2:]):
        
    
        tN = row.find('th',attrs={'data-stat': "team"})
        
        if tN != None:
            team = {}
            teamName = (tN.a.get_text())
            team['name'] = teamName
            teamHref = (tN.a.get('href'))
            readSite = requests.get(site + teamHref)
            soup = BeautifulSoup(readSite.content, 'html.parser')
            dataTables1 = soup.find_all('table') 
            
            teamStats = dataTables1[0]
            
            
            # list1 = [2,3,7,13,18,19.20,21,22]
            # print(teamStats)
            for i,row in enumerate(teamStats.find_all('td')):

                value = row.get('data-stat')
                num = row.get_text()
                if num != '':
                        team[value] = num
                
            # print(team)
            
            league.append(team)
                
            
df = pd.DataFrame(league)
print(df)
