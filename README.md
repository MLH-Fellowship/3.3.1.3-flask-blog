# The Lair of the Gamer Fellowship

A small pixel styled portfolio website with a blog, written with Flask and SQLite!
 

## Installation

Make sure you have python3 and pip installed

Change line 131 of the __init__.py file to your own absolute path before running the app


Create virtual environment using virtualenv
```bash
$ python -m venv python3-virtualenv
```

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install all dependencies

```bash
pip install -r requirements.txt
```

## Usage

Use development .env file
```
URL=localhost:5000
FLASK_ENV=development
```
Start the Python virtual environment

Linux/MacOS:
```bash
$ source python3-virtualenv/bin/activate
```
Windows:
```
> python3-virtualenv\Scripts\activate.bat
```

Start flask development server
```bash
$ flask run
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.
