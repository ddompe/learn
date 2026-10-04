"""A URL is made of parts. Each part answers a question."""

from urllib.parse import urlparse

url = "https://learn.dompe.space/en/automation-ai/?lang=en#top"
parts = urlparse(url)

print("Scheme:", parts.scheme)
print("Host:", parts.netloc)
print("Path:", parts.path)
print("Query:", parts.query)
print("Fragment:", parts.fragment)
