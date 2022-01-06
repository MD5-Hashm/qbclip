use std::process::Command;
fn main() {
Command::new("python")
.arg(r"C:\qb.py")
.spawn()
.expect("failed to execute process");
}