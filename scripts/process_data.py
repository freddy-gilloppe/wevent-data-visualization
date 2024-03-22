

def process_data(data: dict) -> dict:
    top_categories: dict = {}
    coordinates: list = []
    mean_number_of_participants: int = 0
    mean_price: int = 0
    number_of_free_events: int = 0
    mean_price_without_free: int = 0

    events: list[dict] = data['events']
    users: list[dict] = data['users']

    events = addParticipants(users, events)

    for event in events:
        if event['category'] in top_categories:
            top_categories[event['category']] += 1
        else:
            top_categories[event['category']] = 1
            
        try:
            mean_number_of_participants += len(event['participants'])
        except:
            mean_number_of_participants += 0

        try:
            mean_price += event['price']
        except:
            mean_price += 0

        if event['price'] != 0:
            mean_price_without_free += event['price']
        else:
            number_of_free_events += 1
        
        if event['latitude'] == 0 and event['longitude'] == 0 and event['category'] == 'Online': continue
        coordinates.append([event['latitude'], event['longitude']])

    top_categories = sorted(top_categories.items(), key=lambda x: x[1], reverse=True)
    top_categories = dict(top_categories[:5])

    mean_number_of_participants /= len(events) if len(events) > 0 else 1
    mean_price /= len(events) if len(events) > 0 else 1
    mean_price_without_free /= (len(events) if len(events) > 0 else 1) - number_of_free_events        

    onlineUsers: int = len(list(filter(lambda user: user['onlineStatus'], users)))

    process_data = {
        'top_categories': top_categories,
        'number_of_events': len(events),
        'mean_number_of_participants': mean_number_of_participants,
        'mean_price': mean_price,
        'number_of_free_events': number_of_free_events,
        'mean_price_without_free': mean_price_without_free,
        'onlineUsers': onlineUsers,
        'coordinates': coordinates,
    }

    return process_data

def addParticipants(users, events):
    temp: dict = {}
    for user in users:
        for userEvent in user['eventParticipationsList']:
            if userEvent not in temp:
                temp[userEvent] = [user['_id']]
            else:
                temp[userEvent].append(user['_id'])
    for event in events:
        event['participants'] = temp.get(event['_id'], [])
    return events
