{% if False %}
Installation
============

To start a new project with this template::

    django-admin.py startproject \
      --template=https://github.com/2RockSoftware/archive/master.zip \
      --extension=py,rst,yaml,js \
      --name=Makefile,gulpfile.js,package.json,Procfile \
      <project_name>

{% endif %}

Requirements
------------

Below you will find basic setup and deployment instructions for the ITicket
project. To begin you should have the following applications installed on your
local development system::

- Python >= 3.8
- Dev Tools (e.g. Ubuntu) `sudo apt-get install python-pip python-dev libpq-dev postgresql postgresql-contrib` _
- `pipenv the latest`_
- Postgres >= 10
- git >= 1.7
- pipenv
- See also Pipfile

Project Setup
-------------

First clone the repository from BitBucket and switch to the new directory::

  $ git clone git@bitbucket.org:[ORGANIZATION]/{{ project_name }}.git
  $ cd {{ project_name }}

Next, create a virtual environment and install all of the requirements::

  (iticket)$ pip shell
  (iticket)$ pipenv install --dev

Now, create a local settings file and set your DJANGO_SETTINGS_MODULE to use it:::

  cp {{ project_name }}/settings/local.example.py {{ project_name }}/settings/local.py
  echo "DJANGO_SETTINGS_MODULE={{ project_name }}.settings.local" > .env

Exit the virtualenv and reactivate it to activate the settings just changed::

  deactivate
  pipenv shell

Create the Postgres database and run the initial syncdb/migrate::

  createdb -E UTF-8 {{ project_name }}
  python manage.py migrate

You should now be able to run the development server::

  python manage.py runserver

Testing
--------

Run the following command to run the test suite::

    python manage.py test


Code Quality
--------------
We use auto formatter to ensure the quality of the code. New developers need to ensure to run the following commands
to setup auto-formatting::

    pipenv install
    pipenv install --dev
    pre-commit install

You could also manually run the pre-commit checks like this::

    pre-commit run --all-files

Dokku Deployment
----------------

Staging deployment::

    git push staging {local_branch}:develop

Production deployment::

    git push production {local_branch}:master

We use the buildpacks in .buildpacks

Postgres (Ubuntu)
--------

Requirements

1.  Install postgres (see previous notes)
2.  User is in sudoer file


Find your user name

```
$ whoami
userabc
```

Login to postgres as super user

```
$ sudo -u postgres psql
postgres=# \du
                                  List of roles
 Role name |                         Attributes                         | Member of
-----------+------------------------------------------------------------+-----------
 postgres  | Superuser, Create role, Create DB, Replication, Bypass RLS | {}
 userabc   |                                                            | {}

```

Add Super User role to userabc
```
postgres=# ALTER USER userabc WITH SUPERUSER;
ALTER ROLE
```
