import tkinter as tk
import random

class game:
    def __init__(self,master):
        self.master = master
        self.master.title("number guess game")
        
        self.target_number = random.randint(1, 100)
        self.guess_count = 0

        self.label = tk.Label(master,
                             text="enter a number between 1 to 100:",    
                             font=("Arial",20))
        self.label.pack(pady=20)

        self.entry = tk.Entry(master,font=("Arial", 20))
        self.entry.pack(pady=5)

        self.submit_button = tk.Button(master,
                                       text="i answered",
                                       command=self.check_guess,
                                       font=("Arial" , 20),
                                       bg="red")
        self.submit_button.pack(pady=10)


        self.result_label = tk.Label(master, text="", font=("Arial", 20))
        self.result_label.pack(pady=10)  

    def check_guess(self):
        try:
            guess = int(self.entry.get())
            self.guess_count +=1
            if guess < 1 or guess > 100:
                self.result_label.config(text="enter a number between 1 to 100",
                    font=("Arial", 20))
            elif guess < self.target_number:
                self.result_label.config(
                    text="your number is too small",
                    font=("Arial", 20))
            elif guess > self.target_number:
                self.result_label.config(
                    text="number is big try again",
                    font=("Arial", 20))    
            else:
                self.result_label.config(text=f"great you answerd correct you answerd for{self.guess_count} times")

        except ValueError:
            self.result_label.config(text="enter number")
root = tk.Tk()
root.geometry("700x600")
game = game(root)
root.mainloop()
