from flask import Flask, request, jsonify, Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
import datetime
import os
import json

app = Flask(__name__)

SCOPES = ["https://www.googleapis.com/auth/calendar"]
CREDENTIALS_FILE = "credentials.json"
TOKEN_FILE = "token.json"
CALENDAR_ID = "prosopiki.iatros@gmail.com"

# Authenticate with Google Calendar API
def get_calendar_service():
    creds = None
    if os.path.exists(TOKEN_FILE):
        with open(TOKEN_FILE, "r") as token:
            creds = Credentials.from_authorized_user_file(TOKEN_FILE, SCOPES)

    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(CREDENTIALS_FILE, SCOPES)
            creds = flow.run_local_server(port=0)
        with open(TOKEN_FILE, "w") as token:
            token.write(creds.to_json())

    service = build("calendar", "v3", credentials=creds)
    return service

# Get unavailable slots
@app.route("/api/unavailable-slots", methods=["GET"])
def get_unavailable_slots():
    date = request.args.get("date")
    if not date:
        return jsonify({"error": "Date parameter is required."}), 400

    service = get_calendar_service()

    # Define time range for the selected date
    start_of_day = f"{date}T00:00:00Z"
    end_of_day = f"{date}T23:59:59Z"

    events_result = service.events().list(
        calendarId=CALENDAR_ID,
        timeMin=start_of_day,
        timeMax=end_of_day,
        singleEvents=True,
        orderBy="startTime",
    ).execute()

    events = events_result.get("items", [])
    unavailable_slots = [
        event["start"].get("dateTime", event["start"].get("date"))[11:16]
        for event in events
    ]

    return jsonify(unavailable_slots)

# Book an appointment
@app.route("/api/book-appointment", methods=["POST"])
def book_appointment():
    data = request.json
    date = data.get("date")
    time = data.get("time")

    if not date or not time:
        return jsonify({"error": "Date and time are required."}), 400

    service = get_calendar_service()

    start_time = f"{date}T{time}:00"
    end_time = (datetime.datetime.fromisoformat(start_time) + datetime.timedelta(hours=1)).isoformat()

    event_body = {
        "summary": "Patient Appointment",
        "start": {"dateTime": start_time, "timeZone": "UTC"},
        "end": {"dateTime": end_time, "timeZone": "UTC"},
    }

    try:
        event = service.events().insert(calendarId=CALENDAR_ID, body=event_body).execute()
        return jsonify({"message": "Appointment booked successfully!", "eventId": event["id"]})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Update an appointment
@app.route("/api/update-appointment", methods=["PUT"])
def update_appointment():
    data = request.json
    event_id = data.get("eventId")
    date = data.get("date")
    time = data.get("time")

    if not event_id or not date or not time:
        return jsonify({"error": "Event ID, date, and time are required."}), 400

    service = get_calendar_service()

    start_time = f"{date}T{time}:00"
    end_time = (datetime.datetime.fromisoformat(start_time) + datetime.timedelta(hours=1)).isoformat()

    updated_event = {
        "start": {"dateTime": start_time, "timeZone": "UTC"},
        "end": {"dateTime": end_time, "timeZone": "UTC"},
    }

    try:
        event = service.events().patch(
            calendarId=CALENDAR_ID, eventId=event_id, body=updated_event
        ).execute()
        return jsonify({"message": "Appointment updated successfully!", "eventId": event["id"]})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Delete an appointment
@app.route("/api/delete-appointment", methods=["DELETE"])
def delete_appointment():
    event_id = request.args.get("eventId")

    if not event_id:
        return jsonify({"error": "Event ID is required."}), 400

    service = get_calendar_service()

    try:
        service.events().delete(calendarId=CALENDAR_ID, eventId=event_id).execute()
        return jsonify({"message": "Appointment deleted successfully!"})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
