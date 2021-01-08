from django.db import models
from django.contrib.auth.models import AbstractUser

# WANT TO ADD A SEPARATE APP TO THE SITE FOR "CASES"
# WILL MOVE "HISTORICALSEARCHES" AND "SAVEDCASES" TO THE NEW APP

class User(AbstractUser):
    pass

class HistoricalSearches(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    search_string = models.CharField(max_length=250)
    search_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.search_string

class SavedCases(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    case_name = models.CharField(max_length=250)
    index_num = models.CharField(max_length=50)
    decision_date = models.DateField()
    save_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.case_name

class WeekSummary(models.Model):
    summary_string = models.TextField() # HTML string
    saved_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.pk) + "_" + str(self.saved_date)