from django.shortcuts import render

def dashboard(request):

    context = {
        "page_title": "Dashboard",

        # Dashboard Statistics
        "total_hosts": 0,
        "online_hosts": 0,
        "logs_today": 0,
        "critical_alerts": 0,
        "open_incidents": 0,
        "ai_analyses": 0,
    }

    return render(request, "dashboard.html", context)