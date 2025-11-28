# Stage 1: Build the Angular application
FROM node:22-alpine AS build

WORKDIR /app

# Copy package.json and package-lock.json to install dependencies
COPY package.json ./
RUN npm install

# Copy the rest of the application code
COPY . .

# Build the Angular application for production
RUN npm run build --configuration=production

# Stage 2: Serve the application with Nginx
FROM nginx:alpine

# Copy the built Angular application from the build stage
# Replace 'your-app-name' with the actual name of your Angular application's build output folder
COPY --from=build /app/dist/angular-app/browser /usr/share/nginx/html

# Copy custom Nginx configuration (optional, but recommended for Angular apps)
# Create an 'nginx' directory in your project root with a 'default.conf' file
COPY nginx/default.conf /etc/nginx/conf.d/default.conf

# Expose port 80 for Nginx
EXPOSE 80

# Command to start Nginx when the container launches
CMD ["nginx", "-g", "daemon off;"]