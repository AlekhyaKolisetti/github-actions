# adding test commit
def login(username, password):
    return username == "admin" and password == "password123"


def test_login():
    assert login("admin", "password123") == True
    assert login("user", "wrongpassword") == False
