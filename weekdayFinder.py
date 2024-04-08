#import modules
import streamlit as st
import datetime
import calendar

#header
st.title("Week Day Finder")

#Take Date Input value by providing date gui
dateInput = st.date_input("Enter Date", min_value=datetime.date(1900,1,1),max_value=datetime.date(2100,1,1))

#the list which contains all the the weekdays
weekdays=["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]

#retrieving data from the dataInput variable
year=dateInput.year
month=dateInput.month
day=dateInput.day

#It returns the weeknumber like (Monday-0, Tuesday-1, Wednesday-2, Thursday-3, Friday-4, Saturday-5, Sunday-6)
weekValue=calendar.weekday(year,month,day)

#Accessing the weekday by weeknumber
result=weekdays[weekValue]

#Displaying the weekday
st.success('The Week Day is : '+result )