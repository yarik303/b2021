import time
import unittest
from main import *

def measure_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"time pasing {func.__name__}: {execution_time} seconds")
        return result
    return wrapper

class TestMain(unittest.TestCase):

    @measure_time
    def test_addition(self):
        result = blyat(3.14159, 20)
        self.assertEqual(result, 23.14159)

    @measure_time
    def test_subtraction(self):
        result = suka(3.14159, 20)
        self.assertEqual(result, -16.85841)

    @measure_time
    def test_multiplication(self):
        result = nahyu(3.14159, 20)
        self.assertEqual(result, 62.8318)

    @measure_time
    def test_division(self):
        result = pidr(3.14159, 20)
        self.assertEqual(result, 0.15707949999999998)

if __name__ == '__main__':
    unittest.main()
