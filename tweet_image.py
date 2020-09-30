import os
import tweepy

def tweet_image(text, image):
    print("--- <START> tweet ---")

    # Authenticate to Twitter
    print("    ...Authenticating")

    auth = tweepy.OAuthHandler(os.environ.get('CONSUMER_KEY'),
                               os.environ.get('CONSUMER_SECRET'))
    auth.set_access_token(os.environ.get('ACCESS_TOKEN'),
                          os.environ.get('ACCESS_TOKEN_SECRET'))

    # Create API object and verify authentication
    print("    ...Create API object")

    api = tweepy.API(auth,
                     wait_on_rate_limit=True,
                     wait_on_rate_limit_notify=True)
    try:
        api.verify_credentials()
        print("    ...Authentication OK")
    except:
        print("    ...Error during authentication")

    # Create a tweet
    print("    ...Tweeting")

    upload = api.media_upload(image)

    status = api.update_status(text,
                               media_ids=[upload.media_id])

    print("--- <END> tweet ---")

    return status
