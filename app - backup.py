from flask import Flask, render_template, request
from flask_socketio import SocketIO

###VALIDATE###
from validator import validatee
###############

from scraper import scrape
app = Flask(__name__)
app.config['DEBUG'] = True
socketio = SocketIO(app)


@app.route('/validate')
def validate():
    validatee()
    render_template("index.html")


@app.route("/",methods=['GET', 'POST'])
def home():
    
    query = request.form.get('query')
    num = request.form.get('count')
    width = request.form.get('width')
    height = request.form.get('height')
    extension = request.form.get('format')
    scrape(query,num,width,height,extension)
    # scrape(query,num)
    print("Query "+str(query)+" Num : "+str(num))
    return render_template("index.html")

if __name__ == '__main__':
    socketio.run(app, debug=True)


   