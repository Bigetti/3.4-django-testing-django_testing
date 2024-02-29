from django.db import models
import pytest
from model_bakery import baker
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient

from .models import Course, Student



class Student(models.Model):

    name = models.TextField()

    birth_date = models.DateField(
        null=True,
    )


class Course(models.Model):

    name = models.TextField()

    students = models.ManyToManyField(
        Student,
        blank=True,
    )
