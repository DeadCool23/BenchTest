FROM rust:latest

RUN apt-get update && apt-get install -y \
    ca-certificates \
    libssl3 \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY ./servers/target/release/axum-server .

CMD ["./axum-server"]