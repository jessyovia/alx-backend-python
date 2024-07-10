# Python Async Comprehension

This project demonstrates the use of asynchronous programming in Python, focusing on asynchronous comprehensions and generators.

## Project Structure

The project consists of three main tasks:

1. **Async Generator** (`0-async_generator.py`): 
   - An asynchronous coroutine that loops 10 times, each time waiting for 1 second and yielding a random number between 0 and 10.

2. **Async Comprehensions** (`1-async_comprehension.py`): 
   - A coroutine that collects 10 random numbers using an asynchronous comprehension over the `async_generator`.

3. **Measure Runtime** (`2-measure_runtime.py`): 
   - A coroutine that measures the total runtime of executing `async_comprehension` four times in parallel using `asyncio.gather`.

## Files

- `0-async_generator.py`: Defines the asynchronous generator.
- `1-async_comprehension.py`: Defines the asynchronous comprehension.
- `2-measure_runtime.py`: Measures the runtime of the asynchronous comprehension executed in parallel.
- `README.md`: Project documentation.

## Requirements

- Python 3.7
- Ubuntu 18.04 LTS
- `pycodestyle` style (version 2.5.x)

## How to Run

1. **Clone the repository**:
   ```sh
   git clone https://github.com/yourusername/alx-backend-python
   cd alx-backend-python/0x02-python_async_comprehension
