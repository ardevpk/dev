from django.shortcuts import redirect


def red(request, id):
    return redirect("/submitting/")