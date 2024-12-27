contacts = {"number": 4,
         "students": [{"name": "Sarah Holderness", "email": "sarah@mail.com"},
                      {"name": "Harry Potter", "email": "harry@mail.com"},
                      {"name": "Ron Weasley", "email": "ron@mail.com"},
                      {"name": "Hermione Granger", "email": "hermione@mail.com"}]}

for student in contacts.get("students"):
    print(student.get("email"))