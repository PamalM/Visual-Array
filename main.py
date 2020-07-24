import tkinter as tk
import numpy as np


# Class represents a numpy array being visualized through a tkinter window.
class VisualArray:

    # Constructor.
    def __init__(self):

        # Check to see if the entered dimension is a valid entry.
        def valid_Dimension():
            dimension = int(dimEntry.get())
            try:
                if dimension >= 1 and dimension <= 3:
                    VisualArray.display(dimension)

                else:
                    master = tk.Tk()

                    master.resizable(False, False)
                    master.mainloop()

            except ValueError as VE:
                print('Entered non int.')

        # Initiate object attributes.
        # Number of dimensions for user's array. Allowable values (1-3).
        self.numDimensions = 0

        # Background color for window and widgets.
        bgColor = 'indianred3'

        # Create tkinter window object.
        root = tk.Tk()

        # Frame holding text above entry bar.
        frame = tk.Frame(root)
        label1 = tk.Label(frame, text='Enter number of dimensions:', font=('Helvetica 40 bold'), bg=bgColor, fg='white')
        label1.pack()
        label2 = tk.Label(frame, text='Please select between 1 to 3 dimensions.', bg=bgColor, fg='lightcyan',
                          font=('Helvetica 12 bold'))
        label2.pack(padx=90)
        frame.configure(bg=bgColor)
        frame.pack(pady=(40, 20), fill=tk.X)

        # Entry to hold the number of dimensions from user.
        dim = tk.StringVar()
        dimEntry = tk.Entry(root, font=('Helvetica', 90, 'bold'), justify='center', textvariable=dim)
        dimEntry.pack(fill=tk.X)

        # Button to direct user to next GUI.
        nextButton = tk.Button(root, text='NEXT', font='Helvetica 60 bold', command=lambda: valid_Dimension())
        nextButton.pack(fill=tk.X, padx=20, pady=25)

        # Window attributes.
        root.title('Visual Array')
        root.configure(bg=bgColor)
        root.minsize(600, 400)
        root.mainloop()

    def display(numDim):
        print(numDim)


# Run Program.
if __name__ == '__main__':
    visualArray = VisualArray()

