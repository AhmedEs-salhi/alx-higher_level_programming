import unittest

class TestReadme(unittest.TestCase):
    def test_readme(self):
        with open("README.md", "r", encoding="utf-8") as file:
            size_read = file.read()
        self.assertGreater(len(size_read), 0)
