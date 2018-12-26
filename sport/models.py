from django.db import models
import uuid

# Create your models here.

class WeekDay(models.Model):
    id_day_week = models.UUIDField(primary_key=True, default=uuid.uuid4)
    name = models.CharField(max_length=20, null=False)

    def __str__(self):
        return self.name

class ExerciseType(models.Model):
    id_type_exercise = models.UUIDField(primary_key=True, default=uuid.uuid4)
    name = models.CharField(max_length=100, null=False)

    def __str__(self):
        return self.name

class Trainer(models.Model):
    id_trainer = models.UUIDField(primary_key=True, default=uuid.uuid4)
    firstname = models.CharField(max_length=30, null=False)
    lastname = models.CharField(max_length=30, null=False)
    quota = models.PositiveIntegerField(null=False)

    def __str__(self):
        return self.firstname + self.lastname

class Exercise(models.Model):
    id_exercise = models.UUIDField(primary_key=True, default=uuid.uuid4)
    type_exercise = models.ForeignKey(ExerciseType, on_delete=models.SET_NULL, null=True)
    trainer = models.ForeignKey(Trainer, on_delete=models.SET_NULL, null=True)
    hall = models.PositiveIntegerField(null=False)
    start_hour = models.PositiveIntegerField(null=False)
    continue_hours = models.PositiveIntegerField(null=False)
    week_day = models.ForeignKey(WeekDay, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.trainer.lastname + self.type_exercise.name
