import json
import os
from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler

# Load tokens from environment variables for security
SLACK_BOT_TOKEN = "<SLACK_BOT_TOKEN>"
SLACK_APP_TOKEN = "<SLACK_APP_TOKEN>"

admin_user_ids: list[str] = ["<USER_ID_1>", "<USER_ID_2>"]  # Admin user IDs (Slack user IDs to be set as admin for this slack bot)
time_per_person = 1.25  # Time in minutes it takes for one person to get their food

app = App(token=SLACK_BOT_TOKEN)

# Listen to direct messages
@app.event("app_mention")
def hello_command(body, say):
    # Acknowledge the event
    with open("./shared_data.txt", "r") as file:
        highest_count = file.read()

    print("Wait line has this many people:", highest_count)

    estimated_wait_time = int(highest_count) * time_per_person

    # Format the messages
    message = [
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": f"*LunchBox AI* 🤖\n\n👥 {highest_count} people waiting in line"
            }
        },
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": f"⏳ Estimated wait time: {estimated_wait_time} minutes"
            }
        }
    ]

    sent_message: str = body['event']['text']
    user_requesting: str = body['event']['user']
    if "/setmenu" in sent_message and user_requesting in admin_user_ids:
        print(f"Setting menu...: {sent_message}")
        sent_message = sent_message.replace("<@U07HQV26X2P> /setmenu ", "")
        with open("./menu.txt", "w") as file:
            file.write(str(sent_message))

    menu = None
    with open("./menu.txt", "r") as file:
        menu = file.read()
    if menu == "":
        message.append(
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": "❌ No menu set"
                }
            }
        )
    elif menu == "end":
        message.append(
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": "❌ Lunch is over. No food left :("
                }
            }
        )
    elif menu == "leftovers":
        message.append(
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": "❗ There are leftovers! Come and get it :)"
                }
            }
        )
    else:
        message.append(
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": f"🍽️ Today's meal is: {menu}"
                }
            }
        )

    # Convert the message list to a dictionary
    message_dict = {"blocks": message}

    # Send the message
    say(message_dict)

if __name__ == "__main__":
    SocketModeHandler(app, SLACK_APP_TOKEN).start()
