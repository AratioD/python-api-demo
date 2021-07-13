FROM python:3
# Set of a working directory
WORKDIR /app
# Copy requirements to your working directory
COPY requirements.txt ./
# Install requirements
RUN pip install --no-cache-dir -r requirements.txt
# Copy all stuff from your machine to workdirc
COPY . .
#These are the commands what python should run
CMD ["python", "app.py"]

