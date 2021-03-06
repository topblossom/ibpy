# ibpy

[![Build Status](https://travis-ci.org/topblossom/ibpy.svg?branch=master)](https://travis-ci.org/topblossom/ibpy)
[![Built with](https://img.shields.io/badge/Built_with-Cookiecutter_Django_Rest-F7B633.svg)](https://github.com/agconti/cookiecutter-django-rest)
[![Maintainability](https://api.codeclimate.com/v1/badges/64b197c0c119bad90152/maintainability)](https://codeclimate.com/github/topblossom/ibpy/maintainability)
[![Test Coverage](https://api.codeclimate.com/v1/badges/64b197c0c119bad90152/test_coverage)](https://codeclimate.com/github/topblossom/ibpy/test_coverage)

Manage your book reading experience. Check out the project's [documentation](http://topblossom.github.io/ibpy/).

# Prerequisites

- [Docker](https://docs.docker.com/docker-for-mac/install/)  
- poetry

# Local Development

To ensure that requirements are updated: 
```bash
 poetry export  -f requirements.txt --without-hashes  > requirements.txt
```

Start the dev server for local development:
```bash
docker-compose up
```

Run a command inside the docker container:
```bash
docker-compose run --rm web [command]
```


Make migrations in docker container
```bash
docker-compose run --rm web python manage.py makemigrations
```