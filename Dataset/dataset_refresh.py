# https://learn.microsoft.com/pt-br/rest/api/power-bi/datasets/refresh-dataset

# Import packages
import requests
import adal

#  Setup  Parameters
tenant_id = ''
authority_url = f'https://login.microsoftonline.com/{tenant_id}'
resource_url = 'https://analysis.windows.net/powerbi/api'

client_id = ''
client_secret = ''

workspaceId = ''
datesetId = ''

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
refresh_url = f'https://api.powerbi.com/v1.0/myorg/groups/{workspaceId}/datasets/{datesetId}/refreshes'

# Sending the command to update the dataset
r = requests.post(url=refresh_url, headers=access_token_header())
r.raise_for_status()
status = r.raise_for_status()

# if status = 200 ok
print(status)