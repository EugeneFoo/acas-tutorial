from django.shortcuts import redirect # Add the 'redirect' import
from django.http import HttpResponse
from .forms import IssueForm

def index(request):
    return render(request, template_name='index.html')

def submit_issue(request):
    if request.method == "POST":
        form = IssueForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponse("Thank you for your submission!")
    else:
        form = IssueForm()

    return render(request, template_name="submit_issue.html", context={"form": form})