from django.db import models
from django.contrib.auth.models import User

PROJECT_STATUS = [
    ('Waiting on Tou', 'WAITING ON TOU'),
    ('Waiting on Survey', 'WAITING ON SURVEY'),
    ('Waiting on Deposit', 'WAITING ON DEPOSIT'),
    ('Waiting on Installer', 'WAITING ON INSTALLER'),
    ('Waiting on Customer', 'WAITING ON CUSTOMER'),
    ('Waiting on Appointment', 'WAITING ON APPOINTMENT'),
    ('Waiting on Permit', 'WAITING ON PERMIT'),
    ('Waiting on Install', 'WAITING ON INSTALL'),
    ('Install Completed', 'INSTALL COMPLETED'),
]

PROJECT_TIERS = [
    ('Custom', 'CUSTOM'),
    ('Tier 1', 'TIER 1'),
    ('Tier 2', 'TIER 2'),
    ('Tier 3', 'TIER 3'),
    ('Tier 4', 'TIER 4'),
    ('Tier 5', 'TIER 5'),
]

class Record(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.CharField(max_length=75)
    phone = models.CharField(max_length=12)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=25)
    zipcode = models.CharField(max_length=10)
    installer_name = models.CharField(max_length=50, default='No Installer Yet')
    project_status = models.CharField(max_length=50, choices=PROJECT_STATUS, default='Waiting on Survey')
    previous_project_status = models.CharField(max_length=50, choices=PROJECT_STATUS, default='Waiting on Survey')
    project_tier = models.CharField(max_length=50, choices=PROJECT_TIERS, default=' ')
    installer_price = models.IntegerField(default=' ', null=True)
    installer_permit = models.IntegerField(default=' ', null=True)
    customer_permit = models.IntegerField(default=' ', null=True)
    customer_price = models.IntegerField(default=' ', null=True)

    def save(self, *args, **kwargs):
        # Capture the previous project status before saving
        if self.pk:
            original = Record.objects.get(pk=self.pk)
            if original.project_status != self.project_status:
                self.previous_project_status = original.project_status
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    
class RecordNote(models.Model):
    record = models.ForeignKey(Record, on_delete=models.CASCADE)
    note = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    class Meta:
        ordering = ['-created_at']
    
class Installer(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    company_name = models.CharField(max_length = 50)
    email = models.CharField(max_length = 75)
    phone = models.CharField(max_length = 12)
    address = models.CharField(max_length = 100)
    city = models.CharField(max_length = 50)
    state = models.CharField(max_length = 25)
    zipcode = models.CharField(max_length = 10)
    license_number = models.CharField(max_length = 50, default = 'Still Need!')
    
    def __str__(self):
        return (f"{self.company_name}")

class ProjectUpdate(models.Model):
    record = models.ForeignKey(Record, on_delete=models.CASCADE)
    updated_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    update_text = models.TextField()

    def __str__(self):
        return f"Update for Record {self.record.id} by {self.user.username}"
