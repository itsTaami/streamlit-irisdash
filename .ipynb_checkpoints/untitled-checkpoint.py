import streamlit as st
from PIL import Image
from joblib import load

model = load('data/iris_model.joblib')

st.title('Iris flower Predictor')

col1, col2 = st.columns(2)
sepal_length = col1.number_input('Sepal length in cm', min_value=0.0, max_value=15.0, step=0.1, value=5.0)
sepal_width = col1.number_input('Sepal width in cm', min_value=0.0, max_value=15.0, step=0.1, value=4.0)
petal_length = col2.number_input('Petal length in cm', min_value=0.0, max_value=15.0, step=0.1, value=2.0)
petal_width = col2.number_input('Petal width in cm', min_value=0.0, max_value=15.0, step=0.1, value=3.0)

c1, c2, c3 = st.columns(3)
predict_button = c2.button('Predict')

if predict_button:
  prediction = model.predict([[sepal_length, sepal_width, petal_length, petal_width]])[0]
  if prediction == 0:
    image = Image.open('images/iris_setosa.png')
  elif prediction == 1:
    image = Image.open('images/iris_versicolor.png')
  else:
    image = Image.open('images/iris_virginica.png')
    
  c2.subheader("Your prediction is")
  c2.image(image)