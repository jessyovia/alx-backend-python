Unit Tests and Integration Tests
Project Overview
This project focuses on unit testing and integration testing for a Python application. It covers how to write and structure unit tests, use mocking and parameterization, and distinguish between unit and integration tests.

Project Structure
utils.py: Contains utility functions to be tested.
client.py: Contains client-related functionalities.
fixtures.py: Contains fixtures for testing.
test_utils.py: Contains unit tests for utils.py.
README.md: This file.
Testing
Unit Tests
Unit tests are written to test individual functions in isolation. They check that a function returns the expected results for different inputs and edge cases. Mocking is used to isolate the function from external dependencies.

Test File: test_utils.py

Integration Tests
Integration tests are designed to test the interaction between different components of the system. They ensure that various parts of the application work together as expected.

Running the Tests
To run the unit tests, execute the following command:

$ python -m unittest test_utils.py


Documentation

    All modules, classes, and functions in the code are documented.
    Documentation includes purpose, parameters, and return values.

Requirements

    Python 3.7 or later
    Ubuntu 18.04 LTS
    pycodestyle for style checking

For any questions or further information, please contact Jessica Oviahon at jessyovia100@gmial.com
