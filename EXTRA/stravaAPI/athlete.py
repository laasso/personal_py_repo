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


api_instance = strava_api_v3.GearsApi(strava_api_v3.ApiClient(configuration))
id = 41979529 # int | The identifier of the gear.

try:
    # Get Equipment
    api_response = api_instance.get_gear_by_id(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GearsApi->get_gear_by_id: %s\n" % e)
