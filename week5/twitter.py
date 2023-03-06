import re

url = input("URL: ").strip()

# username = re.sub(r"^(https?://)?(www\.)?twitter\.com/(.+)$", "", url)
# matches := re.search(r"^https?://(?:www\.)?twitter\.com/(.+)$", url, re.IGNORECASE)
if matches := re.search(r"^https?://(?:www\.)?twitter\.com/(.+)$", url, re.IGNORECASE):
    print(f"Username:", matches.group(1))