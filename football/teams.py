import pandas as pd
from requests import get
from bs4 import BeautifulSoup
import time
import statistics

    

   
def getStats(team,year):
    data = {}
    r = get(f'https://www.pro-football-reference.com/teams/{team}/{year}.htm')
    print(r.status_code)
    if r.status_code == 200:
        soup = BeautifulSoup(r.content, 'html.parser')
        teamImg = soup.find('img',attrs={'class':'teamlogo'})
        data['logo'] = teamImg['src']
        tables = soup.find('table',attrs={'id':'team_stats'})
        thead = tables.find('thead')
        thead = thead.find_all('tr')
        thead = thead[1]
        columns = thead.find_all('th')
        tbody = tables.find('tbody')
        tbody = tbody.find_all('tr')
        teamOff = tbody[0]
        teamDef = tbody[1]

        cols = []
        team1 = []
        team2 = []
        
        for i,t in enumerate(columns):
            cols.append(t.text)
            data[f'{t.text}']
        for k in teamOff:
            team1.append(k.text)
        for j in teamDef:
            team2.append(j.text)
        print(data)
        # print(team1[-5:-3])
        # cols[0] = 'Team'
        
        # for j in home:
        #     print(j)
getStats('buf',2022)       

#         colsDF = []
#         for i in cols:
#             if i.text == " ":
#                 continue
#             else:

#                 colsDF.append(i.text)

#         colsDF[1] = 'Name'
        
#         df1 = pd.DataFrame(columns=colsDF)
#         # print(df1)
#         for i in perSTATS:
#             statsPER = []
#             for j,stat in enumerate(i):
#                 str1 = stat.text
#                 str1 = str(str1)
                

#                 statsPER.append(str1)
#                 # else:
#                 #     if str1.isdigit():
#                 #         statsPER.append(int(str1))
#                 #     else:
#                 #         statsPER.append(float(str1))
#             # print(statsPER)
#             df1.loc[len(df1.index)] = statsPER
#         df1 = df1.set_index('Name')
        
#         df['perGame'] = df1
        
        
        
#         teamsLine = lines.find_all('span',attrs={'class':'Fw(600) Pend(4px) Ell D(ib) Maw(190px) Va(m)'})
#         for team1 in teamsLine:
#             teamL = len(df['teamName'])
            
#             text1 = team1.text[-teamL::]
            
#             if text1.upper() == df['teamName']:
#                 tr = team1.parent
                
#                 tr = tr.parent
#                 tr = tr.parent
#                 odds = tr.find_all('span',attrs={'class':'Lh(19px)'})
#                 moneyLine = odds[0].text
#                 pointSpread =odds[1].text
#                 totalPtsPred = odds[2].text
#                 # print(moneyLine,pointSpread,totalPtsPred)
#                 totalPtsPred = totalPtsPred[-5:]
#                 pointSpread = pointSpread[-4:] 
                
#                 if(totalPtsPred or moneyLine or pointSpread) != '-': 
#                     if (pointSpread[0] and moneyLine[0] ) == '-':
                        
#                         df['ptsSpread'] = -abs(float(pointSpread[1:]))
#                         df['moneyline'] = -abs(int(moneyLine[1:]))
#                         print(moneyLine[0:])
#                     elif (pointSpread[0] and moneyLine[0]) == '+':
#                         df['ptsSpread'] = abs(float(pointSpread[1:]))
#                         df['moneyline'] = abs(int(moneyLine[0:]))
                    
#                     if (totalPtsPred and moneyLine and pointSpread) == int:
#                         df['pro_totalPts'] = float(totalPtsPred)
#                     else:
#                         df['pro_totalPts'] = 0
#                 if(totalPtsPred or moneyLine or pointSpread) == '-': 
#                     df['ptsSpread'] = 0
#                     df['moneyline'] = 0
#                     df['pro_totalPts'] = 0
#                     continue
#             # if team1.text == df['teamName']:
#             #     print(soup.find(team1).parent)
#         imgT = soup.find('img',attrs={'class':'teamlogo'})
#         teamImg = imgT['src']
#         teamOvr = soup.find('div',attrs={'data-template':'Partials/Teams/Summary'})
#         avgStats = teamOvr.findAll('strong')
#         # avgP = teamOvr.findAll('p')
#         # avgP = avgP[5:8]
#         # for j,t in enumerate(avgP):
#         #     print(t.text)
        
#         avgStats = avgStats[5:7]
#         for i ,value in enumerate(avgStats):
#             feat = f'{value.text[:-1]}'
#             val = float(value.next_sibling[8:13])
#             df[feat] = val
#         recentG = soup.find('div',attrs={'id':'timeline_results'})
#         games1 = recentG.findAll('li',attrs={'class':'result'})
#         games1 = games1[-10:]
#         wins = 0
#         losses = 0
        
#         for i,g in enumerate(games1):
#             info = g.text
            
#             date = info[4:12]
#             if 'beat' in info:
#                 wins +=1
#             elif 'lost' in info:
#                 losses+=1
        
#         df['last10'] = wins/(wins+losses)   
#         cols = ['G','MP','TEAM','SEASON']
#         offense = get_team_stats(team,season_end_year)
#         defense = get_opp_stats(team,season_end_year)
        
        
#         gp = offense.loc["G"] 

#         for c in cols:
#             del offense[c]
#             del defense[c]
#         df['offense'] = offense
#         df['defense'] = defense
#         df['teamLogo'] = teamImg
#             # print(info[12:14])
#             # print(info[28:31])
#         # stDev(team,season_end_year)
#         sDev = stDev(team,season_end_year,gp)
#         df['home_stDev'] = sDev[0]
#         df['homeAll_stDev'] = sDev[1]
#         df['away_stDev'] = sDev[2]
#         df['awayAll_stDev'] = sDev[3]
#         return df
#         # df = pd.DataFrame
#         # for i,value in enumerate(avgStats):

#         #     for j, st in enumerate(value):
#         #         print(st.text[0:6])
#         # print('-------------')

# def getDate(mon,day,year):
#     date = f"1/{day}/{year}"
#     match mon:
#         case "Jan":
#             date = f"1/{day}/{year}"
#         case "Fed":
#             date = f"2/{day}/{year}"
#         case "Mar":
#             date = f"3/{day}/{year}"
#         case "Apr":
#             date = f"4/{day}/{year}"
#         case "May":
#             date = f"5/{day}/{year}"
#         case "Jun":
#             date = f"6/{day}/{year}"
#         case "Jul":
#             date = f"7/{day}/{year}"
#         case "Aug":
#             date = f"8/{day}/{year}"
#         case "Sept":
#             date = f"9/{day}/{year}"
#         case "Oct":
#             date = f"10/{day}/{year}"
#         case "Nov":
#             date = f"11/{day}/{year}"
#         case "Dec":
#             date = f"12/{day}/{year}"
#     return date

# def stDev(team,season_end_year,gp):
    
#     r = get(
#         f'https://www.basketball-reference.com/teams/{team}/{season_end_year}_games.html')
#     if r.status_code == 200:
#         soup = BeautifulSoup(r.content, 'html.parser')
#         record = soup.find('div',attrs={'data-template':'Partials/Teams/Summary'})
#         r1 = record.find('strong').next_sibling
#         # for i,letter in enumerate(r1):
#         #     print(i,letter) 
       
#         sch = soup.find('tbody')
#         row = sch.findAll('tr')
#         row = row[:gp]
#         homePts = []
#         homeDef = []
#         awayPts = []
#         awayDef = []
#         for i,k in enumerate(row):
#             loc = k.find('td',attrs={'data-stat':'game_location'})
#             teamPts = k.find('td',attrs={'data-stat':'pts'})
#             ptsAgt = k.find('td',attrs={'data-stat':'opp_pts'})
#             if loc != None:
#                 if loc.text == '@':
#                     awayPts.append(int(teamPts.text))
#                     awayDef.append(int(ptsAgt.text))
#                 else:
#                     homePts.append(int(teamPts.text))
#                     homeDef.append(int(ptsAgt.text))
        
#         sDHome = statistics.stdev(homePts)
#         sDHomeDef = statistics.stdev(homeDef)
#         sDAway = statistics.stdev(awayPts)
#         sDAwayDef = statistics.stdev(awayDef)
#         sD = [sDHome,sDHomeDef,sDAway,sDAwayDef]
#         return sD
    
# def teamImg(team,year):
#     r = get(
#         f'https://www.basketball-reference.com/teams/{team}/{year}.html')
#     if r.status_code == 200:
#         soup = BeautifulSoup(r.content, 'html.parser')
#         table = soup.find('img',attrs={'class':'teamlogo'})
#         return table['src']

        
# def get_roster(team, season_end_year):
    
#     r = get(
#         f'https://www.basketball-reference.com/teams/{team}/{season_end_year}.html')
#     df = None
#     if r.status_code == 200:
#         soup = BeautifulSoup(r.content, 'html.parser')
#         table = soup.find('table')
#         df = pd.read_html(str(table))[0]
#         df.columns = ['NUMBER', 'PLAYER', 'POS', 'HEIGHT', 'WEIGHT', 'BIRTH_DATE',
#                       'NATIONALITY', 'EXPERIENCE', 'COLLEGE']
#         # remove rows with no player name (this was the issue above)
#         df = df[df['PLAYER'].notna()]
#         df['PLAYER'] = df['PLAYER'].apply(
#             lambda name: remove_accents(name, team, season_end_year))
#         # handle rows with empty fields but with a player name.
#         df['BIRTH_DATE'] = df['BIRTH_DATE'].apply(
#             lambda x: pd.to_datetime(x) if pd.notna(x) else pd.NaT)
#         df['NATIONALITY'] = df['NATIONALITY'].apply(
#             lambda x: x.upper() if pd.notna(x) else '')

#     return df


# def get_team_stats(team, season_end_year, data_format='PER_GAME'):
#     if data_format == 'TOTAL':
#         selector = 'div_totals-team'
#     elif data_format == 'PER_GAME':
#         selector = 'div_per_game-team'
#     elif data_format == 'PER_POSS':
#         selector = 'div_per_poss-team'
#     r = get(
#         f'https://widgets.sports-reference.com/wg.fcgi?css=1&site=bbr&url=%2Fleagues%2FNBA_{season_end_year}.html&div={selector}')
#     df = None
#     if r.status_code == 200:
#         soup = BeautifulSoup(r.content, 'html.parser')
#         table = soup.find('table')
#         df = pd.read_html(str(table))[0]
#         league_avg_index = df[df['Team'] == 'League Average'].index[0]
#         df = df[:league_avg_index]
#         df['Team'] = df['Team'].apply(lambda x: x.replace('*', '').upper())
#         df['TEAM'] = df['Team'].apply(lambda x: TEAM_TO_TEAM_ABBR[x])
#         df = df.drop(['Rk', 'Team'], axis=1)
#         df.loc[:, 'SEASON'] = f'{season_end_year-1}-{str(season_end_year)[2:]}'
#         s = df[df['TEAM'] == team]
#         return pd.Series(index=list(s.columns), data=s.values.tolist()[0])


# def get_opp_stats(team, season_end_year, data_format='PER_GAME'):
#     if data_format == 'TOTAL':
#         selector = 'div_totals-opponent'
#     elif data_format == 'PER_GAME':
#         selector = 'div_per_game-opponent'
#     elif data_format == 'PER_POSS':
#         selector = 'div_per_poss-opponent'
#     r = get(
#         f'https://widgets.sports-reference.com/wg.fcgi?css=1&site=bbr&url=%2Fleagues%2FNBA_{season_end_year}.html&div={selector}')
#     df = None
#     if r.status_code == 200:
#         soup = BeautifulSoup(r.content, 'html.parser')
#         table = soup.find('table')
#         df = pd.read_html(str(table))[0]
#         league_avg_index = df[df['Team'] == 'League Average'].index[0]
#         df = df[:league_avg_index]
#         df['Team'] = df['Team'].apply(lambda x: x.replace('*', '').upper())
#         df['TEAM'] = df['Team'].apply(lambda x: TEAM_TO_TEAM_ABBR[x])
#         df = df.drop(['Rk', 'Team'], axis=1)
#         df.columns = list(map(lambda x: x, list(df.columns)))
#         df.rename(columns={'OPP_TEAM': 'TEAM'}, inplace=True)
#         df.loc[:, 'SEASON'] = f'{season_end_year-1}-{str(season_end_year)[2:]}'
#         s = df[df['TEAM'] == team]
#         return pd.Series(index=list(s.columns), data=s.values.tolist()[0])


# def get_team_misc(team, season_end_year):
#     r = get(
#         f'https://widgets.sports-reference.com/wg.fcgi?css=1&site=bbr&url=%2Fleagues%2FNBA_{season_end_year}.html&div=div_advanced-team')
#     df = None
#     if r.status_code == 200:
#         soup = BeautifulSoup(r.content, 'html.parser')
#         table = soup.find('table')
#         df = pd.read_html(str(table))[0]
#         df.columns = list(map(lambda x: x[1], list(df.columns)))
#         league_avg_index = df[df['Team'] == 'League Average'].index[0]
#         df = df[:league_avg_index]
#         df['Team'] = df['Team'].apply(lambda x: x.replace('*', '').upper())
#         df['TEAM'] = df['Team'].apply(lambda x: TEAM_TO_TEAM_ABBR[x])
#         df = df.drop(['Rk', 'Team'], axis=1)
#         df.rename(columns={'Age': 'AGE', 'Pace': 'PACE', 'Arena': 'ARENA',
#                   'Attend.': 'ATTENDANCE', 'Attend./G': 'ATTENDANCE/G'}, inplace=True)
#         df.loc[:, 'SEASON'] = f'{season_end_year-1}-{str(season_end_year)[2:]}'
#         s = df[df['TEAM'] == team]
#         s = s.loc[:, ~s.columns.str.contains('^Unnamed')]
#         return pd.Series(index=list(s.columns), data=s.values.tolist()[0])


# def get_roster_stats(team: list, season_end_year: int, data_format='PER_GAME', playoffs=False):
#     if playoffs:
#         period = 'playoffs'
#     else:
#         period = 'leagues'
#     selector = data_format.lower()
#     r = get(
#         f'https://widgets.sports-reference.com/wg.fcgi?css=1&site=bbr&url=%2F{period}%2FNBA_{season_end_year}_{selector}.html&div=div_{selector}_stats')
#     df = None
#     possible_teams = [team]
#     for s in TEAM_SETS:
#         if team in s:
#             possible_teams = s
#     if r.status_code == 200:
#         soup = BeautifulSoup(r.content, 'html.parser')
#         table = soup.find('table')
#         df2 = pd.read_html(str(table))[0]
#         for index, row in df2.iterrows():
#             if row['Tm'] in possible_teams:
#                 if df is None:
#                     df = pd.DataFrame(columns=list(row.index)+['SEASON'])
#                 row['SEASON'] = f'{season_end_year-1}-{str(season_end_year)[2:]}'
#                 df = df.append(row)
#         df.rename(columns={'Player': 'PLAYER', 'Age': 'AGE',
#                   'Tm': 'TEAM', 'Pos': 'POS'}, inplace=True)
#         df['PLAYER'] = df['PLAYER'].apply(
#             lambda name: remove_accents(name, team, season_end_year))
#         df = df.reset_index().drop(['Rk', 'index'], axis=1)
#         return df

# def get_team_ratings(*, team=[], season_end_year: int):

#     # Scrape data from URL
#     r = get(f'https://widgets.sports-reference.com/wg.fcgi?css=1&site=bbr&url=%2Fleagues%2FNBA_{season_end_year}_ratings.html&div=div_ratings')
#     if r.status_code == 200:
#         soup = BeautifulSoup(r.content, 'html.parser')
#         table = soup.find('table')
#         df = pd.read_html(str(table))[0]

#         # Clean columns and indexes
#         df = df.droplevel(level=0, axis=1)
        
#         df.drop(columns=['Rk', 'Conf', 'Div', 'W', 'L', 'W/L%'], inplace=True)
#         upper_cols = list(pd.Series(df.columns).apply(lambda x: x.upper()))
#         df.columns = upper_cols

#         df['TEAM'] = df['TEAM'].apply(lambda x: x.upper())
#         df['TEAM'] = df['TEAM'].apply(lambda x: TEAM_TO_TEAM_ABBR[x])

#         # Add 'Season' column in and change order of columns
#         df['SEASON'] = f'{season_end_year-1}-{str(season_end_year)[2:]}'
#         cols = df.columns.tolist()
#         cols = cols[0:1] + cols[-1:] + cols[1:-1]
#         df = df[cols]

#         # Add the ability to either pass no teams (empty list), one team (str), or multiple teams (list)
#         if len(team) > 0:
#             if isinstance(team, str):
#                 list_team = []
#                 list_team.append(team)
#                 df = df[df['TEAM'].isin(list_team)]
#             else:
#                 df = df[df['TEAM'].isin(team)]
                    
#     return df
