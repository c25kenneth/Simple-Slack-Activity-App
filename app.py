from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler
import re
import activityAPI
import tokens

app = App(token=tokens.SLACK_BOT_TOKEN, name="Bored Bot")

@app.message("activity")
def giveActivity(message, say):
    activity = activityAPI.getRandomActivity()
    say(text= activity["activity"])

def main():
    handler = SocketModeHandler(app, tokens.SLACK_APP_TOKEN)
    handler.start()

if __name__ == "__main__":
    main()