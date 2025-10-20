import streamlit as st
import pandas as pd


def run_home():
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.subheader('자동차 데이터를 분석하고, 예측하는 앱')
    st.markdown('</div>', unsafe_allow_html=True)

    try:
        df = pd.read_csv('./data/Car_Purchasing_Data.csv')
        # 이미지 전체 화면에 표시
        st.image('./image/car.jpg', use_container_width=True, width='stretch' )
        st.markdown('---')
        col1, col2 = st.columns([2, 3])
        with col1:
            st.write('')
        with col2:
            st.markdown('''
            **설명**

            이 앱은 공개된 자동차 구매 데이터를 사용해 EDA(탐색적 데이터 분석)와 회귀 모델을 이용한 구매 금액 예측을 제공합니다.
            ''')
            st.write('데이터 샘플:')
            st.dataframe(df.head(6))
            st.write(f'총 샘플 수: {len(df):,}')
    except FileNotFoundError:
        st.warning('데이터 파일이 없습니다. ./data/Car_Purchasing_Data.csv 경로를 확인하세요.')

    st.markdown('---')
    st.caption('간단한 학습 목적의 데모 앱입니다. 실제 서비스용으로는 데이터/모델 검증이 필요합니다.')