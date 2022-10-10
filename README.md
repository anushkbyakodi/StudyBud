# Study Buddy
![image](https://user-images.githubusercontent.com/61583207/194852227-89ed7e07-577a-42f3-93d3-584eb6bb5106.png)

A social platform where students and professionals alike can discuss, learn and share their passion regarding various topics.

## Link to Website
<pre><code>https://akb-studybud.herokuapp.com/
</code></pre>

## Steps to configure website

- Clone Repository
<pre><code>git clone https://github.com/anushkbyakodi/StudyBud.git
</code></pre>

- Move Into Directory
<pre><code>cd studybud
</code></pre>

- Create and activate virtual environment
<pre><code>pip install virtualenv
virtualenv webs
webs\scripts\activate
</code></pre>
You can change the environment name to your liking. I have given a name webs to my environment

- Install Requirements
<pre><code>pip install -r requirements.txt
</code></pre>

## Running the Website

To run the website use command
<pre><code>python manage.py runserver
</code></pre>
You can now access the server at local host: http://127.0.0.1:8000/


## Website Preview

- ### Login/Register Page
![image](https://user-images.githubusercontent.com/61583207/194853030-7fca3492-9304-4301-b5d4-31cc08c0eb3e.png)

- ### Website Home Page
![image](https://user-images.githubusercontent.com/61583207/194853417-7661f44c-d55e-43bd-8b69-1a52e6d32846.png)

- ### Room Interaction Page
![image](https://user-images.githubusercontent.com/61583207/194854216-5e1e9ea7-74d5-43f3-a52b-37b7e4f52c91.png)

- ### Profile Page
![image](https://user-images.githubusercontent.com/61583207/194855097-60eacab1-65d9-47eb-a175-6335b45276e8.png)



## Features and technologies
- Implemented Using Django 4.1.1
- API functionalities for Rooms included
- Custom User models with options to Upload profile pics
- Hosted on Heroku Platform
- Use coolwebsites page to check how information form api can be used to host websites.
