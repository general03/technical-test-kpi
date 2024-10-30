# KPI Intelligence - Full-stack Developer Test 🛠 

Hi! We're glad you want to join KPI Intelligence! We've designed this test so that *you* can show us how you think about a problem and how you implement its solution. We'll discuss about it during our next meeting.

## Project

Paris Region wants to have a web application to track the investments it makes for its high schools buildings. They provided you the [`dataset.json`](dataset.json) files containing the existing investments.

### Stage 1: REST API

Write a REST API to retrieve the investments data:

- [x] List all the investments
- [x] List investments filtered by `ville` and/or by `etat_d_avancement`
- [x] Get a single investment by id

Pay attention to the HTTP methods and status codes you use.

### Stage 2: Web application

Implement a simple web application to show the investments:

- [ ] Display the list of investments in the form of a table
- [ ] Add a form so that we can trigger the API filters
- [ ] Add a page to show the details of a single investment

### Bonus stages

> Those are not required but can be cool to do!

* Add an endpoint to edit an investment
* Deploy your application to Heroku
* Display some graphs or interesting figures in the web application
* Have some cool idea? Go on 👍

## Modalities

* You are free to use the languages and tools you are more comfortable with
* Create a repository on GitHub to store your source code and send us the link by e-mail once you've finished
* Please provide a `README` with instructions to run your project

## License

This project is released under the MIT License.

The dataset was released under Open Licence by Région Île-de-France: https://www.data.gouv.fr/fr/datasets/operations-de-construction-et-de-renovation-dans-les-lycees-francilens/

# Resultat

## Back

## Pre-requis

- Install env management `pip install poetry`
- Import du fichier de donnée `poetry run python cli/cli/main.py upload-file data/dataset.json`
- Update root path of project `export PYTHONPATH=$PYTHONPATH:"/home/david/projects/technical-test-kpi/back"`

## Lancement du serveur

`poetry run fastapi dev __init__.py`

## Accès à l'API

http://localhost:8000/

## Front

## Pre-requis

`wget -qO- https://raw.githubusercontent.com/nvm-sh/nvm/v0.34.0/install.sh | bash`
```
export NVM_DIR="$HOME/.nvm"
[ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh"
[ -s "$NVM_DIR/bash_completion" ] && \. "$NVM_DIR/bash_completion"
```
`nvm install 20`
`nvm use 20`

`cd kpi && npm start`

## Accès au front 

http://localhost:4200