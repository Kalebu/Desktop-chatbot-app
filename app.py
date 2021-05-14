import json
from difflib import get_close_matches
from tkinter import Tk, Entry, Button, Text, Scrollbar


class Chatbot:
    def __init__(self, window):
        window.title('Iris Assitant')
        window.geometry('405x400')
        window.resizable(0, 0)
        self.message_session = Text(window, bd=3, relief="flat", font=(
            "Times", 10), undo=True, wrap="word")
        self.message_session.config(
            width=45, height=15, bg="#596", fg="white", state='disabled')
        self.overscroll = Scrollbar(window, command=self.message_session.yview)
        self.overscroll.config(width=20)
        self.message_session["yscrollcommand"] = self.overscroll.set
        self.message_position = 1.5
        self.send_button = Button(window, text='send', fg='white', bg='blue', width=9, font=(
            'Times', 12), relief='flat', command=self.reply_to_you)
        self.Message_Entry = Entry(window, width=40, font=('Times', 12))
        self.Message_Entry.bind('<Return>', self.reply_to_you)
        self.message_session.place(x=20, y=20)
        self.overscroll.place(x=370, y=50)
        self.send_button.place(x=0, y=360)
        self.Message_Entry.place(x=135, y=365)
        self.Brain = json.load(open('knowledge.json'))

    def add_chat(self, message):
        self.message_position += 1.5
        print(self.message_position)
        self.Message_Entry.delete(0, 'end')
        self.message_session.config(state='normal')
        self.message_session.insert(self.message_position, message)
        self.message_session.see('end')
        self.message_session.config(state='disabled')

    def reply_to_you(self, event=None):
        message = self.Message_Entry.get().lower()
        message = 'you: ' + message+'\n'
        close_match = get_close_matches(message, self.Brain.keys())
        if close_match:
            reply = 'Iris: ' + self.Brain[close_match[0]][0] + '\n'
        else:
            reply = 'Iris: ' + 'Cant it in my knowledge base\n'
        self.add_chat(message)
        self.add_chat(reply)


root = Tk()
Chatbot(root)
root.mainloop()
