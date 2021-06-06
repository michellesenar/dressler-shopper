import argparse
import os
import sys

from dotenv import load_dotenv
from twilio.rest import Client

load_dotenv()

client = Client(os.environ["ACCOUNT"], os.environ["AUTHTOKEN"])

CONTACTS = {"michelle": os.environ["MICHELLE"], "andy": os.environ["ANDY"]}


def send_message(message, recipient=os.environ["ANDY"]):
    client.messages.create(
        to=recipient, from_=os.environ["TWILIO_NUMBER"], body=message
    )


def parse_args(arguments):
    parser = argparse.ArgumentParser(description="Send an SMS message")
    parser.add_argument(
        "recipient", help="Recipient of message", choices=["michelle", "andy"]
    )

    return parser.parse_args()


def main():
    arguments = sys.argv[1:]
    parsed = parse_args(arguments)
    message = input("Enter message: ")
    send_message(message, recipient=CONTACTS[parsed.recipient])


if __name__ == "__main__":
    main()
