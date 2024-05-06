#adding packages
#adding beam package
import apache_beam as beam
#adding json package
import json
#adding sys package
import sys
#adding parsing package
import argparse
#adding logging package
import logging
#locating dev in resources folder
from resources import dev
#locating prod in resources folder
from resources import prod

class ConvertToJson(beam.DoFn):
        def process(self,element,logging_mode):
            #setting up logging
            logging.getLogger().setLevel(logging.getLevelName(logging_mode))
            #Converting element to json
            row=json.dumps(element,default=str)
            #logging row
            logging.debug(' json row : %s ',row)
            #Adding logging
            logging.info('lifecycle_id: %s ', element["data"][0]["feedback"]["id"])
            #yielding of data
            yield row
