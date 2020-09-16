import tweepy
import twitter_config as CFG

def tweet():
    print("--- <START> tweepy ---")

    # Authenticate to Twitter
    print("    ...Authenticating")

    auth = tweepy.OAuthHandler(CFG.CONSUMER_KEY, CFG.CONSUMER_SECRET)
    auth.set_access_token(CFG.ACCESS_TOKEN, CFG.ACCESS_TOKEN_SECRET)

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

    #api.update_status("Hello Tweepy")

    print("--- <END> tweepy ---")

    return True

tweet()
