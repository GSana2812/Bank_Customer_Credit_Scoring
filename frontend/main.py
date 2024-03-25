import streamlit as st
import requests
import json

def run():
    st.title("Credit Scoring Prediction")

    # Input fields
    job = st.text_input("Job Status")
    duration = st.number_input("Duration", min_value=0)
    poutcome = st.text_input("Poutcome")

    #Predict button
    predict_button = st.button("Check Status")

    if predict_button:

        payload = {"job": job, "duration": duration, "poutcome": poutcome}
        res = requests.post(url="http://0.0.0.0:8000/predict_credit", data=json.dumps(payload))
        # Check if the request was successful (status code 200)
        if res.status_code == 200:

            probability = res.json()['Probability']
            approval = res.json()['Credit']

            if approval == 0:
                st.subheader("It can't be approved!")
            if approval == 1:
                st.subheader("It can be approved")



if __name__ == "__main__":
    run()