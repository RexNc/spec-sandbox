"""Implementation of spec clause CS-03 (and the CS-02 de-dup rule it relies on)."""
from datetime import date, datetime, timedelta
from zoneinfo import ZoneInfo


def local_day(ts_utc: datetime, tz: str) -> date:
    """CS-03: days are measured in the client's local time zone."""
    return ts_utc.astimezone(ZoneInfo(tz)).date()


def streak(days: list[date], today: date) -> int:
    """CS-03: consecutive days ending today or yesterday; 0 otherwise."""
    unique = set(days)  # CS-02: one per day
    if today in unique:
        cur = today
    elif today - timedelta(days=1) in unique:
        cur = today - timedelta(days=1)
    else:
        return 0
    n = 0
    while cur in unique:
        n += 1
        cur -= timedelta(days=1)
    return n
