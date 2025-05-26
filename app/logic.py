import random
import re

responses = {
    r"hi|hello|hey": [
        "Hey there! Ready to talk sports?",
        "Hi! What's your favorite team?",
    ],
    r"football|soccer": [
        "Football is exciting! Who's your favorite club?",
        "Premier League or La Liga? 😄",
    ],
    r"cricket": [
        "Do you support India or another team?",
        "Virat Kohli or Rohit Sharma? 🤔",
    ],
    r"thank you|thanks": [
        "You're welcome!",
        "Glad I could chat sports with you!",
    ],
}

default_responses = [
    "I'm all about sports! Ask me about cricket, football, or your favorite players.",
    "Sorry, I didn't catch that. Want to talk cricket or football?",
]

def generate_bot_response(message: str) -> str:
    message = message.lower()
    for pattern, reply_list in responses.items():
        if re.search(pattern, message):
            return random.choice(reply_list)
    return random.choice(default_responses)
