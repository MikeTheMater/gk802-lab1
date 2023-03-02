import requests  # εισαγωγή της βιβλιοθήκης

def more(text):
    count = 0
    for line in text.split('\n'):
        print(line)
        count += 1
        if count % 30 == 0:
            reply = input('Show more (y/n)? ')
            if reply == 'n':
                break

url =input("Give me the url you want:\n")# προσδιορισμός του url

with requests.get(url) as response:  # το αντικείμενο response
    html = response.headers
    print(html['Server'])
    print(html'cookies.get_dict()')
