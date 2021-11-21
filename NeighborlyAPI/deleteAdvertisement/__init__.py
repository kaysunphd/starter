import azure.functions as func
import pymongo
from bson.objectid import ObjectId


def main(req: func.HttpRequest) -> func.HttpResponse:

    id = req.params.get('id')

    if id:
        try:
            url = "mongodb://neighborly:NcsuuiRAVEArnrz7krsbOZc9H9sPsIaEo9MGqm6m5s5YcHP4afW8F7p35n8qwBDOE2GWl7suit2n91Nw1lhZhw==@neighborly.mongo.cosmos.azure.com:10255/?ssl=true&replicaSet=globaldb&retrywrites=false&maxIdleTimeMS=120000&appName=@neighborly@"
            client = pymongo.MongoClient(url)
            database = client['neighborhooddata']
            collection = database['advertisements']
            
            query = {'_id': id}
            result = collection.delete_one(query)
            return func.HttpResponse("")

        except:
            print("could not connect to mongodb")
            return func.HttpResponse("could not connect to mongodb", status_code=500)

    else:
        return func.HttpResponse("Please pass an id in the query string",
                                 status_code=400)
