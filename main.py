import tkinter as tk
import numpy as np


# Class represents a numpy array being visualized through a tkinter window.
class VisualArray:

    # Constructor.
    def __init__(self):

        # Check to see if the entered dimension is a valid entry.
        def valid_Dimension():
            try:
                dimension = int(dimEntry.get())
                
                if dimension >= 1 and dimension <= 3:
                    # Proceed user to next GUI. 
                    VisualArray.display(dimension)

                else:
                    # Direct user to notice window below.
                    raise ValueError

            except ValueError as VE:

                def keyBind(event):
                    master.destroy()
                
                # Otherwise, display notice window to user. 
                master = tk.Tk()

                label1 = tk.Label(master, text='Invalid Dimension Selected!', font='HELVETICA 26 bold', bg='gray20', fg='white')
                label1.pack(fill=tk.X, pady=20, padx=20)

                label2 = tk.Label(master, text='Please select a dimension between 1 and 3.', font='HELVETICA 18', bg='salmon', fg='white')
                label2.pack()

                label3 = tk.Label(master, text='You have entered: ' + dimEntry.get(), bg='gray20', fg='white', font='HELVETICA 14 italic')
                label3.pack(pady=20)

                closeButton = tk.Button(master, text='CLOSE', font='HELVETICA 24 bold', command=lambda:master.destroy())
                closeButton.pack(fill = tk.X, padx=10, pady=10)
                    
                master.configure(bg='salmon')
                master.geometry('400x250')
                master.resizable(False, False)
                master.bind('<Return>', keyBind)
                master.title('Notice!')
                master.mainloop()
                

        # Initiate object attributes.
        # Number of dimensions for user's array. Allowable values (1-3).
        self.numDimensions = 0

        def keyBind(event):
            valid_Dimension()

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
        root.bind("<Return>", keyBind)
        root.mainloop()

    def display(numDim):
        print(numDim)


# Run Program.
if __name__ == '__main__':
    visualArray = VisualArray()

