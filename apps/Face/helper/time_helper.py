from django.conf import settings

import pytz
import datetime

UTC_TIMEZONE = pytz.timezone(settings.TIME_ZONE)
VN_TIMEZONE = pytz.timezone(settings.VN_TIMEZONE)

def now_datetime():
    utcnow = datetime.datetime.now(UTC_TIMEZONE)
    # change to VN time
    vnnow = utcnow.astimezone(VN_TIMEZONE)
    format_dt = vnnow.strftime(r"%Y-%m-%d %H:%M:%S VN")
    return format_dt
