# pip install msal requests
import json
import logging
import requests
import msal

# pip install python-dotenv
from dotenv import load_dotenv
import os
load_dotenv()

clientid = os.getenv('CLIENTID')
secret = os.getenv('SECRET')
authority = os.getenv('AUTHORITY')
sharepoint_host = os.getenv('SHAREPOINT_HOST')
site_name = os.getenv("SITE_NAME")
path = os.getenv("FILEPATH")
ENDPOINT = 'https://graph.microsoft.com/v1.0'
SCOPES = [
    "https://graph.microsoft.com/.default"
]

# msal.ConfidentialClientApplicationのインスタンス化
app = msal.ConfidentialClientApplication(
    clientid, authority=authority, client_credential=secret,
)

def get_access_token() -> dict:
  result = app.acquire_token_silent(SCOPES, account=None)
  if not result:
    logging.info("No suitable token exists with silent.")
    result = app.acquire_token_for_client(scopes=SCOPES)
  if not "access_token" in result:
    print(result.get("error"))
    print(result.get("error_description"))
    print(result.get("correlation_id"))
    os._exit(1)
  return result

def get_some_data_from_graph_api(access_token, endpoint: str) -> None:
  print (endpoint)
  graph_data = requests.get(
      endpoint,
      headers={'Authorization': 'Bearer ' + access_token['access_token']}, ).json()
  return graph_data

def put_some_data_to_graph_api(access_token, endpoint: str, fpath: str) -> None:
  print (endpoint)
  with open(fpath, 'rb') as f:
    graph_data = requests.put(
        endpoint,
        headers={'Authorization': 'Bearer ' + access_token['access_token']},
        data=f).json()
  return graph_data

access_token = get_access_token()
site = get_some_data_from_graph_api(access_token,
  f"{ENDPOINT}/sites/{sharepoint_host}:/sites/{site_name}")
site_id = site["id"]
print (f"site id {site_id}")

print ("----drives---")
drive = get_some_data_from_graph_api(access_token,
  f"{ENDPOINT}/sites/{site_id}/drive")
drive_id = drive["id"]
print (f"drive id {drive_id}")

print ("----files in the path---")
files = get_some_data_from_graph_api(access_token,
  f"{ENDPOINT}/sites/{site_id}/drives/{drive_id}/root:/{path}:/children")
for item in files["value"]:
  print (
    "name:{} , size:{}, created_at:{}, uploaded_at:{}".format(
    item["name"],item["size"],item["createdDateTime"],item["lastModifiedDateTime"])
  )
