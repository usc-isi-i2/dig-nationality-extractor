# -*- coding: utf-8 -*-
# @Author: ZwEin
# @Date:   2016-10-03 23:46:09
# @Last Modified by:   ZwEin
# @Last Modified time: 2016-10-06 23:12:44

import copy 
import types
from digExtractor.extractor import Extractor
import names_helper

class NationalityExtractor(Extractor):

    def __init__(self):
        self.renamed_input_fields = ['text']
        
    def extract(self, doc):
        if 'text' in doc:
            return names_helper.extract(doc['text'])
        return None

    def get_metadata(self):
        return copy.copy(self.metadata)

    def set_metadata(self, metadata):
        self.metadata = metadata
        return self

    def get_renamed_input_fields(self):
        return self.renamed_input_fields