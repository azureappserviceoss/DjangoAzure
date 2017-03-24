from django.db import models

# Create your models here.
class Sector(models.Model):
    """Name lookup for sectors"""
    def __str__(self):
        return self.name
    name = models.CharField(max_length=255)

class Industry(models.Model):
    """Name lookup for industries"""
    def __str__(self):
        return self.name
    name = models.CharField(max_length=255)

class Attachment(models.Model):
    """Information about attachments"""
    def __str__(self):
        return self.name
    name = models.CharField(max_length=255)

class Report(models.Model):
    """Model for a report from any company"""
    def __str__(self):
        return self.name
    name = models.CharField(max_length=255)
    company_name = models.CharField(max_length=255)
    company_ceo = models.CharField(max_length=255)
    company_phone = models.CharField(max_length=30)
    company_email = models.CharField(max_length=255)
    company_location = models.CharField(max_length=255)
    company_country = models.CharField(max_length=60)
    sector = models.ForeignKey(Sector, on_delete=models.CASCADE)
    industry = models.ForeignKey(Industry, on_delete=models.CASCADE)
    isprivate = models.BooleanField(default=True)
    release_date = models.DateField()
