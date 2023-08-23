import requests
import send_email as email

topic = "nvidia"

api_key = "a917a18b35544e91ae6ad213b9523218"
url = "https://newsapi.org/v2/everything?" \
      f"q={topic}&" \
      "sortBy=publishedAt&" \
      "apiKey=a917a18b35544e91ae6ad213b9523218&" \
      "language=en"

# Make request
request = requests.get(url)

# Get a dictionary with data
content = request.json()

# Access the article titles and descriptions
body = ""
for article in content["articles"][:20]:
    if article["title"] is not None:
        body = "Subject: Today's News" \
               + "\n" + body + article["title"] + "\n" \
               + article["description"] \
               + "\n" + article["url"] + 2 * "\n"

body = body.encode("utf-8")
email.send_email(message=body)
