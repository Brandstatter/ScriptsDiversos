from Google import Create_Service
import pandas as pd

#Start service.
CLIENT_SECRET_FILE = 'credentials.json'
API_NAME = 'drive'
API_VERSION = 'v3'
SCOPES = ['https://www.googleapis.com/auth/drive']

service = Create_Service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES)

print(dir(service))

#Listing files in a folder
#TODO Verify item folder
folder_id = '1tBPRYtl_Vdi16JoDToNKi22ruHmfwXdt?hl'

query = f"'{folder_id}' in parents"

response = service.files().list(q=query).execute()
files = response.get('files')
nextPageToken = response.get('nextPageToken')

while nextPageToken:
    response = service.files().list(q=query,pageToken=nextPageToken).execute()
    files.extend(response.get('files')) 
    nextPageToken = response.get('nextPageToken')

df = pd.DataFrame(files)
print(df)

#TODO Discover why the fuck the error token expired is happening