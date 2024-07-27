import requests
from django.shortcuts import redirect, render

from .forms import XTBLoginForm


def xtb_login(request):
    if request.method == "POST":
        form = XTBLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]

            # Logowanie do XTB API
            login_url = "https://xapi.xtb.com/login"
            payload = {"user": username, "password": password}
            response = requests.post(login_url, json=payload)

            if response.status_code == 200:
                data = response.json()
                session_id = data.get("streamSessionId")

                # Pobranie danych o proficie na koniec sesji
                balance_url = "https://xapi.xtb.com/getBalance"
                headers = {"Authorization": f"Bearer {session_id}"}
                balance_response = requests.get(balance_url, headers=headers)

                if balance_response.status_code == 200:
                    balance_data = balance_response.json()
                    profit = balance_data["profit"]
                    return render(request, "profit.html", {"profit": profit})
                else:
                    form.add_error(None, "Nie udało się pobrać danych o proficie.")
            else:
                form.add_error(None, "Nie udało się zalogować.")
    else:
        form = XTBLoginForm()

    return render(request, "xtb_login.html", {"form": form})
