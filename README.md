# room_prediction_model

A model (built in TensorFlow) that predicts the number of people in a room at a given time.

Works as an API in a Flask app, deployed on Heroku. 

POST a timestamp in the format 'DD-MM-YYYY HH:MM', with a response coming in the format of '{ results: {results: PREDICTION} }'
  
Contains a '/get' route that can be used for testing purposes if running on Localhost server.

Built for use in a placement project for my MSc in Software Design with Artificial Intelligence from Athlone Institute of Technology, Ireland.

To download the repo enter the command:

    git clone https://github.com/DarraghTate/room_prediction_model.git
    
To install the required packages (recommended in a virtual environment), enter the command:

    pip install -r requirements.txt
    
To run the development server, enter the command:

    flask run
    
To see the prediction for the provided timestamp (which can be edited in the get() function in app.py), go to the url 

    http://localhost:5000/get
    
This will print the prediction in the window from which the flask script is running. This shows that the GET functionality is operational.
