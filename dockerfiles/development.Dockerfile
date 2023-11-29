FROM python:3.10.13-alpine as base

WORKDIR /supportify-backend

# Copy the requirements file separately to leverage Docker cache
COPY requirements.txt .

# Install build dependencies
RUN apk update && \
    apk upgrade

RUN pip install --upgrade pip==23.3.1 \
 pip install --upgrade setuptools==68.2.2 \
 pip install --no-cache-dir -r requirements.txt

FROM base

COPY . .

# Create a non-root user
RUN adduser -D devops

# Set ownership to the non-root user
RUN chown -R devops:devops /supportify-backend

# Switch to the non-root user
USER devops

# Expose the application port
EXPOSE 8080

# Command to run the application
CMD ["flask", "run", "--host", "0.0.0.0"]