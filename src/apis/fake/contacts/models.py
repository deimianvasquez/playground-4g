import json
from random import randint

class Contact():
    def __init__(self, full_name, email, agenda_slug, address, phone):
        self.full_name = full_name
        self.email = email
        self.agenda_slug = agenda_slug
        self.address = address
        self.phone = phone
        self.id = randint(0, 100000000000)

    def __str__(self):
        return f'{self.full_name} {self.email} {self.agenda_slug} {self.address} {self.phone} {self.id}'

    def serialize(self):
        return {
            'full_name': self.full_name,
            'email': self.email,
            'agenda_slug': self.agenda_slug,
            'address': self.address,
            'phone': self.phone,
            'id': self.id
        }


    def create_json_file(contact_file_path):
        try:
            file = open(contact_file_path)
            file.close()
            return True

        except Exception as error:
            if error.errno == 2:
                with open(contact_file_path, 'w') as file:
                    json.dump([], file, indent=2)
                    file.close()
                    return True
            else:
                return None

    def get_contacts_slug(contact_file_path, agenda_slug):
        if Contact.create_json_file(contact_file_path):
            with open(contact_file_path, 'r') as file:
                contacts = json.load(file)
                file.close()
                return contacts
        else:
            return None
    


   

    # def get_all_contacts_for_user(contact_file_path, agenda_slug):
    #     if Contact.create_json_file(contact_file_path):
    #         with open(contact_file_path, 'r') as file:
    #             contacts = json.load(file)
    #             file.close()
    #             return contacts
    #     else:
    #         return None
        
    def get_all_contacts(contact_file_path):
        if Contact.create_json_file(contact_file_path):
            with open(contact_file_path, 'r') as file:
                contacts = json.load(file)
                file.close()
                return contacts
        else:
            return None

    @classmethod
    def create_contact(cls,contact_file_path, data):
        data = cls(**data)
        with open(contact_file_path, 'r') as file:
            contacts = json.load(file)
            contacts.append(data.serialize())
            file.close()
            with open(contact_file_path, 'w') as file:
                json.dump(contacts, file, indent=2)
                file.close()
                return True
        
    
    def delete_contact(contact_file_path, data=None):
        print(id_contact)
    # def delete_contact(contact_file_path, id_contact=None):
    #     if Contact.create_json_file(contact_file_path):
    #         with open(contact_file_path, 'r') as file:
    #             contacts = json.load(file)
    #             for contact in contacts:
    #                 if contact['id'] == id_contact:
    #                     contacts.remove(contact)
    #                     with open(contact_file_path, 'w') as file:
    #                         json.dump(contacts, file, indent=2)
    #                         file.close()
    #                         return True
    #     else:
    #         return None
            
    # def delete_all_contacts(contact_file_path, agenda_slug=None):
    #     if Contact.create_json_file(contact_file_path):
    #         with open(contact_file_path, 'r') as file:
    #             contacts = json.load(file)
    #             filtered_contacts = list(filter(lambda contact: contact['agenda_slug'] != agenda_slug, contacts))

    #             with open(contact_file_path, 'w') as file:
    #                 json.dump(filtered_contacts, file, indent=2)
    #                 file.close()
    #                 return True
    #     else:   
    #         return None
        
    def update_contact(contact_file_path, id_contact=None, data=None):
       
        with open(contact_file_path, 'r') as file:
            contacts = json.load(file)
            for contact in contacts:
                print(type(contact['id']), type(id_contact))
                if contact['id'] == id_contact:
                    contacts.remove(contact)
                    contacts.append(data)
                    with open(contact_file_path, 'w') as file:
                        json.dump(contacts, file, indent=2)
                        file.close()
                        return True
        return None


# # ![alt text](/apis/img/images.php?blob&random&cat=icon&tags=breathecode,32) Fake Contact-List API

# ⚠️ The use of Insomnia.rest is strongly recomended for this API, [download it here](https://insomnia.rest/).

# #### 1) Get All available agendas right now
# ```
# GET: /apis/fake/contact/agenda
# ```

# #### 2) Create an agenda

# To create an agenda all you have to do is create a contact with a unused agenda_slug and the agenda will automatically be created.

# #### 3) Get All contacts from an Agenda
# ```
# GET: /apis/fake/contact/agenda/{agenda_slug}
# ```

# #### 4) Get One Particular Contact
# ```
# GET: /apis/fake/contact/{contact_id}
# ```

# #### 5) Delete One Particular Contact
# ```
# DELETE: /apis/fake/contact/{contact_id}
# ```

# #### 6) Delete All Contacts from an Agenda
# ```
# DELETE: /apis/fake/contact/agenda/{agenda_slug}
# ```

# #### 7) Create one contact
# ```
# POST: /apis/fake/contact/

# Request (application/json)

#     body:
#     {
#         "full_name": "Dave Bradley",
#         "email": "dave@gmail.com",
#         "agenda_slug": "my_super_agenda",
#         "address":"47568 NW 34ST, 33434 FL, USA",
#         "phone":"7864445566"
#     }
# ```

# #### 8) Update one contact
# ```
# PUT: /apis/fake/contact/{contact_id}

# Request (application/json)

#     body:
#     {
#         "full_name": "Dave Bradley",
#         "email": "dave@gmail.com",
#         "agenda_slug": "my_super_agenda",
#         "address":"47568 NW 34ST, 33434 FL, USA",
#         "phone":"7864445566"
#     }
# ```
