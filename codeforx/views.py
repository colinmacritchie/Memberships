from django.shortcuts import render

#Functions that displays the home page.
def home(request):
    name = "Colin"
    context = {
        "the_name": name,
        }

    return render(request, "base.html", context)
