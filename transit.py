#!/usr/bin/python3
# An object of Flask class is our WSGI application
from flask import Flask
#gtfs-realtime-bindings

# Flask constructor takes the name of current
# module (__name__) as argument
app = Flask(__name__)

# Jinja template landing page for transit web application displaying welcome content and TBJ branding
@app.route("/")
def landing():
   return "TBJ Fans Transit Information"

# jinja template page displaying current Go Trains leaving from Union
@app.route("/go")
def go_transit():
   return "Go Transit Page"

# jinja template page displaying current UP Express Trains leaving from Union
@app.route("/up")
def up_express():
   return "UP Express Page"

# jinja template page displaying current TTC Options close to the Rogers Centre
@app.route("/ttc")
def ttc():
   return "TTC Page"

# jinja template page displaying current Uber wait times
@app.route("/uber")
def uber():
   return "Uber Wait Times"

# jinja template page displaying current Uber wait times
@app.route("/traffic")
def traffic():
   return "Traffic around Rogers Centre"

if __name__ == "__main__":
   app.run(port=5006) # runs the application
   # app.run(port=5006, debug=True) # DEBUG MODE