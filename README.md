## Credit Scoring Approval

Given a person’s credit-related information, the purpose is to build a machine learning model that can classify the credit score.
The data is related with direct marketing campaigns of a Portuguese banking institution. 
The marketing campaigns were based on phone calls. 
Often, more than one contact to the same client was required, 
in order to access if the product (bank term deposit) would be ('yes') or not ('no') subscribed. 


This is a classification problem, taking 3 features into account to perform predictions:

-job - job name <br>
-duration - loan duration <br>
-poutcome - outcome of the previous marketing campaign (categorical: 'failure','nonexistent','success') <br>

This project is to showcase, a new concept added in the repertory of my professional skills, which is docker compose.
In the previous projects, I used a single Dockerfile for all the containerization of the app. In this project, im trying
to wrap both backend and frontend together, and it's simpler and more efficient doing so using docker compose.

The app directory contains backend and frontend directories, in which backend's code uses 
Fastapi to initialize the web service pointing to the port 8000, while the frontend uses a popular framework for 
creating responsive web apps, called streamlit. I have concatenated these 2 services together using docker compose. Docker
compose needs to have 2 Docker files mainly in the backend and frontend directories.

## Setup

 **Run docker compose:**

 `docker-compose up`
