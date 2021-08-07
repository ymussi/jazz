from jazz.api.bazooka.service import BazookaService

class BazookaController:

  @classmethod
  def send_message(cls, message):
    return BazookaService(message).send()
    