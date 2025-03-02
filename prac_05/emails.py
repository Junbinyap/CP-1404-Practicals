"""
Word Occurrences
Estimate: 30 minutes
Actual:   50 minutes
"""

"""
CP1404/CP5632 Practical - Suggested Solution
Email to name dictionary
"""

def main():
    """Creating a dictionary of email IDs """
    email_to_name = {}
    email = input("Email: ")
    while email != "":
        suggested_name = extract_name_from_email(email)
        confirmation = input(f"Is your name {suggested_name}? (Y/n) ")
        if confirmation in ('', 'y'):
            name = suggested_name
        else:
            name = input("Name: ").strip().title()
        email_to_name[email] = name

    print("\nStored emails and names:")
    for email, name in email_to_name.items():
        print(f"{name} ({email})")


def extract_name_from_email(email):
    local_part = email.split('@')[0]
    name_parts = local_part.replace('.', ' ').replace('-', ' ').replace('_', ' ').split()
    name = ' '.join(name_parts).title()
    return name
main()
