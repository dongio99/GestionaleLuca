FROM python:3.10

# Install necessary packages
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    pkg-config \
    libmariadb-dev \
    mariadb-client && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Create a virtual environment
RUN python3.10 -m venv /opt/venv

# Set the PATH environment variable to use the virtual environment
ENV PATH="/opt/venv/bin:$PATH"

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the working directory
COPY requirements.txt .

# Install the Python dependencies
RUN pip install --upgrade pip && \
    pip install -r requirements.txt

# Copy all application code into the working directory
COPY . .

# Make wait-for-mysql.sh executable
RUN chmod +x /app/wait-for-mysql.sh

# Change the working directory to the 'gestionale' directory
WORKDIR /app/gestionale

# Expose port 8000 for the Django server
EXPOSE 8000

# Set the default command for when a container is started
CMD ["../wait-for-mysql.sh", "gestionaleluca-db-1", "3306", "root", "root", "python3.10", "manage.py", "runserver", "0.0.0.0:8000"]