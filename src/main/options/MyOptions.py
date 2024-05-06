#adding packages
import apache_beam as beam
import argparse
from apache_beam.options.pipeline_options import PipelineOptions

#declaring options class
class MyOptions(PipelineOptions):
  @classmethod
  def _add_argparse_args(cls, parser):
    #parameter for topic name
    #parameter will be taken from apllication_*env*.txt
    #parameter is static
    parser.add_argument('--topic_name')
    #parameter for bq kms key
    #parameter will be taken from apllication_*env*.txt
    #parameter is static
    parser.add_argument('--bq_kms_key')
    #parameter for env
    #parameter will be taken from apllication_*env*.txt
    #parameter is static
    parser.add_argument('--env')
