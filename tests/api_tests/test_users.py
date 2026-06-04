import pytest

class TestUsers:

    def test_get_all_users(self, api_session, base_url):
        response = api_session.get(f"{base_url}/users")
        assert response.status_code == 200
        assert isinstance(response.json(), list)
        assert len(response.json()) == 10

    def test_get_user_by_id(self, api_session, base_url):
        user_id = 1
        response = api_session.get(f"{base_url}/users/{user_id}")
        assert response.status_code == 200
        data = response.json()
        assert data["id"] == user_id
        assert "address" in data
        assert data["address"]["city"] == "Gwenborough"

    def test_user_not_found(self, api_session, base_url):
        response =  api_session.get(f"{base_url}/users/1000")
        assert response.status_code == 404

    def test_user_geo_values(self, api_session, base_url):
        response = api_session.get(f"{base_url}/users/1")
        geo_values = response.json()["address"]["geo"]
        assert "lat" in geo_values
        assert geo_values["lat"] != ""