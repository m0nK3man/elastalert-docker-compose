import sys
import json
import ast
import requests

# Function to process and format alert message
def process_alert_message(matches):
    formatted_messages = []

    # Ensure matches is a list
    if not isinstance(matches, list):
        matches = [matches]

    # Iterate over the matches
    for i, alert_data in enumerate(matches):
        formatted_msg = f"Alert #{i+1}\n"
        formatted_msg += f"  Rule ID: {alert_data['details'].get('ruleId')}\n"
        formatted_msg += f"  Message: {alert_data.get('message')}\n"
        formatted_msg += f"  Severity: {alert_data['details'].get('severity')}\n"
        formatted_msg += f"  Data: {alert_data['details'].get('data')}\n"
        formatted_msg += f"  Tags: {', '.join(alert_data['details'].get('tags', []))}\n"
        formatted_msg += f"  File: {alert_data['details'].get('file')}\n"
        formatted_msg += f"  Match: {alert_data['details'].get('match')}\n"
        formatted_msg += f"  Reference: {alert_data['details'].get('reference')}\n"
        formatted_msg += "-" * 50
        formatted_messages.append(formatted_msg)

    return "\n".join(formatted_messages)

# Send formatted message to Telegram
def send_to_telegram(formatted_message, telegram_bot_token, telegram_room_id):
    telegram_url = f"https://api.telegram.org/bot{telegram_bot_token}/sendMessage"
    payload = {
        'chat_id': telegram_room_id,
        'text': formatted_message,
        'parse_mode': 'Markdown'
    }
    response = requests.post(telegram_url, data=payload)
    return response

# Example usage
if __name__ == "__main__":
    # Use ast.literal_eval to safely evaluate the string representation of the list
    try:
        matches = ast.literal_eval(sys.argv[1])
    except (SyntaxError, ValueError) as e:
        print(f"Error parsing input: {e}")
        sys.exit(1)

    # Process the message
    formatted_message = process_alert_message(matches)

    # Send to Telegram
    telegram_bot_token = "7567290410:AAEv0mw9zJ1qDH364raibbuIPmmRmizAJFU"  # Replace with your actual token
    telegram_room_id = "-4740407928"  # Replace with your actual room ID
    response = send_to_telegram(formatted_message, telegram_bot_token, telegram_room_id)

    if response.status_code == 200:
        print("Message sent successfully to Telegram!")
    else:
        print(f"Failed to send message: {response.text}")
