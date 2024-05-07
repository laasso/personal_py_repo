from __future__ import print_function
import time
import strava_api_v3
from strava_api_v3.rest import ApiException
from pprint import pprint
import os
from dotenv import load_dotenv

# Cargar variables de entorno desde el archivo .env
load_dotenv()

# Configure OAuth2 access token for authorization: strava_oauth
configuration = strava_api_v3.Configuration()
configuration.access_token = os.getenv("ACCESS_TOKEN")

# create an instance of the API class
api_instance = strava_api_v3.AthletesApi(strava_api_v3.ApiClient(configuration))

try:
    # Get Authenticated Athlete
    api_response = api_instance.get_logged_in_athlete()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AthletesApi->get_logged_in_athlete: %s\n" % e)