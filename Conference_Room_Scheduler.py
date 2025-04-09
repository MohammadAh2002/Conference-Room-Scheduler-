from datetime import datetime

ROOMS = {
    "A101": 10,
    "B202": 20,
    "MainHall": 100,
    "C303": 15
}

EQUIPMENT = {"projector", "whiteboard", "speaker", "microphone"}
REQUIREDFIELDS = {"room", "date", "start_time", "end_time", "attendees", "equipment"}

# Helper function
def is_valid_time_range(start_time: str, end_time: str) -> bool:
    try:
        start = datetime.strptime(start_time, "%H:%M")
        end = datetime.strptime(end_time, "%H:%M")
        return start < end
    except ValueError:
        return False

# Main Validation function
def reserve_room(request: dict) -> str:
    if set(request.keys()) != REQUIREDFIELDS:
        return "Invalid request: Missing or unexpected fields."

    room = request.get("room")
    date = request.get("date")
    starttime = request.get("start_time")
    endtime = request.get("end_time")
    attendees = request.get("attendees")
    equipment = request.get("equipment")

    if room not in ROOMS:
        return "Invalid request: Unsupported room."

    try:
        date_obj = datetime.strptime(date, "%Y-%m-%d").date()
        if date_obj <= datetime.today().date():
            return "Invalid request: Date must be in the future."
    except ValueError:
        return "Invalid request: Date format must be YYYY-MM-DD."

    if not is_valid_time_range(starttime, endtime):
        return "Invalid request: Invalid or inconsistent time range."

    if not isinstance(attendees, int) or attendees <= 0:
        return "Invalid request: Attendees must be a positive integer."
    if attendees > ROOMS[room]:
        return "Room capacity exceeded"

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

