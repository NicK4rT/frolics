from requests_oauthlib import OAuth1Session

consumer_key = 'TUMBLR_CONSUMER_API_KEY'
consumer_secret = 'TUMBLR_CONSUMER_API_SECRET'
request_token_url = 'https://www.tumblr.com/oauth/request_token'
authorize_url = 'https://www.tumblr.com/oauth/authorize'
access_token_url = 'https://www.tumblr.com/oauth/access_token'

# Step 1: Get request token
oauth = OAuth1Session(consumer_key, client_secret=consumer_secret)
fetch_response = oauth.fetch_request_token(request_token_url)
resource_owner_key = fetch_response.get('oauth_token')
resource_owner_secret = fetch_response.get('oauth_token_secret')

# Step 2: Direct user to authorize URL
print("Go to the following link and authorize the app:")
print(f"{authorize_url}?oauth_token={resource_owner_key}")
verifier = input('Enter the PIN provided by Tumblr: ')

# Step 3: Obtain access token
oauth = OAuth1Session(
    consumer_key,
    client_secret=consumer_secret,
    resource_owner_key=resource_owner_key,
    resource_owner_secret=resource_owner_secret,
    verifier=verifier
)
oauth_tokens = oauth.fetch_access_token(access_token_url)
print("Access Token: ", oauth_tokens['oauth_token'])
print("Access Token Secret: ", oauth_tokens['oauth_token_secret'])
