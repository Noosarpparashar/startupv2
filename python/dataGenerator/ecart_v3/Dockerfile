# Use an official Python runtime as the base image
FROM python:3.9-slim
RUN apt-get update && apt-get install -y postgresql-client

# Set the working directory in the container
WORKDIR /app

# Copy the requirements.txt file to the working directory
COPY requirements.txt .

# Install the Python dependencies
RUN pip install -r requirements.txt

# Copy the entire project code to the working directory
COPY . .

# Set the command to run your Python script
CMD  python callCustomer.py & python callProductStores.py & python callsalesfact.py & python callUpdate.py & python callDelete.py
#docker network create my-network
#docker network connect my-network startupv1-db-1
#docker run --network=my-network my-ecart-data-generator
