from datetime import datetime
import pytz

IST = pytz.timezone('Asia/Kolkata')

def utc_to_timezone(dt: datetime, tz: str) -> datetime:
    tz_obj = pytz.timezone(tz)
    return dt.astimezone(tz_obj)

def ist_to_utc(dt: datetime) -> datetime:
    return IST.localize(dt).astimezone(pytz.utc)
