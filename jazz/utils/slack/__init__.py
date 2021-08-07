import os
import slack

class Slack:

  @classmethod
  def client(cls):
    return slack.WebClient(token=os.environ["SLACK_TOKEN_"])
