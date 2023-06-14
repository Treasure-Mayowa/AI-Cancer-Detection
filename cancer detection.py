import numpy as np
import pickle
import streamlit as st

#loading the saved model
loaded_model = pickle.load(open('trained_model.sav', 'rb'))

def classifier(input_data):
    input_data_as_numpy_array = np.asarray(input_data)

    input_data_reshaped = input_data_as_numpy_array.reshape(1, -1)

    prediction = loaded_model.predict(input_data_reshaped)

    print(prediction)

    if prediction[0] == 0:
        return "Cell is benign"

    else:
        return "Cell is malignant"
    

def main():

    #Creating  a title
    st.title("AI-powered Cancel Detection")

    #Getting user's input 

    radius_mean = st.text_input("Radius Mean")
    texture_mean = st.text_input("Texture Mean")
    perimeter_mean = st.text_input("Perimeter Mean")
    area_mean = st.text_input("Area Mean")
    smoothness_mean = st.text_input("Smoothness Mean")
    compactness_mean = st.text_input("Compactness Mean")
    concavity_mean = st.text_input("Concavity Mean")
    concave_points_mean = st.text_input("Concave Points Mean")
    symmetry_mean = st.text_input("Symmetry Mean")
    fractal_dimension_mean = st.text_input("Fractal Dimension Mean")
    radius_se = st.text_input("Concave Points Mean")
    texture_se = st.text_input("Concave Points Mean")
    perimeter_se = st.text_input("Concave Points Mean")
    area_se = st.text_input("Concave Points Mean")
    smoothness_se = st.text_input("Concave Points Mean")
    compactness_se = st.text_input("Concave Points Mean")
    concavity_se = st.text_input("Concave Points Mean")
    concave_points_se = st.text_input("Concave Points Mean")
    symmetry_se = st.text_input("Concave Points Mean")
    fractal_dimension_se = st.text_input("Concave Points Mean")
    radius_worst = st.text_input("Concave Points Mean")
    texture_worst = st.text_input("Concave Points Mean")
    perimeter_worst = st.text_input("Concave Points Mean")
    area_worst = st.text_input("Concave Points Mean")
    smoothness_worst = st.text_input("Concave Points Mean")
    compactness_worst = st.text_input("Concave Points Mean")
    concavity_worst = st.text_input("Concave Points Mean")
    concave_points_worst = st.text_input("Concave Points Mean")
    symmetry_worst = st.text_input("Concave Points Mean")
    fractal_dimension_worst = st.text_input("Concave Points Mean")

    diagnosis = ' '

    if st.button("Test Result"):
        diagnosis = classifier([radius_mean,	texture_mean,	perimeter_mean,	area_mean,	smoothness_mean,	compactness_mean,	concavity_mean,	concave_points_mean,	symmetry_mean,	fractal_dimension_mean,	radius_se,	texture_se,	perimeter_se,	area_se,	smoothness_se,	compactness_se,	concavity_se,	concave_points_se,	symmetry_se,	fractal_dimension_se,	radius_worst,	texture_worst,	perimeter_worst,	area_worst,	smoothness_worst,	compactness_worst,	concavity_worst,	concave_points_worst,	symmetry_worst, fractal_dimension_worst])
    
    st.success(diagnosis)

if __name__ == "__main__":
    main()