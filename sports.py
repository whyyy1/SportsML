from datetime import datetime, timedelta
import time
import streamlit as st
import basketball.bball as bball
import football.teams as footTeams
import football.ft as ft
def mainStart():
    TODAY = datetime.now()
    sportsList = ["selectSPORT....","basketball", "football", "soccer", "baseball","hockey"]
    option = st.selectbox(f'Select a sports catergory: ',sportsList,key="dateWid")
    
    if option == 'basketball':
        gameDate = st.date_input('Date 1946-Current',TODAY)
        sched = bball.getBasketballGames(gameDate)
        
        bball.run_sim(sched,gameDate)
    elif option == 'football':
        count = 20
        currentYear = TODAY.year
        yearsList = []
        weeks  = []
        for i in range(18):
            weeks.append(i+1)
        
        while count > 0:
            yearsList.append(currentYear)
            currentYear -= 1
            count -= 1
        nflYear = st.selectbox('NFL year: ',yearsList)
        nflWeek = st.selectbox('NFL week: ', weeks)
        ft.getSchedule(nflYear,nflWeek)
        schedFT = ft.getSchedule(nflYear,nflWeek)
        ft.run_sim(schedFT,nflYear)
        # year = st.selectbox
        
        


if __name__ == "__main__":
    
    mainStart()
    time.sleep(10)
    print('requesting again.....')
        