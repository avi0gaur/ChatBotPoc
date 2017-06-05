    ## Chat bot for crmnext.
## **** Avinash Gaur ****
import random
from textblob import TextBlob
import json
import re



class CrmnextChatBot:
    isCardStolen = False

    #Variables for User data
    card_style = None
    Message = None
    UserId = None
    Sentiment = None
    Name = None
    Contact_Number = None
    Pan_Number = None
    Aadhaar_number = None

    AccHolder = "Avinash Gaur"
    # Sentences we'll respond with if the user greeted us
    GREETING_KEYWORDS = ("hello", "hi", "greetings", "sup", "what's up",)

    GREETING_RESPONSES = ["'sup bro", "hey", "*nods*", "hey you get my snap?"]

    # Filter context for cards
    CARD_CONTEXT = ["card", "debit", "credit", "lost"]
    # Filter for check book context

    CHECK_BOOK_CONTEXT = ["checkbook", "book"]

    # Filter Context for card stolen
    CARD_STOLEN_CONTEXT = ["block", "lost"]

    CARD_STOLEN_RESPONSE = ["Sorry to hear that,please tell me your mobile number to proceed?"]

    def __init__(self):
        self.data = []

    def check_for_greeting(self, sentence):
        """If any of the words in the user's input was a greeting, return a greeting response"""
        for word in sentence.split():
            if word.lower() in self.GREETING_KEYWORDS:
                return random.choice(self.GREETING_RESPONSES)
            else:
                return "please be specific"

    def card_block(self, sentence):
        # if the intent is related to card.
        for word in sentence.split():
            if word.lower() in self.CARD_STOLEN_CONTEXT:
                return random.choice(self.CARD_STOLEN_RESPONSE)

    def respond(self, sentence):
        global isCardStolen
        resp = "Could you be more specific. Please !"
        context = self.contextFinder(sentence)
        if context == "CARD_STOLEN":
            resp = random.choice(self.CARD_STOLEN_RESPONSE)
            self.isCardStolen = True
        return resp

    def user_auth(self):
        #self.Contact_Number = input()
        print("Please provide OTP, for user Authentication")
        otp = input()
        print("Hi " + self.AccHolder)
        print("do you want to block your account : xx5404")
        agreeAccBlock = input()
        if agreeAccBlock.lower() == "yes":
            print("Your card has been blocked")
        print("Would you like to raise new card request?")
        newCardRqst = input()
        if newCardRqst.lower() == "yes":
            print("Awesome ! your new card will be delivered on your registered address")

        print("Do you need any other help ?")

        newContextRaise = input()
        if newContextRaise.len() > 1:
            print(self.crmNextChatter(newContextRaise))
        elif newContextRaise.lower() == "no":
            print("Have a nice day Avinash")

    def contextFinder(self, sentence):
        context = "NA"
        for word in sentence.split():
            if word.lower() in self.CARD_CONTEXT:
                context = "CARD_STOLEN"
            elif word.lower() in self.CHECK_BOOK_CONTEXT:
                context = "CHECK_BOOK_REQUEST"
        return context

    def crmNextChatter(self, saying):
        return self.respond(saying)

    Step = "step1"
    def run_bot(self, saying, reConnect):
        if reConnect is True:
            self.isCardStolen = False
        response = "Please be more specific."
        last_four_number = 6547
        polarity = self.Sent_Analysis(saying)
        print(polarity)
        if polarity == "neg":
            response = "Sorry ! do you want me to redirect you to our CSR."
        else:
            if self.isCardStolen:
                if self.Step == "step1":
                    self.Contact_Number = saying
                    regex = re.compile(r'^[789]\d{9}$')
                    bool_validate = re.match(regex, self.Contact_Number)
                    if bool_validate is None:
                        return "Please enter a valid number"
                    else:
                        self.Step = "step2"
                        return"Please tell me your Date Of Birth (dd/mm/yyyy)"
                elif self.Step == "step2":
                    dob = saying
                    self.Step = "step3"
                    return "Please enter OTP sent on your registered mobile number ending with :" + self.Contact_Number[5:9]
                elif self.Step == "step3":
                    if saying == "8459":
                        self.Step = "step4"
                        return "Hi Anjan, I can see two cards registered with your account, which one you want to block?"
                    else:
                        return "OTP is not correct"
                elif self.Step == "step4" and saying.lower() == "both":
                    self.Step = "step5"
                    return "Do you wish to report any fraud transactions"
                elif  self.Step == "step5" and saying.lower() == "no" :
                    self.Step = "step6"
                    return "Sure, your credit card ending 5694 and debit card ending 7654, has been successfully blocked. while replacing do you want to upgrade your card?"
                elif self.Step == "step6" and saying.lower() == "yes":
                    self.Step = "step7"
                    return "Certainly your new international visa credit card and titanium debit card will be delivered by next week. Is there any thing else ?"
                elif self.Step == "step7" and saying.lower() == "no" or saying.lower() == "no thanks":
                    return "Thanks for banking with us have a nice day ! Anjan."
                else:
                    return "Please be specific"
            else:
                response = self.crmNextChatter(saying)
                print(self.isCardStolen)
        return response

    # Method for sentiment analysis
    def Sent_Analysis(self, text):
        blob = TextBlob(text)

        for sentence in blob.sentences:
            polarity = sentence.sentiment.polarity
            print(polarity)
            if polarity > -0.2:
                sent = "pos"
            else:
                sent = "neg"
            return sent
    # Method to create Json object

    def json_create(self, card_style, Message, UserId, Sentiment, Name, Contact_Number, Pan_Number, Aadhaar_number):

        json_sentiment = json.dumps({"Card_Style": card_style,
                                         "User_Input": {"Message": Message, "User_Id": UserId, "Sentiment": Sentiment},
                                         "User_Details": {"Name": Name, "Contact_Number": Contact_Number,
                                                          "PAN_Number": Pan_Number, "Aadhaar_Number": Aadhaar_number}})

        return (json_sentiment)


            # def main():
    #   # Bot starts from here
    #   # Check for greeting words
    #   while True:
    #       clientResponse = input()
    #       if clientResponse == "quit":
    #           break
    #       #response = check_for_greeting(clientResponse)
    #       response =  card_block(clientResponse)

    #       print(response)


    # if __name__ == '__main__':
    #
    #     print("Hi ! How can i make your life easy.")
    #     while True:
    #         saying = input()
    #
    #         if saying == "quit":
    #             break
    #         if isCardStolen:
    #             user_auth()
    #         else:
    #             print(crmNextChatter(saying))
