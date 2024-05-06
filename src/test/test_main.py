import unittest
import xmlrunner
import apache_beam as beam
from apache_beam.testing.test_pipeline import TestPipeline
from apache_beam.options.pipeline_options import PipelineOptions
from apache_beam import pvalue
from apache_beam.testing.util import assert_that
from apache_beam.testing.util import is_not_empty
from apache_beam.testing.util import is_empty
from apache_beam.testing.util import equal_to
from apache_beam import typehints
from apache_beam.io import ReadFromBigQueryRequest
import sys,os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'main'))
from processors import ConvertToJson
from resources import dev
from options import MyOptions
class convert_to_json_test(unittest.TestCase):
    def test_valid_input_data(self):
        output_row=[{"id": "bf4b0b70-9fef-482c-8719-334bfb87ffab","specversion": "1.0","type": "com.hsbc.wpb.fraud.customer.chagetelephones.gb.notifications.v1","dataschema": "https://{schemaregistry}/hsbc/schemas/data/nonmon/1","datacontenttype": "application/json","source": "/hsbc/\u003c\u003e/fraud/feedzai","subject": "","time": "2023-12-12T10:32:53+00:00","data": [{"feedback":{"id":101},"source": "FD_COP","appSource": "UK_CDM","messageHeader": {"customerType": "R","accountType": "NA","countryCode": "GBP","authenticationType": "NA","channelType": "B","txnType": "DNU","requestType": "N","transactionPriority": "L","customerPortfolio": "PERS"},"customerDetail": {"customerNumber": "0800033868"},"transactionDetail": {"transactionTimestamp": "","changeEventOld": "","changeEventNew": "NITINdddd PARASARdd","changeEventReason": "Name","changeEventDelivery": "Insert"}}]}]
        with TestPipeline() as p:
        # with beam.Pipeline() as p:
            rows = (p | 'Create PColl' >> beam.Create(output_row) )   
            new_data = rows|'ConvertToJson' >> beam.ParDo(ConvertToJson.ConvertToJson(),'INFO')
            assert_that(new_data,is_not_empty(),label='test_valid_input_data_valid')
    
    def test_no_input_data(self):
        output_row=[]
        with TestPipeline() as p:
        # with beam.Pipeline() as p:
            rows = (p | 'Create PColl' >> beam.Create(output_row) )   
            assert_that(rows,is_empty(),label='test_no_input_data')
            new_data = rows|'ConvertToJson' >> beam.ParDo(ConvertToJson.ConvertToJson(),'INFO')
if __name__ == '__main__':
    unittest.main(
        testRunner=xmlrunner.XMLTestRunner(output='utest-reports'),
        failfast=False,
        buffer=False,
        catchbreak=False)
