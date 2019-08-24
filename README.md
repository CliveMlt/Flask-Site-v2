# Flask Site v2

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
![Python](https://img.shields.io/badge/python-v3.7-blue.svg)
![GitHub repo size](https://img.shields.io/github/repo-size/CliveMlt/Flask-Site-v2)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](https://opensource.org/licenses/MIT)


## Features
- Gallery
- Todo App
- Calendar
- Bookshelf


## Traditional Setup
``` 
git clone https://github.com/CliveMlt/Flask-Site-v2
cd Flask-Site-v2
pip install -r requirements.txt
python file_server.py
```

### Unix Bash (Linux, Mac, etc.):

``` 
export FLASK_APP=file_server.py
flask run
```

### Windows CMD:

``` 
set FLASK_APP=hello
flask run
```

### Windows Powershell:

``` 
> $env:FLASK_APP = "file_server.py"
> flask run
```



<br>

## Gallery
Gallery Data is stored in /data/data.json.
```
`{
              "objectID": "CC01",
              "url": "https://...",
              "thumb": "https:/...",
              "title": "Photo #1",
              "desc": "Photo Description",
              "date": "14/08/2019"
            }`
```

The **'read_photos()'** function will read the gallery data from the JSON file and sends it to the webpage.
A Jinja loop is used to access this information.
```

      <b>{% for photo in photos %}</b>
            <a href="/collection/{{photo.objectID}}">
              <img src="{{photo.thumb}}">
            </a>
            
            <div>
              <h4>{{photo.title}}</h4>
              <p>{{photo.year}}</p>
            </div>
        {% endfor %}
```

<br>

## Todo App
- Create tasks
- Read tasks
- Delete tasks
- Update tasks

A Jinja loop is used to loop through the tasks.

```
	{% for task in t %}
		{% if task.status == 'complete' %}
			{% else %}
			{% endif %}
      
			{{ task.task }}  	
			{% if task.status == 'complete' %}
			<a href="/uncomplete/{{ task.idTask }}">Uncomplete</a> 
			{% else %}
			<a href="/complete/{{ task.idTask }}">Complete</a> 
			{% endif %}
			<a href="/deletetask/{{ task.idTask }}">Remove</a> 
			<a href="/updatetask/{{ task.idTask }}">Update</a>
	{% endfor %}
```
<br>

## Calendar
- Create Event
- Delete Event

Calendar Data is stored in /data/events.json.
```
  {
    "title": "Feast of Assumption",
    "start": "2019-08-15",
    "url": "https://www.timeanddate.com/holidays/common/assumption"
  }
```

Javascript is used to read the calendar data from the JSON file and display it on the webpage. 

<br>

## Bookshelf
- Create an HTML page displaying all the books available
- Create an HTML page for a book
- Add a Flask route linking the books in the bookshelf page to the specific book
- url_for() is used to display a PDF on a webpage

```
<iframe src="{{ url_for('static', filename='images/books/cisco/ccie1.pdf') }}" width ="100%" height ="1200" frameborder="0"></iframe>
```


<br>
