import streamlit as st

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb

def run_eda():
    # 데이터 불러오기
    df = pd.read_csv('./data/Car_Purchasing_Data.csv')

    st.text('이 데이터는 Car_Purchasing_Data.csv 데이터입니다')

    radio_menu = ['데이터프레임' , '기본통계']
    radio_choice = st.radio('선택하세요', radio_menu)
    if radio_choice == radio_menu[0] :
        st.dataframe( df )
    elif radio_choice == radio_menu[1] :
        st.dataframe( df.describe()  )

    st.subheader('최대 / 최소값 확인')

    min_max_menu = df.columns[ 4 :  ]
    select_choice = st.selectbox('컬럼을 선택하세요', min_max_menu)

    print(select_choice)    

    st.info( f'{select_choice} 는 {  int( df[select_choice].min() )   } 부터 { int( df[select_choice].max() ) } 까지 있습니다.' )

    st.subheader('상관관계분석')

    multi_menu = df.columns[ 4 :  ]
    choice_multi_list = st.multiselect('컬럼을 2개 이상 선택하세요' , multi_menu)

    print(choice_multi_list)

    if len( choice_multi_list ) >= 2 :
                
        st.dataframe( df[choice_multi_list].corr(numeric_only= True) )

        fig1 = plt.figure()
        sb.heatmap(data= df[choice_multi_list].corr(numeric_only= True), vmin=-1, vmax=1, cmap='coolwarm', annot=True, fmt='.2f', linewidths=0.8)         
        st.pyplot(fig1)


    st.subheader('각 컬럼간의 Pair Plot')
    fig2 = sb.pairplot(data= df, vars=['Age', 'Annual Salary', 'Credit Card Debt','Net Worth','Car Purchase Amount'])
    st.pyplot(fig2)