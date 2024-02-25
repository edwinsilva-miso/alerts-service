from flask import request, Response, json, Blueprint
from src.models.alert import Alert
from src.core.services.alert_service import AlertService
from datetime import datetime

alerts = Blueprint("alerts", __name__)


@alerts.route('/event/<int:eventid>', methods=["POST"])
def generate_alert(eventid):
    data = request.json
    event_description = data["description"]
    cancellable = data["cancellable"]

    alert = Alert(event_id=eventid, description=event_description, time=datetime.utcnow(),
                  is_cancellable=bool(cancellable))

    service = AlertService()
    service.send_alert(alert=alert)

    return Response(
        response=json.dumps({
            "status": "success",
            "message": "Event alert subscribed successfully"
        }),
        status=201,
        mimetype='application/json'
    )
