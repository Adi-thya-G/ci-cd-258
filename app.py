from flask import Flask
app=Flask(__name__)
def add_number(a,b):
  return a+b

@app.route("/")
def home():
  return "ci cd pipe line"

@app.route("/add/<int:a>/<int:b>")
def add(a,b):
  return str(add_number(a,b))
if __name__=="__main__":
   app.run(host="0.0.0.0",port=5000)