import time

class ProgressMonitor:
    def __init__(self):
        self.start_time = time.time()

    def update(self, message):
        elapsed = time.time() - self.start_time
        print(f"[{elapsed:.2f}s] {message}")

    def finish(self):
        elapsed = time.time() - self.start_time
        print(f"Proceso completado en {elapsed:.2f} segundos")