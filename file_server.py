from flask import Flask, make_response, request, session, render_template, send_file, Response, url_for, redirect, flash, escape, session
from flask.views import MethodView
from werkzeug import secure_filename
from datetime import datetime
import humanize
import os
import re
import stat
import json
import mimetypes
import sys
from pathlib2 import Path
from flask_debug import Debug
from flask import render_template
from passlib.hash import sha256_crypt
import boto3
import json
from flask_sqlalchemy import SQLAlchemy 
import sqlite3
from flask_basicauth import BasicAuth





app = Flask(__name__, static_url_path='/assets', static_folder='assets')

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todo.db'


db = SQLAlchemy(app)

root = os.path.normpath("/ftpdata")
key = "password"

ignored = ['.bzr', '$RECYCLE.BIN', '.DAV', '.DS_Store', '.git', '.hg', '.htaccess', '.htpasswd', '.Spotlight-V100', '.svn', '__MACOSX', 'ehthumbs.db', 'robots.txt', 'Thumbs.db', 'thumbs.tps']
datatypes = {'audio': 'm4a,mp3,oga,ogg,webma,wav', 'archive': '7z,zip,rar,gz,tar', 'image': 'gif,ico,jpe,jpeg,jpg,png,svg,webp', 'pdf': 'pdf', 'quicktime': '3g2,3gp,3gp2,3gpp,mov,qt', 'source': 'atom,bat,bash,c,cmd,coffee,css,hml,js,json,java,less,markdown,md,php,pl,py,rb,rss,sass,scpt,swift,scss,sh,xml,yml,plist', 'text': 'txt', 'video': 'mp4,m4v,ogv,webm', 'website': 'htm,html,mhtm,mhtml,xhtm,xhtml'}
icontypes = {'fa-music': 'm4a,mp3,oga,ogg,webma,wav', 'fa-archive': '7z,zip,rar,gz,tar', 'fa-picture-o': 'gif,ico,jpe,jpeg,jpg,png,svg,webp', 'fa-file-text': 'pdf', 'fa-film': '3g2,3gp,3gp2,3gpp,mov,qt', 'fa-code': 'atom,plist,bat,bash,c,cmd,coffee,css,hml,js,json,java,less,markdown,md,php,pl,py,rb,rss,sass,scpt,swift,scss,sh,xml,yml', 'fa-file-text-o': 'txt', 'fa-film': 'mp4,m4v,ogv,webm', 'fa-globe': 'htm,html,mhtm,mhtml,xhtm,xhtml'}

app.config['BASIC_AUTH_USERNAME'] = 'clive'
app.config['BASIC_AUTH_PASSWORD'] = 'clive'
basic_auth = BasicAuth(app)

##LPIC DOC
@app.route('/lpic1')
def lpic():
    return render_template("lpic1.html")
##End LPIC DOC




@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html')

@app.route("/clive")
def clive():
    return render_template('clive.html')
    

##Calendar
@app.route('/calendar')
def calendar():
    return render_template("json.html")


@app.route('/data')
def return_data():
    start_date = request.args.get('start', '')
    end_date = request.args.get('end', '')

    with open("events.json", "r") as input_data:
        return input_data.read()

##End Calendar
















##Gallery
@app.route('/gallery')
def index():
    photos = read_photos()
    return render_template('index2.html', photos=photos)

def read_photos():
    # You can update this dictionary by change the attributes in 'data.json' file. An example of one row is given below
    #[{u'artist': u'John Smith', u'price': u'$250', u'title': u'img 001', u'source': u'../static/img/img.jpg', u'year': u'2012', u'desc': u'description'}]
    with open('data/data.json', 'r') as file:
        data = json.load(file,)
    return data

@app.route('/collection/<objectID>')
def collectionItem(objectID):

    # Dynamically route url to the photo that was selected.
    # This example opens new page and displays the photo with its information

    with open('data/data.json', 'r') as file:
        data = json.load(file)

    for record in data:
        if record['objectID'] == objectID:
            return render_template('object.html', photo=record)

    return render_template('index2.html')

app.secret_key = sha256_crypt.encrypt("big secret")

##End Gallery


## Todo App
class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(200))
    complete = db.Column(db.Boolean)

@app.route('/todo')
def todo():
    incomplete = Todo.query.filter_by(complete=False).all()
    complete = Todo.query.filter_by(complete=True).all()

    return render_template('todo.html', incomplete=incomplete, complete=complete)

@app.route('/add', methods=['POST'])
def add():
    todo = Todo(text=request.form['todoitem'], complete=False)
    db.session.add(todo)
    db.session.commit()

    return redirect(url_for('todo'))

@app.route('/todo/complete/<id>')
def complete(id):

    todo = Todo.query.filter_by(id=int(id)).first()
    todo.complete = True
    db.session.commit()
    
    return redirect(url_for('todo'))
#Todo App End



##Bookshelf
@app.route('/bookshelf')
def bookshelf():
    return render_template('bookshelf.html', title='bookshelf')
##Bookshelf End


#Linux Books
@app.route('/lpic101102')
@basic_auth.required
def lpic1():
    return render_template('lpic101102.html', title='LPIC1')

@app.route('/lpic2')
def lpic2():
    return render_template('lpic2.html', title='LPIC1')

@app.route('/lpic3')
def lpic3():
    return render_template('lpic3.html', title='LPIC1')

@app.route('/linux1')
def linux1():
    return render_template('linux1.html', title='LINUX1')

@app.route('/linux2')
def linux2():
    return render_template('linux2.html', title='LINUX2')
#END Linux Books

#Cisco Books
@app.route('/ccie1')
def ccie1():
    return render_template('ccie1.html', title='CCIE')

@app.route('/ccie2')
def ccie2():
    return render_template('ccie2.html', title='CCIE')

@app.route('/ccna1')
def ccna1():
    return render_template('ccna1.html', title='CCNA')

@app.route('/ccna2')
def ccna2():
    return render_template('ccna2.html', title='CCNA')

@app.route('/ccna3')
def ccna3():
    return render_template('ccna3.html', title='CCNA')

@app.route('/ccna4')
def ccna4():
    return render_template('ccna4.html', title='CCNA')

@app.route('/ccna5')
def ccna5():
    return render_template('ccna5.html', title='CCNA')

@app.route('/ccna6')
def ccna6():
    return render_template('ccna6.html', title='CCNA')

@app.route('/ccnpr1')
def ccnpr1():
    return render_template('ccnpr1.html', title='CCNP')

@app.route('/ccnpr2')
def ccnpr2():
    return render_template('ccnpr2.html', title='CCNP')

@app.route('/ccnpr3')
def ccnpr3():
    return render_template('ccnpr3.html', title='CCNP')

@app.route('/ccnpr4')
def ccnpr4():
    return render_template('ccnpr4.html', title='CCNP')

@app.route('/ccnpr5')
def ccnpr5():
    return render_template('ccnpr5.html', title='CCNP')

@app.route('/ccnpr6')
def ccnpr6():
    return render_template('ccnpr6.html', title='CCNP')

@app.route('/ccnpr7')
def ccnpr7():
    return render_template('ccnpr7.html', title='CCNP')

@app.route('/ccnpr8')
def ccnpr8():
    return render_template('ccnpr8.html', title='CCNP')

@app.route('/ccnps1')
def ccnps1():
    return render_template('ccnps1.html', title='CCNP')

@app.route('/ccnps2')
def ccnps2():
    return render_template('ccnps2.html', title='CCNP')

@app.route('/ccnps3')
def ccnps3():
    return render_template('ccnps3.html', title='CCNP')

@app.route('/ccnps4')
def ccnps4():
    return render_template('ccnps4.html', title='CCNP')

@app.route('/ccnps5')
def ccnps5():
    return render_template('ccnps5.html', title='CCNP')

@app.route('/ccnpt1')
def ccnpt1():
    return render_template('ccnpt1.html', title='CCNP')

@app.route('/ccnpt2')
def ccnpt2():
    return render_template('ccnpt2.html', title='CCNP')

@app.route('/ccnpt3')
def ccnpt3():
    return render_template('ccnpt3.html', title='CCNP')

@app.route('/ccnpt4')
def ccnpt4():
    return render_template('ccnpt4.html', title='CCNP')

@app.route('/ccnpt5')
def ccnpt5():
    return render_template('ccnpt5.html', title='CCNP')
#End Cisco Books

#Microsoft Books
@app.route('/mcsa70740a')
def mcsa70740a():
    return render_template('mcsa70740a.html', title='MCSA')

@app.route('/mcsa70740b')
def mcsa70740b():
    return render_template('mcsa70740b.html', title='MCSA')

@app.route('/mcsa70740c')
def mcsa70740c():
    return render_template('mcsa70740c.html', title='MCSA')

@app.route('/mcsa70740d')
def mcsa70740d():
    return render_template('mcsa70740d.html', title='MCSA')

@app.route('/mcsa70741a')
def mcsa70741a():
    return render_template('mcsa70741a.html', title='MCSA')

@app.route('/mcsa70741b')
def mcsa70741b():
    return render_template('mcsa70741b.html', title='MCSA')

@app.route('/mcsa70741c')
def mcsa70741c():
    return render_template('mcsa70741c.html', title='MCSA')

@app.route('/mcsa70742a')
def mcsa70742a():
    return render_template('mcsa70742a.html', title='MCSA')

@app.route('/mcsa70742b')
def mcsa70742b():
    return render_template('mcsa70742b.html', title='MCSA')

@app.route('/mcsa70742c')
def mcsa70742c():
    return render_template('mcsa70742c.html', title='MCSA')

@app.route('/mcsa70744a')
def mcsa70744a():
    return render_template('mcsa70744a.html', title='MCSA')
#End Microsoft Books

#Python Books
@app.route('/python1')
def python1():
    return render_template('python1.html', title='Python')

@app.route('/python2')
def python2():
    return render_template('python2.html', title='Python')

@app.route('/python3')
def python3():
    return render_template('python3.html', title='Python')

@app.route('/python4')
def python4():
    return render_template('python4.html', title='Python')

@app.route('/python5')
def python5():
    return render_template('python5.html', title='Python')

@app.route('/python6')
def python6():
    return render_template('python6.html', title='Python')

@app.route('/python7')
def python7():
    return render_template('python7.html', title='Python')

@app.route('/python8')
def python8():
    return render_template('python8.html', title='Python')

@app.route('/python9')
def python9():
    return render_template('python9.html', title='Python')

@app.route('/python10')
def python10():
    return render_template('python10.html', title='Python')

@app.route('/python11')
def python11():
    return render_template('python11.html', title='Python')
#End Python Books












##END BOOKS



















#File Server 


if __name__ == '__main__':
    bind = os.getenv('FS_BIND', '192.168.0.11', )
    port = os.getenv('FS_PORT', 8080)
    root = os.path.normpath(os.getenv('FS_PATH', r'/media/clive/Webapp/flask-file-server-4-hosting\ftpdata'))
    key = os.getenv('FS_KEY')
    app.run(bind, port, threaded=True, debug=False)
