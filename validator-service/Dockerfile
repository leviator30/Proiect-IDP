# Use a lightweight Node.js 18 image
FROM node:18-alpine

# Set the working directory inside the container
WORKDIR /app

# Copy package files first to optimize Docker layer caching
COPY package*.json ./

# Install only production dependencies
RUN npm install

# Copy the rest of the application code (server.js)
COPY . .

# Expose the internal port defined in your server.js
EXPOSE 3000

# Start the service
CMD ["node", "server.js"]