from email import message
from flask import render_template
from app import app

#Views
@app.route('/')
def index():
  '''
  View root page that returns the index page and its data
  '''
  message = 'Hello World'
  return render_template('index.html', message=message)