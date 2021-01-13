class Party:
    def __init__(self):
        self.people = []

    def invite(self, name):
        self.people.append(name)

    def invited_names(self):
        return ", ".join(name for name in self.people)

    def qty_guests(self):
        return len(self.people)


party = Party()


while True:
    guests_name = input()
    if guests_name == "End":
        break
    party.invite(guests_name)


print(f"Going: {party.invited_names()}")
print(f"Total: {party.qty_guests()}")
