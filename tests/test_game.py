# Developer: Hamdy Abou El Anein
# Contact: info@daylightlinux.ch
# SPDX-License-Identifier: GPL-3.0-only
import unittest
from LizardSpock import CHOICES, RULES, outcome

class GameRulesTests(unittest.TestCase):
    def test_ties(self):
        for choice in CHOICES:
            self.assertEqual(outcome(choice, choice)[0], 0)
    def test_every_pair_has_one_winner(self):
        for a in CHOICES:
            for b in CHOICES:
                if a == b:
                    continue
                result, reason = outcome(a, b)
                self.assertIn(result, (-1, 1))
                self.assertEqual(result, -outcome(b, a)[0])
                self.assertTrue(reason)
    def test_ten_unique_rules(self):
        self.assertEqual(len(RULES), 10)
    def test_invalid(self):
        with self.assertRaises(ValueError):
            outcome("Unknown", "Rock")

if __name__ == "__main__":
    unittest.main()
