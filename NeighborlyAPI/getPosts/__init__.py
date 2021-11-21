import logging
import azure.functions as func
import pymongo
import json
from bson.json_util import dumps


def main(req: func.HttpRequest) -> func.HttpResponse:

    logging.info('Python getPosts trigger function processed a request.')

    try:
        url = "mongodb://neighborly:NcsuuiRAVEArnrz7krsbOZc9H9sPsIaEo9MGqm6m5s5YcHP4afW8F7p35n8qwBDOE2GWl7suit2n91Nw1lhZhw==@neighborly.mongo.cosmos.azure.com:10255/?ssl=true&replicaSet=globaldb&retrywrites=false&maxIdleTimeMS=120000&appName=@neighborly@"
        client = pymongo.MongoClient(url)
        database = client['neighborhooddata']
        collection = database['posts']

        result = collection.find({})
        result = dumps(result)

        return func.HttpResponse(result, mimetype="application/json", charset='utf-8', status_code=200)
    except:
        return func.HttpResponse("Bad request.", status_code=400)