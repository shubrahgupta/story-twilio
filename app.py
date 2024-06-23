import os
from flask import Flask, request, jsonify
from twilio.twiml.messaging_response import MessagingResponse
from langchain_openai import AzureChatOpenAI
from twilio.rest import Client
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_core.output_parsers import StrOutputParser

account_sid = 'TWILIO_ACCOUNT_SID'
auth_token = 'TWILIO_TOKEN'
from_twilio_number = 'TWILIO_PHONE_NO'

prompts = {
    "/story":"""Generate a short and entertaining story of maximum 1200 characters count ONLY for the genre and the age group provided by user.
    Don't generate story for sexual or lewd genre""",
}


def openai_handler(user_response, category):
    parser = StrOutputParser()

    model = AzureChatOpenAI(
        model_name="gpt-35-turbo",
        api_key=os.getenv("AZURE_OPENAI_API_KEY"),
        azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
        api_version=os.getenv("AZURE_OPENAI_API_VERSION"),
        azure_deployment=os.getenv("AZURE_OPENAI_DEPLOYMENT"),
    )

    messages = [
        SystemMessage(content=prompts[category]),
        HumanMessage(content=user_response),
    ]

    chain = model | parser
    response = chain.invoke(messages)
    print(response)
    return response


def make_call(story, from_number):

    client = Client(account_sid, auth_token)
    call = client.calls.create(
        to=from_number,
        from_=from_twilio_number,
        twiml=f'<Response><Say voice="Google.en-IN-Standard-D">Hi, This your Story Teller Bot, {story}</Say></Response>'
    )

def msg_handler(incoming_msg, from_number):

    if '/start' in incoming_msg:
        response = """Hello there! I'm your Storyteller Bot, here to whisk you away on incredible adventures. Whether you seek epic fantasies, heartwarming tales, or thrilling mysteries, I have a story for every mood and moment.
                    \nplease use '/story' tag followed with the genre and age group for which you want to hear the story.
                    \nFollowing template can be used:
                    \n'/story tell me a romantic story for age group of 24-26 years'
                    """
    elif '/story' in incoming_msg:
        response = openai_handler(incoming_msg,'/story')
        make_call(response, from_number)
    else:
        response = """Sorry! I only answer to the tags, please type '/start' for quick guide.
                    """
    return response



app = Flask(__name__)
@app.route('/',methods=['GET'])
def hello():
    return 'Hello all!'

@app.route('/whatsapp', methods=['POST'])
def webhook():
    # Get the incoming message data from the request
    incoming_msg = request.values.get('Body', '').lower()
    from_number = request.values.get('From', '').split('+')[1]

    # Log the incoming message (for debugging purposes)
    print(f'Message from {from_number}: {incoming_msg}')

    resp = MessagingResponse()
    msg = resp.message()
    msg.body(msg_handler(incoming_msg, from_number))
    return str(resp)


if __name__ == '__main__':
    app.run(debug=True)





