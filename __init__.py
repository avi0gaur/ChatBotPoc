import os
from flask import Flask, request, jsonify
from ChatBotPoc import CrmnextChatBot
from flask_cors import CORS, cross_origin

bot = CrmnextChatBot()

app = Flask(__name__)

CORS(app)


# chat_response = [
#     {
#
#         "type": "text",
#         "message": message,
#         "senderId": "123"
#     }
# ]
@app.route('/response', methods=['GET'])
def get_reponse():
    return bot.run_bot("I lost my card")


@app.route('/request', methods=['POST'])
def post_reponse():
    response = request.json['response']
    message = "Default"
    if 'form_data' in response:
         # need to make a parent key called "response"
        contact_number = response.get('contact_number')
        dob = response.get('dob')
        isRe_Connect = response.get('re_connect')
        content = response.get('message')
        message = bot.run_bot(content, isRe_Connect)
    else:
        content = response.get('message')
        isRe_Connect = response.get('re_connect')
        message = bot.run_bot(content, isRe_Connect)

    result = "No Form"

    if message == "#show_form":
        result = {
            "type": "card",
            "template": "form",
            "message":
                {
                    "heading": "Please provide your:",
                    "ok": "OK",
                    "fields":
                       [
                            {
                                "name": "dob",
                                "label": "DOB",
                                "type": "date"
                            },
                            {
                                "name": "mobile",
                                "label": "Mobile",
                                "type": "tel"
                            }

                      ]
                },
            "senderId": "1234"
        }
    elif message == "#showactions":
        result = {
            "type": "action",
            "message": [
                {
                    "label": "I will keep you updated",
                    "response": "OK. Keep me updated",
                },
                {
                    "label": "Any more assisance?",
                    "response": "Yes, I need Assistance"
                }
            ],
            "senderId": "1234"
        }
    elif message == "#re_issue_card_status":
        result = {
        "type": "card",
        "template": "status",
         "message": {
            "heading": "Your Case Status",
            "steps": [
                {
                    "no": "01",
                    "label": "New",
                    "current":True
                }, {
                    "no": "02",
                    "label": "Analysis",
                    "current": True
                }, {
                    "no": "03",
                    "label": "Fixing",
                    "current": True
                }, {
                    "no": "04",
                    "label": "Close",
                    "current": False
                }
            ],

            "fields": [
                {
                    "label": "Case Id",
                    "value": "39462"
                }, {
                    "label": "Estimated Closure",
                    "value": "19th June 2017"
                }, {
                    "label": "Product",
                    "value": "Credit card"
                }
            ],
            "actions": [
                {
                    "label": "Withdraw"
                }, {
                    "label": "Escalate"
                }
            ]
        }
}
    #Json for loan approval
    elif message == "#show_form_loan":
     result = {
            "type": "card",
            "template": "form",
            "message":
                {
                    "heading": "Please provide your:",
                    "ok": "OK",
                    "fields":
                        [
                            {
                                "name": "dob",
                                "label": "DOB",
                                "type": "date"
                            },
                            {
                                "name": "mobile",
                                "label": "Mobile",
                                "type": "tel"
                            },
                            {
                                "name": "pan",
                                "label": "Pan",
                                "type": "pan"
                            },
                            {
                                "name": "amount",
                                "label": "Amount",
                                "type": "amo"
                            },
                            {
                                "name": "duration",
                                "label": "Duration",
                                "type": "dur"
                            }
                    ]
                },
            "senderId": "1234"
        }
    elif message == "#offer_loan_cards":
        result = {
                    "type": "text",
                    "message": "Thanks, here are some offers for you.",
                    "senderId": "1234",
                    "card1_message":"Corporate plus personal loan @ 11% PA",
                    "card2_message":"Super saving loan @ 10.5 PA",
                    "card3_message":"Diamond jubilee plan @ 11.02% PA"
                 }
    elif message == "#cibil_check":
        result = {
                    "type": "text",
                    "message": "#show_cibil_image",
                    "senderId": "1234"
                 }
    else:
        result = {
            "type": "text",
            "message": message,
            "senderId": "1234"
        }


    return jsonify(result)

if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)


