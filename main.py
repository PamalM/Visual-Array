# Visual Array Project by Pamal Mangat.
# (Please see GitHub readme file for project description)

"""
Basic Run-down of the program:
1] Initiate a Visual Array (VA) object by passing a (tk.Tk()) tkinter window object into it's constructor (__init())
2] User is prompted for the #dimensions for the array through a prompt window; (This is all completed within the __init__())
3] User is then prompted for #Elements per dimension, via prompt_ArrayShape().
4] Afterwards, the user is prompted for the data type for the array, via prompt_DataType().
5] Finally, user is directed to the arrayHub() window that contains all the respective methods that can be performed on the array.
6] Depending on the method selected, the arrayHub will display a respective window for each method.
"""


# Class is utilized to provide typography and color attributes to console messages.
class Console:
    purple = '\033[95m'
    cyan = '\033[96m'
    darkCyan = '\033[36m'
    brightBlue = '\u001b[34;1m'
    blue = '\033[94m'
    green = '\033[92m'
    yellow = '\033[93m'
    red = '\033[91m'
    magenta = '\u001b[35m'
    bgBlue = '\u001b[44m'
    bold = '\033[1m'
    underline = '\033[4m'
    end = '\033[0m'

# Try-Catch to ensure the user has the necessary libraries to execute this program.
try:
    print(Console.yellow + Console.bold + '\n[Welcome to Visual Array]\n' + Console.end)
    print(Console.bold + Console.cyan + '---------------------------------\n' + Console.end)
    print(Console.bold + Console.underline + Console.darkCyan + '[Attempting to import required libraries:]' + Console.end)

    # Numpy library allows us to create arrays that are much more space efficient and provide for better code-optimization.
    import numpy as np
    print(Console.brightBlue + '[Numpy]...' + Console.end)

    # Tkinter library allows us to visualize the the numpy array in a Graphical-User-Interface (GUI).
    import tkinter as tk
    print(Console.brightBlue + '[Tkinter]...' + Console.end)

    # Tabulate library is utilized for the console messages and debugging messages printed by the program during execution.
    # Provides for a clean console output, and better visual appeal to the user/programmer when debugging or running the program.
    from tabulate import tabulate
    print(Console.brightBlue + '[Tabulate]...' + Console.end)

    # Os library allows us to write (.txt) files to the user's desktop on their machine.
    import os
    print(Console.brightBlue + '[OS]...' + Console.end)
    import getpass
    print(Console.brightBlue + '[GetPass]...' + Console.end)
    import platform
    print(Console.brightBlue + '[Platform]...' + Console.end)

    print(Console.green + Console.underline + Console.darkCyan + '[Imports were successful!]\n' + Console.end)

except ImportError:
    print(Console.red + '\n[ImportError: Please ensure you have the following libraries installed on your machine before attemping execution.]\n' + Console.end)
    np = None
    tk = None
    tabulate = None
    os = None
    getpass = None
    platform = None

finally:
    print(Console.bold + Console.cyan + '---------------------------------\n' + Console.end)


# Class represents a Numpy array being visualized through a Tkinter window.
# noinspection PyAttributeOutsideInit
class VisualArray:

    # Constructor; Prompts user for for number of dimensions for the array through a small prompt window.
    def __init__(self, master):
        self.array = None
        self.numDimensions = None
        self.numElements = None
        self.dataType = None
        self.shape = None

        # Transfer user to next GUI if entered dimensions is between (1-3).
        def transfer():
            try:
                self.dimension = int(self._dimEntry.get())

                if 1 <= self.dimension <= 3:
                    self.set_NumDimensions(self.dimension)
                    self.master.destroy()
                    self.master.quit()

                    # Transfer user to next GUI using a transfer root link window.
                    root = tk.Tk()
                    self.prompt_ArrayShape(root)
                    root.mainloop()

                # Otherwise, entered dimension isn't the range of (1-3).
                else:
                    raise ValueError

            # Display notice window to user that explains the ValueError.
            except ValueError:
                self._noticeWindow = tk.Tk()

                self._frame = tk.Frame(self._noticeWindow, relief='solid', borderwidth=4, highlightbackground='white',
                                       highlightthickness=4, highlightcolor='gray25', bg='indianred3')

                self._label = tk.Label(self._frame, text='Invalid Dimension Selected!', font='HELVETICA 22 bold', bg='gray20', fg='white').pack(fill=tk.BOTH, pady=10, padx=20)
                self._label2 = tk.Label(self._frame, text='Please select a dimension \nbetween 1 and 3.', font='HELVETICA 18', bg='indianred3', fg='white').pack(pady=10, padx=20)
                self._label3 = tk.Label(self._frame, text='You have entered: ' + self._dimEntry.get(), bg='gray20', fg='white', font='HELVETICA 14 italic').pack(pady=10, padx=20)

                # Button to close notice Window.
                self._buttonFrame = tk.Frame(self._noticeWindow, relief='solid', borderwidth=4, highlightbackground='gray25', highlightthickness=4, highlightcolor='white')
                self._closeButton = tk.Button(self._buttonFrame, text='CLOSE', font='HELVETICA 24 bold', command=lambda: self._noticeWindow.destroy())
                self._closeButton.pack(fill=tk.BOTH, expand=True)

                self._frame.pack(expand=True, fill=tk.BOTH, padx=14, pady=4)
                self._buttonFrame.pack(fill=tk.BOTH, padx=10, pady=(0, 4), expand=True)

                # Notice window attributes.
                self._noticeWindow.configure(bg='gray25')
                self._noticeWindow.geometry('400x250')
                self._noticeWindow.resizable(False, False)
                self._noticeWindow.bind('<Return>', lambda cmd: self._noticeWindow.destroy())
                self._noticeWindow.title('Notice!')
                self._noticeWindow.mainloop()

        self.master = master

        self._frame = tk.Frame(self.master, bg='indianred3', relief='solid', borderwidth=4, highlightbackground='white', highlightthickness=4, highlightcolor='gray25')
        self._frame.grid_columnconfigure(0, weight=1)
        self._frame.grid_rowconfigure(0, weight=1)
        self._frame.grid_rowconfigure(1, weight=1)
        self._frame.grid_rowconfigure(2, weight=1)
        self._frame.grid_rowconfigure(3, weight=1)

        self._label1 = tk.Label(self._frame, text='Enter number of dimensions:', font='Helvetica 36 bold', bg='indianred3', fg='white', relief=tk.FLAT)
        self._label1.grid(row=0, column=0, sticky='nsew', padx=10, pady=10)

        # Dimension entry to hold the number of dimensions from user.
        self._dimEntry = tk.Entry(self._frame, font=('Helvetica', 90, 'bold'), justify='center', textvariable=tk.StringVar(), relief='solid', borderwidth=4)
        self._dimEntry.grid(row=1, column=0, sticky='nsew', padx=20, pady=10)

        # Set the focus of the window to the entry bar.
        self._dimEntry.focus()

        self._label2 = tk.Label(self._frame, text='(Please select between 1 to 3 dimensions.)', bg='indianred3', fg='lightcyan', font='Helvetica 12 bold', relief=tk.FLAT)
        self._label2.grid(row=2, column=0, sticky='nsew', padx=20, pady=10)

        # Button to direct user to next GUI.
        self._buttonFrame = tk.Frame(self.master, relief='solid', borderwidth=4, highlightbackground='gray25', highlightthickness=4, highlightcolor='white')
        self._nextButton = tk.Button(self._buttonFrame, text='NEXT', font='Helvetica 60 bold', command=lambda: transfer())
        self._nextButton.pack(fill=tk.BOTH)

        self._frame.pack(fill=tk.BOTH, padx=14, pady=14, expand=True)
        self._buttonFrame.pack(fill=tk.BOTH, padx=14, pady=(0, 14))

        # Window attributes.
        self.master.title('Visual Array')
        self.master.configure(bg='gray25')
        self.master.geometry('600x400')
        self.master.minsize(600, 400)
        self.master.bind("<Return>", lambda cmd: transfer())
        self.master.mainloop()

    # Prompts user for the Array Shape.
    def prompt_ArrayShape(self, master):

        def transfer():
            self.set_NumElements(self._shapeScale.get())
            self.master.destroy()
            self.master.quit()
            root = tk.Tk()
            self.prompt_DataType(root)
            root.mainloop()

        self.master = master
        self._frame = tk.Frame(self.master, bg='indianred3', relief='solid', borderwidth=4, highlightbackground='white', highlightthickness=4, highlightcolor='gray25')

        self._label1 = tk.Label(self._frame, text='SELECT THE NUMBER OF ELEMENTS PER DIMENSION:', font='HELVETICA 20 bold', bg='salmon', fg='white', relief=tk.FLAT)
        self._label1.pack(expand=True, fill=tk.BOTH, padx=10, pady=10)

        # Scale to get user input for the numbers of elements per dimension.
        self._shapeScale = tk.Scale(self._frame, from_=1, to=10, orient=tk.HORIZONTAL, activebackground='yellow', tickinterval=9, relief=tk.RAISED)
        self._shapeScale.config(background='gray20', fg='white', font='HELVETICA 24 bold', sliderlength=100, sliderrelief=tk.GROOVE)
        self._shapeScale.pack(expand=True, fill=tk.X, padx=10, pady=10)
        self._shapeScale.focus()

        # Button to direct user to next GUI.
        self._buttonFrame = tk.Frame(self.master, relief='solid', borderwidth=4, highlightbackground='gray25', highlightthickness=4, highlightcolor='white')
        self._nextButton = tk.Button(self._buttonFrame, text='NEXT', font='Helvetica 60 bold', command=lambda: transfer())
        self._nextButton.pack(fill=tk.BOTH)

        self._frame.pack(fill=tk.BOTH, padx=14, pady=14, expand=True)
        self._buttonFrame.pack(fill=tk.BOTH, padx=14, pady=(0, 14))

        # Window attributes.
        self.master.title('Visual Array')
        self.master.configure(bg='gray25')
        self.master.geometry('600x300')
        self.master.minsize(600, 300)
        self.master.bind("<Return>", lambda cmd: transfer())
        master.mainloop()

    # Prompts user for the Data Type for array.
    def prompt_DataType(self, master):

        # Method transfers user and initializes the array with the attributes specified, before entering the arrayHub.
        def transfer():
            self.set_DataType(self._listBox.get(self._listBox.curselection()))
            self.master.destroy()
            self.master.quit()

            if self.get_DataType() == 'Integer':
                self.array = np.zeros(shape=(int(self.get_NumDimensions()), int(self.get_NumElements())), dtype='i')
            elif self.get_DataType() == 'Float':
                self.array = np.zeros(shape=(int(self.get_NumDimensions()), int(self.get_NumElements())), dtype='float')
            elif self.get_DataType() == 'Boolean':
                self.array = np.ones((int(self.get_NumDimensions()), int(self.get_NumElements())), dtype=np.bool)
            elif self.get_DataType() == 'String':
                self.array = np.empty([int(self.get_NumDimensions()), int(self.get_NumElements())], dtype="<U20")

                # Added in quotation marks around empty strings, to prevent blank list boxes when String data type is selected.
                # (Done so, for visual appeal.)
                self._x = 0
                while self._x < self.get_NumElements():
                    self.array[0][self._x] = "''"
                    if self.get_NumDimensions() == 2:
                        self.array[1][self._x] = "''"
                    elif self.get_NumDimensions() == 3:
                        self.array[1][self._x] = "''"
                        self.array[2][self._x] = "''"
                    self._x += 1

            # Log into the console the array's contents; For testing/debugging purposes.
            print(Console.blue + Console.bold + 'New array initialized with attributes:' + Console.end + Console.magenta + Console.bold)
            print(tabulate([[str(self.get_NumDimensions()), str(self.get_NumElements()), str(self.get_DataType())]],
                           headers=['Dimensions', 'Elements', 'Data Type:'],
                           tablefmt='fancy_grid') + '\n' + Console.end)

            print(Console.blue + Console.bold + 'Array Contents:' + Console.end + Console.magenta + Console.bold)
            self._temp1 = []  # Holds number of dimensions.
            self._temp2 = []  # Holds contents of each dimension.
            self._dimCount = 0
            for element in self.array:
                self._dimCount += 1
                self._temp1.insert(self._dimCount-1, 'Dimension [{0}]'.format(str(self._dimCount)))
                self._temp2.append(list(element))

            print(tabulate([self._temp2], headers=[*self._temp1], tablefmt='fancy_grid') + Console.end)
            print(Console.bold + Console.green + '-------------------------------------------------------' + Console.end)
            print(Console.yellow + Console.bold + 'Please See Array Hub window.' + Console.end)
            print(Console.bold + Console.green + '-------------------------------------------------------' + Console.end)

            # Transfer.
            root = tk.Tk()
            self.arrayHub(root)
            root.mainloop()

        self.master = master
        self._frame = tk.Frame(self.master, bg='indianred3', relief='solid', borderwidth=4, highlightbackground='white', highlightthickness=4, highlightcolor='gray25')
        self._frame.grid_columnconfigure(0, weight=1)
        self._frame.grid_rowconfigure(0, weight=1)
        self._frame.grid_rowconfigure(1, weight=1)
        self._frame.grid_rowconfigure(2, weight=1)

        self._label1 = tk.Label(self._frame, text='Select Data Type:', font='Helvetica 40 bold', bg='indianred3', fg='white')
        self._label1.grid(row=0, column=0, sticky='nsew', padx=20, pady=10)

        # Present user with list of options of data types to select from.
        self._listBox = tk.Listbox(self._frame, justify='center', cursor='dot', bg='mintcream', fg='lightslateblue', font='HELVETICA 24 bold')
        self._listBox.config(relief='solid', borderwidth=4, highlightbackground='white', highlightthickness=4, highlightcolor='gray25', selectmode='single', height=4)
        self._listBox.insert(1, 'Integer')
        self._listBox.insert(2, 'Boolean')
        self._listBox.insert(3, 'Float')
        self._listBox.insert(4, 'String')
        self._listBox.select_set(0)
        self._listBox.grid(row=1, column=0, sticky='nsew', padx=20, pady=10)
        self._listBox.focus()

        # Button to direct user to next GUI.
        self._buttonFrame = tk.Frame(self.master, relief='solid', borderwidth=4, highlightbackground='gray25', highlightthickness=4, highlightcolor='white')
        self._nextButton = tk.Button(self._buttonFrame, text='NEXT', font='Helvetica 60 bold', command=lambda: transfer())
        self._nextButton.pack(fill=tk.BOTH)

        self._frame.pack(fill=tk.BOTH, padx=14, pady=14, expand=True)
        self._buttonFrame.pack(fill=tk.BOTH, padx=14, pady=(0, 14))

        # Window attributes.
        self.master.title('Visual Array')
        self.master.configure(bg='gray25')
        self.master.minsize(600, 400)
        self.master.bind("<Return>", lambda cmd: transfer())
        self.master.mainloop()

    # Displays the array's contents and available methods.
    def arrayHub(self, master):
        # The terminal method directs the user depending on the tag specified.
        # (InsertWindow = 1, DeleteWindow = 2, SearchWindow = 3, SplitWindow = 4, SortWindow = 5, FilterWindow = 6)
        def terminal(tag):
            root = tk.Toplevel()
            if tag == 1:
                self.insert(root)
            elif tag == 2:
                self.delete(root)
            elif tag == 3:
                self.search(root)
            elif tag == 4:
                self.split_(root)
            elif tag == 5:
                self.sort_(root)
            elif tag == 6:
                self.filter_(root)
            root.mainloop()

        # Update label in arrayHub that shows the selected list element for the user.
        def updateSelection(tag):
            # Bunch of if/else statements to ensure that the address for the selectionLabel for the selected element is coming from the right listbox/dimension.
            if tag == 3 and self._listBox['bg'] == 'azure':
                self._selection = self._listBox.curselection()
                self._msg = 'Selected: array[0]' + str(list(self._selection))
            elif tag == 3 and self._listBox2['bg'] == 'azure':
                self._selection = self._listBox2.curselection()
                self._msg = 'Selected: array[1]' + str(list(self._selection))
            elif tag == 3 and self._listBox3['bg'] == 'azure':
                self._selection = self._listBox3.curselection()
                self._msg = 'Selected: array[2]' + str(list(self._selection))
            elif tag == 2 and self._listBox['bg'] == 'azure':
                self._selection = self._listBox.curselection()
                self._msg = 'Selected: array[0]' + str(list(self._selection))
            elif tag == 2 and self._listBox2['bg'] == 'azure':
                self._selection = self._listBox2.curselection()
                self._msg = 'Selected: array[1]' + str(list(self._selection))
            elif tag == 2 and self._listBox3['bg'] == 'azure':
                self._selection = self._listBox3.curselection()
                self._msg = 'Selected: array[2]' + str(list(self._selection))
            elif tag == 1 and self._listBox['bg'] == 'azure':
                if self.get_NumDimensions() != 1:
                    self._selection = self._listBox.curselection()
                    self._msg = 'Selected: array[0]' + str(list(self._selection))
                else:
                    self._selection = self._listBox.curselection()
                    self._msg = 'Selected: array' + str(list(self._selection))
            elif tag == 1 and self._listBox2['bg'] == 'azure':
                self._selection = self._listBox2.curselection()
                self._msg = 'Selected: array[1]' + str(list(self._selection))
            elif tag == 1 and self._listBox3['bg'] == 'azure':
                self._selection = self._listBox3.curselection()
                self._msg = 'Selected: array[2]' + str(list(self._selection))

            # Update the label and the window.
            self._selectionLabel.config(text=self._msg)
            self.master.after(1, self._selectionLabel.update())

        # Method makes a call to updateSelection() to update the selectionLabel with the selected element from listbox 1,2 or 3.
        def tagger(tag):
            # The focused listbox will temp. have it's background changed to allow proper dimensional addressing of the array.
            # The selected listbox (focused listbox) will have the 'azure' background color. This will be changed back once the label has been updated.
            if tag == 1:
                self._listBox.config(bg='azure')
                self._listBox.config(relief='raised')
                self.master.update()
                self._listBox.focus_set()
                updateSelection(1)
                self._listBox.config(bg='bisque')
                self._listBox.config(relief='groove')
            elif tag == 2:
                self._listBox2.config(bg='azure')
                self._listBox.config(relief='raised')
                self.master.update()
                self._listBox2.focus_set()
                updateSelection(2)
                self._listBox2.config(bg='bisque')
                self._listBox.config(relief='groove')
            elif tag == 3:
                self._listBox3.config(bg='azure')
                self._listBox.config(relief='raised')
                self.master.update()
                self._listBox3.focus_set()
                updateSelection(3)
                self._listBox3.config(bg='bisque')
                self._listBox.config(relief='groove')

        # Method destroys array hub window and restarts application; (Binded to the newArray button)
        def restart():
            self.master.destroy()
            self.master.quit()
            root = tk.Tk()
            self.__init__(root)
            root.mainloop()

        self.master = master
        self._frame = tk.Frame(self.master, bg='indianred3', relief='solid', borderwidth=4, highlightbackground='white', highlightthickness=4, highlightcolor='gray25')

        # Frame holds the listBoxes for each dimension. (Displaying the array's contents)
        self._arrayFrame = tk.Frame(self._frame, bg='indianred', relief='solid', borderwidth=2, highlightbackground='gray25', highlightthickness=2, highlightcolor='gray25')
        self._label1 = tk.Label(self._arrayFrame, text='Array Contents:', fg='white', bg='black', font='Helvetica 24 bold')
        self._arrayFrame.grid_columnconfigure(0, weight=1)
        self._arrayFrame.grid_columnconfigure(1, weight=1)
        self._arrayFrame.grid_columnconfigure(2, weight=1)
        self._arrayFrame.grid_rowconfigure(0, weight=1)
        self._arrayFrame.grid_rowconfigure(1, weight=1)

        # Listbox to hold 1st dimensional elements.
        self._listBox = tk.Listbox(self._arrayFrame, justify='center', font='VERDANA 26 bold', selectborderwidth=1, bg='bisque')
        self._listBox.config(relief='groove', selectbackground='gray25', selectforeground='white')

        # Listbox to hold the 3rd dimensional elements.
        self._listBox2 = tk.Listbox(self._arrayFrame, justify='center', font='VERDANA 26 bold', selectborderwidth=1, bg='bisque')
        self._listBox2.config(relief='groove', selectbackground='gray25', selectforeground='white')

        # Listbox to hold the 3rd dimensional elements.
        self._listBox3 = tk.Listbox(self._arrayFrame, justify='center', font='VERDANA 26 bold', selectborderwidth=1, bg='bisque')
        self._listBox3.config(relief='groove', selectbackground='gray25', selectforeground='white')

        # Pre-select the first item in the first dimension from listbox.
        self._listBox.select_set(0)
        self._listBox.focus()

        # Returns the selected element from listBox 1; Converts listbox selection to correct format and returns it.
        def conv(tag):
            if tag == 'Integer':
                x = int(self._listBox.get('active'))
            elif tag == 'Float':
                x = float(self._listBox.get('active'))
            elif tag == 'String':
                x = str(self._listBox.get('active'))
            elif tag == 'Boolean':
                x = bool(self._listBox.get('active'))
            return x

        # Pack in other listbox widgets depending on dimensions specified by user.
        if self.get_NumDimensions() == 1:
            # Fill the first dimensional listBox with content from self.array[0].
            for element in np.nditer(self.array):
                self._listBox.insert(tk.END, element)

            self._label1.pack(fill=tk.X, expand=True)
            self._listBox.pack(fill=tk.BOTH, expand=True)

            # Specified label output needs to be altered slightly depending on the dimensions of the array.
            self._msg = "You selected: array[" + str(list(self.array.flatten()).index(conv(self.get_DataType()))) + "]"

        elif self.get_NumDimensions() == 2:
            for element in self.array[0]:
                self._listBox.insert(tk.END, element)
            for element in self.array[1]:
                self._listBox2.insert(tk.END, element)

            self._label1.pack(fill=tk.X, expand=True)
            self._listBox.pack(side=tk.LEFT, expand=True, fill=tk.BOTH)
            self._listBox2.pack(side=tk.RIGHT, expand=True, fill=tk.BOTH)

            self._msg = "You selected: array[0][" + str(list(self.array.flatten()).index(conv(self.get_DataType()))) + "]"

        else:
            for element in self.array[0]: self._listBox.insert(tk.END, element)
            for element in self.array[1]: self._listBox2.insert(tk.END, element)
            for element in self.array[2]: self._listBox3.insert(tk.END, element)

            self._label1.grid(row=0, column=0, columnspan=3, sticky='nsew')
            self._listBox.grid(row=1, column=0, sticky='nsew', columnspan=1)
            self._listBox2.grid(row=1, column=1, sticky='nsew', columnspan=1)
            self._listBox3.grid(row=1, column=2, sticky='nsew', columnspan=1)

        self._msg = "You selected: array[0][" + str(list(self.array.flatten()).index(conv(self.get_DataType()))) + "]"

        self._arrayFrame.pack(fill=tk.BOTH, padx=20, expand=True, pady=5)

        # Draw and pack in the selection label; This label shows the user the selected index of the element from within the listBoxes.
        self._selectionLabel = tk.Label(self._frame, text=self._msg, font='HELVETICA 14 bold', bg='gray99', fg='black', justify='center')
        self._selectionLabel.config(borderwidth=2, relief='solid', highlightbackground='gray25', highlightthickness=2, highlightcolor='gray25')
        self._selectionLabel.pack(fill=tk.BOTH, padx=20, pady=5, expand=True)

        # Frame containing buttons with methods to perform on the given array.
        self._methodsFrame = tk.Frame(self._frame, bg='indianred3', relief='solid', borderwidth=2, highlightbackground='gray25', highlightthickness=2, highlightcolor='gray25')
        self._methodsFrame.grid_columnconfigure(0, weight=1)
        self._methodsFrame.grid_columnconfigure(1, weight=1)
        self._methodsFrame.grid_columnconfigure(2, weight=1)
        self._methodsFrame.grid_rowconfigure(0, weight=1)
        self._methodsFrame.grid_rowconfigure(1, weight=1)
        self._methodsFrame.grid_rowconfigure(2, weight=1)

        self._label2 = tk.Label(self._methodsFrame, text='Array Methods:', fg='white', bg='black', font='Helvetica 24 bold')
        self._label2.grid(row=0, column=0, columnspan=3, sticky='nsew')

        # Array Method Buttons.
        self._insertButton = tk.Button(self._methodsFrame, text='INSERT', font='HELVETICA 30 bold', width=20, command=lambda: terminal(1), relief='raised')
        self._insertButton.grid(row=1, column=0, sticky='nsew')

        self._deleteButton = tk.Button(self._methodsFrame, text='DELETE', font='HELVETICA 30 bold', width=20, command=lambda: terminal(2), relief='raised')
        self._deleteButton.grid(row=2, column=0, sticky='nsew')

        self._searchButton = tk.Button(self._methodsFrame, text='SEARCH', font='HELVETICA 30 bold', width=20, command=lambda: terminal(3), relief='raised')
        self._searchButton.grid(row=1, column=1, sticky='nsew')

        self._splitButton = tk.Button(self._methodsFrame, text='SPLIT', font='HELVETICA 30 bold', width=20, command=lambda: terminal(4), relief='raised')
        self._splitButton.grid(row=2, column=1, sticky='nsew')

        self._sortButton = tk.Button(self._methodsFrame, text='SORT', font='HELVETICA 30 bold', width=20, command=lambda: terminal(5), relief='raised')
        self._sortButton.grid(row=1, column=2, sticky='nsew')

        self._filterButton = tk.Button(self._methodsFrame, text='FILTER', font='HELVETICA 30 bold', width=20, command=lambda: terminal(6), relief='raised')
        self._filterButton.grid(row=2, column=2, sticky='nsew')

        self._methodsFrame.pack(fill=tk.BOTH, padx=20, expand=True, pady=10)

        # Bottom frame containing array's attributes and a new array button.
        self._bottomFrame = tk.Frame(self.master, bg='gray25', relief='solid', borderwidth=4, highlightbackground='white', highlightthickness=4, highlightcolor='gray25')
        self._bottomFrame.columnconfigure(0, weight=1)
        self._bottomFrame.columnconfigure(1, weight=1)
        self._bottomFrame.columnconfigure(2, weight=1)
        self._bottomFrame.rowconfigure(0, weight=1)
        self._bottomFrame.rowconfigure(1, weight=1)
        self._bottomFrame.rowconfigure(2, weight=1)

        # Frame containing attributes of the array.
        self._arrayAttributeFrame = tk.Frame(self._bottomFrame, bg='gray25')
        self._arrayAttributeFrame.columnconfigure(0, weight=1)
        self._arrayAttributeFrame.columnconfigure(1, weight=1)
        self._arrayAttributeFrame.rowconfigure(0, weight=1)
        self._arrayAttributeFrame.rowconfigure(1, weight=1)
        self._arrayAttributeFrame.rowconfigure(2, weight=1)
        self._aLabel1 = tk.Label(self._arrayAttributeFrame, text=str(self.get_NumDimensions()) + ' Dimensions', bg='gray25', fg='white', font='Helvetica 15 bold')
        self._aLabel1.grid(row=0, column=0, sticky='nsw', columnspan=2)
        self._aLabel2 = tk.Label(self._arrayAttributeFrame, text=str(self.get_NumElements()) + ' Elements per dimension', bg='gray25', fg='white', font='Helvetica 15 bold')
        self._aLabel2.grid(row=1, column=0, sticky='nsw', columnspan=2)
        self._aLabel3 = tk.Label(self._arrayAttributeFrame, text="Datatype: " + str(self.get_DataType()), bg='gray25', fg='white', font='Helvetica 14 bold')
        self._aLabel3.grid(row=2, column=0, sticky='nsw', columnspan=2)

        # Restart program and launch new array.
        self._newArrayButton = tk.Button(self._bottomFrame, text='NEW ARRAY', font='HELVETICA 30 bold', width=20, command=lambda: restart())
        self._newArrayButton.grid(row=0, column=2, sticky='ew', padx=20, pady=5, rowspan=3)

        # Pack/Draw in the frames.
        self._arrayAttributeFrame.grid(row=0, column=0, sticky='nsew', padx=20, columnspan=2, pady=5)
        self._frame.pack(fill=tk.BOTH, padx=14, pady=(14, 4), expand=True)
        self._bottomFrame.pack(fill=tk.BOTH, padx=14, pady=(0, 14), expand=True)

        # Window attributes.
        self.master.config(bg='gray25')
        self.master.title('Visual Array Hub')
        self.master.geometry('875x525')
        self.master.minsize(875, 700)

        # These bindings to the window ensure that the window is being updated immediately, and displaying the correct selection from listBoxes.
        self._listBox.bind('<<ListboxSelect>>', lambda cmd: tagger(1))
        self._listBox2.bind('<<ListboxSelect>>', lambda cmd: tagger(2))
        self._listBox3.bind('<<ListboxSelect>>', lambda cmd: tagger(3))

        self.master.mainloop()

    # Method inserts element at given location in array.
    def insert(self, master):

        def add():
            try:
                self._msg = None
                if self.get_DataType() != 'Boolean':
                    if self.get_DataType() == 'String':
                        self._temp = "'" + str(self._elementEntry.get()) + "'"
                    else:
                        self._temp = self._elementEntry.get()

                    if self.get_NumDimensions() == 1:
                        # Had to perform an extra check for the float data type because was having trouble entering it into the listbox initially.
                        # Was having trouble inserting a float, but every other data type was working. Special case must be added for the float and the string data types.
                        if self.get_DataType() == 'Float':
                            self.array[0, int(self.indexEntry.get())] = self._elementEntry.get()

                        else:
                            self.array[0][int(self.indexEntry.get())] = self._temp

                        self._msg = 'Inserted Element [' + self._elementEntry.get() + "] @ Index [" + self.indexEntry.get() + "] in Dimension [1]"

                    elif self.get_NumDimensions() == 2 or 3:
                        # Dictionary to bind selections from drop-down box to correct array indexing.
                        self._dimVal = {'Dimension [1]': 0, 'Dimension [2]': 1, 'Dimension [3]': 2}

                        if self.get_DataType() == 'Float':
                            self.array[self._dimVal.get(self._tkvar.get())][int(self.indexEntry.get())] = self._elementEntry.get()
                        else:
                            self.array[self._dimVal.get(self._tkvar.get())][int(self.indexEntry.get())] = self._temp

                        self._msg = 'Inserted Element [' + self._elementEntry.get() + "] @ Index [" + self.indexEntry.get() + "] in " + self._tkvar.get()

                else:
                    self.boolConv = {"True": 1, "False": 0}
                    if self.get_NumDimensions() == 1:
                        self.array[0][int(self.indexEntry.get())] = self.boolConv.get(self._boolVar.get())
                        self._msg = 'Inserted Element [' + self._boolVar.get() + "] @ Index [" + self.indexEntry.get() + "] in Dimension [1]"
                    elif self.get_NumDimensions() == 2 or 3:
                        if self._tkvar.get() == 'Dimension [1]':
                            self.array[0][int(self.indexEntry.get())] = self.boolConv.get(self._boolVar.get())
                        elif self._tkvar.get() == 'Dimension [2]':
                            self.array[1][int(self.indexEntry.get())] = self.boolConv.get(self._boolVar.get())
                        if self._tkvar.get() == 'Dimension [3]':
                            self.array[2][int(self.indexEntry.get())] = self.boolConv.get(self._boolVar.get())

                    self._msg = 'Inserted Element [' + self._boolVar.get() + "] @ Index [" + self.indexEntry.get() + "] in " + self._tkvar.get()

                print(Console.bold + Console.cyan + '-------------------------------------------------------' + Console.end)
                print(Console.green + Console.bold + self._msg + Console.end)
                print(Console.bold + Console.cyan + '-------------------------------------------------------' + Console.end)

                self.master.destroy()
                self.master.quit()
                root = tk.Tk()
                self.arrayHub(root)
                root.mainloop()

            # Display an error window if the entered element/index cannot be added into the array.
            except ValueError as VE:
                print(VE)
                self._valErrorWindow = tk.Tk()

                self._frame = tk.Frame(self._valErrorWindow, bg='indianred3')

                self._label = tk.Label(self._frame, text='You have entered a value for the element \nor index that cannot be inserted into the array.')
                self._label.config(bg='indianred3', fg='white', font='HELVETICA 14 bold')
                self._label.pack(fill=tk.X, pady=(20, 6), expand=True)
                self._label2 = tk.Label(self._frame, text='Your element must be ' + str(self.get_DataType()).lower() + ' type.')
                self._label2.config(bg='ivory', fg='indianred3', font='HELVETICA 14 bold')
                self._label2.pack(fill=tk.X, expand=True)

                self.closeButton = tk.Button(self._frame, text='CLOSE', font='HELVETICA 24 bold', command=lambda: self._valErrorWindow.destroy())
                self.closeButton.pack(fill=tk.X, padx=20, pady=(10, 10), expand=True)

                self._frame.pack(padx=10, pady=10, expand=True, fill=tk.BOTH)

                self._valErrorWindow.config(bg='gray25')
                self._valErrorWindow.geometry('375x175')
                self._valErrorWindow.minsize(300, 175)
                self._valErrorWindow.title('Value Error!')
                self._valErrorWindow.resizable(False, False)
                self._valErrorWindow.bind('<Return>', lambda cmd: self._valErrorWindow.destroy())
                self._valErrorWindow.mainloop()

            # Display an error window if the index specified by the user is invalid.
            except IndexError:
                self._indexErrorWindow = tk.Tk()

                self._frame = tk.Frame(self._indexErrorWindow, bg='indianred3')

                self._label = tk.Label(self._frame, text='You have entered an index value that \ndoesn\'t correspond with this array. \nPlease enter a valid index.')
                self._label.config(bg='ivory', fg='indianred3', font='HELVETICA 14 bold')
                self._label.pack(fill=tk.X, pady=(25, 10), expand=True)

                self.closeButton = tk.Button(self._frame, text='CLOSE', font='HELVETICA 24 bold', command=lambda: self._indexErrorWindow.destroy())
                self.closeButton.pack(fill=tk.X, padx=20, pady=(10, 10), expand=True)

                self._frame.pack(padx=10, pady=10, expand=True, fill=tk.BOTH)

                self._indexErrorWindow.config(bg='gray25')
                self._indexErrorWindow.geometry('375x175')
                self._indexErrorWindow.minsize(300, 175)
                self._indexErrorWindow.title('Index Error!')
                self._indexErrorWindow.resizable(False, False)
                self._indexErrorWindow.bind('<Return>', lambda cmd: self._indexErrorWindow.destroy())
                self._indexErrorWindow.mainloop()

        # String variables to hold given array and element entered by user.
        self.element = tk.StringVar()
        self.dimension = tk.StringVar()
        self.index = tk.StringVar()

        self.alpha = master

        self._label1 = tk.Label(self.alpha, text='Insert Element:', bg='gray28', fg='white', font='HELVETICA 20 bold')
        self._label1.pack(fill=tk.X, padx=20, pady=20)

        # If the data type selected is boolean, than the user may only pick from the True/False options from drop-down box for the element.
        if self.get_DataType() != 'Boolean':
            self._elementEntry = tk.Entry(self.alpha, font='HELVETICA 24 bold', justify='center', textvariable=self.element)
            self._elementEntry.pack(fill=tk.X, padx=20)
            self._elementEntry.focus()

        else:
            self._boolVar = tk.StringVar(self.alpha)
            self._options = ['True', 'False']
            self._boolVar.set(self._options[0])
            self._elementBox = tk.OptionMenu(self.alpha, self._boolVar, *self._options)
            self._elementBox.pack(fill=tk.BOTH, padx=20)

        # If the dimension isn't 1, then a drop-down menu will be presented to the user to select which dimension to insert element in.
        if self.get_NumDimensions() != 1:
            self.alpha.after(1, self.alpha.minsize(400, 400))
            self._tkvar = tk.StringVar()
            self._options = []
            x = 0
            while x < int(self.get_NumDimensions()):
                x += 1
                self._options.append(str('Dimension [' + str(x) + "]"))
            self._label2 = tk.Label(self.alpha, text='Select Dimension: ', bg='gray28', fg='white', font='HELVETICA 20 bold')
            self._label2.pack(fill=tk.X, padx=20, pady=20)

            self._tkvar = tk.StringVar(self.alpha)
            self._tkvar.set(self._options[0])
            self._dimensionBox = tk.OptionMenu(self.alpha, self._tkvar, *self._options).pack(fill=tk.BOTH, padx=20)

        self._label3 = tk.Label(self.alpha, text='@ Index: ', bg='gray28', fg='white', font='HELVETICA 20 bold', )
        self._label3.pack(fill=tk.X, padx=20, pady=20)
        self.indexEntry = tk.Entry(self.alpha, font='HELVETICA 24 bold', justify='center', textvariable=self.index)
        self.indexEntry.pack(fill=tk.X, padx=20)
        self._insertButton = tk.Button(self.alpha, text='INSERT', font='HELVETICA 24 bold', command=lambda: add())
        self._insertButton.pack(fill=tk.X, padx=20, pady=20)

        self.alpha.title('INSERT:')
        self.alpha.config(bg='indianred')
        self.alpha.minsize(400, 300)
        self.alpha.bind('<Return>', lambda cmd: add())
        self.alpha.resizable(False, False)
        self.alpha.mainloop()

    # Method removes element at given location in array.
    def delete(self, master):
        def remove():
            try:
                # When an element is deleted, it's index value sets the element back to it's 'null' or default value when the array was first initialized.
                self.nullConv = {'Integer': 0, 'Float': 0.0, 'Boolean': 1, 'String': "''"}
                self.msg = None
                if self.get_NumDimensions() == 1:
                    self.msg = 'Deleted Element [' + str(self.array[0][int(self._indexDeleteEntry.get())]) + "] @ Index [" + self._indexDeleteEntry.get() + "] in Dimension [1]"
                    self.array[0][int(self._indexDeleteEntry.get())] = self.nullConv.get(self.get_DataType())

                elif self.get_NumDimensions() != 1:
                    if self._tkvar.get() == 'Dimension [1]':
                        self.msg = 'Deleted Element ['+str(self.array[0][int(self._indexDeleteEntry.get())])+"] @ Index ["+self._indexDeleteEntry.get()+"] in "+self._tkvar.get()
                        self.array[0][int(self._indexDeleteEntry.get())] = self.nullConv.get(self.get_DataType())

                    elif self._tkvar.get() == 'Dimension [2]':
                        self.msg = 'Deleted Element ['+str(self.array[1][int(self._indexDeleteEntry.get())])+"] @ Index ["+self._indexDeleteEntry.get()+"] in " + self._tkvar.get()
                        self.array[1][int(self._indexDeleteEntry.get())] = self.nullConv.get(self.get_DataType())
                    elif self._tkvar.get() == 'Dimension [3]':
                        self.msg = 'Deleted Element ['+str(self.array[2][int(self._indexDeleteEntry.get())])+"] @ Index ["+self._indexDeleteEntry.get()+"] in "+self._tkvar.get()
                        self.array[2][int(self._indexDeleteEntry.get())] = self.nullConv.get(self.get_DataType())

                print(Console.bold + Console.cyan + '-------------------------------------------------------' + Console.end)
                print(Console.green + Console.bold + self.msg + Console.end)
                print(Console.bold + Console.cyan + '-------------------------------------------------------' + Console.end)

                self.master.destroy()
                self.master.quit()
                tunnel = tk.Tk()
                self.arrayHub(tunnel)
                tunnel.mainloop()

            except IndexError:
                self.indexError_Window = tk.Tk()

                self._label10 = tk.Label(self.indexError_Window, text='Invalid index specified. Either the index you\nentered was out of bounds, or does not exist')
                self._label10.config(bg='indianred', fg='white', font='HELVETICA 14 bold')
                self._label10.pack(fill=tk.X, padx=30, pady=(25, 10))

                self.closeButton = tk.Button(self.indexError_Window, text='CLOSE', font='HELVETICA 24 bold', command=lambda: self.indexError_Window.destroy())
                self.closeButton.pack(fill=tk.X, padx=20, pady=(10, 0))

                self.indexError_Window.title('Index Error:')
                self.indexError_Window.minsize(375, 175)
                self.indexError_Window.resizable(False, False)
                self.indexError_Window.config(bg='indianred')
                self.indexError_Window.bind('<Return>', lambda cmd: self.indexError_Window.destroy())
                self.indexError_Window.mainloop()

            except ValueError:
                # Display an error window if the entered element/index cannot be added into the array.
                self._valErrorWindow = tk.Tk()

                self.label9 = tk.Label(self._valErrorWindow, text='You have entered an index value\nthat cannot be removed from the array.')
                self.label9.config(bg='indianred', fg='white', font='HELVETICA 14 bold')
                self.label9.pack(fill=tk.X, padx=30, pady=(25, 10))
                self._label10 = tk.Label(self._valErrorWindow, text='Please try a different value again.')
                self._label10.config(bg='indianred', fg='white', font='HELVETICA 14 bold')
                self._label10.pack(fill=tk.X, padx=30)

                self.closeButton = tk.Button(self._valErrorWindow, text='CLOSE', font='HELVETICA 24 bold', command=lambda: self._valErrorWindow.destroy())
                self.closeButton.pack(fill=tk.X, padx=20, pady=(10, 0))

                self._valErrorWindow.config(bg='indianred')
                self._valErrorWindow.geometry('375x175')
                self._valErrorWindow.minsize(300, 175)
                self._valErrorWindow.title('Value Error!')
                self._valErrorWindow.resizable(False, False)
                self._valErrorWindow.bind('<Return>', lambda cmd: self._valErrorWindow.destroy())
                self._valErrorWindow.mainloop()

        self.alpha = master

        # String variable holds the index to be deleted.
        self.index = tk.StringVar()

        self._label1 = tk.Label(self.alpha, text='Delete Index:', bg='gray28', fg='white', font='HELVETICA 20 bold')
        self._label1.pack(fill=tk.X, padx=20, pady=20)
        self._indexDeleteEntry = tk.Entry(self.alpha, font='HELVETICA 24 bold', justify='center')
        self._indexDeleteEntry.pack(fill=tk.X, padx=20)
        self._indexDeleteEntry.focus()

        # If more than one dimension is present, than a drop-down menu must be presented to the user to specify which dimension to delete element from.
        if self.get_NumDimensions() != 1:
            self.alpha.geometry('400x280')
            self.alpha.minsize(400, 280)
            self._tkvar = tk.StringVar()
            self._options = []
            self._x = 0
            while self._x < int(self.get_NumDimensions()):
                self._x += 1
                self._options.append(str('Dimension [' + str(self._x) + "]"))
            self._label2 = tk.Label(self.alpha, text='Select Dimension: ', bg='gray28', fg='white', font='HELVETICA 20 bold', )
            self._label2.pack(fill=tk.X, padx=20, pady=20)

            self._tkvar = tk.StringVar(self.alpha)
            self._tkvar.set(self._options[0])
            self._dimensionBox = tk.OptionMenu(self.alpha, self._tkvar, *self._options).pack(fill=tk.BOTH, padx=20)

        else:
            self.alpha.geometry('400x200')
            self.alpha.minsize(400, 200)

        self._deleteButton = tk.Button(self.alpha, text='DELETE', font='HELVETICA 24 bold', command=lambda: remove())
        self._deleteButton.pack(fill=tk.X, padx=20, pady=20)

        # Window attributes.
        self.alpha.title('DELETE:')
        self.alpha.config(bg='indianred')
        self.alpha.bind('<Return>', lambda cmd: remove())
        self.alpha.resizable(False, False)
        self.alpha.mainloop()

    # Method searches array for specified element from user.
    def search(self, master):
        # Method find's element in given array.
        def find():

            def searchAgainBind():
                self._displaySearchWindow.destroy()
                root = tk.Tk()
                self.search(root)
                root.mainloop()

            try:
                if self.get_DataType() == 'Boolean':
                    self.searchedIndex = np.where(self.array == bool(self._indexSearchEntry.get()))
                elif self.get_DataType() == 'String':
                    self.searchedIndex = np.where(self.array == "'" + str(self._indexSearchEntry.get()) + "'")
                elif self.get_DataType() == 'Float':
                    self.searchedIndex = np.where(self.array == float(self._indexSearchEntry.get()))
                elif self.get_DataType() == 'Integer':
                    self.searchedIndex = np.where(self.array == int(self._indexSearchEntry.get()))

                self._searchedElement = self._indexSearchEntry.get()

                # Output to console the search message.

                self._searchZip = list(zip(self.searchedIndex[0], self.searchedIndex[1]))
                self._x = 0
                self._dimensions = []
                self._indexes = []

                # Iterate through search results and add the index and dimension to their own respective lists to be printed back to the user.
                # We need to alter the dimension that is returned, by adding 1 so that dimension 1 is 1 not 0. (Due to python indexing by zero)
                for result in self._searchZip:
                    self._x += 1
                    self._dimensions.append(result[0] + 1)
                    self._indexes.append(result[1])

                self._zip = zip(self._indexes, self._dimensions)
                self._msg = 'Searched for element [' + str(self._indexSearchEntry.get()) + '] within the array.'

                print(Console.bold + Console.cyan + '-------------------------------------------------------' + Console.end)
                print(Console.green + Console.bold + self._msg)
                print('[Search results below]:')
                print(tabulate([*self._zip], headers=['Index', 'Dimension'], tablefmt='fancy_grid'))
                print('Total Occurrences: [' + str(self._x) + "]." + Console.end)
                print(Console.bold + Console.cyan + '-------------------------------------------------------' + Console.end)

                # Close current window and display the search results in new window.
                self.alpha.destroy()

                self._displaySearchWindow = tk.Tk()

                self._label1 = tk.Label(self._displaySearchWindow, text='Search results for Element [' + str(self._searchedElement) + "]: ")
                self._label1.pack(fill=tk.BOTH, padx=10, pady=10, expand=True)

                self._resultBox = tk.Listbox(self._displaySearchWindow, justify='center', font='VERDANA 26 bold', selectborderwidth=1, bg='bisque')

                self._y = 0
                if self.get_NumDimensions() == 1:
                    for result in self._indexes:
                        self._resultBox.insert(tk.END, 'array[' + str(result) + "]")
                else:
                    for result in self._dimensions:
                        self._resultBox.insert(tk.END, 'array[' + str(result-1) + "][" + str(self._indexes[self._y]) + "]")
                        self._y += 1

                self._resultBox.select_set(0)

                self._resultBox.pack(fill=tk.BOTH, padx=10, pady=10, expand=True)

                self._bottomFrame = tk.Frame(self._displaySearchWindow, bg='indianred')
                self._searchAgainButton = tk.Button(self._bottomFrame, text='NEW SEARCH', font='HELVETICA 24 bold', width=10, command=lambda: searchAgainBind())
                self._searchAgainButton.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
                self._doneButton = tk.Button(self._bottomFrame, text='DONE', font='HELVETICA 24 bold', width=10, command=lambda: self._displaySearchWindow.destroy())
                self._doneButton.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)
                self._bottomFrame.pack(fill=tk.BOTH, padx=10, pady=10)

                self._displaySearchWindow.title('Search Complete')
                self._displaySearchWindow.minsize(400, 225)
                self._displaySearchWindow.config(bg='indianred')
                self._displaySearchWindow.resizable(False, False)
                self._displaySearchWindow.mainloop()

            except ValueError:
                self._valueErrorWindow = tk.Tk()
                self._label1 = tk.Label(self._valueErrorWindow, text='Could not locate the element:')
                self._label1.config(bg='indianred', fg='white', font='HELVETICA 22 bold')
                self._label1.pack(fill=tk.X, padx=10, pady=(20, 0))
                self._label2 = tk.Label(self._valueErrorWindow, text='[' + str(self._indexSearchEntry.get()) + ']')
                self._label2.config(bg='gray24', fg='thistle', font='HELVETICA 20 bold')
                self._label2.pack(fill=tk.X, padx=25, pady=10)
                self._label3 = tk.Label(self._valueErrorWindow, text='within the specified array.')
                self._label3.config(bg='indianred', fg='white', font='HELVETICA 20 bold')
                self._label3.pack(fill=tk.X, padx=10)
                self.closeButton = tk.Button(self._valueErrorWindow, text='CLOSE', width=20, font='HELVETICA 22 bold', command=lambda: self._valueErrorWindow.destroy())
                self.closeButton.pack(fill=tk.X, padx=20, pady=20)
                self._valueErrorWindow.title('Value Error:')
                self._valueErrorWindow.minsize(400, 225)
                self._valueErrorWindow.resizable(False, False)
                self._valueErrorWindow.config(bg='indianred')
                self._valueErrorWindow.bind('<Return>', lambda cmd: self._valueErrorWindow.destroy())
                self._valueErrorWindow.mainloop()

        self.alpha = master

        self._label = tk.Label(self.alpha, text='Search for element:', bg='gray28', fg='white', font='HELVETICA 20 bold')
        self._label.pack(fill=tk.X, padx=20, pady=20)
        self._indexSearchEntry = tk.Entry(self.alpha, font='HELVETICA 24 bold', justify='center')
        self._indexSearchEntry.pack(fill=tk.X, padx=20)
        self._indexSearchEntry.focus()

        self._searchButton = tk.Button(self.alpha, text='SEARCH', font='HELVETICA 24 bold', command=lambda: find())
        self._searchButton.pack(fill=tk.X, padx=20, pady=20)

        # Search window attributes.
        self.alpha.geometry('400x200')
        self.alpha.minsize(400, 200)
        self.alpha.title('SEARCH:')
        self.alpha.config(bg='indianred')
        self.alpha.bind('<Return>', lambda cmd: find())
        self.alpha.resizable(False, False)
        self.alpha.mainloop()

    # Method splits the array depending on split/Axis amount specified by user.
    def split_(self, master):

        # Method attempts to split the array with user specified method and split/axis values if applicable.
        def _split():

            try:
                if self._tkvar.get() == 'hsplit()':
                    return np.hsplit(self.array, int(self._splitVal.get())), str(self._tkvar.get())
                elif self._tkvar.get() == 'vsplit()':
                    return np.vsplit(self.array, int(self._splitVal.get())), str(self._tkvar.get())
                elif self._tkvar.get() == 'dsplit()':
                    return np.dsplit(self.array, int(self._splitVal.get())), str(self._tkvar.get())
                else:
                    return np.array_split(self.array, int(self._splitVal.get()), axis=int(self._axisVal.get())), str(self._tkvar.get())

            except ValueError as VE:
                err = VE
                # Display an error window if the entered element/index cannot be added into the array.
                self._valErrorWindow = tk.Tk()

                if self._splitVal.get() == "":
                    self._label1 = tk.Label(self._valErrorWindow, text="No value entered for split amount.")
                    self._label1.config(text="No value entered for split amount." + "\nPlease supply a value for the empty entry bar.")
                    self._label1.config(bg='ivory', fg='indianred3', font='HELVETICA 12 bold', justify='center')
                    self._label1.pack(fill=tk.BOTH, pady=5, padx=10)
                    self._valErrorWindow.geometry('300x100')
                    self._valErrorWindow.minsize(300, 100)
                    self.closeButton = tk.Button(self._valErrorWindow, text='CLOSE', font='HELVETICA 24 bold', command=lambda: self._valErrorWindow.destroy())
                    self.closeButton.pack(fill=tk.X, pady=5, padx=10)

                if not self._splitVal.get().isdigit() and self._splitVal.get() != 'N/A':
                    self._label1 = tk.Label(self._valErrorWindow, text="Please enter an integer value into the split amount.")
                    self._label1.config(bg='ivory', fg='indianred3', font='HELVETICA 12 bold', justify='center')
                    self._label1.pack(fill=tk.BOTH, pady=5, padx=10)
                    self._valErrorWindow.geometry('300x95')
                    self._valErrorWindow.minsize(300, 95)
                    self.closeButton = tk.Button(self._valErrorWindow, text='CLOSE', font='HELVETICA 24 bold', command=lambda: self._valErrorWindow.destroy())
                    self.closeButton.pack(fill=tk.X, pady=5, padx=10)

                else:
                    self._valErrorWindow.grid_columnconfigure(0, weight=1)
                    self._valErrorWindow.grid_rowconfigure(0, weight=1)
                    self._valErrorWindow.grid_rowconfigure(1, weight=1)
                    self._label1 = tk.Label(self._valErrorWindow, text=str(err)+'\nPlease try a value diff. than [' + str(self._axisVal.get()) + "]")
                    self._label1.config(bg='ivory', fg='indianred3', font='HELVETICA 12 bold', justify='center')
                    self._label1.grid(row=0, column=0, sticky='nsew', pady=15)
                    self._valErrorWindow.geometry('300x150')
                    self._valErrorWindow.minsize(300, 150)
                    self.closeButton = tk.Button(self._valErrorWindow, text='CLOSE', font='HELVETICA 24 bold', command=lambda: self._valErrorWindow.destroy())
                    self.closeButton.grid(row=1, column=0, sticky='nsew', pady=15)

                self._valErrorWindow.config(bg='indianred')
                self._valErrorWindow.title('VALUE ERROR!')
                self._valErrorWindow.resizable(False, False)
                self._valErrorWindow.bind('<Return>', lambda cmd: self._valErrorWindow.destroy())
                self._valErrorWindow.mainloop()

            except IndexError as IE:
                # Display an error window if the entered element/index cannot be added into the array.
                self._valIndexErrorWindow = tk.Tk()

                # Condition checks whether the axis value specified by the user is a valid integer.
                if not self._axisVal.get().isdigit():
                    self._label1 = tk.Label(self._valIndexErrorWindow, text="Axis value must be an integer value.")
                    self._label1.config(bg='ivory', fg='indianred3', font='HELVETICA 12 bold', justify='center')
                    self._label1.pack(fill=tk.BOTH, pady=5, padx=10)
                    self._valErrorWindow.geometry('300x95')
                    self._valErrorWindow.minsize(300, 95)
                    self.closeButton = tk.Button(self._valIndexErrorWindow, text='CLOSE', font='HELVETICA 24 bold', command=lambda: self._valIndexErrorWindow.destroy())
                    self.closeButton.pack(fill=tk.X, pady=5, padx=10)

                else:
                    self._valIndexErrorWindow.grid_columnconfigure(0, weight=1)
                    self._valIndexErrorWindow.grid_rowconfigure(0, weight=1)
                    self._valIndexErrorWindow.grid_rowconfigure(1, weight=1)
                    self._label1 = tk.Label(self._valIndexErrorWindow, text=IE)
                    self._label1.config(bg='ivory', fg='indianred3', font='HELVETICA 12 bold', justify='center')
                    self._label1.grid(row=0, column=0, sticky='nsew', pady=15)
                    self._valIndexErrorWindow.geometry('300x150')
                    self._valIndexErrorWindow.minsize(300, 150)
                    self.closeButton = tk.Button(self._valIndexErrorWindow, text='CLOSE', font='HELVETICA 24 bold', command=lambda: self._valIndexErrorWindow.destroy())
                    self.closeButton.grid(row=1, column=0, sticky='nsew', pady=15)

                self._valIndexErrorWindow.config(bg='indianred')
                self._valIndexErrorWindow.title('INDEX ERROR!')
                self._valIndexErrorWindow.resizable(False, False)
                self._valIndexErrorWindow.bind('<Return>', lambda cmd: self._valIndexErrorWindow.destroy())
                self._valIndexErrorWindow.mainloop()

        # Pop displays the user their split array after the method has been performed. This will create a copy of the array that the user can export to their machine; .txt format.
        # ** Please note, this is only a copy of the original array, so closing this window will not affect the original copy of the array. The split result can be exported however.
        def popUp():
            x = _split()
            print(Console.bold + Console.cyan + '-------------------------------------------------------' + Console.end)
            print(Console.bold + Console.green + "Executed: " + str(x[1]) + " method on array.")
            print(Console.bold + Console.cyan + 'Axis: ' + str(self._axisVal.get()) + " Split: " + str(self._splitVal.get()))
            print(Console.bold + Console.cyan + '-------------------------------------------------------' + Console.end)

            self._y = []
            for element in x[0]:
                self._y.append(element)
            z = 0
            for element in self._y:
                for elements in list(element):
                    self._y[z] = elements
                z += 1

            self.alpha = tk.Tk()

            self._label1 = tk.Label(self.alpha, text='You selected:\n' + str(x[1]), bg='indianred3', fg='ivory', font='HELVETICA 20 bold').pack(fill=tk.X, padx=20, pady=5)

            self.label = tk.Text(self.alpha, font='Helvetica 18 bold', height=14)
            for element in self._y:
                self.label.tag_configure("center", justify='center')
                self.label.insert(tk.END, str(element) + "\n")
                self.label.tag_add("center", "1.0", "end")
            self.label.pack(padx=20, pady=5, fill=tk.X)

            def saveText():
                # Get specific username of user's to allow use to write to their local desktop on their machines.
                username = getpass.getuser()

                # Get the user's machine.
                uMachine = platform.system()
                if uMachine == 'Darwin':
                    filename = "//Users//{0}//Desktop//splitArray.txt".format(username)
                elif uMachine == 'Windows':
                    filename = "C:\\Users\\{0}\\Desktop\\splitArray.txt".format(username)
                elif uMachine == 'Linux':
                    filename = "//home//{0}//Desktop//splitArray.txt".format(username)
                else:
                    filename = 'NOF'
                if filename != 'NOF':
                    file = open(filename, 'w')
                    # Write the contents of the array before split, and after the split alongside,  the attributes specified by the user into the .txt file.
                    file.write(str(self.label.get("1.0", tk.END)))
                    file.close()
                else:
                    print('Error determining user OS; Error writing to file!')

            # Button saves content's in the textbox to the user's desktop.
            self.saveButton = tk.Button(self.alpha, text='Save as .txt', font='HELVETICA 24 bold', command=lambda: saveText())
            self.saveButton.pack(fill=tk.X, padx=20, pady=5)

            self._label2 = tk.Label(self.alpha, text='Saves .txt to your desktop.', bg='indianred3', fg='ivory', font='HELVETICA 10 italic').pack(fill=tk.X, padx=20, pady=5)

            # Window attributes.
            self.alpha.title('SPLIT RESULT: ')
            self.alpha.config(bg='indianred3')
            self.alpha.resizable(False, False)
            self.alpha.geometry('500x450')
            self.alpha.mainloop()

        self.master = master

        # This method is binded to execute when an option is selected from the split method drop-down menu.
        # Method disabled/enables entry states depending on the method selected from the drop-down menu.
        def methodSelect():
            if self._tkvar.get() == 'array_Split()':
                self._axisEntry.config(state='normal')
                self._axisVal.set('')
                self._splitEntry.config(state='normal')
                self._splitVal.set('')

            else:
                if self._tkvar.get() == 'hsplit()' or self._tkvar.get() == 'vsplit()':
                    self._splitEntry.config(state='normal')
                    self._splitVal.set('')
                else:
                    self._splitEntry.config(state='disabled')
                    self._splitVal.set('N/A')

                self._axisEntry.config(state='disabled')
                self._axisVal.set('N/A')

                self.master.after(1, self.master.update())

        # Drop-Down menu containing the different split methods that can be performed on the array.
        self._label1 = tk.Label(self.master, text='Select specific split method:', bg='gray28', fg='white', font='HELVETICA 20 bold').pack(fill=tk.BOTH, padx=10, pady=(10, 5))
        self._tkvar = tk.StringVar(self.master)
        self._options = ['array_Split()', 'hsplit()', 'vsplit()']
        self._splitMethodBox = tk.OptionMenu(self.master, self._tkvar, *self._options, command=lambda cmd: methodSelect())
        self._tkvar.set(self._options[0])
        self._splitMethodBox.pack(fill=tk.BOTH, padx=10, pady=5)

        # Entry containing the number of splits to be performed on the array.
        self._label2 = tk.Label(self.master, text='Enter number of splits:', bg='gray28', fg='white', font='HELVETICA 20 bold').pack(fill=tk.BOTH, padx=10, pady=5)
        self._splitVal = tk.StringVar()
        self._splitEntry = tk.Entry(self.master, font='HELVETICA 24 bold', justify='center', textvariable=self._splitVal)
        self._splitEntry.pack(fill=tk.BOTH, padx=10, pady=5)
        self._splitEntry.focus()

        self._frame = tk.Frame(self.master, bg='indianred3')

        # If array_Split() is selected by user, then we can split the array also on a given axis; Not available for the other particular methods.
        self._label3 = tk.Label(self._frame, text='Axis=', bg='gray28', fg='white', font='HELVETICA 20 bold').pack(side=tk.LEFT, fill=tk.X, pady=5)
        self._axisVal = tk.StringVar(self._frame)
        self._axisEntry = tk.Entry(self._frame, font='HELVETICA 24 bold', justify='center', textvariable=self._axisVal)
        self._axisEntry.pack(fill=tk.X, side=tk.RIGHT, pady=5)

        self._frame.pack(fill=tk.X, padx=20, pady=5)

        self._insertButton = tk.Button(self.master, text='INSERT', font='HELVETICA 24 bold', command=lambda: popUp())
        self._insertButton.pack(fill=tk.X, padx=10, pady=5)

        self.master.title('SPLIT:')
        self.master.geometry('400x225')
        self.master.resizable(False, False)
        self.master.minsize(400, 280)
        self.master.config(bg='indianred')
        self.master.bind('<Return>', lambda cmd: popUp())
        self.master.mainloop()

    def sort_(self, master):
        self._sortedArray = np.sort(self.array)
        print(self._sortedArray)

    def filter_(self, master):
        print('[FILTER]')

    # Getter methods.
    def get_NumDimensions(self): return self.numDimensions

    def get_DataType(self): return self.dataType

    def get_Array(self): return self.array

    def get_NumElements(self): return self.numElements

    # Setter methods.
    def set_NumDimensions(self, val): self.numDimensions = val

    def set_DataType(self, val): self.dataType = val

    def set_NumElements(self, val): self.numElements = val


def main():
    master = tk.Tk()
    visualArray = VisualArray(master)
    master.mainloop()


if __name__ == '__main__':
    main()
