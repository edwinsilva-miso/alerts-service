import datetime

class Alert:
    def __init__(self, event_id: int, description: str, time: datetime, is_cancellable: bool):
        self.event_id = event_id
        self.description = description
        self.time = time
        self.is_cancellable = is_cancellable
