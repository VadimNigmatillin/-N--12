class Message:
    def __init__(self, username, email, subject, message, file_path=None):
        self.username = username
        self.email = email
        self.subject = subject
        self.message = message
        self.file_path = file_path

    
message1 = Message(
    username = "Vadim",
    email = "vadim@mail.ru",
    subject = "Testing Message",
    message = "This is a test message.",
    file_path = "C:\\Windows\\System32\\notepad.exe"
)