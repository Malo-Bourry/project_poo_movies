class Network:
    def __init__(self, list_of_friend=[]):
        self.list_of_friends = list_of_friend
    
    def add_friend_to_network(self, friend):
        self.list_of_friends.append(friend)

    def display_list_of_friends(self):
        for friend in self.list_of_friends:
            print(friend.name)