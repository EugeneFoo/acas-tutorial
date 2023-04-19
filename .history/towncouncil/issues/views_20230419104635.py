from django.shortcuts import render
from django.shortcuts import redirect # Add the 'redirect' import
from django.http import HttpResponse
from .forms import IssueForm

def index(request):
    return render(request, template_name='index.html')

    from django.http import HttpResponse
from .forms import IssueForm


def submit_issue(request):
    if request.method == "POST":
        form = IssueForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("thank_you")
    else:
        form = IssueForm()

    return render(request, template_name="submit_issue.html", context={"form": form})

    def thank_you(request):
    
    return render(request, template_name="thank_you.html")