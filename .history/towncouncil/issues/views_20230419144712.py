from django.shortcuts import render
from django.shortcuts import redirect # Add the 'redirect' import
from django.http import HttpResponse
from django.contrib.auth.models import Group
from govtech_csg_acas.modelpermissions.shortcuts import (
    get_model_permissions,
    assign_perm,
    sudo,
)
from .forms import IssueForm
from govtech_csg_acas.securefileupload.decorator import upload_config
from .models import Issue
from django.shortcuts import get_object_or_404
from govtech_csg_acas.viewpermissions.decorators import public
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
# Import mimetypes module
import mimetypes
# import os module
import os
# Import HttpResponse module
from django.http.response import HttpResponse

@public
def index(request):
    return render(request, template_name='index.html')

@public
@upload_config(whitelist_name="CUSTOM", whitelist=["image/png", "image/jpeg"], file_size_limit=3000)
def submit_issue(request):
    if request.method == "POST":
        form = IssueForm(request.POST, request.FILES)
        if form.is_valid():
             with sudo():
                # Saves the form, which transparently saves the Issue object
                form.save()
                # Retrieve the Issue object and assign permissions to the responder group
                submitted_issue = Issue.objects.get(id=form.instance.id)
                permissions = get_model_permissions(Issue)
                responder_group = Group.objects.get(name=submitted_issue.type)
                assign_perm(permissions["read"], responder_group, submitted_issue)
                assign_perm(permissions["update"], responder_group, submitted_issue)
                return redirect("thank_you")
    else:
        form = IssueForm()

    return render(request, template_name="submit_issue.html", context={"form": form})

@public
def thank_you(request):    
    return render(request, template_name="thank_you.html")

@login_required
def list_issues(request):
    user_groups = list(request.user.groups.values_list("name", flat=True))
    issues = Issue.objects.filter(type__in=user_groups)
    return render(request, template_name="list_issues.html", context={"issues": issues})

@login_required
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


@login_required(login_url="/", redirect_field_name="")
def logout_responder(request):
    logout(request)
    return redirect("index")

@public
def download_file(:
   # code to check or protect the file from unauthorized access
   response = HttpResponse()  
   response['X-File'] = '/uploads/issues/2023/04/19/489bb71c-9523-4e80-b121-dda734c2fafb.png'  
   return response