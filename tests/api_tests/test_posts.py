class TestPosts:

    def test_create_post(self, api_session, base_url):
        payload = {"title": "test", "body": "Hello from pytest", "userId": 1}
        response = api_session.post(f"{base_url}/posts", json=payload)
        assert response.status_code == 201
        data = response.json()
        assert "id" in data
        assert data["title"] == payload["title"]

    def test_update_post(self, api_session, base_url):
        post_id = 1
        payload = {"title": "Updated title", "body": "Updated body"}
        response = api_session.put(f"{base_url}/posts/{post_id}", json=payload)
        assert response.status_code == 200
        assert response.json()["title"] == "Updated title"

    def test_response_time(self, api_session, base_url):
        """Ensure response is fast enough."""
        response = api_session.get(f"{base_url}/posts/1")

        assert response.elapsed.total_seconds() < 2.0
