# Use official Python 3.10 image
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Install dependencies first for better caching
COPY pyproject.toml .
RUN pip install --no-cache-dir .

# Copy the rest of the application
COPY . .

# Expose default MCP server port
EXPOSE 8000

# Set environment variables
ENV MCP_TRANSPORT_TYPE=sse
ENV MCP_SERVER_HOST=0.0.0.0
ENV MCP_SERVER_PORT=8000

# Run the application
CMD ["python", "main.py"]
