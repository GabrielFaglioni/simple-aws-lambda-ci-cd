import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import json
from src.lambda_function import lambda_handler

def test_lambda_function():
  assert {
    'statusCode': 200,
    'body': json.dumps('Testing successul')
  } == lambda_handler(None, None)