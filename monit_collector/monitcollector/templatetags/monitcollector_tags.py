import time

from django import template
from django.conf import settings
from django.utils import timezone

register = template.Library()

try:
    monit_update_period = settings.MONIT_UPDATE_PERIOD
except:
    monit_update_period = 60


@register.filter
def timestamp_to_date(timestamp):
    if not isinstance(timestamp, int):
        return ""
    return timezone.datetime.fromtimestamp(timestamp)


@register.filter
def time_class(timestamp):
    if not isinstance(timestamp, int):
        return ""
    if int(time.time()) > int(timestamp) + 3*monit_update_period:
        return "danger"
    return ""


@register.filter
def time_str(uptime):
    """ converts uptime in seconds to a time string """
    if not isinstance(uptime, int):
        return ""
    mins = (uptime/60) % 60
    hours = (uptime/60/60) % 24
    days = (uptime/24/60/60) % 365
    years = uptime/365/24/60/60
    if years == 0:
        if days == 0:
            if hours == 0:
                return "{:.0}m".format(mins)
            return "{:.0}h {:.0}m".format(hours, mins)
        return "{:.0}d {:.0}h {:.0}m".format(days, hours, mins)
    return "{:.0}y {:.0}d {:.0}h {:.0}m".format(years, days, hours, mins)

# does nothing at the moment!
@register.filter
def status_str(status, monitor):
    # if monitor == 0 and status not in ['starting...', 'stopping...', 'restarting...', 'disable monitoring...', 'enable monitoring...']:
    # return "Not monitored"
    return status


@register.filter
def status_class(status, monitor):
    # has to be first
    # if monitor == 0 and status not in ['starting...', 'stopping...', 'restarting...', 'disable monitoring...', 'enable monitoring...']:
    # return 'blue'
    if status == 'running':
        return 'green'
    if status in ['starting...', 'stopping...', 'restarting...']:
        return 'yellow'
    # else return error color
    return 'red'


@register.filter
def in_MB(value):
    if not isinstance(value, (int, str)):
        return ""
    return str(round(float(value)/1.e3, 1))+" MB"


@register.filter
def in_GB(value):
    if not isinstance(value, (int, str)):
        return ""
    return str(round(float(value)/1.e6, 1))+" GB"


@register.filter
def percent(value):
    if not isinstance(value, (float, str)):
        return ""
    return str(round(value, 1))+"%"
