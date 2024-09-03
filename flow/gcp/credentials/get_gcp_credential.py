# from google.oauth2 import service_account


# def get_gcp_credential():
#   credentials = service_account.Credentials.from_service_account_file('./keys/gcp.json')
  
#   return credentials


import google.auth
def get_gcp_credential():
  credentials, project = google.auth.default()
  return credentials