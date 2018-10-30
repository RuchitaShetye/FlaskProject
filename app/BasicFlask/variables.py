from flask import Flask
app=Flask(__name__)
@app.route("/")
def index():
    return "Hello World!"  
@app.route("/hi/<name>")
def hello_name(name):
    return "Hi %s" %name

@app.route("/hello/<int:name>")
def hello_int(name):
    return "Hello %d" %name

if __name__=="__main__":
    app.run(debug=True)

