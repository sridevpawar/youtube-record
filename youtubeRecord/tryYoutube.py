from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow

SCOPES = ['https://www.googleapis.com/auth/youtube.readonly']

API_SERVICE_NAME = 'youtube'
API_VERSION = 'v3' 
API_KEY = 'AIzaSyDra_9QxfJa4HV5GHoIhGMqbZtV-JUPBS0 '
CLIENT_SECRETS_FILE = 'client_secrets.json'
flow = InstalledAppFlow.from_client_secrets_file(CLIENT_SECRETS_FILE, SCOPES)
credentials = flow.run_console()
service = build(API_SERVICE_NAME, API_VERSION, credentials = credentials)
serviceR = service.liveBroadcasts().list(
    broadcastStatus='active',
    part='id,snippet',
    maxResults=50
  )
serviceRR = serviceR.execute()
for stream in serviceRR.get('items', []):
    print('%s (%s)'.format(stream['snippet']['title'], stream['id']))