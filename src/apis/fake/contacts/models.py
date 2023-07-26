import json
from random import randint

class Contact():
    
    def __generate_id():
        return randint(0, 100000000000)

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


    def get_all_contacts_for_user(contact_file_path, agenda_slug):
        if Contact.create_json_file(contact_file_path):
            with open(contact_file_path, 'r') as file:
                contacts = json.load(file)
                file.close()
                return contacts
        else:
            return None
        
    def get_all_contacts(contact_file_path):
        if Contact.create_json_file(contact_file_path):
            with open(contact_file_path, 'r') as file:
                contacts = json.load(file)
                file.close()
                return contacts
        else:
            return None


    def create_contact(contact_file_path, data=None):
        data.update({'id': Contact.__generate_id()})

        #verificar si la agenda existe
        if Contact.create_json_file(contact_file_path):
            with open(contact_file_path, 'r') as file:
                contacts = json.load(file)
                if data is None:
                    # retorno un error 
                    return None
                else:
                    contacts.append(data)
                    file.close()
                    with open(contact_file_path, 'w') as file:
                        json.dump(contacts, file, indent=2)
                        file.close()
                        return True
        else:
            return None
    
    def delete_contact(contact_file_path, id_contact=None):
        if Contact.create_json_file(contact_file_path):
            with open(contact_file_path, 'r') as file:
                contacts = json.load(file)
                for contact in contacts:
                    if contact['id'] == id_contact:
                        contacts.remove(contact)
                        with open(contact_file_path, 'w') as file:
                            json.dump(contacts, file, indent=2)
                            file.close()
                            return True
        else:
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
        if Contact.create_json_file(contact_file_path):
            with open(contact_file_path, 'r') as file:
                contacts = json.load(file)
                for contact in contacts:
                    if contact['id'] == id_contact:
                        contacts.remove(contact)
                        data.update({'id': id_contact})
                        contacts.append(data)
                        with open(contact_file_path, 'w') as file:
                            json.dump(contacts, file, indent=2)
                            file.close()
                            return True
        else:
            return None
