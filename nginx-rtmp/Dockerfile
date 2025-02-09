# Use the official Nginx image as a base
FROM nginx:alpine

# Install dependencies
RUN apk add --no-cache \
    gcc \
    g++ \
    make \
    git \
    pcre-dev \
    openssl-dev \
    zlib-dev

# Clone the RTMP module and Nginx
RUN git clone https://github.com/arut/nginx-rtmp-module.git /nginx-rtmp-module && \
    wget http://nginx.org/download/nginx-1.23.1.tar.gz && \
    tar -zxvf nginx-1.23.1.tar.gz && \
    mv nginx-1.23.1 /nginx

# Build Nginx with the RTMP module
WORKDIR /nginx
RUN ./configure --with-http_ssl_module --add-module=/nginx-rtmp-module && \
    make && \
    make install

# Copy the Nginx configuration file
COPY nginx.conf /usr/local/nginx/conf/nginx.conf

# Expose the RTMP port
EXPOSE 1935

# Start Nginx
CMD ["/usr/local/nginx/sbin/nginx", "-g", "daemon off;"]