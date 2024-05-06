#adding packages
#adding beam package
import apache_beam as beam
#adding json package
import json
#adding sys package
import sys
#adding arg package
import argparse
#locating dev in resources frolder
from resources import dev
#locating prod in resources folder
from resources import prod

class BQReadRequest(beam.DoFn):
        def process(self,element,env):
                print("******************")
                
                #print(str(end_date.get()),type(end_date))
                #Checking of environment
                if env == "dev":
                        query=dev.query
                if env == "prod":
                        query=prod.query
               
                #query printing
                print(query)
                from apache_beam.io import ReadFromBigQueryRequest
                #yield read from bigquery request
                yield ReadFromBigQueryRequest(query=query,use_standard_sql=True)
