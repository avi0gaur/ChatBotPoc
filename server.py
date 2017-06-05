
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
@app.route('/response',methods=['GET'])
def get_reponse():
        return bot.run_bot("I lost my card")

@app.route('/request',methods=['POST'])
def post_reponse():
    content = request.json['message']
    isRe_Connect = request.json['re_connect']
    message = bot.run_bot(content,isRe_Connect)
    chat_response = {
            "type": "text",
            "message": message,
            "senderId": "1234"
        }
    
    return jsonify(chat_response)

if __name__ == '__main__':
    app.run(debug=True)


