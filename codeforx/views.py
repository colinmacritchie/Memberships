from django.shortcuts import render

#Functions that displays the home page.
def home(request):

    return render(request, "base.html", {})