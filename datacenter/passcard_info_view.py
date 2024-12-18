from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render
from django.shortcuts import get_object_or_404, get_list_or_404
from datacenter.scripts_for_code import get_duration, format_duration, is_visit_long



def passcard_info_view(request, passcode):
    this_passcard_visits = []
    passcard = get_object_or_404(Passcard, passcode=passcode)
    visits = get_list_or_404(Visit, passcard=passcard)
    for visit in visits:
        this_passcard_visits.append(
            {
                "entered_at": visit.entered_at,
                "duration": format_duration(visit),
                "is_strange": is_visit_long(visit),
            },
        )
    context = {"passcard": visits, "this_passcard_visits": this_passcard_visits}
    return render(request, "passcard_info.html", context)
