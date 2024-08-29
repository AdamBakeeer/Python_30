import webbrowser

url_lists = [
    'https://www.python.org',
    'https://www.linkedin.com/in/asabeneh'
]

for url in url_lists:
    webbrowser.open_new_tab(url)