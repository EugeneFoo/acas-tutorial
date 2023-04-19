from django.shortcuts import render
from django.shortcuts import redirect # Add the 'redirect' import
from django.http import HttpResponse
from .forms import IssueForm
from govtech_csg_acas.securefileupload.decorator import upload_config
from .models import Issue
from django.shortcuts import get_object_or_404
from govtech_csg_acas.viewpermissions.decorators import public
from django.contrib import messages
from django.contrib.auth import authenticate, login

@public
def index(request):
    return render(request, template_name='index.html')

@public
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

@public
def thank_you(request):    
    return render(request, template_name="thank_you.html")

def list_issues(request):
    issues = Issue.objects.all()
    return render(request, template_name="list_issues.html", context={"issues": issues})

def display_issue(request, issue_id):
    issue = get_object_or_404(Issue, pk=issue_id)

    if request.method == "POST":
        new_status = request.POST.get("issue_status")
        if new_status != issue.status:
            Issue.objects.filter(pk=issue_id).update(status=new_status)
        return redirect("display_issue", issue_id=issue_id)
    else:
        return render(request, template_name="display_issue.html", context={"issue": issue})


@public
def login_responder(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("list_issues")
        else:
            messages.error(
                request,
                "Username or password is incorrect!",
                extra_tags="alert alert-danger alert-dismissible fade show",
            )

    return render(request, template_name="login_responder.html")