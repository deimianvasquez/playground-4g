import os, json
from .models import Sound
from flask import Blueprint, jsonify, request, render_template, send_from_directory, send_file


sound = Blueprint('sound', __name__)

static_file_dir = os.path.join(os.path.dirname(os.path.realpath(__file__)))
fx_file_path = os.path.join(os.path.dirname(__file__), 'data', 'fx.json')
sound_file_path = os.path.join(os.path.dirname(__file__), 'data', 'songs.json')


@sound.route('/', methods=['GET'])
def handle_index():
    if request.method == 'GET':
        return render_template('sound.html')


@sound.route('/all', methods=['GET'])
def handle_get_all_sound():
    if request.method == 'GET':
        sound = Sound.get_all_sound(fx=fx_file_path, sound=sound_file_path)
       
        if sound:
            return jsonify(sound), 200
        else:
            return jsonify({"error": "Something went wrong"}), 500


@sound.route('/fx', methods=['GET'])
def handle_gel_all_fx():
    if request.method == 'GET':
        fx = Sound.get_all_fx(fx_file_path)
        if fx:
            return jsonify(fx), 200

        else:
            return jsonify({"error": "Something went wrong"}), 500




@sound.route('/songs', methods=['GET'])
def handle_get_all_songs():
    if request.method == 'GET':
        songs = Sound.get_all_songs(sound_file_path)
        if songs:
            return jsonify(songs), 200

        else:
            return jsonify({"error": "Something went wrong"}), 500


@sound.route('/<path:path>', methods=['GET'])
def handle_get_song(path=None):
    if request.method == 'GET':
        ruta = os.path.join(static_file_dir, path)
        response = send_from_directory(static_file_dir, path)
        return response, 200


       