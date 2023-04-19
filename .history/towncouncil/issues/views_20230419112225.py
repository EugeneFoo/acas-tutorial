from django.shortcuts import render
from django.shortcuts import redirect # Add the 'redirect' import
from django.http import HttpResponse
from .forms import IssueForm
from govtech_csg_acas.securefileupload.decorator import upload_config
from .models import Issue

def index(request):
    return render(request, template_name='index.html')

@upload_config(whitelist_name="CUSTOM", whitelist=["image/png", "image/jpeg"], file_size_limit=3000)
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

def list_issues(request):
    issues = Issue.objects.all()
    return render(request, template_name="list_issues.html", context={"issues": issues})