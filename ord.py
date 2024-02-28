from requests_oauthlib import OAuth1Session

post_id = 'target post id'
operation = 'destroy'
url = "https://api.twitter.com/1.1/statuses/%s/%s.json"%(operation,post_id)

Consumer_Key = 'X app's consumer key'
Consumer_Secret = 'X app's consumer secret'

Access_Token = 'X app's access token'
Access_Secret = 'X app's access secret'

tw =  OAuth1Session(Consumer_Key, Consumer_Secret, Access_Token, Access_Secret)
tw.tweet(url)
