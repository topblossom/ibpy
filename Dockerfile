#based on
FROM python:3.8-slim
ENV PYTHONUNBUFFERED 1

# Allows docker to cache installed dependencies between builds
COPY  pyproject.toml poetry.lock ./
RUN pip install poetry

RUN poetry config virtualenvs.create false \
                && poetry export --without-hashes -f requirements.txt --dev \
                |  poetry run pip install -r /dev/stdin \
                && poetry debug



# Because initially we only copy the lock and pyproject file, we can only install the dependencies
# in the RUN above, as the `packages` portion of the pyproject.toml file is not
# available at this point. Now, after the whole package has been copied in, we run `poetry install`
# again to only install packages, scripts, etc. (and thus it should be very quick).
# See this issue for more context: https://github.com/python-poetry/poetry/issues/1899
RUN poetry install --no-interaction

# Adds our application code to the image
COPY . code
WORKDIR code

EXPOSE 8000

# Run the production server
CMD poetry run newrelic-admin run-program gunicorn --bind 0.0.0.0:$PORT --access-logfile - icgbooks.wsgi:application
ENTRYPOINT ["poetry", "run"]