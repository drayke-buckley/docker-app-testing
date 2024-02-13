# Base image
FROM draykkon/python_app_base:latest

# Set the working directory
WORKDIR /app

# Copy the contents of the src folder into the container
COPY src /app

RUN conda env create -f /app/environment.yml -y

SHELL ["conda", "run", "-n", "dockertest", "/bin/bash", "-c"]

EXPOSE 8001

ENTRYPOINT python /app/setup.py | python -m uvicorn /app/src/main:app --reload --port 8001