from __future__ import print_function
import time
import strava_api_v3
from strava_api_v3.rest import ApiException
from pprint import pprint
import os
from dotenv import load_dotenv

# Cargar variables de entorno desde el archivo .env
load_dotenv()

# Configurar OAuth2 access token for authorization: strava_oauth
configuration = strava_api_v3.Configuration()
configuration.access_token = os.getenv("ACCESS_TOKEN")

api_instance = strava_api_v3.ActivitiesApi(strava_api_v3.ApiClient(configuration))
id = 10978004039 # int | The identifier of the activity.
include_all_efforts = True # bool | To include all segments efforts. (optional)

try:
    # Get Activity
    api_response = api_instance.get_activity_by_id(id, include_all_efforts=include_all_efforts)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ActivitiesApi->get_activity_by_id: %s\n" % e)