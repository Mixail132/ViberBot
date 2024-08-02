from config import viber
from viberbot.api.viber_requests import (
    ViberMessageRequest,
    ViberConversationStartedRequest)
from flask import Flask, request, Response


app = Flask(__name__)


@app.route("/bot", methods=["POST"])
def incoming():
    viber_request = viber.parse_request(request.get_data())
    if isinstance(viber_request, ViberMessageRequest):
        message = viber_request.message
        viber.send_messages(viber_request.sender.id, [message])
    elif isinstance(viber_request, ViberConversationStartedRequest):
        print(viber_request.user.id)
    return Response(status=200)


@app.route("/viber")
def checking():
    return "My Viber Bot is working"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8443, debug=True)
