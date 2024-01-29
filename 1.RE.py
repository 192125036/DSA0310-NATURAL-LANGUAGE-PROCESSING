import re

def find_emails(text):
    # Define the regular expression pattern for matching email addresses
    email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

    # Use re.findall() to find all email addresses in the text
    emails_found = re.findall(email_pattern, text)

    return emails_found

# Example text containing email addresses
sample_text = """
Hello, you can contact me at john.doe@example.com or support@company.com for any queries.
Alternatively, reach out to info@website.org. Thank you!
"""

# Find and print all email addresses in the example text
found_emails = find_emails(sample_text)
print("Found emails:", found_emails)
