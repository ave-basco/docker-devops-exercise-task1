# DevOps Task 1
A repo containing a simple webapp powered by FastAPI written in Python, a UI in next.js, and a MySQL database which are meant to be deployed separately in Docker containers. The Dockerfiles for configuration of the containers and a docker-compose.yml are included in this repo for replication.

**FastAPI source code:** https://bitbucket.org/metawhale/fast-api-clean/src/main/

**Next.js source code:** https://bitbucket.org/metawhale/nextjs_app/src/main/

## Getting Started

### Prerequisites

Make sure you have the following installed:

- [Docker Desktop](https://www.docker.com/)
- Git

---

## Running the Project Locally

### 1. Clone the Repository
```bash
git clone https://github.com/ave-basco/docker-devops-exercise-task1
cd docker-devops-exercise-task1
```
### 2. Startup Docker Engine locally
### 3. Build and start containers
```bash
docker-compose up --build
```
### 4. Stopping and starting the containers
To Start:
```bash
docker-compose up 
```

To Stop:
```bash
docker-compose down
```

## Local Hosting

**FastAPI hosted locally on port 8000** http://localhost:8000/
**Next.js UI hosted locally on port 3000** http://localhost:3000/

