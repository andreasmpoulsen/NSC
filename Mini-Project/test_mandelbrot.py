import unittest
import looped_docstr as naive


class TestMandelbrot(unittest.TestCase):
    def test_naive(self):

        result = naive.mandelbrot((1 + 1j))
        self.assertEqual(result, 2)

        result = naive.mandelbrot((0 + 0*1j))
        self.assertEqual(result, 80)

        result = naive.mandelbrot((0 + 10*1j))
        self.assertEqual(result, 1)

        result = naive.mandelbrot((1 + 0*1j))
        self.assertEqual(result, 3)

        result = naive.mandelbrot((-1 + -1*1j))
        self.assertEqual(result, 3)

        result = naive.mandelbrot((-1 + 0*1j))
        self.assertEqual(result, 80)

        result = naive.mandelbrot((0 + -1*1j))
        self.assertEqual(result, 80)


if __name__ == "__main__":
    unittest.main()
