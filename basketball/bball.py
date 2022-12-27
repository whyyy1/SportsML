import pandas as pd
from datetime import datetime
from requests import get
from bs4 import BeautifulSoup
from basketball.constants import NBA_TEAM
from datetime import datetime, timedelta
import streamlit as st
from scipy.stats import norminvgauss
import random
from sklearn.model_selection import TimeSeriesSplit
from sklearn.feature_selection import SequentialFeatureSelector
from sklearn.linear_model import RidgeClassifier
from sklearn.preprocessing import MinMaxScaler
from scipy.stats import invgauss
import numpy as np
import basketball.teams  as teams

def gameAvg(game):
    # print(game)
    # fg total 
    fgm = game[0][0]
    fga = game[0][1]
    fgp = game[0][2]
    #3 pt fg
    thfgm = game[0][3]
    thfga = game[0][4]
    thfgp = game[0][5]

    #2 pt fg
    twfgm = game[0][6]
    twfga = game[0][7]
    twfgp = game[0][8]
    stats = []
    for i in range (0,2):
        #sim from range of jumpshots in game
        shot_Chart = []
       
        for j in range(0,int(fga)):
            
            fgPer = np.random.random()
            #if lower than fgp it is a made basket
            if(fgPer <= fgp):
                
                
                shot_type_per = np.random.random()
                
                
                
                
                    
                if (shot_type_per <= thfgp) and (shot_type_per <= twfgp) :
                    
                    shot_Chart.append(3)
                    
                elif shot_type_per <= twfgp :

                    shot_Chart.append(2)
                    
            elif(fgPer > fgp): 
                shot_Chart.append(0)
        
        # stats.append(totalPTS)
                #was it a two or a three
        print(shot_Chart)
    # print(np.average(stats))


def getStats(team1,team2,team1score,team2score,date):
    TODAY = datetime.now().strftime('%Y-%m-%d')
    
    
    away = team1
    home = team2
    homeTeam = teams.pageData(home,2023)
    awayTeam = teams.pageData(away,2023)
    # print(homeTeam)
    # for val in constants.NBA_TEAM:
    #     print(val)
    images = [homeTeam['teamLogo'],awayTeam['teamLogo']]
    homeTeam['offense']['st_dev'] = round(homeTeam['home_stDev'])
    homeTeam['defense']['st_dev'] = round(homeTeam['homeAll_stDev'])
    awayTeam['offense']['st_dev'] = round(awayTeam['away_stDev'])
    awayTeam['defense']['st_dev'] = round(awayTeam['awayAll_stDev'])
    
    homeOffDF = pd.DataFrame(homeTeam['offense'])
    tPP = float(homeTeam['pro_totalPts']) 
    hSpr = float(homeTeam['ptsSpread'])
    aSpr = float(awayTeam['ptsSpread'])
    l10H = homeTeam['last10']
    l10A = awayTeam['last10'] 
    hmL = homeTeam['moneyline']
    amL = awayTeam['moneyline']
    
    homeDefDF = pd.DataFrame(homeTeam['defense'])
    
    awayOffDF = pd.DataFrame(awayTeam['offense'])
    
    awayDefDF = pd.DataFrame(awayTeam['defense'])
    homeProSTATS = homeOffDF-awayDefDF
    awayProSTATS = awayOffDF-homeDefDF
    
    scores = [homeOffDF,homeDefDF,awayOffDF,awayDefDF]
    col = [f"{home}_Off",f"{home}_Def",f"{away}_Off",f"{away}_Def"]
    gameData = pd.concat(scores,axis=1,keys=col)
    gameData.loc['totalProPTS'] = tPP
    gameData.loc['awaySpread'] = aSpr
    gameData.loc['homeSpread'] = hSpr
    gameData.loc['last10H'] = l10H
    gameData.loc['last10A'] = l10A
    gameData.loc['homeML'] = hmL
    gameData.loc['awayML'] = amL
    
    homeSTATSMADE = gameData.iloc[:,0]
    homeSTATSALL = gameData.iloc[:,1]
    awaySTATSMADE = gameData.iloc[:,2]
    awaySTATSALL = gameData.iloc[:,3]
    
    # st.write(awaySTATSMADE)
    # st.write(homeSTATSALL)
    #Project home score 
    home_pts = homeSTATSMADE.loc['PTS']
    home_div = homeSTATSMADE.loc['st_dev']
    home_ptsAll = homeSTATSALL.loc['PTS']
    home_divAll = homeSTATSALL.loc['st_dev']
    away_pts = awaySTATSMADE.loc['PTS']
    away_div = awaySTATSMADE.loc['st_dev']
    away_ptsAll = awaySTATSALL.loc['PTS']
    away_divAll = awaySTATSALL.loc['st_dev']
    projectSpred = [homeSTATSALL.loc['homeSpread'],homeSTATSALL.loc['awaySpread'],homeSTATSALL['totalProPTS']] 
    l10 = [homeSTATSALL['last10H'],homeSTATSALL['last10A']]
    listML = [homeSTATSALL['homeML'],homeSTATSALL['awayML']]
    
    gameStats=[home_pts,home_div,away_ptsAll,away_divAll,away_pts,away_div,home_ptsAll,home_divAll,projectSpred,l10,listML]
    
    st.header(f'{home} vs {away}')
    st.header(f'O/U: {round(home_pts + away_pts)} ' + f' / {home} current odds: {homeTeam["moneyline"]} '+f' / {away} current odds: {awayTeam["moneyline"]}')
    
    if TODAY == str(date):
        st.header(f'O/U: {tPP} ' + f' / {home} current odds: {homeTeam["moneyline"]} '+f' / {away} current odds: {awayTeam["moneyline"]}')
    st.image(images[0],home)
    st.write(f'{home} Project PTS: {home_pts} -- {home_pts-home_div}(-) or {home_pts+home_div}(+)')
    st.write(f'HOME: {homeOffDF}')
    st.write(f'Last 10: {l10H}')
    homePlyStats = pd.DataFrame(homeTeam["perGame"].copy())
    homePlyStats = homePlyStats.astype(str)
    print(homePlyStats.info())
    # st.dataframe(f'PLAYER STATS: {homePlyStats}')
    homePROJECTED = homeProSTATS+homeOffDF
    # st.dataframe(homeProSTATS+homeOffDF)
    gameAvg(homeOffDF)
    
    st.image(images[1],away)
    st.write(f'{away} Project PTS: {away_pts} -- {away_pts-away_div}(-) or {away_pts+away_div}(+)')
    st.write(f'AWAY: {awayOffDF}')
    st.write(f'Last 10: {l10A}')
    # st.dataframe(awayProSTATS+awayOffDF)
    # gameSimN = st.number_input('Number of games sim:',10,5000) 
    # gamesEnd = mulSim(gameSimN,gameStats,home,away)
    # for i in gamesEnd[0]:
    #     st.write(i)
    # st.bar_chart(gamesEnd[1])
    # awayRoster = teams.get_roster(away,2023)
    # print(awayRoster)
    # awayRoster = teams.get_roster_stats(awayRoster,2023)
    # print(awayRoster.)
    rr = RidgeClassifier(alpha=1)
    split = TimeSeriesSplit(n_splits=3)
    
        # st.bar_chart(df)
        # st.dataframe(df)

def getBasketballGames(date):
    r = get(f"https://www.nba.com/games?date={date}")
    
    if r.status_code==200:
            soup = BeautifulSoup(r.content, 'html.parser')
            table = soup.findAll('span', attrs={'class': 'MatchupCardTeamName_teamName__9YaBA'})
            gL = []
            sG = []
            for t1 in table:
                
                if len(sG)!=2:
                    t = t1.text.upper()
                    if t in NBA_TEAM:
                        
                        sG.append(NBA_TEAM[t])
                if len(sG)==2:
                    gL.append(sG)
                    sG = []
            scoresF = soup.findAll('p',attrs={'class':'MatchupCardScore_p__dfNvc GameCardMatchup_matchupScoreCard__owb6w'})
            finalScore = []
            list1 = []
            for fs in scoresF:
                if len(list1)!=2:
                    list1.append(fs.text)  
                if len(list1)==2:
                    finalScore.append(list1)
                    list1 = []
            returnLit = [gL,finalScore]
            return returnLit
    if r.status_code != 200:
        print(r.status_code)




def run_sim(data,date):
    current = date
    yesterday = date - timedelta(days=1)
    yesterday = yesterday.strftime('%Y-%m-%d')
    
    gameList = []
    s = []
    for i ,game in enumerate (data[0]):
        if len(data[1])>0:
            s.append(data[1][0])
        gameList.append(game)
    gN = len(gameList)
    gamesLIST = st.selectbox(f'{gN} Game(s)',gameList,key="gl")

    if len(s)>0:
        
        
        st.header(f'Score : {gamesLIST[1]} {s[0][0]} - {gamesLIST[0]} {s[0][1]}')
        # home_Team = gamesLIST[1]
        # home_score = s[0][1]
        # away_Team = gamesLIST[0]
        # away_score = s[0][0]
    
   
        # getStats(home_Team,away_Team,home_score,away_score,date)
    
      
    
    getStats(gamesLIST[0],gamesLIST[1],0,0,yesterday)