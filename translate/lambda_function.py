# imported libraries
import json
import decimal
import boto3


def lambda_handler(event, context):
    ''' Accepts some US dollar input and returns the amount of change
        needed to make up that value.
        :param event: a request that has a JSON input with some "amount" value
        :return: a response with the correct US change to make up the amount,
            formatted in JSON as the number of quarters/dimes/nickels/pennies.
    '''
    
    print(event)
    client = boto3.client('translate', region_name="us-west-2")
    # check that the request has some input body
    if 'body' in event:
        event = json.loads(event["body"])

    # get float "amount"
    text = event["phrase"]
    result = client.translate_text(Text=text, SourceLanguageCode="auto", TargetLanguageCode="en")
    # calculate the resultant change and store the result (res)
    response = {
        "statusCode": "200",
        "headers": { "Content-type": "application/json" },
        "body": json.dumps({"result": result})
    }

    return response
