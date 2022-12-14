import json
from aws_lambda_powertools.utilities import parameters


def handler(event, context):
    """Secret snatcher!

    Parameters
    ----------
    event: dict, required
        Expects key to be retrieved to be passed as a query param.

    context: object, required
        Lambda Context runtime methods and attributes

    Returns
    ------
    API Gateway Lambda Proxy Output Format: dict

        JSON with secret
    """

    # We'd probably do some better error handling in real life.
    key = event.queryStringParameters.key

    return {
        "statusCode": 200,
        "body": json.dumps({
            "secret": parameters.get_secret(key),
        }),
    }
