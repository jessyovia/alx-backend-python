# Python Async

This repository contains Python scripts demonstrating the use of asynchronous programming with asyncio.

## Description

- `0-basic_async_syntax.py`: Contains the `wait_random` coroutine that waits for a random delay and returns it.
- `1-concurrent_coroutines.py`: Contains the `wait_n` coroutine that spawns `wait_random` n times and returns the list of delays in ascending order.
- `2-measure_runtime.py`: Contains the `measure_time` function that measures the total execution time for `wait_n`.
- `3-tasks.py`: Contains the `task_wait_random` function that returns an asyncio.Task.
- `4-tasks.py`: Contains the `task_wait_n` coroutine that spawns `task_wait_random` n times and returns the list of delays in ascending order.

## Running the Code

To run any of the scripts, execute them using Python 3. For example:

```bash
python3 0-main.py
