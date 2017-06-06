import os
from flask import Flask, request, jsonify
from ChatBotPoc import CrmnextChatBot
from flask_cors import CORS, cross_origin

bot = CrmnextChatBot()

app = Flask(__name__)

app.debug = True

CORS(app)

<<<<<<< HEAD
@app.route('/')
def mainpage():
    return render_template('index.html')
    
=======

@app.route('/')
def mainpage():
    return render_template('index.html')
>>>>>>> b5c8eedefe7c1be23962b2a3c55e01539420b58f

@app.route('/request', methods=['POST'])
def post_reponse():

    isRe_Connect = request.json['re_connect']
    content = request.json['message']
    messageType = request.json['type']
    action = "Default"
    contact_number = "4659"

    if messageType == "data":
        data = request.json['data']
        contact_number = data.get('contact_number')
        dob = data.get('dob')

    action = bot.run_bot(content, isRe_Connect,contact_number)
    result = "No Form"

    if action == "#show_form":
        result = {
            "type": "card",
            "template": "form",
            "message":
                {
                    "heading": "Please provide your details:",
                    "ok": "OK",
					"reesponse": "Detials Provided",
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
    elif action == "#showactions":
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
    elif action == "#re_issue_card_status":
        result = {
            "type": "card",
            "template": "status",
            "message": {
                "heading": "Your Case Status",
                "steps": [
                    {
                        "no": "01",
                        "label": "New",
                        "current": True
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
                        "label": "Withdraw",
						"response": "Withdraw",
                    }, {
                        "label": "Escalate",
						"response": "Escalate",
                    }
                ]
            }
        }
    # Json for loan approval
    elif action == "#show_form_loan":
        result = {
            "type": "card",
            "template": "form",
            "message": {
                "heading": "Please provide your details:",
                "ok": "OK",
				"response": "loan form submitted",
                "fields": [
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
    elif action == "#offer_loan_cards":
        result = {
            "type": "batch",
            "message": [
				{
					"type": "text",
					"message": "Thanks, here are some offers for you.",
					"senderId": "1234"
				},
				{
					"type": "card",
					"template": "info",
					"message": "Corporate plus personal loan @ 11% PA",
					"senderId": "1234"
				},				{
					"type": "card",
					"template": "info",
					"message": "Super saving loan @ 10.5 PA",
					"senderId": "1234"
				},				{
					"type": "card",
					"template": "info",
					"message": "Diamond jubilee plan @ 11.02% PA",
					"senderId": "1234"
				}
			]
        }
    elif action == "#cibil_check":
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
