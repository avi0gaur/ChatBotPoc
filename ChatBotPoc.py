## Chat bot for crmnext.
## **** Avinash Gaur and Sachin Arora ****
import random
from textblob import TextBlob


class CrmnextChatBot:

    #Boolean variables for context decisions
    isCardStolen = False
    isLoanNeeded = False

    # Variables for User data
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

    #Filter for loan context

    LOAN_CONTEXT = ["loan", "money", "personal"]

    #Loan Context form
    LOAN_RESPONSE = ["#show_form_loan"]

    CARD_STOLEN_RESPONSE = ["#show_form"]

    CARD_ACTION_FORM = ["#showactions"]

    def __init__(self):
        self.data = []

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
        elif context == "APPLY_LOAN":
            resp = random.choice(self.LOAN_RESPONSE)
            self.isLoanNeeded = True
        return resp


    def contextFinder(self, sentence):
        context = "NA"
        for word in sentence.split():
            if word.lower() in self.CARD_CONTEXT:
                context = "CARD_STOLEN"
            elif word.lower() in self.LOAN_CONTEXT:
                context = "APPLY_LOAN"
        return context

    def crmNextChatter(self, saying):
        return self.respond(saying)

    Step = "step2"

    # Bot running form this point
    def run_bot(self, saying, reConnect):
        if reConnect is True:
            self.isCardStolen = False
            self.isLoanNeeded = False
        response = "Please be more specific."
        last_four_number = 6547
        polarity = self.Sent_Analysis(saying)
        print(polarity)
        if polarity == "neg":
            response = "Sorry ! do you want me to redirect you to our CSR."
        else:
            if self.isCardStolen:
                if self.Step == "step2":
                    self.Contact_Number = "8882874659" #contactNumber
                    #regex = re.compile(r'^[789]\d{9}$')
                    #bool_validate = re.match(regex, self.Contact_Number)

                    dob = "11/11/1111" #dob_user
                    self.Step = "step3"
                    return "Please enter OTP sent on your registered mobile number ending with :" + self.Contact_Number[6:10]
                elif self.Step == "step3":
                    if saying == "8459":
                        self.Step = "step4"
                        return "Hi Anjan, I can see two cards registered with your account, which one you want to block?"
                    else:
                        return "OTP is not correct"
                elif self.Step == "step4" and saying.lower() == "both":
                    self.Step = "step5"
                    return "Do you wish to report any fraud transactions"
                elif self.Step == "step5" and saying.lower() == "no":
                    self.Step = "step6"
                    return "Sure, your credit card ending 5694 and debit card ending 7654, has been successfully blocked. while replacing do you want to upgrade your card?"
                elif self.Step == "step6" and saying.lower() == "yes":
                    self.Step = "step7"
                    return "Certainly your new international visa credit card and titanium debit card will be delivered by next week. Is there any thing else ?"
                elif self.Step == "step7" and saying.lower() == "no" or saying.lower() == "no thanks":
                    return "#re_issue_card_status"
                else:
                    return "Please be specific"
            elif self.isLoanNeeded:
               response = self.run_bot_Loan(saying)
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



    # Loan Journey

    step_loan = "step1"
    def run_bot_Loan(self, saying):

        if self.step_loan == "step1":
            self.step_loan = "step2"
            return "#offer_loan_cards"
        elif self.step_loan == "step2":
            self.step_loan = "step3"
            return "Awesome choice, Please Authorize us to do a CIBIL check to process your Loan"
        elif self.step_loan == "step3" and saying.lower() == "yes":
            return "#cibil_check"
        else:
            return "Please be specific"
