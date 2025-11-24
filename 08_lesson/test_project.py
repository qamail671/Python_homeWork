
import pytest
import requests

base_url = "https://yougile.com/api-v2"
HEADERS = {'Content-Type': 'application/json', 'Authorization': 'Bearer '}


@pytest.fixture
def create_project():
    # Фикстура для создания проекта, которая будет использоваться в тестах
    response = requests.post(base_url + "/projects",
                             headers=HEADERS, json={"title": "RGD01"})
    assert response.status_code == 201
    project_id = response.json().get("id")
    yield project_id
    # Очистка: удаление проекта после теста
    requests.delete(base_url + '/projects/{project_id}', headers=HEADERS)


def test_create_project_positive():
    # Позитивный тест на создание проекта
    payload = {"title": "New Project"}
    response = requests.post(base_url + '/projects',
                             headers=HEADERS, json=payload)
    assert response.status_code == 201
    assert "id" in response.json()


def test_create_project_negative():
    # Негативный тест на создание проекта без обязательного поля
    response = requests.post(base_url + '/projects', headers=HEADERS, json={})
    assert response.status_code == 400


def test_update_project_positive(create_project):
    # Позитивный тест на обновление проекта
    project_id = create_project
    response = requests.put(base_url + '/projects/' + project_id,
                            headers=HEADERS, json={"title": "Updated Project"})
    assert response.status_code == 200
    assert response.json().get("id") is not project_id


def test_update_project_negative():
    # Негативный тест на обновление несуществующего проекта
    response = requests.put(base_url + '/projects/invalid_id',
                            headers=HEADERS, json={"name": "Updated Project"})
    assert response.status_code == 400


def test_get_project_positive(create_project):
    # Позитивный тест на получение информации о проекте
    project_id = create_project
    response = requests.get(base_url + '/projects/'+project_id,
                            headers=HEADERS)
    assert response.status_code == 200
    assert response.json().get("id") == project_id


def test_get_project_negative():
    # Негативный тест на получение информации о несуществующем проекте
    response = requests.get(base_url + '/projects/invalid_id',
                            headers=HEADERS)
    assert response.status_code == 404
