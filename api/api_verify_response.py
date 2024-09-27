import requests

def test_get_user():
    response = requests.get("https://reqres.in/api/users",
        params={"page": "2"},
        headers={"Accept":"Application/json"}
        )
    json_data = response.json()
    #print(response.json())
    #print(response.status_code)
    #print(response.headers['Content-Type'])
    assert response.status_code == 200
    assert "application/json" in response.headers['Content-Type']
    assert json_data['page'] == 2
    assert json_data['per_page'] == 6
    assert json_data['total'] == 12
    assert json_data['total_pages'] == 2

    print(response.request.headers)
    print(response.request.body)


# PyTest, Selenium, Request, Python, Agile, Jira
# Page Object Model, Behave, Git