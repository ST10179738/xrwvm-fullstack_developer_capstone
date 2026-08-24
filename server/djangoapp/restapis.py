import requests
import os
from dotenv import load_dotenv


load_dotenv()

backend_url = os.getenv(
    'backend_url', default="http://localhost:3030")
sentiment_analyzer_url = os.getenv(
    'sentiment_analyzer_url',
    default="http://localhost:5000/")


def get_request(endpoint, **kwargs):
    """
    Perform a GET request to the Express/MongoDB backend service.
    """
    params = ""
    if kwargs:
        for key, value in kwargs.items():
            params = params + key + "=" + str(value) + "&"

    request_url = backend_url + endpoint + "?" + params

    print("GET from {}".format(request_url))
    try:
        # Call GET method of requests library with URL and parameters
        response = requests.get(request_url)
        return response.json()
    except Exception as err:
        # If any network error occurs
        print(f"Network exception occurred: {err}")
        return None


def analyze_review_sentiments(text):
    """
    Call the Sentiment Analyzer microservice to analyze review text.
    """
    request_url = sentiment_analyzer_url + "analyze/" + text
    try:
        # Call GET method of requests library
        response = requests.get(request_url)
        return response.json()
    except Exception as err:
        print(f"Unexpected {err=}, {type(err)=}")
        print("Network exception occurred")
        return {"sentiment": "neutral"}


def post_review(data_dict):
    """
    Perform a POST request to add a new review in the backend database.
    """
    request_url = backend_url + "/insert_review"
    try:
        response = requests.post(request_url, json=data_dict)
        print(response.json())
        return response.json()
    except Exception as err:
        print(f"Network exception occurred: {err}")
        return None
