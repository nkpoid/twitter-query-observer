import json
import logging
import os

import requests
import tweepy


class QueryObserver(tweepy.StreamingClient):
    def on_tweet(self, tweet: tweepy.Tweet):
        logger.info(tweet)
        requests.post(
            os.environ["WEBHOOK_URL"],
            json.dumps({"content": f"https://twitter.com/twitter/statuses/{tweet.id}"}),
            headers={"Content-Type": "application/json"},
        )


if __name__ == "__main__":
    logger = logging.getLogger("QueryObserver")
    logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s:%(message)s")

    streamer = QueryObserver(os.environ["BEARER_TOKEN"])
    logger.info(f"Rules:{streamer.get_rules().data}")  # type:ignore

    streamer.filter()
