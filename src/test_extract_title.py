import unittest
import pytest

from extract_title import extract_title

class TestExtractTitle(unittest.TestCase):
    def test_extract_title_basic(self):
        markdown = "# Hello World"
        self.assertEqual(extract_title(markdown), "Hello World")

    def test_extract_title_no_h1(self):
        markdown = "Hello World\n## Subtitle"
        with pytest.raises(ValueError):
            extract_title(markdown)
            
    def test_extract_title_h2_not_used(self):
        markdown = "## Not a title"
        with pytest.raises(ValueError):
            extract_title(markdown)
            
    def test_extract_title_whitespace(self):
        markdown = "#    Hello World   "
        self.assertEqual(extract_title(markdown), "Hello World")
        
    def test_extract_title_later_line(self):
        markdown = "Intro text\n# Real Title\nMore text"
        self.assertEqual(extract_title(markdown), "Real Title")

if __name__ == "__main__":
    unittest.main()