# Use an official lightweight Linux base image
FROM ubuntu:latest

# Set the maintainer (optional)
LABEL maintainer="your-email@example.com"

# Update the package list and install Python
RUN apt update && apt install -y python3 python3-pip \
    && rm -rf /var/lib/apt/lists/*  # Clean up to reduce image size

# Set Python as the default command
CMD ["python3", "--version"]
