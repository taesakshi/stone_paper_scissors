#Stone Paper Scissor

import random
import tkinter as tk

class StonePaperScissor:
    def __init__(self):
        self.GAME_FOLDER = 'D:/batches/Python_1/stone_paper_scissor/'
        #Create a window and set primary attributes
        self.window = tk.Tk()
        self.window.title('Stone Paper Scissor')
        self.window.geometry('400x500') #'wxh'
        self.window.resizable(False,False)
        self.window.iconbitmap(self.GAME_FOLDER + 'game_icon.ico')

        #image list
        self.images = [
            tk.PhotoImage(file= self.GAME_FOLDER + 'stone.png'),
            tk.PhotoImage(file=self.GAME_FOLDER + 'paper.png'),
            tk.PhotoImage(file=self.GAME_FOLDER + 'scissor.png'),
        ]

        #Frames for players and play area
        frame_computer = tk.Frame(master=self.window, bg='#FFAEC9', height=100)
        frame_play_area = tk.Frame(master=self.window, bg='#FFF200', height=300)
        frame_player = tk.Frame(master=self.window, bg='#99D9EA', height=100)

        #widgets for super computer
        lbl_sc_title = tk.Label(master=frame_computer, text = 'Super Computer : ', bg = frame_computer['bg'])
        lbl_sc_score = tk.Label(master=frame_computer, text='0', bg=frame_computer['bg'])
        lbl_sc_stone = tk.Label(master=frame_computer, image= self.images[0], bg= frame_computer['bg'] )
        lbl_sc_paper = tk.Label(master=frame_computer, image=self.images[1], bg=frame_computer['bg'])
        lbl_sc_scissor = tk.Label(master=frame_computer, image=self.images[2], bg=frame_computer['bg'])

        #widgets for master player
        lbl_mp_title = tk.Label(master=frame_player, text='Master Player : ', bg=frame_player['bg'])
        lbl_mp_score = tk.Label(master=frame_player, text='0', bg=frame_player['bg'])
        bttn_mp_stone = tk.Button(master=frame_player, image=self.images[0], bg=frame_player['bg'], command=self.fx1)
        bttn_mp_paper = tk.Button(master=frame_player, image=self.images[1], bg=frame_player['bg'], command=self.fx2)
        bttn_mp_scissor = tk.Button(master=frame_player, image=self.images[2], bg=frame_player['bg'], command=self.fx3)

        #Add the frames to the window
        frame_computer.pack(expand=True, fill=tk.X)
        frame_play_area.pack(expand=True, fill=tk.X)
        frame_player.pack(expand=True, fill=tk.X)

        #Add the widgets to the containers (frame/window)
        lbl_sc_title.grid(row= 0, column =0)
        lbl_sc_score.grid(row=0, column= 1)
        lbl_sc_stone.grid(row=1, column=0, padx=25)
        lbl_sc_paper.grid(row=1, column=1, padx=25)
        lbl_sc_scissor.grid(row=1, column=2, padx=25)

        bttn_mp_stone.grid(row=0, column=0, padx=25)
        bttn_mp_paper.grid(row=0, column=1, padx=25)
        bttn_mp_scissor.grid(row=0, column=2, padx=25)
        lbl_mp_title.grid(row= 1, column =0)
        lbl_mp_score.grid(row=1, column= 1)

        #window mainloop keeps the window alive and listening-responding to events.
        self.window.mainloop()


    def computer_plays(self):
        ch = random.choice([0,1,2])


    def fx1(self):
        print('player throws stone')

    def fx2(self):
        print('player throws paper')

    def fx3(self):
        print('player throws scissor')

def main():
    sps = StonePaperScissor()

main()