// Example FFI with pyo3
// https://pyo3.rs/latest/guide/ffi.html

use pyo3::prelude::*;

fn fib_result(n: usize) -> usize {
    if n < 2 {
        n
    } else {
        fib_result(n - 1) + fib_result(n - 2)
    }
}

#[pyfunction]
fn fib(n: usize) -> PyResult<usize> {
    Ok(fib_result(n))
}

#[pymodule]
fn rust_py_ffi(m: &Bound<'_, PyModule>) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(fib, m)?)?;
    Ok(())
}