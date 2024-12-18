from datacenter.models import Visit
from django.shortcuts import render, get_list_or_404
from datacenter.scripts_for_code import get_duration, format_duration, is_visit_long


def storage_information_view(request):
    non_closed_visits = []
    visits_not_leaved = get_list_or_404(Visit, leaved_at=None)
    for visit in visits_not_leaved:

        non_closed_visits.append(
            {
                "who_entered": visit.passcard,
                "entered_at": visit.entered_at,
                "duration": format_duration(visit),
                "is_strange": is_visit_long(visit),
            }
        )

    context = {
        "non_closed_visits": non_closed_visits,
    }
    return render(request, "storage_information.html", context)
