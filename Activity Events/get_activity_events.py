# Import packages
import requests
import adal
import json

# Function to write the api return to a json file
def escrever_json(dash):
    with open('jujuba2.json', 'w', encoding='utf8') as f:
        json.dump(dash, f, ensure_ascii=False, sort_keys=True, indent=4, separators=(',', ':'))

# Setup  Parameters
tenant_id = ''
authority_url = f'https://login.microsoftonline.com/{tenant_id}'
resource_url = 'https://analysis.windows.net/powerbi/api'
client_id = ''
client_secret = ''

# Generate token for accessing Power BI APIs
def access_token_header():
    context = adal.AuthenticationContext(authority=authority_url,
                                        validate_authority=True,
                                        api_version=None)

    token = context.acquire_token_with_client_credentials(resource_url, client_id, client_secret)
    access_token = token.get('accessToken')
    header = {'Authorization': f'Bearer {access_token}'}
    return header

# Define the url for the api call
url = "https://api.powerbi.com/v1.0/myorg/admin/activityevents?startDateTime='2023-12-03T00:00:00Z'&endDateTime='2023-12-03T23:59:59Z'"

# Making the api call and extracting the data
response = requests.get(url=url, headers=access_token_header())
heads = response.headers
con = heads.json()

# Response = 200 OK
print(heads)

# Write and save the json file with the api result
escrever_json(con)