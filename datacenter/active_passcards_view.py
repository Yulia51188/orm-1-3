from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render
from django.shortcuts import get_list_or_404


def active_passcards_view(request):
    active_pass_users = get_list_or_404(Passcard, is_active=True)

    context = {
        "active_passcards": active_pass_users,
    }
    return render(request, "active_passcards.html", context)