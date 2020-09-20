from flask import Flask
 
 app = flask(__name__)
 
 @app.route('/')
 
 def index():
     return "Hello from the Server"
     
 if __name__ == '__main__':
      app.run(debug=True)
