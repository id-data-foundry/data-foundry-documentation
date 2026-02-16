# Use the latest official Ruby image
FROM ruby:latest

# Set environment variables
ENV JEKYLL_ENV=production \
    LC_ALL=C.UTF-8

# Install essential build tools and dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Set the working directory inside the container
WORKDIR /usr/src/app

# Copy Gemfile and Gemfile.lock first for efficient caching
COPY Gemfile* ./

# Install Bundler and project dependencies
RUN gem install bundler && bundle install

# Copy the rest of the source code
COPY . .

# Default command (can be overridden)
CMD ["bundle", "exec", "jekyll", "build"]
