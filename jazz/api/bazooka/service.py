import json
import os

from werkzeug.exceptions import NotFound

from jazz.utils.slack import Slack

class Bazooka:

  def __init__(self, message):
      self.message = message.get("text")
      self.channel_id = os.environ["BAZOOKA_CHANNEL_ID_"]

class BazookaService(Bazooka):

  def send(self):
    client = Slack.client()

    message = f"Bazooka: {self.message}"
    print(message)

    client.chat_postMessage(
        channel=self.channel_id, text=message, link_names=1)

    return {
        'statusCode': 200,
        'body': json.dumps(message)
    }
