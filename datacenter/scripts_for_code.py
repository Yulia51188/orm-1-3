from django.utils.timezone import localtime
from datacenter.models import Passcard
from datacenter.models import Visit

def get_duration(visit):
    visit_enter = localtime(visit.entered_at)
    leaved_at = localtime(visit.leaved_at)
    duration = leaved_at - visit_enter
    return duration.total_seconds()


def format_duration(visit):
    duration = get_duration(visit)
    fake_duration = str(duration).split(".")[0]
    real_duration = int(fake_duration)
    hours = real_duration // 3600
    minute = real_duration % 3600 // 60
    return f"{hours}ч {minute}м"


def is_visit_long(visit):
    duration = get_duration(visit)
    hours = duration // 3600
    return hours > 1