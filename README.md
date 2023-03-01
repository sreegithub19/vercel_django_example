## Start , run , push to Github, and deploy to Vercel a new Django project

- mkdir vercel-django-example
- cd vercel-django-example
- pip install Django virtualenv
- django-admin startproject vercel_app .
- virtualenv ~/.ve/vercel
- source ~/.ve/vercel/bin/activate
- pip3 install -r requirements.txt
- python manage.py startapp example (Add an app to the project)
- python3 manage.py runserver (may or may not work locally, we can directly deploy)
- git add . && git commit -m "Changes" && git push origin master && vercel --prod
- vercel --prod

## Versions used:

Python - 3.8.0

(Reference link: https://jay-hale.medium.com/django-on-vercel-in-30-minutes-e69eed15b616)

- To change Python versions:

  (not working)

  - - pyenv global 3.8.0
  - - pyenv global

  (not working)

  - - For Mac,
  - - - brew unlink python@3.10
  - - - brew unlink python@3.8
  - - - brew link --force python@3.8

  (working)

  - python --version
    - Python 3.10.8
  - PYENV_VERSION=3.8.0
  - python --version
    - Python 3.8.0



Demo:

Part 1:
https://user-images.githubusercontent.com/55496113/222208872-fa49f89c-fb8a-4f10-a7cd-c5bc45cd341c.mp4

Part 2:
https://user-images.githubusercontent.com/55496113/222208903-d9be5d03-477f-4e8e-b8d9-fde50ed72255.mp4

