import os
from flask import Blueprint, jsonify, request, url_for, render_template
from .models import Contact

contact = Blueprint('contacts', __name__)
contact_file_path = os.path.join(os.path.dirname(__file__), 'contact.json')

@contact.route('/', methods=['GET'])
def welcome_contact():
    return render_template('contact.html')


@contact.route('/agenda/<string:id_agenda>', methods=['GET'])
def get_all_agendas(id_agenda=None):
    if request.method == 'GET':
        if id_agenda is None:
            return jsonify({"msg": "You must send a agenda_slug"}), 400
        
        all_agendas = Contact.get_all_contacts_for_user(contact_file_path, id_agenda)
        contacts = []
        for agenda in all_agendas:
            if agenda['agenda_slug'] == id_agenda:
                contacts.append(agenda)
        if all_agendas is None:
            return jsonify({"msg": "Internal server error"}), 500
        
        return jsonify(contacts), 200
    return jsonify({"msg": "Method not allowed"}), 405



@contact.route('/<int:id_contact>', methods=['GET'])
def get_one_contact(id_contact=None):
    if request.method == 'GET':
        if id_contact is None:
            return jsonify({"msg": "You must send a contact_id"}), 400
        
        contacts = []
        all_contacts = Contact.get_all_contacts(contact_file_path)
        for contact in all_contacts:
            if contact['id'] == id_contact:
                contacts.append(contact)
                break
            else:
                return jsonify({"msg": "Contact not found"}), 404
            
        if all_contacts is None:
            return jsonify({"msg": "Internal server error"}), 500
        
        return jsonify(contacts), 200
    return jsonify({"msg": "Method not allowed"}), 405



@contact.route('/<int:id_contact>', methods=['DELETE'])
def delete_one_contact(id_contact=None):
    if request.method == "DELETE":
        if id_contact is None:
            return jsonify({"msg": "You must send a contact_id"}), 400
        
        result = Contact.delete_contact(contact_file_path, id_contact)
        print(result)
        if result is None:
            return jsonify({"msg": "User not found"}), 404
        
        if result:
            return jsonify({"msg": "Contact deleted successfully"}), 204
    return jsonify({"msg": "Method not allowed"}), 405



@contact.route('/agenda/<string:id_agenda>', methods=['DELETE'])
def delete_all_contacts(id_agenda=None):
    if request.method == "DELETE":
        result = Contact.delete_all_contacts(contact_file_path, id_agenda)
        if result is None:
            return jsonify({"msg": "Internal server error"}), 500

        if result:
            return jsonify({"msg": "Contacts deleted successfully"}), 204
    return jsonify({"msg": "Method not allowed"}), 405
        

@contact.route('/', methods=['POST'])
def create_one_contact():
    if request.method == "POST":
        Contact.create_json_file(contact_file_path)

        data = request.json
        if data is None:
            return jsonify({"msg": "You must send a json"}), 400
        
        new_contact = Contact.create_contact(contact_file_path, data)

        if new_contact is None:
            return jsonify({"msg": "Internal server error"}), 500
        
        if new_contact is True:
            return jsonify({"msg": "Contact created successfully"}), 201
        
        return jsonify({"msg": "You must send a json"}), 400
    
    return jsonify({"msg": "Method not allowed"}), 405


@contact.route('/<int:id_contact>', methods=['PUT'])
def update_one_contact(id_contact=None):
    if request.method == "PUT":
        if id_contact is None:
            return jsonify({"msg": "You must send a contact_id"}), 400
        
        data = request.json
        if data is None:
            return jsonify({"msg": "You must send a json"}), 400
        
        result = Contact.update_contact(contact_file_path, id_contact, data)
        
        if result is None:
            return jsonify({"msg": "Internal server error"}), 500
        
        if result is True:
            return jsonify({"msg": "Contact updated successfully"}), 204
        
        return jsonify({"msg": "Contact not found"}), 404
    
    return jsonify({"msg": "Method not allowed"}), 405


