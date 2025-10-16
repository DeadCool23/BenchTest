use chrono::Utc;
use serde::Serialize;
use sysinfo::System;

#[derive(Debug, Clone, Serialize)]
pub struct SystemMetrics {
    pub timestamp: String,
    pub cpu_percent: f32,
    pub ram_percent: f32,
    pub ram_used_mb: u64,
    pub ram_total_mb: u64,
    pub thread_count: usize,
}

pub fn collect_metrics() -> SystemMetrics {
    let mut system = System::new_all();
    system.refresh_cpu();
    system.refresh_memory();
    system.refresh_processes();

    let current_pid = sysinfo::get_current_pid().unwrap();
    let cpu_usage = system.global_cpu_info().cpu_usage();
    let used_memory = system.used_memory();
    let total_memory = system.total_memory();
    let ram_percent = (used_memory as f64 / total_memory as f64) * 100.0;

    let thread_count = if let Some(process) = system.process(current_pid) {
        process.tasks().map(|t| t.len()).unwrap_or(0)
    } else {
        0
    };

    SystemMetrics {
        timestamp: Utc::now().to_rfc3339(),
        cpu_percent: cpu_usage,
        ram_percent: ram_percent as f32,
        ram_used_mb: used_memory / 1024 / 1024,
        ram_total_mb: total_memory / 1024 / 1024,
        thread_count,
    }
}

#[cfg(test)]
mod metrics {
    use crate::collect_metrics;

    #[test]
    pub fn check_collector() {
        let a = collect_metrics();
        println!("{:?}", a);
    }
}
