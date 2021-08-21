# room_prediction_model

A model (built in TensorFlow) that predicts the number of people in a room at a given time.

Works as an API in a Flask app, deployed on Heroku. 

POST a timestamp in the format 'DD-MM-YYYY HH:MM', with a response coming in the format of '{ results: {results: <PREDICTION>} }'
  
Contains a '/get' route that can be used for testing purposes.

Built for use in a placement project for my MSc in Software Design with Artificial Intelligence from Athlone Institute of Technology, Ireland.
