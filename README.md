# Setting up the development environment
Prerequisites Python3 and Pip [(install guide)](https://docs.python-guide.org/dev/virtualenvs/#make-sure-you-ve-got-python-pip), virtualenv [(install guide)](https://docs.python-guide.org/dev/virtualenvs/#lower-level-virtualenv), and git [(another install guide)](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git).

1. Clone the repository

2. Navigate to the repository's top level (the level with 'README.md', 'requirements.txt', the folder 'app', etc)

3. Create a virtual environment with python 3 and enter it [(guide here)](https://docs.python-guide.org/dev/virtualenvs/#basic-usage)

4. Install the required python packages from requirements.txt [(guide here)](https://pip.pypa.io/en/stable/user_guide/#requirements-files)

5. Create a copy of 'config-example.py' in the same directory called 'config.py' and fill it in with your secrets. 'config.py' already has an entry in '.gitignore'

6. Set the Flask environment variables

Unix:

~~~bash
export FLASK_ENV=development
export FLASK_APP=myapp
~~~

Windows CMD:

~~~bash
set FLASK_ENV=development
set FLASK_APP=myapp
~~~

Windows PowerShell:

~~~bash
$env:FLASK_ENV='development'
$env:FLASK_APP='application.py'
~~~

7. Run it!

~~~bash
flask run
~~~

# Build and Test
TODO: Describe and show how to build your code and run the tests. 

# Contribute
TODO: Explain how other users and developers can contribute to make your code better. 

If you want to learn more about creating good readme files then refer the following [guidelines](https://www.visualstudio.com/en-us/docs/git/create-a-readme). You can also seek inspiration from the below readme files:
- [ASP.NET Core](https://github.com/aspnet/Home)
- [Visual Studio Code](https://github.com/Microsoft/vscode)
- [Chakra Core](https://github.com/Microsoft/ChakraCore)
