import pytest
from model_bakery import baker
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from .models import Course, Student



def test_example():
    assert False, "Just test example"



@pytest.fixture
def client():
    return APIClient()
    


@pytest.fixture
def student_factory():
    def create_student(**kwargs):
        return baker.make(Student, **kwargs)
    return create_student


@pytest.fixture
def course_factory():
    def create_course(**kwargs):
        return baker.make(Course, **kwargs)
    return create_course




@pytest.mark.django.db
def test_retrieve_course(api_client, course_factory):
     # Создаем курс через фабрику
    Course= course_factory
    # Строим URL для получения курса
    url = reverse('course-detail', kwargs={'pk': course_pk})
    # Делаем запрос к API
    responce = api_client.get(url)
    # Проверяем, что код ответа равен 200
    assert responce.status_code == status.HTTP_200_OK
    # Проверяем, что полученный курс совпадает с созданным
    assert responce.data['id'] == course.id
    assert responce.data['name'] == course.name





