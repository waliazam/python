import re

text = "Contact us at support@example.com or sales@example.com."

pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4}'

emails = re.findall(pattern, text)

print(emails)



import re

log_entries = """
2023-03-12 14:55:02, Info: System startup
2023-03-12 15:05:10, Warning: Low disk space
2023-03-12 15:15:25, Error: Network connection failed
"""

pattern = r'(\d{4}-\d{2}-\d{2}) (\d{2}:\d{2}:\d{2}), (\w+): (.+)'

matches = re.finditer(pattern, log_entries)

for match in matches:
    date = match.group(1)
    time = match.group(2)
    level = match.group(3)
    message = match.group(4)
    print(f"Date: {date}, Time: {time}, Level: {level}, Message: {message}")
