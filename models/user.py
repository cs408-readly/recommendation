import numpy as np
from bson.objectid import ObjectId

class User:

    def __init__(self, database):

        self.user = database.db.users

    def get_preferences(self, user_id=None):

        if user_id is None:

            data = []

            cur = self.user.find({})
            for doc in cur:

                try:
                    items = [(item, doc['local']['sources'][item]) for item in doc['local']['sources']]
                    sorted_items = sorted(items, key=lambda x: x[0])

                    counts = [item[1] for item in sorted_items]
                    data.append(counts)
                except KeyError:
                    print(doc)

            return np.array(data)

        else:

            user = self.user.find_one({ '_id': ObjectId(user_id) })
            print(user)

            items = [(item, user['local']['sources'][item]) for item in user['local']['sources']]
            sorted_items = sorted(items, key=lambda x: x[0])

            counts = [item[1] for item in sorted_items]

            find_dict = { i:source for i, source in enumerate(sorted(user['local']['sources']))}

            return np.array(counts), find_dict
