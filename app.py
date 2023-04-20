# pylint: disable=missing-module-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=line-too-long
# pylint: disable=broad-except
# pylint: disable=too-few-public-methods
# pylint: disable=too-many-instance-attributes

import os

from flask import Flask, request, render_template

from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)


@app.route('/')
def home():
    """home page"""
    data = {
        'socureSdkKey': os.getenv("SOCURE_SDK_KEY")
    }
    return render_template('home.html', **data)


@app.route('/onSuccess', methods=['POST'])
def on_success():
    refid = request.form.get('referenceId')
    print(f'app.py: refid: {refid}')
    data = {
        'referenceId': refid
    }
    return render_template('onSuccess.html', **data)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
