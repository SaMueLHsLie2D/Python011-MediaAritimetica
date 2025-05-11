import unittest
from media import calcular_media


class TestCalculoMedia(unittest.TestCase):

    def test_media_inteiros(self):
        self.assertEqual(calcular_media(4, 6), 5.0)

    def test_media_floats(self):
        self.assertAlmostEqual(calcular_media(5.5, 2.5), 4.0)

    def test_media_negativos(self):
        self.assertEqual(calcular_media(-3, -7), -5.0)

    def test_media_misto(self):
        self.assertEqual(calcular_media(-2, 6), 2.0)


if __name__ == '__main__':
    unittest.main()
