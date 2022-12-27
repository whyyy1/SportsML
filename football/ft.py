import pandas as pd
from datetime import datetime
from requests import get
from bs4 import BeautifulSoup
from datetime import datetime, timedelta
import streamlit as st
import numpy as np
from football.constantsTeams import NFL_TEAM
import football.teams as teamsFT

def getSchedule(year,week):
    # r = get(f"https://www.espn.com/nfl/schedule/_/week/{week}/year/{year}/seasontype/2")
    r = get(f'https://www.cbssports.com/nfl/schedule/{year}/regular/{week}/')
    if r.status_code==200:
            soup = BeautifulSoup(r.content, 'html.parser')
            matchups = soup.find_all('span',attrs={'class':'TeamName'})
            # print(matchups)
            games1 = []
            
            list1 = []
            for i, games in enumerate(matchups):
                if len(list1)<2:
                    list1.append(games.text)
                if len(list1) == 2:
                    games1.append(list1)
                    list1 = []
            return games1


def run_sim(teams,year):

    gL = len(teams)
    gamePicked = st.selectbox(f'{gL} Games', teams)             
    homeTeam = gamePicked[1]
    awayTeam = gamePicked[0]           
    homeAbbr = NFL_TEAM[homeTeam].lower()
    awayAbbr = NFL_TEAM[awayTeam].lower()
    home = teamsFT.getStats(homeAbbr,year)
    away = teamsFT.getStats(awayAbbr,year) 
    print(home)   
    # st.image(home['logo']) 
    
    # st.image(away['logo']) 
