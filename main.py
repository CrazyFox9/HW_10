from flask import Flask
import utils

app = Flask(__name__)


@app.route('/')
def main():
    pass


@app.route('/candidate/<candidate_id>')
def candidate(candidate_id):
    pass


@app.route('/skills/<skill>')
def skills(skill):
    pass
