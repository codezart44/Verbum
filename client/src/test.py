import requests

def test_insert_entry():
    url = "http://127.0.0.1:5000/api/entries/insert-one"
    payload = {
        "word": "test",
        "pos": "noun",
        "description": "this is a test",
        "translation": "test",
    }
    # payload = 1
    response = requests.post(url, json=payload)
    print(response.status_code)
    print(response.text)

def test_update_entry():
    url = "http://127.0.0.1:5000/api/entries/update-one"
    payload = {
        "word": "asdadasd",
        "pos": "noun",
        "description": "this is for testing",
        "translation": "test",
    }
    # payload = 1
    response = requests.put(url, json=payload)
    print(response.status_code)
    print(response.text)

def test_select_randn_entries(n: int):
    url = f"http://127.0.0.1:5000/api/entries/select-randn/{n}"
    response = requests.get(url)
    print(response.status_code)
    print(response.text)

def test_select_entry():
    url = "http://127.0.0.1:5000/api/entries/select-one/asdadasd"
    response = requests.get(url)
    print(response.status_code)
    print(response.text)

def main():
    # test_select_entry()
    test_update_entry()
    test_select_entry()

    # test_insert_entry()
    # test_update_entry()
    # test_select_randn_entries("12")

if __name__=="__main__":
    main()
