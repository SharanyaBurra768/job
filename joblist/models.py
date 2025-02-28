from django.db import models

# Create your models here.
class JobApplication(models.Model):
    job_id = models.CharField(max_length=255)
    applicant_id = models.CharField(max_length=255)
    applicant_name = models.CharField(max_length=255)
    applicant_email = models.EmailField()
    applied_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.applicant_name} - {self.job.title}"