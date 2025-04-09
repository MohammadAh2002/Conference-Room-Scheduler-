from datetime import datetime
from helpervalidator import *

"""Validates room booking requests based on fields, Rooms, EQUIPMENT, and REQUIREDFIELDS."""

ROOMS = {
    "A101": 10,
    "B202": 20,
    "MainHall": 100,
    "C303": 15
}

EQUIPMENT = {"projector", "whiteboard", "speaker", "microphone"}
REQUIREDFIELDS = {"room", "date", "start_time", "end_time", "attendees", "equipment"}

# Main Validation function
def reserve_room(request: dict) -> str:
    """Checks if a room booking request is valid and returns a status message."""
    
    # Check if all the Field is Exist.
    if set(request.keys()) != REQUIREDFIELDS:
        return "Invalid request: Missing or unexpected fields."

    # Fill the Fields
    room = request.get("room")
    date = request.get("date")
    starttime = request.get("start_time")
    endtime = request.get("end_time")
    attendees = request.get("attendees")
    equipment = request.get("equipment")

    # Validate Rooms
    if room not in ROOMS:
        return "Invalid request: Unsupported room."

    # Validate date
    try:
        date_obj = datetime.strptime(date, "%Y-%m-%d").date()
        if date_obj <= datetime.today().date():
            return "Invalid request: Date must be in the future."
    except ValueError:
        return "Invalid request: Date format must be YYYY-MM-DD."

    # Validate Start and End Time
    if not is_valid_time_range(starttime, endtime):
        return "Invalid request: Invalid or inconsistent time range."

    # Validate Attendees
    if not isinstance(attendees, int) or attendees <= 0:
        return "Invalid request: Attendees must be a positive integer."
    if attendees > ROOMS[room]:
        return "Room capacity exceeded"

    # Validate equipment
    if not isinstance(equipment, list):
        return "Invalid request: Equipment must be a list."
    equipment = [item.lower() for item in equipment]
    for item in equipment:
        if item not in EQUIPMENT:
            return f"Invalid equipment requested: '{item}' not available."

    return "Booking confirmed"

print(reserve_room({
    "room": "A101",
    "date": "2025-05-01",
    "start_time": "09:00",
    "end_time": "11:00",
    "attendees": 8,
    "equipment": ["Projector", "WhiteBoard"]
}))

