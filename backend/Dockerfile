# Use official Python 3.11 slim image as base
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Create non-root user with UID 1000
RUN useradd -m -u 1000 appuser && chown appuser:appuser /app

# Copy application file with proper ownership
COPY --chown=appuser:appuser app.py .

# Switch to non-root user
USER appuser

# Document the port the application listens on
EXPOSE 8080

# Run the application
CMD ["python", "app.py"]
