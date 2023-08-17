import requests
import send_email as email

api_key = "a917a18b35544e91ae6ad213b9523218"
url = "https://newsapi.org/v2/everything?q=tesla&" \
      "from=2023-07-17&sortBy=publishedAt&apiKey=" \
      "a917a18b35544e91ae6ad213b9523218"

# Make request
request = requests.get(url)

# Get a dictionary with data
content = request.json()

# Access the article titles and descriptions
body = ""
for article in content["articles"]:
    if article["title"] is not None:
        body = body + article["title"] + "\n" + article["description"] + 2*"\n"

body = body.encode("utf-8")
email.send_email(message=body)

