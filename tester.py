from third import count_letter_in_string
import unittest

class TestGreeter(unittest.TestCase):

    def setUp(self):
        self.stringempty = ''
        self.notastring = 345
        self.stringwith_four_a = 'hello alabama'

    def test_emptystring(self):
        self.assertEqual(count_letter_in_string(self.stringempty, 'a'), 0)

    def test_notastring(self):
        self.assertEqual(count_letter_in_string(self.notastring, 'a'), 0)

    def test_number_with_number(self):
        self.assertEqual(count_letter_in_string(self.notastring, 3), 0)

    def test_counting_positive(self):
        self.assertEqual(count_letter_in_string(self.stringwith_four_a, 'a'), 4)

    def test_counting_multipleletter(self):
        self.assertEqual(count_letter_in_string(self.stringwith_four_a, 'al'), 0)

    def test_counting_zero(self):
        self.assertEqual(count_letter_in_string(self.stringwith_four_a, 'z'), 0)


if __name__ == '__main__':
    unittest.main()
