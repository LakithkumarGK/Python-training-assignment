import unittest
from unittest.mock import patch

class Car:
    def __init__(self, brand, model, year, mileage):
        self.brand = brand
        self.model = model
        self.year = year
        self.mileage = mileage

    def drive(self, distance):
        self.mileage += distance

    def display_info(self):
        print(f"BRAND     | {self.brand}")
        print(f"MODEL     | {self.model}")
        print(f"YEAR      | {self.year}")
        print(f"MILEAGE   | {self.mileage}")


class TestCar(unittest.TestCase):

    def setUp(self):
        # Create a Car instance for testing
        self.car = Car("Toyota", "Corolla", 2020, 5000)

    def test_initialization(self):
        # Test if the car is initialized correctly
        self.assertEqual(self.car.brand, "Toyota")
        self.assertEqual(self.car.model, "Corolla")
        self.assertEqual(self.car.year, 2020)
        self.assertEqual(self.car.mileage, 5000)

    def test_drive(self):
        # Test the drive method
        self.car.drive(100)
        self.assertEqual(self.car.mileage, 5100)
        # Removed test_display_info
    def test_display_info(self):
        """
        Test the `display_info` method of the `Car` class.
        This test verifies that the `display_info` method correctly outputs
        the expected car information to the standard output. The output is
        captured and compared against the expected formatted string.
        Steps:
        - Mock the `sys.stdout` to capture printed output.
        - Call the `display_info` method of the `Car` instance.
        - Assert that the expected output is present in the captured output.
        Expected Output:
        BRAND     | Toyota
        MODEL     | Corolla
        YEAR      | 2020
        MILEAGE   | 5000
        """
        # Test the display_info method (output verification)
        expected_output = (
            "BRAND     | Toyota\n"
            "MODEL     | Corolla\n"
            "YEAR      | 2020\n"
            "MILEAGE   | 5000\n"
        )
        # Removed test_display_info
        from io import StringIO

        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.car.display_info()
        self.assertIn(expected_output.strip(), mock_stdout.getvalue().strip())

if __name__ == "__main__":
    unittest.main()