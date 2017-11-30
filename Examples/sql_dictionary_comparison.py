class UserTable:
    def __init__(self):
        self.id = [0]
        self.name = [0]
        self.height = [0]
        self.weight = [0]

    def _find_index(self, user_id):
        try:
            index = self.id.index(user_id)
        except ValueError:
            return self.id[-1] + 1
        return index

    def update_or_add_user(self, user_data):
        user_index = self._find_index(user_data["id"])
        new_user = False

        try:
            self.id[user_index]
        except IndexError:
            new_user = True

        for field in user_data.keys():
            if new_user:
                getattr(self, field).append(user_data[field])
            else:
                getattr(self, field)[user_index] = user_data[field]

        new_user_output = "Added user {user_name}\nUser ID: {user_id}".format(user_name = user_data["name"], user_id = user_index)
        update_user_output = "Updated user {user_name}".format(user_name = user_data["name"])
        print(new_user_output if new_user else update_user_output)
        
        return new_user

    def get_user_data(self, user_id, requested_data = None):
        output = {}
        try:
            self.id[user_id]
        except IndexError:
            return "User not found"
        
        data_to_get = requested_data if requested_data else vars(self).keys()
        for field in data_to_get:
            output[field] = getattr(self, field)[user_id]

        return output

