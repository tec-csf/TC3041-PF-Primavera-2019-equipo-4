# Using lightweight alpine image
FROM python:3.6-alpine

# Installing packages
RUN apk update

# Defining working directory and adding source code
WORKDIR /usr/src/app
COPY requirements.txt ./

# Install API dependencies
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install influxdb
RUN pip install dnspython

# Add application code.
COPY . ./

# Start app
CMD [ "python", "./main.py" ]