use axum::{
    Router,
    extract::Json,
    http::StatusCode,
    response::{IntoResponse, Response},
    routing::{get, post},
};
use objs::*;

async fn handler_metrics() -> Response {
    let m = metrics::collect_metrics();
    Json(m).into_response()
}

async fn handler_mixed_obj(Json(payload): Json<MixedObject>) -> Response {
    match serde_json::to_string(&payload) {
        Ok(json_string) => {
            println!("Сериализованный JSON: {}", json_string);
            StatusCode::NO_CONTENT.into_response()
        }
        Err(e) => {
            eprintln!("Ошибка сериализации: {}", e);
            (StatusCode::INTERNAL_SERVER_ERROR, "Ошибка сериализации").into_response()
        }
    }
}

async fn handler_flat_obj(Json(payload): Json<FlatObject>) -> Response {
    match serde_json::to_string(&payload) {
        Ok(json_string) => {
            println!("Сериализованный JSON: {}", json_string);
            StatusCode::NO_CONTENT.into_response()
        }
        Err(e) => {
            eprintln!("Ошибка сериализации: {}", e);
            (StatusCode::INTERNAL_SERVER_ERROR, "Ошибка сериализации").into_response()
        }
    }
}

async fn handler_deep_obj(Json(payload): Json<DeepObject>) -> Response {
    match serde_json::to_string(&payload) {
        Ok(json_string) => {
            println!("Сериализованный JSON: {}", json_string);
            StatusCode::NO_CONTENT.into_response()
        }
        Err(e) => {
            eprintln!("Ошибка сериализации: {}", e);
            (StatusCode::INTERNAL_SERVER_ERROR, "Ошибка сериализации").into_response()
        }
    }
}

const ADDR: &'static str = "0.0.0.0:6789";

#[tokio::main]
async fn main() {
    let app = Router::new()
        .route("/mixed", post(handler_mixed_obj))
        .route("/flat", post(handler_flat_obj))
        .route("/deep", post(handler_deep_obj))
        .route("/metrics", get(handler_metrics));

    let listener = tokio::net::TcpListener::bind(ADDR)
        .await
        .unwrap_or_else(|e| panic!("Failed to bind to address: {}\ne: {}", ADDR, e));

    axum::serve(listener, app)
        .await
        .unwrap_or_else(|e| panic!("Server error: {}", e));
}
