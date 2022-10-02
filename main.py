import numpy as np
import pandas as pd
from datetime import date
import streamlit as st
import csv
from db_fxns import *
import plotly.express as px


 



def main():

    st.title("Expense Tracker")
    menu = ['Add Expense','Reports','Charts']
    create_table()
    choice = st.sidebar.selectbox("Menu",menu)
    if choice == 'Add Expense':
        col1,col2,col3,col4,col5 = st.columns(5)
        with col1:
            item = st.text_area("Expense Item")
        with col2:
            expense_type = st.selectbox("Expense Type",["Food", "Household", "Transportation", "Products", "other"])
            if expense_type == "other":
                expense_type = st.text_input("Expense Type")
        with col3:
            expense_date = st.date_input("Expense Date")
        with col4:
            expense_amount = st.number_input("Expense Amount")
        # with col5:
        #     total = total_expense()   
        if st.button("Add Expense"):
            add_expense(expense_date ,item, expense_type, expense_amount)
            st.success("Successfully added expense: {}, {}, {}, {}".format(expense_date,item,expense_type,expense_amount))
    
    elif choice == "Charts":
        
        result = view_all_expenses()
        df = pd.DataFrame(result,columns=['Date','Item','Type','Amount'])
        df.set_index('Date',inplace=True)
        # st.dataframe(df)
        total = df['Amount'].sum()
        # st.subheader(f"Total expense is {total}".format(total))
        # p1 = px.pie(df, names='Item', values=df['Amount'])
        # st.plotly_chart(p1)
        new_df = pd.DataFrame(result, columns=['Date','Item','Type','Amount'])
        # st.dataframe(df)
        total = new_df['Amount'].sum()
        x_axis_val = st.selectbox('Select X-Axis Value', options=new_df.columns)
        Y_axis_val = st.selectbox('Select Y-Axis Value', options=new_df.columns)
        hist = px.histogram(new_df, x=x_axis_val, y=Y_axis_val)
        line = px.line(new_df, x=x_axis_val, y=Y_axis_val)
        pie = px.pie(new_df, names=x_axis_val, values=Y_axis_val)
        density = px.density_heatmap(new_df, x=x_axis_val, y=Y_axis_val)
        st.plotly_chart(hist)
        st.plotly_chart(line)
        st.plotly_chart(pie)
        st.plotly_chart(density)
        
        
            
    elif choice == 'Reports':
        result = view_all_expenses()
        df = pd.DataFrame(result,columns=['Date','Item','Type','Amount'])
        total = df['Amount'].sum() 
        new_df = df = pd.DataFrame(result,columns=['Date','Item','Type','Amount'])
        df['Total'] = total
        new_df.set_index('Date',inplace=True)
        st.dataframe(new_df)
        st.download_button(label='Download Expenses',file_name='expenses.csv',data=new_df.to_csv(),mime='text/csv')
        
            
            
        
    
        
if __name__ == "__main__":
    main()
 
    
