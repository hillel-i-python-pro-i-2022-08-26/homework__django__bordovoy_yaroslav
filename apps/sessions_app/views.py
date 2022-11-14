import datetime

from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

KEY__VISIT_COUNT = "visit_counter"


def sessions_app(request: HttpRequest) -> HttpResponse:
    session = request.session
    visit_counter = session.get(KEY__VISIT_COUNT, 0)
    visit_counter += 1
    session[KEY__VISIT_COUNT] = visit_counter

    last_session = session.get("last_session", datetime.datetime.now())
    return render(
        request,
        "templates_for__sessions/sessions.html",
        {
            "title": "Session",
            "visit_counter": visit_counter,
            "session_id": session.session_key,
            "datetime": last_session,
        },
    )
