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

# Crear una instancia de la clase API
api_instance = strava_api_v3.SegmentsApi(strava_api_v3.ApiClient(configuration))
id = 789 # int | The identifier of the segment leaderboard.
gender = 'gender_example' # str | Filter by gender. (optional)
age_group = 'age_group_example' # str | Premium Feature. Filter by age group. (optional)
weight_class = 'weight_class_example' # str | Premium Feature. Filter by weight class. (optional)
following = True # bool | Filter by friends of the authenticated athlete. (optional)
club_id = 789 # int | Filter by club. (optional)
date_range = 'date_range_example' # str | Filter by date range. (optional)
context_entries = 56 # int |  (optional)
page = 56 # int | Page number. (optional)
per_page = 30 # int | Number of items per page. Defaults to 30. (optional) (default to 30)

try:
    # Obtener la tabla de clasificación del segmento
    api_response = api_instance.get_leaderboard_by_segment_id(id, gender=gender, age_group=age_group, weight_class=weight_class, following=following, club_id=club_id, date_range=date_range, context_entries=context_entries, page=page, per_page=per_page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SegmentsApi->get_leaderboard_by_segment_id: %s\n" % e)
