# story-narratives-twilio

*This is a submission for [Twilio Challenge v24.06.12](https://dev.to/challenges/twilio)*

Ever wanted to go back to your childhood, when grandma told you stories about animals and birds, adding her own little twists while you sat in wonder about what would happen next? Ever felt bored and wished someone would read you magical stories that could transport you to another realm? Well, we've got just the thing for you!

## What We Built
We(@khemraj_bawaskar_f283a984 and I) have created a storyteller bot for WhatsApp that reads stories to you over a call. Simply provide the genre and maturity level, and our bot will deliver an engaging storytelling experience tailored to your preferences.

## Demo
[![StoryTeller Bot Demo](https://img.youtube.com/vi/s7uwEDdPI9k/0.jpg)](https://www.youtube.com/watch?v=s7uwEDdPI9k)


## Twilio and AI
We have leveraged the WhatsApp Sandbox feature of Twilio to create a storyteller bot that uses a webhook link for a Flask server. By integrating Azure OpenAI LLM for advanced AI capabilities and Twilio's voice call feature, our bot can call users and tell them a story in their desired genre.

We have a command '/story' to generate the response from the bot.

To get into the sandbox, follow this:

![Whatsapp Sandbox](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/03wqadkztp1ax9jh7hgy.jpeg)

This link can help you get started with the Twilio Whatsapp sandbox: [https://www.twilio.com/docs/whatsapp/sandbox](https://www.twilio.com/docs/whatsapp/sandbox)

When the sandbox starts, the user can get started with '/start' command, which throws the following message: 

*Hello there! I'm your Storyteller Bot, here to whisk you away on incredible adventures. Whether you seek epic fantasies, heartwarming tales, or thrilling mysteries, I have a story for every mood and moment.*

*Please use '/story' tag followed with the genre and age group for which you want to hear the story.*
*Following template can be used:*
*'/story tell me a romantic story for age group of 24-26 years*

The user can accordingly use the commands and get responses.

**/story:** Generates a story using Azure OpenAI from the genre and the maturity level provided by the user, and calls the user to read them a beautiful story.


