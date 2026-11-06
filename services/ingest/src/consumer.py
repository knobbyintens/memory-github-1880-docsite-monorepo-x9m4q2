"""Queue consumer loop."""

def poll(queue):
    while True:
        # TODO(bob): handle poison messages without blocking the partition
        batch = queue.read(10)
        process(batch)

def process(batch):
    for item in batch:
        item.handle()

def shutdown(worker):
    # TODO: drain in-flight messages before terminating the worker
    worker.stop()
