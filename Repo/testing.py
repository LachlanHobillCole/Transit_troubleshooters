# %%
import unittest
from Calculations import Emission_Factor


class TestEmissionFactor(unittest.TestCase):
    def setUp(self):
        self.emission_factors = Emission_Factor()

    def test_diesel(self):
        fuel_type = "Diesel"
        emissions_data = self.emission_factors.get_emission_factor(fuel_type)
        self.assertEqual(2671.2, emissions_data)

    def test_cng(self):
        fuel_type = "CNG"
        emissions_data = self.emission_factors.get_emission_factor(fuel_type)
        self.assertEqual(1974.1, emissions_data)

    # def test_error(self):
    # self.assertRaises(None, get_emission_factor, fuel_type = 'abc')


# %%


if __name__ == "__main__":
    unittest.main()

# %%
