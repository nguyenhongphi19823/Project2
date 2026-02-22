from main import get_emails_by_role


def test_returns_matching_emails():
    users = [
        {"email": "a@test.com", "role": "admin"},
        {"email": "b@test.com", "role": "tester"},
        {"email": "c@test.com", "role": "tester"},
    ]
    assert get_emails_by_role(users, "tester") == ["b@test.com", "c@test.com"]


def test_returns_empty_list_when_no_matches():
    users = [
        {"email": "a@test.com", "role": "admin"},
        {"email": "b@test.com", "role": "tester"},
    ]
    assert get_emails_by_role(users, "manager") == []


def test_handles_empty_input():
    assert get_emails_by_role([], "tester") == []
