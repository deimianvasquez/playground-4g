import os
from flask import Flask, url_for, render_template
from flask_cors import CORS
from flask_bootstrap import Bootstrap

from apis.fake.todo.routes import todo
from apis.fake.contacts.routes import contact
from apis.fake.sound.routes import sound

app = Flask(__name__)
CORS(app)
bootstrap = Bootstrap(app)
app.url_map.strict_slashes = False

app.register_blueprint(todo, url_prefix='/apis/fake/todos')
app.register_blueprint(contact, url_prefix='/apis/fake/contact')
app.register_blueprint(sound, url_prefix='/apis/fake/sound')


@app.route('/')
def index():
    return render_template('home.html')

if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=PORT, debug=True)