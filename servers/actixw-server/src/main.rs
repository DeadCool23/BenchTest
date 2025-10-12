use actix_web::{App, HttpResponse, HttpServer, Responder, post, web::Json};
use objs::*;

#[post("/mixed")]
async fn handler_mixed_obj(Json(_payload): Json<MixedObject>) -> impl Responder {
    HttpResponse::NoContent().finish()
}

#[post("/flat")]
async fn handler_flat_obj(Json(_payload): Json<FlatObject>) -> impl Responder {
    HttpResponse::NoContent().finish()
}

#[post("/deep")]
async fn handler_deep_obj(Json(_payload): Json<DeepObject>) -> impl Responder {
    HttpResponse::NoContent().finish()
}

const ADDR: &str = "127.0.0.1:8181";

#[actix_web::main]
async fn main() -> std::io::Result<()> {
    HttpServer::new(|| {
        App::new()
            .service(handler_mixed_obj)
            .service(handler_flat_obj)
            .service(handler_deep_obj)
    })
    .bind(ADDR)?
    .run()
    .await
}
