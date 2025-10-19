use actix_web::{App, HttpResponse, HttpServer, Responder, get, post, web::Json};
use objs::*;

#[get("/metrics")]
async fn handler_metrics() -> impl Responder {
    let m = metrics::collect_metrics();
    HttpResponse::Ok().json(m)
}

#[post("/mixed")]
async fn handler_mixed_obj(Json(payload): Json<MixedObject>) -> impl Responder {
    match serde_json::to_string(&payload) {
        Ok(json_string) => {
            println!("Сериализованный JSON: {}", json_string);
            HttpResponse::NoContent().finish()
        }
        Err(e) => {
            eprintln!("Ошибка сериализации: {}", e);
            HttpResponse::InternalServerError().body("Ошибка сериализации")
        }
    }
}

#[post("/flat")]
async fn handler_flat_obj(Json(payload): Json<FlatObject>) -> impl Responder {
    match serde_json::to_string(&payload) {
        Ok(json_string) => {
            println!("Сериализованный JSON: {}", json_string);
            HttpResponse::NoContent().finish()
        }
        Err(e) => {
            eprintln!("Ошибка сериализации: {}", e);
            HttpResponse::InternalServerError().body("Ошибка сериализации")
        }
    }
}

#[post("/deep")]
async fn handler_deep_obj(Json(payload): Json<DeepObject>) -> impl Responder {
    match serde_json::to_string(&payload) {
        Ok(json_string) => {
            println!("Сериализованный JSON: {}", json_string);
            HttpResponse::NoContent().finish()
        }
        Err(e) => {
            eprintln!("Ошибка сериализации: {}", e);
            HttpResponse::InternalServerError().body("Ошибка сериализации")
        }
    }
}

const ADDR: &str = "0.0.0.0:9876";

#[actix_web::main]
async fn main() -> std::io::Result<()> {
    HttpServer::new(|| {
        App::new()
            .service(handler_mixed_obj)
            .service(handler_flat_obj)
            .service(handler_deep_obj)
            .service(handler_metrics)
    })
    .bind(ADDR)?
    .run()
    .await
}
