def is_valid_email(email):
    # Check for spaces
    if " " in email:
        return False

    # Check for exactly one '@'
    if email.count("@") != 1:
        return False

    username, domain = email.split("@")

    # Username and domain should not be empty
    if not username or not domain:
        return False

    # Domain must contain a dot
    if "." not in domain:
        return False

    # Domain should not start or end with a dot
    if domain.startswith(".") or domain.endswith("."):
        return False

    return True


# Example usage
emails = [
    "user@example.com",
    "anjali.patel@gmail.com",
    "user@domain",
    "@gmail.com",
    "user@.com",
    "user@domain.",
    "user name@gmail.com",
    "user@@gmail.com"
]

for email in emails:
    print(f"{email}: {is_valid_email(email)}")