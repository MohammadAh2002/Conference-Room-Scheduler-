# Conference-Room-Scheduler
Exercise: Conference Room Scheduler 
Overview 
You have been hired to build part of a backend system for a conference center. Your task is 
to implement a Python function that processes room booking requests and determines 
whether a booking is valid. 
Supported Rooms 
Room      | Max Capacity ----------|-------------- 
A101      | 10 people 
B202      | 20 people 
MainHall  | 100 people 
C303      | 15 people 
Available Equipment - projector - whiteboard - speaker - microphone 
Task 1: reserve_room(request: dict) -> str 
Implement a function that receives a dictionary representing a booking request. The 
dictionary must include the following fields: - room: a string, one of the supported room names (e.g., "A101", "B202", "MainHall", "C303") - date: a string in the format YYYY-MM-DD representing a future date - start_time: a string in HH:MM 24-hour format - end_time: a string in HH:MM 24-hour format, must be after start_time - attendees: an integer indicating number of people attending, must not exceed room 
capacity - equipment: a list of strings, each representing a requested equipment item 
The function must return one of the following strings based on validation: - "Booking confirmed" – if the request is fully valid. - "Invalid request" – if the request is missing or contains improperly formatted fields. - "Room capacity exceeded" – if the number of attendees exceeds the room's capacity. - "Invalid equipment requested" – if any of the requested equipment items are not available. - "Booking confirmed" – if the request is fully valid. - "Invalid request" – if the request is missing or contains improperly formatted fields. - "Room capacity exceeded" – if the number of attendees exceeds the room's capacity. - "Invalid equipment requested" – if any of the requested equipment items are not available. 
Request Dictionary Format 
 
{ 
    "room": "A101",             # Must be one of the supported room names 
    "date": "2025-05-01",       # Must be a valid future date, format YYYY-MM-DD 
    "start_time": "09:00",      # HH:MM 24-hour format 
    "end_time": "11:00",        # Must be after start_time 
    "attendees": 8,             # Integer, must not exceed room capacity 
    "equipment": ["projector"]  # List of strings, all must be supported 
} 
 
You should use a helper function to manage the time validation. 
 
Task 2: is_valid_time_range(start_time: str, end_time: str) -> bool 
 
This helper function checks if: - Both start_time and end_time are in valid "HH:MM" format. - start_time is strictly earlier than end_time. 
 
Return True if valid, otherwise False. 
 
You must use this helper inside reserve_room(). 
 
Examples 
 
Valid Request 
 
reserve_room({ 
    "room": "A101", 
    "date": "2025-05-01", 
    "start_time": "09:00", 
    "end_time": "11:00", 
    "attendees": 8, 
    "equipment": ["projector", "whiteboard"] 
}) 
# Output: "Booking confirmed" 
 
Exceeds Capacity 
 
reserve_room({ 
    "room": "A101", 
    "date": "2025-05-01", 
    "start_time": "09:00", 
    "end_time": "11:00", 
    "attendees": 15, 
    "equipment": ["projector"] 
}) 
# Output: "Room capacity exceeded" 
Invalid Equipment 
reserve_room({ 
"room": "B202", 
"date": "2025-06-10", 
"start_time": "14:00", 
"end_time": "15:30", 
"attendees": 10, 
"equipment": ["coffee machine"] 
}) 
# Output: "Invalid equipment requested" 
Bonus Challenges 
Try to: - Accept equipment names regardless of letter case (e.g., "Projector" and "projector" are 
both valid). - Reject requests with unexpected fields in the dictionary. - Return specific error messages instead of the generic "Invalid request". 
