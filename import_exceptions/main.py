from contact_book import find_contact,

try:
    find_contact()
except KeyError:
    print("Contact not found")

finally:
    print("Contact operations completed")

