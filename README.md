# Python Wiki Search 🔍

A simple Python project that searches Wikipedia articles using the Wikipedia REST API.

## 📝 Features

- Search for Wikipedia topics.
- Display article titles and descriptions.
- Show article URLs.
- Display up to 5 search results by default.

## ⚙️ Customize Search Results

By default, the program displays up to 5 results. You can change the number of results by modifying the `limit` value in the `params` dictionary.

```python
params = {
    "q": text,
    "limit": 5
}
```

Replace `5` with any number you want. For example:

```python
"limit": 10
```

This requests up to 10 search results.

## 🛠️ Installation

Install the required Python library:

```bash
pip install requests
```

## 🚀 Run the Project

```bash
python main.py
```

## 🧰 Technologies Used

- Python
- Requests library
- Wikipedia REST API


