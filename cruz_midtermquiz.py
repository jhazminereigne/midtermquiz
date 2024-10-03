import requests
import json


access_token = "YjQzYTYxMzItNjQzYS00ZTczLThiZmEtYTFhMjI0MjI0MzU1ZDk2NmZkYzYtM2U3_P0A1_60c4241b-f916-4111-96c4-b4c6eecaa22e"

meeting_title = "Cruz Test Meeting"
start_time = "2024-10-11T14:00:00+00:00"
end_time = "2024-10-11T15:00:00+00:00"

room_name = "Test Room"
participant_email = "dennissegail@gmail.com"

message_text = "Hello, this is a test message!"

url = "https://webexapis.com/v1/meetings"

headers = {
    "Authorization": f"Bearer {access_token}",
    "Content-Type": "application/json"
}

meeting_data = {
    "title": meeting_title,
    "start": start_time,
    "end": end_time
}

response = requests.post(url, headers=headers, json=meeting_data)
if response.status_code == 200:
    print("Meeting created successfully!")
    meeting_id = response.json()["id"]
    print(f"Meeting ID: {meeting_id}")
else:
    print("Failed to create meeting.")

room_data = {
    "title": room_name
}

room_url = url.replace("meetings", "rooms")
response = requests.post(room_url, headers=headers, json=room_data)
if response.status_code == 200:
    print("Room created successfully!")
    room_id = response.json()["id"]
    print(f"Room ID: {room_id}")
else:
    print("Failed to create room.")

membership_data = {
    "roomId": room_id,
    "personEmail": participant_email,
    "isModerator": False
}

membership_url = url.replace("meetings", "memberships")
response = requests.post(membership_url, headers=headers, json=membership_data)
if response.status_code == 200:
    print("Participant added successfully!")
else:
    print("Failed to add participant.")

message_data = {
    "roomId": room_id,
    "text": message_text
}

message_url = url.replace("meetings", "messages")
response = requests.post(message_url, headers=headers, json=message_data)
if response.status_code == 200:
    print("Message sent successfully!")
    message_id = response.json()["id"]
    print(f"Message ID: {message_id}")
else:
    print("Failed to send message.")

def delete_message(message_id):
    message_url = url.replace("meetings", f"messages/{message_id}")
    response = requests.delete(message_url, headers=headers)
    if response.status_code == 204:
        print("Message deleted successfully!")
    else:
        print("Failed to delete message.")


delete_message(message_id)