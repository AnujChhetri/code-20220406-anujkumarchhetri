import unittest
import BMI_calculator


class TestingSum(unittest.TestCase):

    def test_bmi_calculate(self):
        self.assertEqual(BMI_calculator.calculate_bmi(171, 96), 32.83061454806607, "It should be 32.83061454806607")
        self.assertEqual(BMI_calculator.calculate_bmi(171, "121"), "", "It should be ''")

    def test_get_range(self):
        self.assertEqual(BMI_calculator.get_range(32.83061454806607), "30-34.9", "It should be '30-34.9'")
        self.assertEqual(BMI_calculator.get_range(32), "30-34.9", "It should be '30-34.9'")
        self.assertEqual(BMI_calculator.get_range("32.83061454806607"), False, "It should be False")

    def test_process_data(self):
        input = ({"Gender": "Female", "HeightCm": 166, "WeightKg": 62})
        with self.assertRaises(ValueError) as ve:
            BMI_calculator.process_data(input)
        self.assertEqual(
            str(ve.exception),
            """Wrong data provided, refer to the following error message:
 <class 'dict'> is provided where as 'list' is required"""
        )


if __name__ == '__main__':
    unittest.main()
