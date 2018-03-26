from django.db import models
from django.contrib.auth import get_user_model

from model_utils.models import TimeStampedModel

User = get_user_model()


class Location(TimeStampedModel):
    address = models.CharField(max_length=255, blank=False)
    slug = models.CharField(max_length=255, unique=True)


class UniversityDepartment(TimeStampedModel):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class ResearcherProfile(TimeStampedModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    department = models.ForeignKey(
        UniversityDepartment, on_delete=models.CASCADE)

    def __str__(self):
        return self.first_name + " " + self.last_name


class Experiment(TimeStampedModel):
    researchers = models.ManyToManyField(User)
    name = models.CharField(max_length=255)
    human_subject_id = models.CharField(max_length=255, blank=False)

    def __str__(self):
        return self.name


class Session(TimeStampedModel):
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    experiment = models.ForeignKey(Experiment, on_delete=models.CASCADE)
    session_number = models.PositiveIntegerField(default=0)
    start_time = models.DateTimeField(blank=False)
    end_time = models.DateTimeField(blank=False)

    def __str__(self):
        return "Session {} ({}-{})".format(
            self.start_time.strftime("%m%d%Y%H%M"))

