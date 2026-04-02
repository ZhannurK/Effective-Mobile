# Docker Nginx Web Application

A containerized web application demonstrating Docker best practices with a Python backend and nginx reverse proxy. Built for the Effective Mobile DevOps test assignment.

## Architecture

The application consists of two Docker containers orchestrated with Docker Compose:

- **Backend Service**: A Python HTTP server listening on port 8080 (internal only)
- **Nginx Service**: An nginx reverse proxy accepting external requests on port 80 and forwarding them to the backend

```
External Client → Nginx (port 80) → Backend (port 8080)
                    ↓
              Docker Network (app-network)
```

The backend is isolated within a Docker network and is not directly accessible from the host system. All external traffic flows through nginx, which acts as a reverse proxy to the backend service.

## Prerequisites

- Docker (version 20.10 or higher)
- Docker Compose (version 2.0 or higher)

## Project Structure

```
docker-nginx-webapp/
├── backend/
│   ├── Dockerfile          # Backend container configuration
│   └── app.py              # Python HTTP server application
├── nginx/
│   └── nginx.conf          # Nginx reverse proxy configuration
├── docker-compose.yml      # Service orchestration configuration
├── .gitignore              # Git ignore rules
└── README.md               # This file
```

## Getting Started

### Starting the Project

Build and start both services with a single command:

```bash
docker-compose up --build
```

This command will:
1. Build the backend Docker image from the Dockerfile
2. Pull the nginx:alpine image
3. Create the app-network Docker network
4. Start both containers with health monitoring
5. Wait for the backend to be healthy before starting nginx

### Verifying the Deployment

Once the services are running, verify the deployment with:

```bash
curl http://localhost
```

**Expected Response:**
```
Hello from Effective Mobile!
```

You can also test with a web browser by navigating to `http://localhost`.

### Stopping the Project

Stop and remove all containers, networks, and volumes:

```bash
docker-compose down
```

## Security Features

This project implements several Docker security best practices:

- **Network Isolation**: Backend port 8080 is not exposed to the host system, only accessible via the internal Docker network
- **Non-Root User**: Backend application runs as a non-root user (appuser, UID 1000)
- **Minimal Base Images**: Uses `python:3.11-slim` and `nginx:alpine` for reduced attack surface
- **Read-Only Volumes**: Nginx configuration is mounted as read-only
- **Health Checks**: Both services have health monitoring to ensure availability
- **No Secrets in Repository**: Sensitive data excluded via .gitignore

## Technical Details

### Backend Service

- **Base Image**: python:3.11-slim
- **Port**: 8080 (internal only)
- **User**: appuser (UID 1000)
- **Health Check**: HTTP request to localhost:8080 every 30 seconds

### Nginx Service

- **Base Image**: nginx:alpine
- **Port**: 80 (exposed to host)
- **Configuration**: Custom nginx.conf with upstream backend
- **Proxy Headers**: Host, X-Real-IP, X-Forwarded-For
- **Health Check**: HTTP request to localhost:80 every 30 seconds

### Docker Compose

- **Network**: Dedicated bridge network (app-network)
- **Service Dependencies**: Nginx waits for backend to be healthy before starting
- **Container Names**: backend-app, nginx-proxy

## Troubleshooting

### Services won't start

Check if port 80 is already in use:
```bash
sudo lsof -i :80
```

### Backend not responding

Check backend logs:
```bash
docker logs backend-app
```

### Nginx errors

Check nginx logs:
```bash
docker logs nginx-proxy
```

### View all running containers

```bash
docker ps
```

## Development

To make changes to the backend application:

1. Edit `backend/app.py`
2. Rebuild and restart: `docker-compose up --build`

To modify nginx configuration:

1. Edit `nginx/nginx.conf`
2. Restart nginx: `docker-compose restart nginx`
