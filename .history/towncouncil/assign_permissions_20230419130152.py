from django.contrib.auth.models import Group
from govtech_csg_acas.modelpermissions.shortcuts import (
    get_model_permissions,
    assign_perm,
    sudo,
)

from issues.models import Issue


permissions = get_model_permissions(Issue)
with sudo():
    for issue_type in ("Facilities", "Road", "Sewerage", "Others"):
        print(f"Assigning permissions for issue type '{issue_type}'...")
        group = Group.objects.get(name=issue_type)
        issues = Issue.objects.filter(type=issue_type)
        for issue in issues:
            assign_perm(permissions["read"], group, issue)
            assign_perm(permissions["update"], group, issue)
        print(f"Finished assigning permissions for issue type '{issue_type}'\n")