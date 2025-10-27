import streamlit as st
from joblib import load
model = load('data/iris_model.joblib')

col1, col2= st.columns(2)


with col1:
    st.subheader("Sepal Measurements")
    sepalLength = st.number_input("Sepal Length", placeholder="Type a number...")
    sepalWidth = st.number_input("Sepal Width", placeholder="Type a number...")

with col2:
     st.subheader("Petal Measurements")
     petalLength = st.number_input("Petal Length", placeholder="Type a number...")
     petalWidth = st.number_input("Petal Width", placeholder="Type a number...")
    
predict_btn = st.button("Predict", type="primary")


if predict_btn:

    prediction = model.predict([[sepalLength, sepalWidth, petalLength, petalWidth]])[0]

    if prediction == 0:
        flower_name = "Iris Setosa"
        flower_img = "images/iris_setosa.png"
    elif prediction == 1:
        flower_name = "Iris Versicolour"
        flower_img = "images/iris_versicolor.png"
    else:
        flower_name = "Iris Virginica"
        flower_img = "images/iris_virginica.png"

    st.success(flower_name)
    st.image(flower_img, width=300, caption=flower_name)

