# To Do List
## Project #2

---

### _Clone the repository from Github_ ###

Clone the repositoy from Github into a directory.

```bash
  git clone <repository> <path>
```

---

### _Setting up the Virtual Environment_ ###

Now create a new virtual environment.

Run the following command:

```bash
  python -m venv venv  # you may have to use python3 instead of python
```

Activate the virtual environment.

Run one of the following commands depending on the type of operating system you are using:

> MacOS, Linux, ChromeOS:  
> `source venv/bin/activate`  
> Windows:  
> `venv\Scripts\activate.bat`

---

### _Install Project Dependencies_ ###

Install the project dependencies.

Navigate to the project root directory.

Run the following commands:

```bash
  pip install django
```

```bash
  pip freeze install
```

```bash
  requirements.txt
```

---

### _Running the Application_ ###

Navigate to the `nyc-guide` directory.

Run the following commmand:

```bash
  python manage.py runserver 
  # you may have to replace python with python3
```

Point your browser to use the app:
[http://localhost:8000](http://localhost:8000)

---

### _Stopping the Application_ ###

Shut down the server.

Run the following command in the terminal:

```bash
  Ctrl+C
```

---

### _Exiting the Virtual Environment_ ###

Run the following command:

```bash
  deactivate
```


The following  in this project:
- Python data structures such as Lists, Dictionaries and their associated methods
- Python Classes and Inheritance
- Django [URLs](https://docs.djangoproject.com/en/3.2/topics/http/urls/) to understand how to capture parameters in views
- Django [Templates](https://docs.djangoproject.com/en/3.2/ref/templates/language/)
-Django [Migrations]
-Django [Models]
-Django [Shell]
-Django [Static CSS]
-Django [Post Create Content]
---
