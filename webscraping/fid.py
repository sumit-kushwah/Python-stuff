import requests, re, ast


f_username = "sharon.shavi.9"
x = requests.get("https://www.facebook.com/" + f_username)

matchs = re.findall(r'\"name\":\"[a-zA-Z0-9_ ]+\"', x.text)

for match in matchs:
    match = "{" + match + "}"
    match_as_dict = ast.literal_eval(match)
    print(match_as_dict['userID'])
