import tkinter as tk
import numpy as np


# Class represents a numpy array being visualized through a tkinter window.
class VisualArray:

    # Constructor; Prompts user for the # of dimensions for array.
    def __init__(self):

        # Numpy array attributes.
        self.dataType = None
        self.numDimensions = None
        self.array = []

        self.beta = []

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

        # Beta window displays the list's contents and buttons to respective methods that can be performed on array.
        self.beta = tk.Tk()

        # Method destroys current GUI and restarts application.
        def restart():
            self.beta.destroy()
            self.beta.quit()
            self.__init__()

        # Frame to listbox containing array elements.
        arrayFrame = tk.Frame(self.beta, bg='indianred')

        label1 = tk.Label(arrayFrame, text='Array Contents:', fg='white', bg='black', font='Helvetica 24 bold')
        label1.pack(fill=tk.X, pady=(10,30))

        # Listbox to hold the contents of the array.
        listBox = tk.Listbox(arrayFrame, justify='center', font='TIMES 26 bold', width=20, height=10,
                             selectborderwidth=1, bg='lavenderblush', relief='sunken', selectbackground='oldlace')

        for key in self.array:
            listBox.insert(tk.END, key)

        listBox.pack(side=tk.RIGHT)

        # If the content of the array exceeds 11, then insert a scroll bar left of the listbox.
        if listBox.size() >= 11:
            # Add scrollbar to listbox.
            scrollbar = tk.Scrollbar(arrayFrame, orient="vertical", command=listBox.yview)
            scrollbar.pack(side=tk.LEFT, fill=tk.Y)
            listBox.config(yscrollcommand=scrollbar.set)

        arrayFrame.grid(row=0, column=0)
        self.beta.columnconfigure(0, weight=1)
        self.beta.rowconfigure(0, weight=1)

        # Frame containing buttons with methods to perform on the given array.
        methodFrame = tk.Frame(self.beta, bg='indianred')

        label3 = tk.Label(methodFrame, text='Array Methods:', fg='white', bg='black', font='Helvetica 24 bold')
        label3.pack(fill=tk.X, pady=10)

        insertButton = tk.Button(methodFrame, text='INSERT', font='HELVETICA 30 bold', width=20, command=lambda: self.insert())
        insertButton.pack(fill=tk.X, pady=10)

        deleteButton = tk.Button(methodFrame, text='DELETE', font='HELVETICA 30 bold', width=20)
        deleteButton.pack(fill=tk.X, pady=10)

        searchButton = tk.Button(methodFrame, text='SEARCH', font='HELVETICA 30 bold', width=20)
        searchButton.pack(fill=tk.X, pady=10)

        splitButton = tk.Button(methodFrame, text='SPLIT', font='HELVETICA 30 bold', width=20)
        splitButton.pack(fill=tk.X, pady=10)

        sortButton = tk.Button(methodFrame, text='SORT', font='HELVETICA 30 bold', width=20)
        sortButton.pack(fill=tk.X, pady=10)

        filterButton = tk.Button(methodFrame, text='FILTER', font='HELVETICA 30 bold', width=20)
        filterButton.pack(fill=tk.X, pady=10)

        methodFrame.grid(row=0, column=1)
        self.beta.columnconfigure(1, weight=1)
        self.beta.rowconfigure(1, weight=1)

        label4 = tk.Label(self.beta, text='Number of Dimensions: ' + str(self.get_NumDimensions()) + '\nType: ' +
                          str(self.get_DataType()) + '\n[' + str(listBox.size()) + '] elements.', bg='indianred',
                          font='HELVETICA 18')
        label4.grid(row=1, column=0)

        newArrayButton = tk.Button(self.beta, text='NEW ARRAY', font='HELVETICA 30 bold', width=20,
                                   command=lambda: restart())
        newArrayButton.grid(row=1, column=1)

        # Beta window attributes.
        self.beta.config(bg='indianred')
        self.beta.title('Visual Array Hub')
        self.beta.geometry('875x525')
        self.beta.minsize(875, 525)
        self.beta.mainloop()

    # Method inserts element at given location in array.
    def insert(self):

        def add():
            self.array.insert(int(indexEntry.get()), elementEntry.get())
            print('Inserted [' + str(elementEntry.get()) + '] @ Index ' + str(indexEntry.get()))
            charlie.destroy()
            charlie.quit()
            self.beta.destroy()
            self.beta.quit()
            self.arrayHub()


        charlie = tk.Tk()

        label1 = tk.Label(charlie, text='Insert Element:', bg='gray28', fg='white', font='HELVETICA 20 bold')
        label1.pack(fill=tk.X, padx=20, pady=20)

        # String variables to hold given array and element entered by user.
        element = tk.StringVar()
        index = tk.StringVar()

        elementEntry = tk.Entry(charlie, font='HELVETICA 24 bold', justify='center', textvariable=element)
        elementEntry.pack(fill=tk.X, padx=20)

        label2 = tk.Label(charlie, text='@ Index: ', bg='gray28', fg='white', font='HELVETICA 20 bold',
                          textvariable=index)
        label2.pack(fill=tk.X, padx=20, pady=20)

        indexEntry = tk.Entry(charlie, font='HELVETICA 24 bold', justify='center')
        indexEntry.pack(fill=tk.X, padx=20)

        insertButton = tk.Button(charlie, text='INSERT', font='HELVETICA 24 bold', command=lambda: add())
        insertButton.pack(fill=tk.X, padx=20, pady=20)

        charlie.geometry('400x300')
        charlie.title('INSERT:')
        charlie.config(bg='indianred')
        charlie.minsize(400, 300)
        charlie.mainloop()

    # Getter methods.
    def get_NumDimensions(self):
        return self.numDimensions

    def get_DataType(self):
        return self.dataType

    def get_Array(self):
        return self.array

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
