# JokesAPI

A simple API for getting jokes about Chuck Norris and Dads.

This code was written for a technical test,
it's not really designed to stand alone.

## Run the code

First create and activate your virtualenv - with the `venv` package on OSX or Linux, this will be:

```bash
python3 -m venv venv
source venv/bin/activate
```

With your virtualenv active, install the project locally:

```bash
pip install -e .
```

Then you will need to execute flask.

Use a program like "postman" to see the outputs of the calls

##JOKES ENDPOINT
GET ("/")
  Output is a random joke from api.chucknorris or icanhazdadjoke.api
GET("/Chuck")
  Output is a random joke from api.chucknorris
GET("/Dad")
  Output is a random joke from icanhazdadjoke api
  
POST ("/?joke=")
  Save in mongodbatlas a joke you write as a parameter
PUT ("/?joke=&number=")
  Update a joke writting as parameter the new joke and a number of the joke you want to update
DELETE ("/?number=")
  Delete a joke from mongodbatlas
  
##MATH ENDPOINT
GET("/numbers?numeros=")
  Output is the least common multiple from numbers you write as params.
GET("/number?numero=")
  Output is the number you write as param + 1.
