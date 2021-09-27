# views.py
import http.client
import json
import datetime
from os import stat

from django.core.cache import cache
from django.conf import settings
from rest_framework.response import Response
from rest_framework.views import APIView

from courses.models import Course

PDGA_BASE_URL = 'api.pdga.com'
PDGA_CACHE_KEY = 'pdga_auth'

class PDGAPIView(APIView):
   """
   API View to connect with the PDGA API. Uses 'login', 'logout', 'events',
   and 'courses' endpoints to request relevant data. 
   """

   def authenticate(self):
      """
      Authenticate the server session and cache credentials
      """
      print('LOGIN')
      api_connection = http.client.HTTPSConnection(PDGA_BASE_URL)
      headers = {
            'Content-Type': 'application/json'
         }
      body = json.dumps({
         'username':settings.PDGA_UN, 
         'password':settings.PDGA_PW
         })
      api_connection.request(
         'POST', 
         '/services/json/user/login', 
         body, 
         headers
         )

      response = api_connection.getresponse()
      str_response = response.read().decode()
      json_response = json.loads(str_response)
      if response.status == 401:
         auth_401_response = {'status': response.status, 'error': json_response[0]}
         return Response(auth_401_response)
      cache.set(PDGA_CACHE_KEY, json_response, None)
      return Response(json_response)

   def destroy_session(self, session_data):
      """
      Submit request to end current session and clear credentials from cache
      """
      api_connection = http.client.HTTPSConnection(PDGA_BASE_URL)
      headers = {
           'X-CSRF-Token': session_data['token'],
           'Cookie': f'{session_data["session_name"]}={session_data["sessid"]}'
        }
      api_connection.request(
         'POST', 
         '/services/json/user/logout', 
         None, 
         headers
         )

      response = api_connection.getresponse()
      str_response = response.read().decode()
      json_response = json.loads(str_response)
      if response.status == 406:
         auth_406_response = {'status': response.status, 'error': json_response[0]}
         cache.delete(PDGA_CACHE_KEY)
         return Response(auth_406_response)
      cache.delete(PDGA_CACHE_KEY)
      return Response(json_response)

   def get_upcoming_events(self, session_data, event_params):
      """
      Request for upcoming events. Should set event parameter equal to users
      current state. By default, will return all events within the next 90 days.
      """
      today_date = datetime.date.today()

      start_date = f'start_date={today_date.isoformat()}'
      end_date = f'end_date={(today_date + datetime.timedelta(days=90)).isoformat()}'
      state = f'state={event_params.upper()}'
      limit = 'limit=7'

      api_connection = http.client.HTTPSConnection(PDGA_BASE_URL)
      headers = {
            'Cookie': f'{session_data["session_name"]}={session_data["sessid"]}'
         }
      api_connection.request(
         'GET', 
         f'/services/json/event?{start_date}&{end_date}&{state}&{limit}', 
         None, 
         headers
         )

      response = api_connection.getresponse()
      str_response = response.read().decode()
      json_response = json.loads(str_response)
      if response.status == 401:
         auth_401_response = {'status': response.status, 'error': json_response[0]}
         return Response(auth_401_response)
      return Response(json_response)

   def search_courses_by_name(self, session_data):
      search_term = self.request.query_params.get('search-term', None)

      if search_term is None:
         auth_400_response = {'status': 400, 'error': 'No query parameters were found. Please provide a search term.'}
         return Response(auth_400_response)

      api_connection = http.client.HTTPSConnection(PDGA_BASE_URL)
      headers = {
            'Cookie': f'{session_data["session_name"]}={session_data["sessid"]}'
         }
      api_connection.request(
         'GET', 
         f'/services/json/course?course_name={search_term}', 
         None, 
         headers
         )

      response = api_connection.getresponse()
      str_response = response.read().decode()
      json_response = json.loads(str_response)

      for course in json_response['courses']:
         try:
            course_object = Course.objects.get(pdga_id=int(course['course_id']))
            course['id'] = course_object.id
            course['image_url'] = course_object.image_url
            course['image_alt'] = course_object.image_alt
         except Course.DoesNotExist:
            course['id'] = None
            course['image_url'] = None
            course['image_alt'] = None
            continue

      if response.status == 401:
         auth_401_response = {'status': response.status, 'error': json_response[0]}
         return Response(auth_401_response)
      return Response(json_response)

   def get_nearby_courses(self, session_data):
      """
      Requests the 10 nearest courses to a given location. Seperate 'lat' and 'lng'
      query params are required for the request to work. 
      """
      print("Courses")
      lat = self.request.query_params.get('lat', None)
      lng = self.request.query_params.get('lng', None)

      if lat is not None and lng is not None:
         coords = f'latitude={lat}&longitude={lng}'
      else:
         auth_400_response = {'status': 400, 'error': 'No query parameters were found. Please provide lat and lng.'}
         return Response(auth_400_response)

      api_connection = http.client.HTTPSConnection(PDGA_BASE_URL)
      headers = {
            'Cookie': f'{session_data["session_name"]}={session_data["sessid"]}'
         }
      api_connection.request(
         'GET', 
         f'/services/json/course?{coords}', 
         None, 
         headers
         )

      response = api_connection.getresponse()
      str_response = response.read().decode()
      json_response = json.loads(str_response)

      for course in json_response['courses']:
         try:
            course_object = Course.objects.get(pdga_id=int(course['course_id']))
            course['id'] = course_object.id
            course['image_url'] = course_object.image_url
            course['image_alt'] = course_object.image_alt
         except Course.DoesNotExist:
            course['id'] = None
            course['image_url'] = None
            course['image_alt'] = None
            continue

      if response.status == 401:
         auth_401_response = {'status': response.status, 'error': json_response[0]}
         return Response(auth_401_response)
      return Response(json_response)

   def get(self, request):
      """
      Handles the requests to this endpoint and redirects to correct request method.
      """
      pdga_auth = cache.get(PDGA_CACHE_KEY)

      login = self.request.query_params.get('login', None)
      logout = self.request.query_params.get('logout', None)
      events = self.request.query_params.get('events', None)
      courses = self.request.query_params.get('courses', None)
      courses_search = self.request.query_params.get('courses-search', None)

      if login is not None and not pdga_auth:
         return self.authenticate()
      elif logout is not None and pdga_auth is not None:
         return self.destroy_session(pdga_auth)
      elif events is not None and pdga_auth is not None:
         return self.get_upcoming_events(pdga_auth, events)
      elif courses is not None and pdga_auth is not None:
         return self.get_nearby_courses(pdga_auth)
      elif courses_search is not None and pdga_auth is not None:
         return self.search_courses_by_name(pdga_auth)

      # Conditional check on connection to api
      if pdga_auth:
         status = 200
         msg = 'connected to api'
      else:
         status = 500
         msg = 'not connected to api'

      return Response({
         # Provide a default response to help find correct endpoint and to
         # check on the sessions status
         'HEADER': 'Please use one of the following query params:',
         'status': status,
         'msg': msg,
         'valid_params': {
            'login': 'Create a new session with the PDGA API',
            'logout': 'Terminate an existing session',
            'events': 'Get all events in provided state over next 90 days. Requires a two character state_province code',
            'courses': 'Get nearest ten courses to coordinates provided. Requires "lat" and "lng" params' ,
            'courses-search': 'Search courses by name. Requires a "search-term" param'
            }
         })