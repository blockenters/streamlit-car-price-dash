import streamlit as st
from app_eda import run_eda
from app_home import run_home
from app_ml import run_ml


def _local_css():
    css = """
    <style>
    .stApp {
        background: linear-gradient(180deg, #f8fafc 0%, #eef2ff 100%);
        color: #0f172a;
        font-family: 'Segoe UI', Roboto, 'Nanum Gothic', sans-serif;
    }
    .main-header {
        font-size:28px; font-weight:700; color:#0b1220; margin-bottom:6px;
    }
    .card { padding:12px; border-radius:10px; background: white; box-shadow: 0 2px 8px rgba(12, 18, 42, 0.06); }
    .muted { color: #334155 }
    </style>
    """
    st.markdown(css, unsafe_allow_html=True)


def main():
    st.set_page_config(page_title='자동차 구매 금액 예측', layout='wide', initial_sidebar_state='expanded')

    _local_css()

    # App header
    st.markdown('<div class="main-header">자동차 구매 금액 예측 대시보드</div>', unsafe_allow_html=True)
    st.markdown('<div class="muted">데이터 기반의 간단한 EDA와 회귀 모델을 이용한 예측 시연</div>', unsafe_allow_html=True)

    menu = ['Home', 'EDA', 'ML']
    choice = st.sidebar.selectbox('메뉴', menu)

    if choice == 'Home':
        run_home()
    elif choice == 'EDA':
        run_eda()
    elif choice == 'ML':
        run_ml()


if __name__ == '__main__':
    main()

