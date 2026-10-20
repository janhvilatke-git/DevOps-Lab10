from prometheus_client import start_http_server, Counter
import time


REQUESTS = Counter(
    "devops_lab10_requests_total",
    "Total number of application runs"
)


def greet(name):
    return f"Hello, {name}! Welcome to DevOps Lab 10."


def add(a, b):
    return a + b


if __name__ == "__main__":
    start_http_server(8000)
    print("Prometheus metrics available on port 8000")

    while True:
        REQUESTS.inc()
        print(greet("Student"))
        print("Addition result:", add(10, 20))
        time.sleep(10)