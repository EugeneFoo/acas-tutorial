from django.contrib.auth.models import Group, User


manager_responder = User.objects.create_user(username="ManagerResponder", password="password")
print("Created responder 'ManagerResponder'\n")

issue_types = ("Facilities", "Road", "Sewerage", "Others")
for issue_type in issue_types:
    group = Group.objects.create(name=issue_type)
    print(f"Created group '{group.name}'")

    responder = User.objects.create_user(username=issue_type + "Responder", password="password")
    responder.groups.add(group)
    print(f"Created responder '{responder.username}' and added to group '{group.name}'")
    manager_responder.groups.add(group)
    print(f"'ManagerResponder' added to group '{group.name}'\n")

special_responder = User.objects.create_user(username="FacilitiesRoadResponder", password="password")
print("Created responder 'FacilitiesRoadResponder'")
for group in Group.objects.filter(name__in=("Facilities", "Road")):
    special_responder.groups.add(group)
    print(f"Added 'FacilitiesRoadResponder' to group '{group.name}'")