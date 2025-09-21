import time
from fastapi import FastAPI
from fastapi.responses import RedirectResponse
import rust_py_ffi

app = FastAPI()


def fib_py(n: int):
    if n < 2:
        return n
    else:
        return fib_py(n - 1) + fib_py(n - 2)


@app.get("/")
def read_root():
    return RedirectResponse("/docs")


@app.get("/fib_rust/{n}")
def read_root(n: int):
    start_time = time.time()
    result = rust_py_ffi.fib(n)
    end_time = time.time()
    return {"result": result, "time": end_time - start_time}


@app.get("/fib_py/{n}")
def read_root(n: int):
    start_time = time.time()
    result = fib_py(n)
    end_time = time.time()
    return {"result": result, "time": end_time - start_time}


if __name__ == "__main__":
    fastapi.run(app, host="0.0.0.0", port=8000)
