def is_valid_time_range(start_time: str, end_time: str) -> bool:
    try:
        start = datetime.strptime(start_time, "%H:%M")
        end = datetime.strptime(end_time, "%H:%M")
        return start < end
    except ValueError:
        return False