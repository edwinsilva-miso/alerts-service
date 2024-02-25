from src.models.alert import Alert


class AlertService:

    def __init__(self):
        print("Alert")

    def send_alert(self, alert):
        print("Send alert event")
