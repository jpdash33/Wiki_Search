import requests

text = input("=> ").strip()

url = "https://en.wikipedia.org/w/rest.php/v1/search/page"

headers = {
    "User-Agent": "MyPythonWikiSearch/1.0 (learning project)"
}

params = {
    "q": text,       # The search query, such as python
    "limit": 5      # Return at most 5 search results
}


response = requests.get(
    url,
    params=params,
    headers=headers,
    timeout=10
)


if response.ok:
    data = response.json()

    for page in data.get("pages", []):
        print("\nTitle:", page["title"])
        print("Description:", page.get("description"))
        print("URL:", "https://en.wikipedia.org/wiki/" + page["key"])
    print("\n")
else:
    print("\nError:", response.text,"\n")