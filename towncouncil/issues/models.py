from django.db import models
from django.utils import timezone
from django.core.validators import RegexValidator
from govtech_csg_acas.modelpermissions.decorators import orm_default_permissions_check
from govtech_csg_acas.securefileupload.validators import acas_file_validator
from govtech_csg_acas.securemodelpkid.model import RandomIDModel

@orm_default_permissions_check
class Issue(RandomIDModel):
    # Personal particulars of submitter
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=8, validators=[RegexValidator(regex="[986][0-9]{7}")])

    # Information about the issue
    summary = models.TextField()
    description = models.TextField()
    location = models.TextField()
    evidence = models.FileField(upload_to="uploads/issues/%Y/%m/%d", validators=[acas_file_validator])
    submit_date = models.DateTimeField("date submitted", default=timezone.now)
    type = models.CharField(
        max_length=10,
        choices=[
            ("Facilities", "Facilities"),
            ("Road", "Road"),
            ("Sewerage", "Sewerage"),
            ("Others", "Others"),
        ],
        default="Others"
    )
    status = models.CharField(
        max_length=8,
        choices=[
            ("Pending", "Pending"),
            ("Open", "Open"),
            ("Resolved", "Resolved")
        ],
        default="Open"
    )

    def __str__(self):
        return self.summary