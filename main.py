import streamlit as st
import pandas as pd
@st.cache
def load_date():
    titanic_df = pd.read_csv('titanic.csv')
    return titanic_df
titanic_df = load_date()

def main():

    st.title('Titanic Dataset Exploration')
    st.write('The Titanic dataset contains information about the passengers onboard the Titanic.')

    st.header('Dataset Preview')
    st.dataframe(titanic_df.head())

    st.header('Data Summary')
    st.write(titanic_df.describe())

    st.header('Data Visualization')
    st.write('Here are some visualizations of the dataset.')

    # Add any visualizations you like here (e.g., bar plots, histograms, etc.)
    # For example:
    st.bar_chart(titanic_df['Pclass'].value_counts())

if __name__ == '__main__':
     main()
