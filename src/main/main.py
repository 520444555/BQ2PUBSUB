#adding packages
import apache_beam as beam
from apache_beam.io.gcp.internal.clients import bigquery
from apache_beam.options.pipeline_options import PipelineOptions
import logging
import json
import sys
import argparse
from options import MyOptions
from processors import BQReadRequest
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'test'))
import test_main
import unittest

#setting up options
my_pipeline_options = PipelineOptions().view_as(MyOptions.MyOptions)

#only calling statements here
def run():
    #Create pipeline
    with beam.Pipeline(options=PipelineOptions()) as pipeline:
        #Creating PCollection
        rows = (pipeline | beam.Create([None])
        #Reading from Bigquery
            | 'Read BQ Table' >> beam.ParDo(BQReadRequest.BQReadRequest(),my_pipeline_options.env))
        results = rows | 'ReadAll' >> beam.io.ReadAllFromBigQuery(kms_key=my_pipeline_options.bq_kms_key)
        #Converting results to json
        new_data = results|'ConvertToJson' >> beam.Map(lambda x:json.dumps(x,default=str))
        #UTF encoding
        utf_data=new_data |'UTF-8' >> beam.Map(lambda x: x.encode('utf-8'))
        #publish data to pubsub
        utf_data | 'Publish to PubSub' >> beam.io.WriteToPubSub(my_pipeline_options.topic_name)

if __name__ == '__main__':
    #Adding logging
    logger = logging.getLogger().setLevel(logging.INFO)
    #return a suite of all test cases
    suite = unittest.TestLoader().loadTestsFromModule(test_main)
    #display result
    result_unittest = unittest.TextTestRunner().run(suite)
    #check if unittest are successful
    if result_unittest.wasSuccessful():
        #run the pipeline
    	run()
