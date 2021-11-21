import azure.functions as func
import pymongo

def main(req: func.HttpRequest) -> func.HttpResponse:

    request = req.get_json()

    if request:
        try:
            url = "mongodb://neighborly:NcsuuiRAVEArnrz7krsbOZc9H9sPsIaEo9MGqm6m5s5YcHP4afW8F7p35n8qwBDOE2GWl7suit2n91Nw1lhZhw==@neighborly.mongo.cosmos.azure.com:10255/?ssl=true&replicaSet=globaldb&retrywrites=false&maxIdleTimeMS=120000&appName=@neighborly@"

            client = pymongo.MongoClient(url)
            database = client['neighborhooddata']
            collection = database['advertisements']

            rec_id1 = collection.insert_one(request)

            return func.HttpResponse(req.get_body())

        except ValueError:
            print("could not connect to mongodb")
            return func.HttpResponse('Could not connect to mongodb', status_code=500)

    else:
        return func.HttpResponse(
            "Please pass name in the body",
            status_code=400
        )