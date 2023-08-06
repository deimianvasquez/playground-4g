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
        
    
    def delete_contact(contact_file_path, id_contact=None):
        with open(contact_file_path, 'r') as file:
            contacts = json.load(file)
            for contact in contacts:
                if contact['id'] == id_contact:
                    contacts.remove(contact)
                    with open(contact_file_path, 'w') as file:
                        json.dump(contacts, file, indent=2)
                        file.close()
                        return True
        return None

            
    def delete_all_contacts(contact_file_path, agenda_slug=None):
        if Contact.create_json_file(contact_file_path):
            with open(contact_file_path, 'r') as file:
                contacts = json.load(file)
                filtered_contacts = list(filter(lambda contact: contact['agenda_slug'] != agenda_slug, contacts))

                with open(contact_file_path, 'w') as file:
                    json.dump(filtered_contacts, file, indent=2)
                    file.close()
                    return True
        else:   
            return None
        

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


