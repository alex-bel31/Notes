import datetime
import uuid

class Note:
    def __init__(self, title, body):
        self.id = uuid.uuid4()
        self.title = title
        self.body = body
        self.date = datetime.datetime.now()
