import math
import unittest

from dynamics_metrics import margot_pi, soter_mu


class TestDynamicsMetrics(unittest.TestCase):
    def test_margot_earth_matches_published_table(self):
        # Margot (2015) Table 1: Earth Pi = 8.1e2 for C = 2 sqrt(3), t*=tMS.
        self.assertTrue(math.isclose(margot_pi(1.0, 1.0), 8.1e2, rel_tol=0.03))

    def test_margot_mars_matches_published_table(self):
        # Margot (2015) Table 1: Mars Pi = 5.4e1.
        self.assertTrue(math.isclose(margot_pi(0.107, 1.523679), 5.4e1, rel_tol=0.03))

    def test_soter_is_mass_ratio(self):
        self.assertEqual(soter_mu(1000.0, 10.0), 100.0)


if __name__ == "__main__":
    unittest.main()
