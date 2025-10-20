import streamlit as st
# 모델 불러오기 위한 라이브러리
import joblib
import pandas as pd


def run_ml():
    st.subheader('구매 금액 예측하기')

    st.info('아래 정보를 입력하면, 학습된 회귀 모델로 구매 금액을 예측합니다.')

    col1, col2 = st.columns(2)
    with col1:
        gender = st.radio('성별', ['여자', '남자'])
        age = st.number_input('나이', min_value=18, max_value=100, value=35)
        salary = st.number_input('연봉 (달러)', min_value=0, value=50000, step=1000)
    with col2:
        debt = st.number_input('카드 빚 (달러)', min_value=0, value=3000, step=100)
        worth = st.number_input('순자산 (달러)', min_value=0, value=50000, step=1000)
        st.write('')

    gender_data = 0 if gender == '여자' else 1

    if st.button('예측하기'):
        # 로컬 모델 파일 확인
        model_path = './model/regressor.pkl'
        try:
            regressor = joblib.load(model_path)
        except FileNotFoundError:
            st.error(f'모델 파일을 찾을 수 없습니다: {model_path}')
            st.info('먼저 학습한 모델을 `./model/regressor.pkl` 위치에 넣어주세요.')
            return
        except Exception as e:
            st.error(f'모델을 불러오는 중 오류가 발생했습니다: {e}')
            return

        new_data = [{'Gender': gender_data, 'Age': age, 'Annual Salary': salary, 'Credit Card Debt': debt, 'Net Worth': worth}]
        df_new = pd.DataFrame(new_data)

        try:
            y_pred = regressor.predict(df_new)
        except Exception as e:
            st.error(f'예측 중 오류가 발생했습니다: {e}')
            return

        pred_value = float(y_pred[0])
        if pred_value < 0:
            st.warning('예측 결과가 음수입니다. 입력값을 확인해주세요.')
        else:
            price = f"{int(round(pred_value)):,}"
            st.success(f'예측한 구매 금액: {price} 달러')

            st.markdown('**입력 요약**')
            st.table(df_new)

            csv = df_new.to_csv(index=False).encode('utf-8')
            st.download_button('입력값 CSV로 다운로드', csv, file_name='input_sample.csv', mime='text/csv')
        
