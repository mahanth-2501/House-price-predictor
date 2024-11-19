import boto3, json
import base64
import os
from sklearn.preprocessing import PolynomialFeatures

ENDPOINT_NAME = 'kmeans-1590412531-9820533'
runtime= boto3.client('runtime.sagemaker', region_name='us-east-2')

def lambda_handler(event, context):
    print(event)
    data = json.loads(event)
    features = [[data['floors'], data['waterfront'], data['bedrooms'], data['basement'], data['view'], data['bathrooms'], data['condition'], data['year_build'], data['grade'], data['sqft_living']]]
    
    poly = PolynomialFeatures(degree=3, include_bias=False)
    features = poly.fit_transform(features)

    payload = ''
    for val in features[0]:
        payload += str(val)
        payload += ','
    payload = payload[:-1]

    response = runtime.invoke_endpoint(
                      EndpointName=ENDPOINT_NAME,
                      ContentType='text/csv',
                      Body=payload
                  )

    response = json.loads(response['Body'].read().decode())
    print(response)
    # TODO implement
    return response['predictions'][0]['score']
