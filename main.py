# importing libraries
import random
import re
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import streamlit as st
from PIL import Image
from st_animation import typing_animation_html, typing_animation_css, typing_animation_js
from df_to_csv_conv import convert_df
from quotes import quotes


# page config
favicon = Image.open("favicon.ico")
st.set_page_config(
    layout="wide", 
    page_icon=favicon,
    page_title="Data Tales Unfolded"
)

# main page starts
st.markdown(
    typing_animation_html + typing_animation_css + typing_animation_js, 
    unsafe_allow_html=True
)

st.write(f"<h3 style='text-align: center;'>{random.choice(quotes)}</h3>", unsafe_allow_html=True)    # fetches a random random quote everytime page gets refreshed
st.write('---')    # draws a horizontal line just like html tag <hr> does

st.write("<h3 style='text-align: center;'>Before Proceding to Main part, Let's first talk about what are the factors that actually affect the standing of a university 🏫 on such a Competitive scale where everyone wants to be on Top 👇🏼</h3>", unsafe_allow_html=True)
st.write("<h5 style='text-align: center;'>🧑🏼‍🏫Teaching, Importance: 30%</h5>", unsafe_allow_html=True)
st.write("<h5 style='text-align: center;'>🔬Research, Importance: 30%</h5>", unsafe_allow_html=True)
st.write("<h5 style='text-align: center;'>📚Citations, Importance: 30%</h5>", unsafe_allow_html=True)
st.write("<h5 style='text-align: center;'>🌏International Outlook, Importance: 7.5%</h5>", unsafe_allow_html=True)
st.write("<h5 style='text-align: center;'>💰Industry Income, Importance: 2.5</h5>", unsafe_allow_html=True)
st.write("")
st.write("<h6>Wondering what is this all, read statements below to get more know more about them</h6>", unsafe_allow_html=True)
st.write("* **Teaching** is a measure of the learning experience and quality at a university. It is based on the reputation among academics, and statistics about staff, students and research.")
st.write("* **Research** is a measure of both the quality and quantity of research output, based on reputation, research income and productivity.")
st.write("* **Citations** measures how influential that research is, and counts the number of times work published by academics at the university is cited in other papers.")
st.write("* **International Outlook** measures the environment and attitude with respect to international students, staff and research. It is based on international-to-domestic ratios across staff, students and research collaborations.")
st.write("* **Innovation or Industry Income** is a measure of innovation at a university, based on how much the university earns from its inventions and industrial work.")

col1, col2, col3 = st.columns(3)    # This will make 3 columns which will have equal division

with col1:
    st.write("")

with col2:
    st.image("ranking_methodology.jpg")

with col3:
    st.write("")
    st.write("<h6 style='display: flex; align-items: center; justify-content: center; height: 50vh;'>Feel Free to use the expander(Hover over the image and you will get a expander), if you want a closer look</h6>", unsafe_allow_html=True)
st.write("<h6 style='text-align: center;'>Image Credits: <a href='https://www.timeshighereducation.com/student/advice/world-university-rankings-explained'>Times Higher Education</a> </h6>", unsafe_allow_html=True)
st.write("---")

filenames = [
    "2011_rankings.csv", 
    "2012_rankings.csv", 
    "2013_rankings.csv", 
    "2014_rankings.csv", 
    "2015_rankings.csv", 
    "2016_rankings.csv", 
    "2017_rankings.csv", 
    "2018_rankings.csv", 
    "2019_rankings.csv", 
    "2020_rankings.csv", 
    "2021_rankings.csv", 
    "2022_rankings.csv", 
    "2023_rankings.csv"
]
dfs = {}      

for filename in filenames:
    key = filename.split(".")[0]
    df = pd.read_csv(filename)
    dfs[key] = df    # Stores filename as key which can be further used to retrieve data

univ_names = []
for key, df in dfs.items():
    univ_names.extend(df['name'].unique())

univ_names = list(set(univ_names))    # This will make sure that univ_names only contain unique values
univ_names.sort()    # Sorts university names in alphabetical order
univ_names.insert(0, 'Select University')    # Inserts 'Select University' at index 0, as this needs to be our first element

st.write("<h2 style='text-align: center;'>Indiviual University Stats 📊📈📉</h2>", unsafe_allow_html=True)
univ_name = st.selectbox('Select University, (or Alternatively you can type your desired university, it will display if it will be present in the dataset)', univ_names)
plot_color = st.color_picker('Pick Plot Color', '#000000')

if univ_name != 'Select University':
    visibility = True
    years = []
    teaching_ranks = []
    research_ranks = []
    citations_ranks = []    
    international_outlook_ranks = []
    industry_income_ranks = []
    overall_ranks = []
    ranks = []

    for key, df in dfs.items():
        univ_df = df[df['name'] == univ_name]

        if not univ_df.empty:
            country = univ_df['location'].iloc[0]
            year = key.split("_")[0]
            teaching_rank = univ_df['scores_teaching_rank'].iloc[0]
            research_rank = univ_df['scores_research_rank'].iloc[0]
            citations_rank = univ_df['scores_citations_rank'].iloc[0]
            international_outlook_rank = univ_df['scores_international_outlook_rank'].iloc[0]
            industry_income_rank = univ_df['scores_industry_income_rank'].iloc[0]
            overall_rank = univ_df['scores_overall_rank'].iloc[0]
            rank = univ_df['rank'].iloc[0]
            rank = str(rank)
            rank = re.findall(r'\d+', rank)    # extracting integer values out of the range

            if rank == []:
                st.warning("😔 Rank Undefined, Pls select other University")
                visibility = False
            
            if visibility:
                rank = rank[0]
                years.append(year)
                teaching_ranks.append(int(teaching_rank))
                research_ranks.append(int(research_rank))
                citations_ranks.append(int(citations_rank))
                international_outlook_ranks.append(int(international_outlook_rank))
                industry_income_ranks.append(int(industry_income_rank))
                overall_ranks.append(int(overall_rank))
                ranks.append(int(rank))

    if visibility:
        col1, col2 = st.columns(2)
        with col1:
            relationships = (
                'Teaching Rank vs Year', 
                'Research Rank vs Year', 
                'Citations Rank vs Year', 
                'International Outlook Rank vs Year', 
                'Industry Income Rank vs Year', 
                'Rank vs Year', 
                'Overall Rank vs Year'
            )
            relationship = st.selectbox('Choose Relation', relationships)
            
            if relationship == "Teaching Rank vs Year":
                fig, ax = plt.subplots()
                ax.plot(years, teaching_ranks, color=plot_color)
                ax.invert_yaxis()
                plt.xlabel('Year')
                plt.ylabel('Teaching Rank')
                plt.title(univ_name + f" ({country})")
                st.pyplot(fig)
            elif relationship == "Research Rank vs Year":
                fig, ax = plt.subplots()
                ax.plot(years, research_ranks, color=plot_color)
                ax.invert_yaxis()
                plt.xlabel('Year')
                plt.ylabel('Research Rank')
                plt.title(univ_name + f" ({country})")
                st.pyplot(fig)
            elif relationship == "Citations Rank vs Year":
                fig, ax = plt.subplots()
                ax.plot(years, citations_ranks, color=plot_color)
                ax.invert_yaxis()
                plt.xlabel('Year')
                plt.ylabel('Citations Rank')
                plt.title(univ_name + f" ({country})")
                st.pyplot(fig)
            elif relationship == "International Outlook Rank vs Year":
                fig, ax = plt.subplots()
                ax.plot(years, international_outlook_ranks, color=plot_color)
                ax.invert_yaxis()
                plt.xlabel('Year')
                plt.ylabel('International Outlook Rank')
                plt.title(univ_name + f" ({country})")
                st.pyplot(fig)
            elif relationship == "Industry Income Rank vs Year":
                fig, ax = plt.subplots()
                ax.plot(years, industry_income_ranks, color=plot_color)
                ax.invert_yaxis()
                plt.xlabel('Year')
                plt.ylabel('Industry Income Rank')
                plt.title(univ_name + f" ({country})")
                st.pyplot(fig)
            elif relationship == "Rank vs Year":
                fig, ax = plt.subplots()
                ax.plot(years, ranks, color=plot_color)
                ax.invert_yaxis()
                plt.xlabel('Year')
                plt.ylabel('Rank')
                plt.title(univ_name + f" ({country})")
                st.pyplot(fig)
            elif relationship == "Overall Rank vs Year":
                fig, ax = plt.subplots()
                ax.plot(years, overall_ranks, color=plot_color)
                ax.invert_yaxis()
                plt.xlabel('Year')
                plt.ylabel('Overall Rank')
                plt.title(univ_name + f" ({country})")
                st.pyplot(fig)

        with col2:
            st.write(f"<h3 style='text-align: center;'>{univ_name}'s Data</h3>", unsafe_allow_html=True)
            data = { 
                'Year': years, 
                'Teaching Rank':teaching_ranks, 
                'Research Rank':research_ranks, 
                'Citations Rank':citations_ranks, 
                'International Outlook Rank':international_outlook_ranks, 
                'Industry Income Rank':industry_income_ranks, 
                'Rank': ranks,
                'Overall Rank':overall_ranks
            }
            df = pd.DataFrame(data)
            df_styled = df.style.format({'Year': '{:^}', 'Rank': '{:^}', 'Overall Rank': '{:^}', 'Teaching Rank': '{:^}', 'International Outlook Rank': '{:^}', 'Research Rank': '{:^}', 'Citations Rank': '{:^}', 'Industry Income Rank':'{:^}'}).set_properties(**{'text-align': 'center'}).set_table_styles([{'selector': 'th', 'props': [('text-align', 'center')]}])
            st.table(df_styled)
            st.write('Additionally you can download this data from here')
        
            csv_data = convert_df(df)
            st.download_button(
                label="Download data as CSV",
                data=csv_data,
                file_name=f'{univ_name}_data.csv',
                mime='text/csv',
            )
            plt.savefig('fig.png')

            with open('fig.png', "rb") as file:
                st.download_button(
                    label="Download Plot",
                    data=file,
                    file_name=f'{univ_name}_plot.png',
                    mime='image/png',
                )
        
        st.write("---")
        st.write(f"<h2 style='text-align: center;'>{univ_name}'s Stats</h2>", unsafe_allow_html=True)

        if 1 <= int(np.mean(ranks)) <= 10:
            st.write("<h3 style='text-align: center;'>Reputation: Global Superstar</h3>", unsafe_allow_html=True)
        if 10 <= int(np.mean(ranks)) <= 50:
            st.write("<h3 style='text-align: center;'>Reputation: Highly prestigious university with a global reputation</h3>", unsafe_allow_html=True)
        if 50 <= int(np.mean(ranks)) <= 100:
            st.write("<h3 style='text-align: center;'>Reputation: Internationally recognized university with a strong reputation</h3>", unsafe_allow_html=True)
        if 100 <= int(np.mean(ranks)) <= 200:
            st.write("<h3 style='text-align: center;'>Reputation: Well-regarded university with a broad range of academic strengths</h3>", unsafe_allow_html=True)
        if 200 <= int(np.mean(ranks)) <= 500:
            st.write("<h3 style='text-align: center;'>Reputation: Established university with a strong regional reputation and international outlook</h3>", unsafe_allow_html=True)
        
        rank_type = [ 
            'Teaching Rank', 
            'Research Rank', 
            'Citations Rank', 
            'International Outlook Rank', 
            'Industry Income Rank', 
            'Rank', 
            'Overall Rank'
        ]
        ranks_achieved = [
            int(np.mean(teaching_ranks)),
            int(np.mean(research_ranks)), 
            int(np.mean(citations_ranks)),
            int(np.mean(international_outlook_ranks)), 
            int(np.mean(industry_income_ranks)),
            int(np.mean(ranks)), 
            int(np.mean(overall_ranks))
        ]
        years_of_lowest_ranking = [
            df.loc[df['Teaching Rank'] == max(teaching_ranks), 'Year'].max(),
            df.loc[df['Research Rank'] == max(research_ranks), 'Year'].max(), 
            df.loc[df['Citations Rank'] == max(citations_ranks), 'Year'].max(),
            df.loc[df['International Outlook Rank'] == max(international_outlook_ranks), 'Year'].max(), 
            df.loc[df['Industry Income Rank'] == max(industry_income_ranks), 'Year'].max(),
            df.loc[df['Rank'] == max(ranks), 'Year'].max(),
            df.loc[df['Overall Rank'] == max(overall_ranks), 'Year'].max() 
        ]
        years_of_highest_ranking = [
            df.loc[df['Teaching Rank'] == min(teaching_ranks), 'Year'].max(),
            df.loc[df['Research Rank'] == min(research_ranks), 'Year'].max(), 
            df.loc[df['Citations Rank'] == min(citations_ranks), 'Year'].max(),
            df.loc[df['International Outlook Rank'] == min(international_outlook_ranks), 'Year'].max(), 
            df.loc[df['Industry Income Rank'] == min(industry_income_ranks), 'Year'].max(),
            df.loc[df['Rank'] == min(ranks), 'Year'].max(), 
            df.loc[df['Overall Rank'] == min(overall_ranks), 'Year'].max()            
        ]
        highest_ranks = [
            min(teaching_ranks),
            min(research_ranks), 
            min(citations_ranks),
            min(international_outlook_ranks), 
            min(industry_income_ranks),
            min(ranks),
            min(overall_ranks)
        ]
        lowest_ranks = [
            max(teaching_ranks),
            max(research_ranks), 
            max(citations_ranks),
            max(international_outlook_ranks), 
            max(industry_income_ranks), 
            max(ranks),
            max(overall_ranks)
        ]
        col1, col2, col3 = st.columns(3)
        with col1:
            st.write("<h4 style='text-align: center;'>Average Ranking</h4>", unsafe_allow_html=True)
            data_for_avg_stats = {'Type': rank_type, 'Rank Acheived': ranks_achieved}
            df_for_avg_ranking = pd.DataFrame(data_for_avg_stats)
            st.table(df_for_avg_ranking)
        
            csv_data = convert_df(df_for_avg_ranking)
            st.download_button(
                label="Download data as CSV",
                data=csv_data,
                file_name=f'{univ_name}_avg_stats_data.csv',
                mime='text/csv',
            )
        with col2:
            st.write("<h4 style='text-align: center;'>Highest Rankings Achieved</h4>", unsafe_allow_html=True)
            data_for_highest_ranking = { 'Type': rank_type, 'Year':years_of_highest_ranking, 'Rank Acheived': highest_ranks}
            df_for_highest_ranking = pd.DataFrame(data_for_highest_ranking)
            st.table(df_for_highest_ranking)

            csv_data = convert_df(df_for_highest_ranking)
            st.download_button(
                label="Download data as CSV",
                data=csv_data,
                file_name=f'{univ_name}_highest_ranking_data.csv',
                mime='text/csv',
            )
        with col3:
            st.write("<h4 style='text-align: center;'>Lowest Rankings Achieved</h4>", unsafe_allow_html=True)
            data_for_lowest_ranking = { 'Type': rank_type, 'Year':years_of_lowest_ranking, 'Rank Acheived': lowest_ranks}
            df_for_lowest_ranking = pd.DataFrame(data_for_lowest_ranking)
            st.table(df_for_lowest_ranking)

            csv_data = convert_df(df_for_lowest_ranking)
            st.download_button(
                label="Download data as CSV",
                data=csv_data,
                file_name=f'{univ_name}_lowest_ranking_data.csv',
                mime='text/csv',
            )
else:
    st.warning('⚠️ To Get Started, Please select a university from the dropdown menu')

st.write("---")
st.write("<h2 style='text-align: center;'>Compare 2 Universities Stats ⚔️</h2>", unsafe_allow_html=True)

col1, col2 = st.columns(2)
visibility_of_c1 = True
visibility_of_c2 = True

with col1:
    univ1 = st.selectbox("Select First University, (or Alternatively you can type your desired university, it will display if it will be present in the dataset)", univ_names)
    if univ1 == "Select University":
        st.warning('⚠️ To Get Started, Please select a university from the dropdown menu')
    else:
        univ1_years = []
        univ1_teaching_ranks = []
        univ1_research_ranks = []
        univ1_citations_ranks = []
        univ1_international_outlook_ranks = []
        univ1_industry_income_ranks = []
        univ1_ranks = []
        univ1_overall_ranks = []
        for key, df in dfs.items():
            univ_df1 = df[df['name'] == univ1]
            if not univ_df1.empty:
                country1 = univ_df1['location'].iloc[0]
                year1 = key.split("_")[0]
                teaching_rank1 = univ_df1['scores_teaching_rank'].iloc[0]
                research_rank1 = univ_df1['scores_research_rank'].iloc[0]
                citations_rank1 = univ_df1['scores_citations_rank'].iloc[0]
                international_outlook_rank1 = univ_df1['scores_international_outlook_rank'].iloc[0]
                industry_income_rank1 = univ_df1['scores_industry_income_rank'].iloc[0]
                rank1 = univ_df1['rank'].iloc[0]
                overall_rank1 = univ_df1['scores_overall_rank'].iloc[0]
                rank1 = str(rank1)
                rank1 = re.findall(r'\d+', rank1)
                
                if rank1 == []:
                    st.warning("😔 Rank Undefined, Pls select other University")
                    visibility_of_c1 = False
                
                if visibility_of_c1:
                    rank1 = rank1[0]
                    univ1_years.append(year1)
                    univ1_teaching_ranks.append(int(teaching_rank1))
                    univ1_research_ranks.append(int(research_rank1))
                    univ1_citations_ranks.append(int(citations_rank1))
                    univ1_international_outlook_ranks.append(int(international_outlook_rank1))
                    univ1_industry_income_ranks.append(int(industry_income_rank1))
                    univ1_ranks.append(int(rank1))
                    univ1_overall_ranks.append(int(overall_rank1))

with col2:
    univ2 = st.selectbox("Select Second University, (or Alternatively you can type your desired university, it will display if it will be present in the dataset)", univ_names)
    
    if univ2 == "Select University":
        st.warning('⚠️ To Get Started, Please select a university from the dropdown menu')
    
    else:
        univ2_years = []
        univ2_teaching_ranks = []
        univ2_research_ranks = []
        univ2_citations_ranks = []
        univ2_international_outlook_ranks = []
        univ2_industry_income_ranks = []
        univ2_ranks = []
        univ2_overall_ranks = []
        for key, df in dfs.items():
            univ_df2 = df[df['name'] == univ2]
            if not univ_df2.empty:
                country2 = univ_df2['location'].iloc[0]
                year2 = key.split("_")[0]
                rank2 = univ_df2['rank'].iloc[0]
                overall_rank2 = univ_df2['scores_overall_rank'].iloc[0]
                teaching_rank2 = univ_df2['scores_teaching_rank'].iloc[0]
                international_outlook_rank2 = univ_df2['scores_international_outlook_rank'].iloc[0]
                industry_income_rank2 = univ_df2['scores_industry_income_rank'].iloc[0]
                research_rank2 = univ_df2['scores_research_rank'].iloc[0]
                citations_rank2 = univ_df2['scores_citations_rank'].iloc[0]
                rank2 = str(rank2)
                rank2 = re.findall(r'\d+', rank2)
                
                if rank2 == []:
                    st.warning("😔 Rank Undefined, Please select other University")
                    visibility_of_c2 = False
                
                if visibility_of_c2:
                    rank2 = rank2[0]
                    univ2_years.append(year2)
                    univ2_teaching_ranks.append(int(teaching_rank2))
                    univ2_research_ranks.append(int(research_rank2))
                    univ2_citations_ranks.append(int(citations_rank2))
                    univ2_international_outlook_ranks.append(int(international_outlook_rank2))
                    univ2_industry_income_ranks.append(int(industry_income_rank2))
                    univ2_ranks.append(int(rank2))
                    univ2_overall_ranks.append(int(overall_rank2))

col1, col2 = st.columns(2)
if univ1 != "Select University" and univ2 != "Select University":
    if univ1 == univ2:
        st.write("<h4 style='text-align: center;'>Oops, You selected same Universities 😆</h4>", unsafe_allow_html=True)
    else:
        c1, c2 = 0, 0
        with col1:
            if visibility_of_c1:
                st.write(f"<h4>{univ1} ({country1})</h4>", unsafe_allow_html=True)
                st.write("<h4>➡️Average Ranking</h4>", unsafe_allow_html=True)
                st.write(f"<h5>Teaching Rank: {int(np.mean(univ1_teaching_ranks))}</h5>", unsafe_allow_html=True)
                st.write(f"<h5>Research Rank: {int(np.mean(univ1_research_ranks))}</h5>", unsafe_allow_html=True)
                st.write(f"<h5>Citations Rank: {int(np.mean(univ1_citations_ranks))}</h5>", unsafe_allow_html=True)
                st.write(f"<h5>International Outlook Rank: {int(np.mean(univ1_international_outlook_ranks))}</h5>", unsafe_allow_html=True)
                st.write(f"<h5>Industry Income Rank: {int(np.mean(univ1_industry_income_ranks))}</h5>", unsafe_allow_html=True)
                st.write(f"<h5>Rank: {int(np.mean(univ1_ranks))}</h5>", unsafe_allow_html=True)
                st.write(f"<h5>Overall Rank: {int(np.mean(univ1_overall_ranks))}</h5>", unsafe_allow_html=True)
                
                st.write("<h4>➡️Highest Rankings Achieved</h4>", unsafe_allow_html=True)
                st.write(f"<h5>Teaching Rank Achieved: {min(univ1_teaching_ranks)}</h5>", unsafe_allow_html=True)
                st.write(f"<h5>Research Rank Achieved: {min(univ1_research_ranks)}</h5>", unsafe_allow_html=True)
                st.write(f"<h5>Citations Rank Achieved: {min(univ1_citations_ranks)}</h5>", unsafe_allow_html=True)
                st.write(f"<h5>International Outlook Rank Achieved: {min(univ1_international_outlook_ranks)}</h5>", unsafe_allow_html=True)
                st.write(f"<h5>Industry Income Rank Achieved: {min(univ1_industry_income_ranks)}</h5>", unsafe_allow_html=True)
                st.write(f"<h5>Rank Achieved: {min(univ1_ranks)}</h5>", unsafe_allow_html=True)
                st.write(f"<h5>Overall Rank Achieved: {min(univ1_overall_ranks)}</h5>", unsafe_allow_html=True)
        
        with col2:
            if visibility_of_c2:
                st.write(f"<h4>{univ2} ({country2})</h4>", unsafe_allow_html=True)
                st.write("<h4>➡️Average Ranking</h4>", unsafe_allow_html=True)
                st.write(f"<h5>Teaching Rank: {int(np.mean(univ2_teaching_ranks))}</h5>", unsafe_allow_html=True)
                st.write(f"<h5>Research Rank: {int(np.mean(univ2_research_ranks))}</h5>", unsafe_allow_html=True)
                st.write(f"<h5>Citations Rank: {int(np.mean(univ2_citations_ranks))}</h5>", unsafe_allow_html=True)
                st.write(f"<h5>International Outlook Rank: {int(np.mean(univ2_international_outlook_ranks))}</h5>", unsafe_allow_html=True)
                st.write(f"<h5>Industry Income Rank: {int(np.mean(univ2_industry_income_ranks))}</h5>", unsafe_allow_html=True)
                st.write(f"<h5>Rank: {int(np.mean(univ2_ranks))}</h5>", unsafe_allow_html=True)
                st.write(f"<h5>Overall Rank: {int(np.mean(univ2_overall_ranks))}</h5>", unsafe_allow_html=True)

                st.write("<h4>➡️Highest Rankings Achieved</h4>", unsafe_allow_html=True)
                st.write(f"<h5>Teaching Rank Achieved: {min(univ2_teaching_ranks)}</h5>", unsafe_allow_html=True)
                st.write(f"<h5>Research Rank Achieved: {min(univ2_research_ranks)}</h5>", unsafe_allow_html=True)
                st.write(f"<h5>Citations Rank Achieved: {min(univ2_citations_ranks)}</h5>", unsafe_allow_html=True)
                st.write(f"<h5>International Outlook Rank Achieved: {min(univ2_international_outlook_ranks)}</h5>", unsafe_allow_html=True)
                st.write(f"<h5>Industry Income Rank Achieved: {min(univ2_industry_income_ranks)}</h5>", unsafe_allow_html=True)
                st.write(f"<h5>Rank Achieved: {min(univ2_ranks)}</h5>", unsafe_allow_html=True)
                st.write(f"<h5>Overall Rank Achieved: {min(univ2_overall_ranks)}</h5>", unsafe_allow_html=True)

st.write("---")
year = st.slider('Select Year', min_value=2012, max_value=2023)
dct = {2012:1, 2013:2, 2014:3, 2015:4, 2016:5, 2017:6, 2018:7, 2019:8, 2020:9, 2021:10, 2022:11, 2023:12}
filename = filenames[dct[year]]
df = pd.read_csv(filename)

col1, col2, col3 = st.columns(3)
with col1:
    st.write("")
with col2:
    top_universities_acc_to_rank = df[df['rank'].str.replace('=', '').apply(pd.to_numeric, errors='coerce').between(1, 10)]
    st.write(f"<h5>Top 10 Universities in {year} based on Rank</h5>", unsafe_allow_html=True)
    st.write(top_universities_acc_to_rank[['rank', 'name']])
with col3:
    st.write("")

st.write("---")
st.markdown("**Dataset Used:** [Link To Dataset↗️](https://www.kaggle.com/datasets/r1chardson/the-world-university-rankings-2011-2023)")
