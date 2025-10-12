use serde::{Deserialize, Serialize};

#[derive(Debug, Serialize, Deserialize)]
pub struct MixedObject {
    pub f1: String,
    pub f2: i32,
    pub f3: bool,
    pub f4: f64,
    pub f5: F5,
    pub f6: F6,
    pub f7: F7,
    pub f8: F8,
    pub f9: F9,
    pub f10: F10,
}

#[derive(Debug, Serialize, Deserialize)]
pub struct F5 {
    pub f51: String,
    pub f52: i32,
    pub f53: bool,
    pub f54: f64,
    pub f55: F55,
}

#[derive(Debug, Serialize, Deserialize)]
pub struct F55 {
    pub f551: String,
    pub f552: i32,
    pub f553: bool,
    pub f554: f64,
    pub f555: F555,
}

#[derive(Debug, Serialize, Deserialize)]
pub struct F555 {
    pub f5551: String,
    pub f5552: i32,
    pub f5553: bool,
    pub f5554: f64,
    pub f5555: F5555,
}

#[derive(Debug, Serialize, Deserialize)]
pub struct F5555 {
    pub f55551: String,
    pub f55552: i32,
    pub f55553: bool,
    pub f55554: f64,
}

#[derive(Debug, Serialize, Deserialize)]
pub struct F6 {
    pub f61: String,
    pub f62: i32,
    pub f63: bool,
    pub f64: f64,
    pub f65: F65,
}

#[derive(Debug, Serialize, Deserialize)]
pub struct F65 {
    pub f651: String,
    pub f652: i32,
    pub f653: bool,
    pub f654: f64,
}

#[derive(Debug, Serialize, Deserialize)]
pub struct F7 {
    pub f71: String,
    pub f72: i32,
    pub f73: bool,
    pub f74: f64,
    pub f75: F75,
}

#[derive(Debug, Serialize, Deserialize)]
pub struct F75 {
    pub f751: String,
    pub f752: i32,
    pub f753: bool,
    pub f754: f64,
}

#[derive(Debug, Serialize, Deserialize)]
pub struct F8 {
    pub f81: String,
    pub f82: i32,
    pub f83: bool,
    pub f84: f64,
    pub f85: F85,
}

#[derive(Debug, Serialize, Deserialize)]
pub struct F85 {
    pub f851: String,
    pub f852: i32,
    pub f853: bool,
    pub f854: f64,
}

#[derive(Debug, Serialize, Deserialize)]
pub struct F9 {
    pub f91: String,
    pub f92: i32,
    pub f93: bool,
    pub f94: f64,
    pub f95: F95,
}

#[derive(Debug, Serialize, Deserialize)]
pub struct F95 {
    pub f951: String,
    pub f952: i32,
    pub f953: bool,
    pub f954: f64,
}

#[derive(Debug, Serialize, Deserialize)]
pub struct F10 {
    pub f101: String,
    pub f102: i32,
    pub f103: bool,
    pub f104: f64,
    pub f105: F105,
}

#[derive(Debug, Serialize, Deserialize)]
pub struct F105 {
    pub f1051: String,
    pub f1052: i32,
    pub f1053: bool,
    pub f1054: f64,
}
