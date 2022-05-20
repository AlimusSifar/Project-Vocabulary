from website import create_app


def test_get_homepage():
    app = create_app()
    with app.test_client() as client:
        response = client.get("/")
        assert response.status_code == 200
        # print(response.data)
        # assert b"<h1>Vocabulary</h1>" in response.data


def test_get_about():
    app = create_app()
    with app.test_client() as client:
        response = client.get("/about")
        assert response.status_code == 200
        # print(response.data)
        assert b"<h1>About</h1>" in response.data


# def test_get_profile():
#     app = create_app()
#     with app.test_client() as client:
#         response = client.get("/profile")
#         assert response.status_code == 200
#         print(response.data)
#         assert b"<h1>Profile</h1>" in response.data
