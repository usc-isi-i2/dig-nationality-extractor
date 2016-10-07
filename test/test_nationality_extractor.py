import sys
import time
import os
import unittest

# sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
# TEST_DATA_DIR = os.path.join(os.path.dirname(__file__), 'data')

from digExtractor.extractor import Extractor
from digExtractor.extractor_processor import ExtractorProcessor
from digNationalityExtractor.nationality_extractor import NationalityExtractor

class TestServiceExtractorMethods(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_age_extractor(self):
        doc = {'content': "American Antiguans Panamanian Hello World", 'b': 'world'}

        extractor = NationalityExtractor().set_metadata({'extractor': 'nationality'})
        extractor_processor = ExtractorProcessor().set_input_fields(['content']).set_output_field('extracted').set_extractor(extractor)
        updated_doc = extractor_processor.extract(doc)
        self.assertEqual(updated_doc['extracted'][0]['value'], ['Panamanian', 'American', 'Antiguans'])

    

if __name__ == '__main__':
    unittest.main()



