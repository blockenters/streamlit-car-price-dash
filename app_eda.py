import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb


def run_eda():
    st.subheader('탐색적 데이터 분석 (EDA)')

    try:
        df = pd.read_csv('./data/Car_Purchasing_Data.csv')
    except FileNotFoundError:
        st.error('데이터 파일을 찾을 수 없습니다. ./data/Car_Purchasing_Data.csv 경로를 확인하세요.')
        return

    st.write('데이터 정보 요약')
    col1, col2 = st.columns([3, 1])
    with col1:
        view = st.radio('보기 선택', ['데이터프레임', '기본 통계', '컬럼 정보'])
        if view == '데이터프레임':
            st.dataframe(df)
        elif view == '기본 통계':
            st.dataframe(df.describe(include='all'))
        else:
            st.write(df.dtypes)

    with col2:
        st.metric('행 수', f'{df.shape[0]:,}')
        st.metric('열 수', df.shape[1])

    st.markdown('---')

    # numeric columns for plotting
    numeric_cols = df.select_dtypes(include=['number']).columns.tolist()
    if not numeric_cols:
        st.warning('숫자형 컬럼이 없어 시각화를 할 수 없습니다.')
        return

    st.subheader('단일 컬럼 시각화')
    colx = st.selectbox('컬럼 선택', numeric_cols)
    plot_type = st.selectbox('그래프 종류', ['Histogram', 'Boxplot'])
    fig, ax = plt.subplots(figsize=(6, 3))
    if plot_type == 'Histogram':
        ax.hist(df[colx].dropna(), bins=20, color='#2563eb', alpha=0.8)
        ax.set_xlabel(colx)
        ax.set_ylabel('count')
    else:
        ax.boxplot(df[colx].dropna())
        ax.set_xlabel(colx)
    st.pyplot(fig)

    st.markdown('---')
    st.subheader('두 컬럼 관계 분석')
    cols = st.multiselect('두 개 선택 (scatter)', numeric_cols, default=numeric_cols[:2])
    if len(cols) == 2:
        fig2, ax2 = plt.subplots(figsize=(6, 4))
        ax2.scatter(df[cols[0]], df[cols[1]], alpha=0.6)
        ax2.set_xlabel(cols[0])
        ax2.set_ylabel(cols[1])
        st.pyplot(fig2)

    st.markdown('---')
    st.subheader('상관관계 히트맵')
    sel = st.multiselect('상관계산할 컬럼 선택 (최소 2개)', numeric_cols, default=numeric_cols[:4])
    if len(sel) >= 2:
        corr = df[sel].corr()
        st.dataframe(corr)
        fig3, ax3 = plt.subplots(figsize=(6, 5))
        sb.heatmap(corr, vmin=-1, vmax=1, cmap='coolwarm', annot=True, fmt='.2f', linewidths=0.6, ax=ax3)
        st.pyplot(fig3)

    st.markdown('---')
    st.subheader('페어 플롯 (작은 샘플로 생성)')
    pair_cols = st.multiselect('페어플롯 컬럼 선택', numeric_cols, default=numeric_cols[:4])
    if len(pair_cols) >= 2:
        # 샘플링해서 그리기 (pairplot은 큰 데이터에서 느림)
        sample_df = df[pair_cols].dropna().sample(n=min(300, len(df)))
        try:
            g = sb.pairplot(sample_df)
            st.pyplot(g.fig)
        except Exception as e:
            st.error(f'페어플롯 생성 중 오류: {e}')