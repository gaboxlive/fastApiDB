#!/bin/bash
# build-and-run.sh

# Build frontend
echo "Building Angular frontend..."
cd frontend
npm install
npm run build --prod
cd ..

# Copy built frontend to nginx directory
echo "Copying built files..."
mkdir -p frontend-dist
cp -r frontend/dist/angular-app/browser/* frontend-dist/

# Build and run with Docker Compose
echo "Starting services with Docker Compose..."
docker-compose down
docker-compose up --build