import tkinter as tk
import numpy as np


# Class represents a numpy array being visualized through a tkinter window.
class VisualArray:

    # Constructor; Prompts user for the # of dimensions for array.
    def __init__(self):

        # Numpy array attributes.
        self.dataType = None
        self.numDimensions = None

        # Check to see if user dimension entry is valid.
        def valid_Dimension():
            try:
                # Attempt to convert given dimension to int, if error than display notice window. 
                dimension = int(dimEntry.get())
                
                if 1 <= dimension <= 3:
                    # Proceed user to next GUI, to receive the data type for the array.
                    self.set_NumDimensions(dimension)
                    # Destroy the current GUI.
                    root.destroy()
                    root.quit()

                    # Proceed to next GUI.
                    self.prompt_DataType()

                else:
                    # Direct user to notice window below.
                    # The entry was a valid int, but not within the range (1-3).
                    raise ValueError

            except ValueError as VE:

                # Method binds <Return> key press to close master window.
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

        # Method binds the <Return> key press same command as nextButton.
        def keyBind2(event):
            valid_Dimension()

        # Background color for window and widgets.
        bgColor = 'indianred3'

        # Create tkinter window object.
        root = tk.Tk()

        # Frame holding text above entry bar.
        frame = tk.Frame(root, bg=bgColor).pack(pady=(40, 20), fill=tk.X)
        label1 = tk.Label(frame, text='Enter number of dimensions:', font='Helvetica 40 bold', bg=bgColor, fg='white')
        label1.pack()
        label2 = tk.Label(frame, text='Please select between 1 to 3 dimensions.', bg=bgColor, fg='lightcyan',
                          font='Helvetica 12 bold').pack(padx=90)

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
        root.bind("<Return>", keyBind2)
        root.mainloop()

    # Method prompts user for the data type for their specified array. 
    def prompt_DataType(self):

        # Method fetches the selected data type from the listbox. 
        def selected_DataType():
            self.set_DataType(listBox.get(listBox.curselection()))
            alpha.destroy()
            alpha.quit()
            self.arrayHub()
        
        # Bind the <Return> key to the button press command.
        def keyBind(event):
            selected_DataType()
        
        # Background color for window and widgets.
        bgColor = 'indianred3'

        # Create tkinter window object.
        alpha = tk.Tk()

        # Frame holding text above entry bar.
        frame = tk.Frame(alpha, bg=bgColor)
        label1 = tk.Label(frame, text='Select datatype:', font='Helvetica 40 bold', bg=bgColor, fg='white').pack()

        # Present user with list of options of datatypes to select from.
        listBox = tk.Listbox(frame, justify='center', cursor='dot', bg='mintcream', fg='lightslateblue',
                             font='HELVETICA 20 bold', selectbackground='oldlace', relief='raised',
                             selectmode='single', height=4)
        listBox.insert(1, 'Integer')
        listBox.insert(2, 'Boolean')
        listBox.insert(3, 'Float')
        listBox.insert(4, 'String')
        listBox.select_set(0)
        listBox.pack(fill=tk.BOTH, pady=10)
        frame.pack(pady=(40, 20), fill=tk.X)

        # Button to direct user to next GUI.
        nextButton = tk.Button(alpha, text='NEXT', font='Helvetica 60 bold', command=lambda: selected_DataType())
        nextButton.pack(fill=tk.X, padx=20, pady=10)

        # Alpha window attributes.
        alpha.title('Visual Array')
        alpha.configure(bg=bgColor)
        alpha.minsize(600, 375)
        alpha.bind("<Return>", keyBind)
        alpha.mainloop()

    # Method displays the array alongside the methods and tasks that can be performed on the array. 
    def arrayHub(self):
        print('Array # Dimensions: ' + str(self.get_NumDimensions()))
        print('Array Data Type: ' + self.get_DataType())

        # Beta window displays the list's contents and buttons to respective methods that can be performed on array.
        beta = tk.Tk()
        beta.title('Visual Array Hub')
        beta.geometry('875x525')
        beta.mainloop()

    # Getter methods.
    def get_NumDimensions(self):
        return self.numDimensions

    def get_DataType(self):
        return self.dataType

    # Setter methods.
    def set_NumDimensions(self, val):
        self.numDimensions = val

    def set_DataType(self, val):
        self.dataType = val


# Execute program. 
if __name__ == '__main__':
    visualArray = VisualArray()
    # For testing purposes.
    visualArray.set_DataType('Integer')
    visualArray.set_NumDimensions(1)
    visualArray.arrayHub()
