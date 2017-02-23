import numpy as np

class User:

    def __init__(self, database):

        self.user = database.db.users

    def get_preferences(self, user_id=None):

        if user_id is None:

            data = []

            cur = self.user.find()
            for doc in cur:

                counts = [item['count'] for item in doc['sources']]
                data.append(counts)

            return np.array(data)


        else:

            user = self.user.find_one({ '_id': user_id })
            data = np.array(user.sources)

            return data
