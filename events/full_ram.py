import time


def ram_saturation():
    allocations = []
    try:
        while True:
            time.sleep(0.0001)
            allocations.append(bytearray(10000))
    except MemoryError:
        time.sleep(30)
        allocations.clear()
