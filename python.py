from flask import Flask
from flask import request
# Flask constructor takes the name of 
# current module (__name__) as argument.
app = Flask(__name__)
exiting = False
  
# The route() function of the Flask class is a decorator, 
# which tells the application which URL should call 
# the associated function.
@app.route('/')
# URL is bound with hello_world() function.
def hello_world():
    return 'Hello this is the flask app automation build and deploy #4'

'''
def shutdown_server():
    func = request.environ.get('werkzeug.server.shutdown')
    if func is None:
        raise RuntimeError('Not running with the Werkzeug Server')
    func()
    
@app.route('/shutdown')
def shutdown():
    shutdown_server()
    return 'Server shutting down...'
'''  
# main driver function
if __name__ == '__main__':
  
    # run() method of Flask class runs the application 
    # on the local development server.
    app.run(host='0.0.0.0',port=80)
