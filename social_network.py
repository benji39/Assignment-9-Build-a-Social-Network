class Person:
    '''A person in the social network with a name and a list of friends.'''

    def __init__(self, name):
        self.name = name
        self.friends = []

    def add_friend(self, friend):
        # Avoid adding the same friendship more than once.
        if friend not in self.friends:
            self.friends.append(friend)


class SocialNetwork:
    '''A social network represented with adjacency lists.'''

    def __init__(self):
        self.people = {}

    def add_person(self, name):
        if name not in self.people:
            self.people[name] = Person(name)
        else:
            print(f"{name} is already in the network!")

    def add_friendship(self, person1_name, person2_name):
        if person1_name not in self.people:
            print(f"Friendship not created. {person1_name} doesn't exist!")
            return
        if person2_name not in self.people:
            print(f"Friendship not created. {person2_name} doesn't exist!")
            return
        if person1_name == person2_name:
            print("Friendship not created. A person cannot friend themselves!")
            return

        person1 = self.people[person1_name]
        person2 = self.people[person2_name]
        person1.add_friend(person2)
        person2.add_friend(person1)

    def print_network(self):
        for name, person in self.people.items():
            friend_names = [friend.name for friend in person.friends]
            print(f"{name} is friends with: {', '.join(friend_names)}")


# Test your code here
if __name__ == "__main__":
    network = SocialNetwork()

    # Add six people.
    for name in ["Alex", "Jordan", "Morgan", "Taylor", "Casey", "Riley"]:
        network.add_person(name)

    # Add eight bidirectional friendships.
    network.add_friendship("Alex", "Jordan")
    network.add_friendship("Alex", "Morgan")
    network.add_friendship("Jordan", "Taylor")
    network.add_friendship("Morgan", "Casey")
    network.add_friendship("Taylor", "Riley")
    network.add_friendship("Casey", "Riley")
    network.add_friendship("Morgan", "Riley")
    network.add_friendship("Alex", "Taylor")

    # Edge cases: missing person, duplicate person, duplicate friendship.
    network.add_friendship("Jordan", "Johnny")
    network.add_person("Alex")
    network.add_friendship("Alex", "Jordan")

    print("\nSocial Network:")
    network.print_network()
