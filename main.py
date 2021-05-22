import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import time

st.title('streamlit 超入門')

st.write('プログレスバー')
'Start!!'

latest_iteration = st.empty()
bar = st.progress(0)

for i in range(1,100):
    latest_iteration.text(f'Iteration {i+1}')
    bar.progress(i +1)
    time.sleep(0.1)


left_column, right_column = st.beta_columns(2)
button = left_column.button('右からむに文字を表示')
if button:
    right_column.write('ここは右からむ')

expander = st.beta_expander('問合せ') 
expander.write('問合せ内容を書く')
# text = st.text_input('あならの好きな趣味を')
# condition = st.slider('あなたの今の調子は？', 0, 10, 5)

# 'あなたの趣味：', text
# 'コンディション', condition

# option = st.selectbox(
#     'あなたが好きな数字を教えてください。',
#     list(range(1,11))
# )
# 'あなたのスキが数字は', option, 'です'

# if st.checkbox('Show Image'):
#     img = Image.open('DSCF4892.jpg')
#     st.image(img, caption="JJ", use_column_width=True)



# df = pd.DataFrame(
#     np.random.rand(100, 2)/[50, 50] + [35.69, 139.70],
#     columns=['lat', 'lon']
# )

#df
#st.map(df)

#st.area_chart(df)
