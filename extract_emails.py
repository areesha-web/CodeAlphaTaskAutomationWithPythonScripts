import re

# Input and output file paths
input_file = 'input.txt'
output_file = 'emails.txt'

# Read the input file
with open(input_file, 'r') as file:
    text = file.read()

# Extract email addresses using regex
email_pattern = r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+'
emails = re.findall(email_pattern, text)

# Save emails to the output file
with open(output_file, 'w') as file:
    for email in emails:
        file.write(email + '\n')

print(f"{len(emails)} email(s) extracted and saved to '{output_file}'.")
