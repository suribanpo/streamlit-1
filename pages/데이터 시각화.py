import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

csv_file = st.file_uploader(label='데이터를 업로드해주세요. 단, CSV 파일만 가능합니다. ')


if csv_file is not None:
    csv_file_df = pd.read_csv(csv_file, encoding="euc-kr")
    st.write(csv_file_df.head())

    column = st.radio(label='열 이름을 선택해주세요.', options=csv_file_df.columns)
    st.subheader(column + '의 분포를 그려보겠습니다.!')
    st.bar_chart(csv_file_df[column].value_counts())

    fig, ax = plt.subplots()
    sns.histplot(csv_file_df[column], binrange=[2500, 7000], binwidth=100)
    st.pyplot(fig)