class Email:
    def __init__(self, sender, receiver, content, is_sent=False):
        self.sender = sender
        self.receiver = receiver
        self.content = content
        self.is_sent = is_sent

    def send(self):
        self.is_sent = True

    def get_info(self):
        return f"{self.sender} says to {self.receiver}: {self.content}. Sent: {self.is_sent}"


class MailBox:
    def __init__(self):
        self.emails = []

    def add_emails(self, email):
        self.emails.append(email)

    def send_emails(self, emails_indices):
        for i in emails_indices:
            self.emails[i].send()

    def print_mailbox(self):
        for email in self.emails:
            print(email.get_info())


mail_box = MailBox()

while True:
    commands = input()
    if commands == "Stop":
        break
    sender, receiver, content = commands.split()
    email = Email(sender, receiver, content)
    mail_box.add_emails(email)

emails_to_send = [int(i) for i in input().split(", ")]
mail_box.send_emails(emails_to_send)
mail_box.print_mailbox()
