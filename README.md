# rust-py-ffi

This project demonstrates the integration between Rust and Python(w Fastapi) using PyO3 for Foreign Function Interface (FFI). It compares the performance of a Fibonacci function implemented in both Rust and Python, where a FastAPI endpoint calls the Rust function for computation.

## Performance Comparison (Fibonacci)

| Implementation | Result    | Time (seconds) |
|----------------|-----------|----------------|
| Rust           | 102334155 | 0.353371       |
| Python         | 102334155 | 29.310354      |


### `/fib_rust/{n}`

- **Description:** Calculates the Fibonacci sequence for a given number `n` using the Rust implementation.
- **Method:** `GET`
- **Path Parameters:**
    - `n` (integer): The number for which to calculate the Fibonacci sequence.
- **Response:**
    ```json
    {
      "result": 102334155,
      "time": 0.35337138175964355,
    }
    ```

### `/fib_py/{n}`

- **Description:** Calculates the Fibonacci sequence for a given number `n` using the Python implementation.
- **Method:** `GET`
- **Path Parameters:**
    - `n` (integer): The number for which to calculate the Fibonacci sequence.
- **Response:**
    ```json
    {
      "result": 102334155,
      "time": 29.310354709625244,
    }
    ```