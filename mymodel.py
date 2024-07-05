import streamlit as st
import pandas as pd
import pickle
from PIL import Image
Image.open('tnb_logo.png').convert('RGB').save('tnb.jpeg')
im= Image.open("tnb.jpeg")
st.image(im, width=200, caption="tnb Logo")
coll, col2=st.columns(2)
df = pd.read_csv('electricity_usage.csv')


st.dataframe(df)

with coll:
    df_city=df.groupby('City')['ElectricityBill'].sum().reset_index()

    st.bar_chart(df,x="City", y="MonthlyHours")

    with col2:
        df_city =df.groupby('City') ['ElectricityBill'].sum().reset_index()

        st.bar_chart(df, x="City", y="ElectricityBill")
fan = st.slider("Number of Fan", 5,20, value=10)
fridge = st.slider("Number of Refrigerator", 18,23, value=20)
aircon = st.slider("Number of Aircon', 0,3 value=1")
tv = st.slider("Number of TNB", 5,20, value=3)
hour = st.slider("Number of TV", 390,600, value=400)

model = pickle.load(open("LRmodel.pkl", "rb"))
new_data={'Fan':[fan],'Refrigerator':[fridge],'AirConditioner':[aircon],'Television':[tv],'MonthlyHours':[hour]}
        
pd.DataFrame.from_dict(new_data)
pred = model.predict(pd.DataFrame.from_dict(new_data))

pred = round(pred[0], 2)
st.subheader('The predicted Electricity Bill is' + str(pred))