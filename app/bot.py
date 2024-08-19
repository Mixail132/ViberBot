""" The Flask application to handle incoming requests to the bot. """

from config import viber, bot_vars
from viberbot.api.viber_requests import ViberMessageRequest
from viberbot.api.viber_requests import ViberConversationStartedRequest
from viberbot.api.messages.text_message import TextMessage
from flask import Flask, request, Response


app = Flask(__name__)


@app.route("/viber", methods=["POST"])
def incoming():
    """ Handles the incoming requests to the bot. """
    viber_request = viber.parse_request(request.get_data())
    if isinstance(viber_request, ViberMessageRequest):
        message = viber_request.message
        viber.send_messages(viber_request.sender.id, [message])
    elif isinstance(viber_request, ViberConversationStartedRequest):
        message = TextMessage(text=viber_request.user.id)
        viber.send_messages(bot_vars.admin, [message])

    return Response(status=200)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8443, debug=True)
