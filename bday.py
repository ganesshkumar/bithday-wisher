#!/usr/bin/python

from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/wish', methods = ['GET'])
def named():
    to = request.args.get('to', '', type=str)
    message = request.args.get('message', 'Happy Birthday!', type=str)
    from_ = request.args.get('from', '', type=str)
    return render_template('wish.html', to=to, message=message, from_=from_)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == "__main__":
    app.run()