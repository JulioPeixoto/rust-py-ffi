# rust-py-ffi

This project demonstrates the integration between Rust and Python(w Fastapi) using PyO3 for Foreign Function Interface (FFI). It compares the performance of a Fibonacci function implemented in both Rust and Python, where a FastAPI endpoint calls the Rust function for computation.

## Performance Comparison (Fibonacci)

| Implementation | Result    | Time (seconds) |
| -------------- | --------- | -------------- |
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
    "time": 0.35337138175964355
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
    "time": 29.310354709625244
  }
  ```

## Como Iniciar

Siga os passos abaixo para configurar e executar o projeto:

### 1. Clonar o Repositório

```bash
git clone https://github.com/seu-usuario/rust-py-ffi.git
cd rust-py-ffi
```

### 2. Configurar o Ambiente Python

Certifique-se de ter o `uv` instalado. Se não tiver, pode instalá-lo com `pip install uv`.
Em seguida, sincronize as dependências e o ambiente virtual:

```bash
uv sync
```

### 3. Compilar a Extensão Rust

O `maturin` será usado para compilar o código Rust e torná-lo disponível para o Python. Execute o comando `develop` para um ambiente de desenvolvimento:

```bash
maturin develop
```

### 4. Rodar a Aplicação FastAPI

Com a extensão Rust compilada e o ambiente Python configurado, você pode iniciar a aplicação FastAPI:

```bash
fastapi run src/main.py --host 0.0.0.0 --port 8000 --reload
```

A aplicação estará acessível em `http://localhost:8000`. Você pode ir para `http://localhost:8000/docs` para ver a documentação interativa da API.
