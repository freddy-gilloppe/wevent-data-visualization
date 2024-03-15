import pymongo
import dotenv
import os

def fetch_data(start_date=None, end_date=None) -> dict:
    dotenv.load_dotenv()
    # mongo_uri = dotenv.get_key('.env', 'MONGO_URI')
    mongo_uri = os.environ["MONGO_URI"]

    client = pymongo.MongoClient(mongo_uri)
    database = client.wevent

    # Search events and apply eventual filters
    events = list(database.events.find({}))
    if start_date:
        events = list(filter(lambda event: event['startDate'].split('T')[0] >= start_date.strftime('%Y-%m-%d'), events))
    if end_date:
        events = list(filter(lambda event: event['endDate'].split('T')[0] <= end_date.strftime('%Y-%m-%d'), events))
    
    # List users
    users = list(database.users.find({}))

    return {'events': events, 'users': users}
