# Visual Array Project by Pamal Mangat.
# (Please see GitHub readme file for project description)

"""
Basic Run-down of the program:
1] Initiate a Visual Array (VA) object by passing a (tk.Tk()) tkinter window object into it's constructor (__init())
2] User is prompted for the #dimensions for the array through a prompt window; (This is all completed within the __init__())
3] User is then prompted for #Elements per dimension, via prompt_ArrayShape().
4] Afterwards, the user is prompted for the data type for the array, via prompt_DataType().
5] Finally, user is directed to the arrayHub() window that contains all the respective methods that can be performed on the array.
"""

# Numpy library allows us to create arrays that are much more space efficient and provide better code-optimization.
import numpy as np

# Tkinter library allows us to visualize the the numpy array in a Graphical-User-Interface (GUI).
import tkinter as tk

# Tabulate library is utilized for the console messages and debugging messages printed by the program during execution.
# Provides for a clean console output, and better visual appeal to the user/programmer when debugging or running the program.
from tabulate import tabulate


# Class represents a Numpy array being visualized through a Tkinter window.
class VisualArray:

    # Constructor; Prompts user for for number of dimensions for the array through a small prompt window.
    def __init__(self, master):

        # Array attributes.
        self.array = []
        self.numDimensions = None
        self.numElements = None
        self.dataType = None
        self.shape = None

        # Method transfers user to next GUI if entered dimension is within the range (1-3).
        # Each method will have it's own transfer() method that is unique to that window.
        def transfer():
            try:
                # Try to convert entry to integer value; Handled ValueError with notice Window.
                self.dimension = int(self._dimEntry.get())

                # Check to ensure the entered dimensions are between (1-3).
                if 1 <= self.dimension <= 3:
                    self.set_NumDimensions(self.dimension)
                    self.master.destroy()
                    self.master.quit()

                    # Root tkinter window directs user to next GUI.
                    root = tk.Tk()
                    self.prompt_ArrayShape(root)
                    root.mainloop()

                # Otherwise, it was a valid integer entry, but not within the range of 1-3.
                else:
                    raise ValueError

            # Otherwise, display notice window to user.
            except ValueError:
                self._noticeWindow = tk.Tk()
                self._frame = tk.Frame(self._noticeWindow, relief='solid', borderwidth=4, highlightbackground='white', highlightthickness=4)
                self._frame.config(highlightcolor='gray25', bg='indianred3')

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

        # Tkinter attributes.
        self.master = master

        # Frame holding contents of the window.
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

    # Prompts user for the  Array Shape.
    def prompt_ArrayShape(self, master):

        # Method transfers user to next GUI.
        def transfer():
            self.set_NumElements(self._shapeScale.get())
            self.master.destroy()
            self.master.quit()

            # Create root link to next window.
            root = tk.Tk()
            self.prompt_DataType(root)
            root.mainloop()

        # Window and frame object containing widgets.
        self.master = master
        self._frame = tk.Frame(self.master, bg='indianred3', relief='solid', borderwidth=4, highlightbackground='white', highlightthickness=4, highlightcolor='gray25')

        # Text label @ top of frame.
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

        # Pack and draw in the widgets.
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

        # Method saves selected item from listBox (Data Type) and transfers user to next GUI.
        # Method also initializes the array with the attributes specified by the user,  before entering the arrayHub.
        def transfer():
            self.set_DataType(self._listBox.get(self._listBox.curselection()))
            self.master.destroy()
            self.master.quit()

            # Initiate and create the array with user specified attributes; (Create the array before entering the arrayHub.)
            if self.get_DataType() == 'Integer':
                self.array = np.zeros(shape=(int(self.get_NumDimensions()), int(self.get_NumElements())), dtype='i')
            elif self.get_DataType() == 'Float':
                self.array = np.zeros(shape=(int(self.get_NumDimensions()), int(self.get_NumElements())), dtype='f')
            elif self.get_DataType() == 'Boolean':
                self.array = np.ones((int(self.get_NumDimensions()), int(self.get_NumElements())), dtype=np.bool)
            elif self.get_DataType() == 'String':
                self.array = np.empty([int(self.get_NumDimensions()), int(self.get_NumElements())], dtype="<U20")
                self.x = 0
                # Since numpy creates an uninitialized array of string (empty) by initializing random numbers, we will reset them back to "''" to rep. blank string.
                # Only doing this for visual appearances in the GUI, usually not the most efficient method when working with numpy arrays of fixed size.
                while self.x < self.get_NumElements():
                    self.array[0][self.x] = "''"
                    if self.get_NumDimensions() == 2:
                        self.array[1][self.x] = "''"
                    elif self.get_NumDimensions() == 3:
                        self.array[1][self.x] = "''"
                        self.array[2][self.x] = "''"
                    self.x += 1

            # Log into the console the array's contents; For testing/debugging purposes.
            print(tabulate([[]], headers=['\nArray Attributes:'], tablefmt='presto'))
            print(tabulate([[self.get_NumDimensions(), self.get_NumElements(), self.get_DataType()]], headers=['Dimensions', 'Elements', 'Data Type:'], tablefmt='fancy_grid'))

            print(tabulate([[]], headers=['\nArray Contents:'], tablefmt='presto'))
            self.temp1 = []
            self.x = 0
            self.temp2 = []
            for element in self.array:
                self.x += 1
                self.temp1.append(self.x)
                self.temp2.append(list(element))

            if self.x == 1:
                print(tabulate([[self.temp2[0]]], headers=['Dimension ['+str(self.temp1[0]) + ']'], tablefmt='fancy_grid'))
            elif self.x == 2:
                print(tabulate([[self.temp2[0],self.temp2[1]]],
                               headers=['Dimension ['+str(self.temp1[0])+']', 'Dimension [' + str(self.temp1[1]) + ']'],
                               tablefmt='fancy_grid'))
            elif self.x == 3:
                print(tabulate([[self.temp2[0],self.temp2[1], self.temp2[2]]],
                               headers=['Dimension ['+str(self.temp1[0])+']', 'Dimension [' + str(self.temp1[1]) + ']', 'Dimension [' + str(self.temp1[2]) + ']'],
                               tablefmt='fancy_grid'))

            print(tabulate([[]], headers=['\nPlease See Array Hub window.'], tablefmt='simple'))

            # Direct user to the next screen.
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
            root.mainloop()

        # Update label in arrayHub that shows the selected list element for the user.
        def updateSelection(tag):
            # Bunch of if/else statements to ensure that the address for the selectionLabel for the selected element is coming from the right listbox/dimension.
            if tag == 3 and self._listBox['bg'] == 'azure':
                self.selection = self._listBox.curselection()
                self.msg2 = 'Selected: array[0]' + str(list(self.selection))
            elif tag == 3 and self._listBox2['bg'] == 'azure':
                self.selection = self._listBox2.curselection()
                self.msg2 = 'Selected: array[1]' + str(list(self.selection))
            elif tag == 3 and self._listBox3['bg'] == 'azure':
                self.selection = self._listBox3.curselection()
                self.msg2 = 'Selected: array[2]' + str(list(self.selection))
            elif tag == 2 and self._listBox['bg'] == 'azure':
                self.selection = self._listBox.curselection()
                self.msg2 = 'Selected: array[0]' + str(list(self.selection))
            elif tag == 2 and self._listBox2['bg'] == 'azure':
                self.selection = self._listBox2.curselection()
                self.msg2 = 'Selected: array[1]' + str(list(self.selection))
            elif tag == 2 and self._listBox3['bg'] == 'azure':
                self.selection = self._listBox3.curselection()
                self.msg2 = 'Selected: array[2]' + str(list(self.selection))
            elif tag == 1 and self._listBox['bg'] == 'azure':
                if self.get_NumDimensions() != 1:
                    self.selection = self._listBox.curselection()
                    self.msg2 = 'Selected: array[0]' + str(list(self.selection))
                else:
                    self.selection = self._listBox.curselection()
                    self.msg2 = 'Selected: array' + str(list(self.selection))
            elif tag == 1 and self._listBox2['bg'] == 'azure':
                self.selection = self._listBox2.curselection()
                self.msg2 = 'Selected: array[1]' + str(list(self.selection))
            elif tag == 1 and self._listBox3['bg'] == 'azure':
                self.selection = self._listBox3.curselection()
                self.msg2 = 'Selected: array[2]' + str(list(self.selection))

            # Update the label and the window.
            self.selectionLabel.config(text=self.msg2)
            self.master.after(1, self.selectionLabel.update())

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
            self.msg2 = "You selected: array[" + str(list(self.array.flatten()).index(conv(self.get_DataType()))) + "]"

        elif self.get_NumDimensions() == 2:
            for element in self.array[0]:
                self._listBox.insert(tk.END, element)
            for element in self.array[1]:
                self._listBox2.insert(tk.END, element)

            self._label1.pack(fill=tk.X, expand=True)
            self._listBox.pack(side=tk.LEFT, expand=True, fill=tk.BOTH)
            self._listBox2.pack(side=tk.RIGHT, expand=True, fill=tk.BOTH)

            self.msg2 = "You selected: array[0][" + str(list(self.array.flatten()).index(conv(self.get_DataType()))) + "]"

        else:
            for element in self.array[0]:
                self._listBox.insert(tk.END, element)
            for element in self.array[1]:
                self._listBox2.insert(tk.END, element)
            for element in self.array[2]:
                self._listBox3.insert(tk.END, element)

            self._label1.grid(row=0, column=0, columnspan=3, sticky='nsew')
            self._listBox.grid(row=1, column=0, sticky='nsew', columnspan=1)
            self._listBox2.grid(row=1, column=1, sticky='nsew', columnspan=1)
            self._listBox3.grid(row=1, column=2, sticky='nsew', columnspan=1)

            self.msg2 = "You selected: array[0][" + str(list(self.array.flatten()).index(conv(self.get_DataType()))) + "]"

        self._arrayFrame.pack(fill=tk.BOTH, padx=20, expand=True, pady=5)

        # Draw and pack in the selection label; This label shows the user the selected index of the element from within the listBoxes.
        self.selectionLabel = tk.Label(self._frame, text=self.msg2, font='HELVETICA 14 bold', bg='gray99', fg='black', justify='center')
        self.selectionLabel.config(borderwidth=2, relief='solid', highlightbackground='gray25', highlightthickness=2, highlightcolor='gray25')
        self.selectionLabel.pack(fill=tk.BOTH, padx=20, pady=5, expand=True)

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

                if self.get_DataType() != 'Boolean':
                    self.temp = ("'" + str(self.elementEntry.get()) + "'") if self.get_DataType() == 'String' else str(self.elementEntry.get())

                    if self.get_NumDimensions() == 1:
                        # For visual appeal, we will include the quotation marks around inputed string elements to depict string elements.
                        self.array[0][int(self.indexEntry.get())] = self.temp
                        print(tabulate([[]],
                                       headers=['\nInserted Element [' + self.elementEntry.get() + "] @ Index [" + self.indexEntry.get() + "] in Dimension [1]"],
                                       tablefmt='presto'))

                    elif self.get_NumDimensions() == 2 or 3:
                        self.temp = ("'" + str(self.elementEntry.get()) + "'") if self.get_DataType() == 'String' else str(self.elementEntry.get())
                        if self.tkvar.get() == 'Dimension [1]':
                            self.array[0][int(self.indexEntry.get())] = self.temp
                        elif self.tkvar.get() == 'Dimension [2]':
                            self.array[1][int(self.indexEntry.get())] = self.temp
                        if self.tkvar.get() == 'Dimension [3]':
                            self.array[2][int(self.indexEntry.get())] = self.temp
                        print(tabulate([[]],
                                       headers=['\nInserted Element [' + self.elementEntry.get() + "] @ Index [" + self.indexEntry.get() + "] in " + self.tkvar.get()],
                                       tablefmt='presto'))

                else:
                    self.boolConv = {"True": 1, "False": 0}

                    if self.get_NumDimensions() == 1:
                        self.array[0][int(self.indexEntry.get())] = self.boolConv.get(self.boolVar.get())
                        print(tabulate([[]],
                                       headers=['\nInserted Element [' + self.boolVar.get() + "] @ Index [" + self.indexEntry.get() + "] in Dimension [1]"],
                                       tablefmt='presto'))

                    elif self.get_NumDimensions() == 2 or 3:
                        if self.tkvar.get() == 'Dimension [1]':
                            self.array[0][int(self.indexEntry.get())] = self.boolConv.get(self.boolVar.get())
                        elif self.tkvar.get() == 'Dimension [2]':
                            self.array[1][int(self.indexEntry.get())] = self.boolConv.get(self.boolVar.get())
                        if self.tkvar.get() == 'Dimension [3]':
                            self.array[2][int(self.indexEntry.get())] = self.boolConv.get(self.boolVar.get())

                    print(tabulate([[]],
                                   headers=['\nInserted Element [' + self.boolVar.get() + "] @ Index [" + self.indexEntry.get() + "] in " + self.tkvar.get()],
                                   tablefmt='presto'))

                self.master.destroy()
                self.master.quit()
                root = tk.Tk()
                self.arrayHub(root)
                root.mainloop()

            except ValueError:
                # Display an error window if the entered element/index cannot be added into the array.
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

            except IndexError:
                # Display an error window if the index specified by the user is invalid.
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

        self.label1 = tk.Label(self.alpha, text='Insert Element:', bg='gray28', fg='white', font='HELVETICA 20 bold')
        self.label1.pack(fill=tk.X, padx=20, pady=20)

        # If the data type selected is boolean, than the user may only pick from the True/False options from drop-down box for the element.
        if self.get_DataType() != 'Boolean':
            self.elementEntry = tk.Entry(self.alpha, font='HELVETICA 24 bold', justify='center', textvariable=self.element)
            self.elementEntry.pack(fill=tk.X, padx=20)
            self.elementEntry.focus()

        else:
            self.boolVar = tk.StringVar(self.alpha)
            self.options2 = ['True', 'False']
            self.boolVar.set(self.options2[0])
            self.elementBox = tk.OptionMenu(self.alpha, self.boolVar, *self.options2)
            self.elementBox.pack(fill=tk.BOTH, padx=20)

        # If the dimension isn't 1, then a drop-down menu will be presented to the user to selected which dimension to enter element in.
        if self.get_NumDimensions() != 1:
            self.alpha.after(1, self.alpha.minsize(400, 400))
            self.tkvar = tk.StringVar()
            self.options = []
            x = 0
            while x < int(self.get_NumDimensions()):
                x += 1
                self.options.append(str('Dimension [' + str(x) + "]"))
            self.label2 = tk.Label(self.alpha, text='Select Dimension: ', bg='gray28', fg='white', font='HELVETICA 20 bold', )
            self.label2.pack(fill=tk.X, padx=20, pady=20)

            self.tkvar = tk.StringVar(self.alpha)
            self.tkvar.set(self.options[0])
            self.dimensionBox = tk.OptionMenu(self.alpha, self.tkvar, *self.options).pack(fill=tk.BOTH, padx=20)

        self.label3 = tk.Label(self.alpha, text='@ Index: ', bg='gray28', fg='white', font='HELVETICA 20 bold', )
        self.label3.pack(fill=tk.X, padx=20, pady=20)
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
                if self.get_NumDimensions() == 1:
                    print(tabulate([[]],
                                   headers=['\nDeleted Element [' + str(self.array[0][int(self.indexDeleteEntry.get())]) + "] @ Index [" + self.indexDeleteEntry.get() + "] in Dimension [1]"],
                                   tablefmt='presto'))
                    self.array[0][int(self.indexDeleteEntry.get())] = self.nullConv.get(self.get_DataType())

                elif self.get_NumDimensions() != 1:
                    if self.tkvar.get() == 'Dimension [1]':
                        print(tabulate([[]],
                                       headers=['\nDeleted Element [' + str(self.array[0][int(self.indexDeleteEntry.get())]) + "] @ Index [" + self.indexDeleteEntry.get() + "] in" + self.tkvar.get()],
                                       tablefmt='presto'))
                        self.array[0][int(self.indexDeleteEntry.get())] = self.nullConv.get(self.get_DataType())

                    elif self.tkvar.get() == 'Dimension [2]':
                        print(tabulate([[]],
                                       headers=['\nDeleted Element [' + str(self.array[1][int(self.indexDeleteEntry.get())]) + "] @ Index [" + self.indexDeleteEntry.get() + "] in" + self.tkvar.get()],
                                       tablefmt='presto'))
                        self.array[1][int(self.indexDeleteEntry.get())] = self.nullConv.get(self.get_DataType())
                    elif self.tkvar.get() == 'Dimension [3]':
                        print(tabulate([[]],
                                       headers=['\nDeleted Element [' + str(self.array[2][int(self.indexDeleteEntry.get())]) + "] @ Index [" + self.indexDeleteEntry.get() + "] in" + self.tkvar.get()],
                                       tablefmt='presto'))
                        self.array[2][int(self.indexDeleteEntry.get())] = self.nullConv.get(self.get_DataType())

                self.master.destroy()
                self.master.quit()
                tunnel = tk.Tk()
                self.arrayHub(tunnel)
                tunnel.mainloop()

            except IndexError:
                self.indexError_Window = tk.Tk()

                self.label10 = tk.Label(self.indexError_Window, text='Invalid index specified. Either the index you\nentered was out of bounds, or does not exist')
                self.label10.config(bg='indianred', fg='white', font='HELVETICA 14 bold')
                self.label10.pack(fill=tk.X, padx=30, pady=(25, 10))

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
                self.label10 = tk.Label(self._valErrorWindow, text='Please try a different value again.')
                self.label10.config(bg='indianred', fg='white', font='HELVETICA 14 bold')
                self.label10.pack(fill=tk.X, padx=30)

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

        self.label1 = tk.Label(self.alpha, text='Delete Index:', bg='gray28', fg='white', font='HELVETICA 20 bold')
        self.label1.pack(fill=tk.X, padx=20, pady=20)
        self.indexDeleteEntry = tk.Entry(self.alpha, font='HELVETICA 24 bold', justify='center')
        self.indexDeleteEntry.pack(fill=tk.X, padx=20)
        self.indexDeleteEntry.focus()

        # If more than one dimension is present, than a drop-down menu must be presented to the user to specify which dimension to delete element from.
        if self.get_NumDimensions() != 1:
            self.alpha.geometry('400x280')
            self.alpha.minsize(400, 280)
            self.tkvar = tk.StringVar()
            self.options = []
            x = 0
            while x < int(self.get_NumDimensions()):
                x += 1
                self.options.append(str('Dimension [' + str(x) + "]"))
            self.label2 = tk.Label(self.alpha, text='Select Dimension: ', bg='gray28', fg='white', font='HELVETICA 20 bold', )
            self.label2.pack(fill=tk.X, padx=20, pady=20)

            self.tkvar = tk.StringVar(self.alpha)
            self.tkvar.set(self.options[0])
            self.dimensionBox = tk.OptionMenu(self.alpha, self.tkvar, *self.options).pack(fill=tk.BOTH, padx=20)

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
                self.displaySearch_Window.destroy()
                root = tk.Tk()
                self.search(root)
                root.mainloop()

            try:
                if self.get_DataType() == 'Boolean':
                    self.searchedIndex = np.where(self.array == bool(self.indexSearchEntry.get()))
                elif self.get_DataType() == 'String':
                    self.searchedIndex = np.where(self.array == "'" + str(self.indexSearchEntry.get()) + "'")
                elif self.get_DataType() == 'Float':
                    self.searchedIndex = np.where(self.array == float(self.indexSearchEntry.get()))
                elif self.get_DataType() == 'Integer':
                    self.searchedIndex = np.where(self.array == int(self.indexSearchEntry.get()))

                self.searchedElement = self.indexSearchEntry.get()

                # Output to console the search message.

                self.searchZip = list(zip(self.searchedIndex[0], self.searchedIndex[1]))
                self.x = 0
                self.dimensions = []
                self.indexes = []

                # Iterate through search results and add the index and dimension to their own respective lists to be printed back to the user.
                # We need to alter the dimension that is returned, by adding 1 so that dimension 1 is 1 not 0. (Due to python indexing by zero)
                for result in self.searchZip:
                    self.x += 1
                    self.dimensions.append(result[0] + 1)
                    self.indexes.append(result[1])

                self.zip = zip(self.indexes, self.dimensions)

                print(tabulate([[]], headers=['\nSearched for element [' + str(self.indexSearchEntry.get()) + '] within the array.'], tablefmt='presto'))
                print('[Search results below]:')
                print(tabulate([*self.zip], headers=['Index', 'Dimension'], tablefmt='fancy_grid'))
                print('Total Occurences: [' +  str(self.x) + "].")

                # Close current window and display the search results in new window.
                self.alpha.destroy()

                self.displaySearch_Window = tk.Tk()

                self.label1 = tk.Label(self.displaySearch_Window, text='Search results for Element [' + str(self.searchedElement) + "]: ")
                self.label1.pack(fill=tk.BOTH, padx=10, pady=10, expand=True)

                self.resultBox = tk.Listbox(self.displaySearch_Window, justify='center', font='VERDANA 26 bold', selectborderwidth=1, bg='bisque')

                self.y = 0
                if self.get_NumDimensions() == 1:
                    for result in self.indexes:
                        self.resultBox.insert(tk.END, 'array[' + str(result) + "]")
                else:
                    for result in self.dimensions:
                        self.resultBox.insert(tk.END, 'array[' + str(result-1) + "][" + str(self.indexes[self.y]) + "]")
                        self.y += 1

                self.resultBox.select_set(0)

                self.resultBox.pack(fill=tk.BOTH, padx=10, pady=10, expand=True)

                self._bottomFrame = tk.Frame(self.displaySearch_Window, bg='indianred')
                self.searchAgainButton = tk.Button(self._bottomFrame, text='NEW SEARCH', font='HELVETICA 24 bold', width=10, command=lambda: searchAgainBind())
                self.searchAgainButton.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
                self.doneButton = tk.Button(self._bottomFrame, text='DONE', font='HELVETICA 24 bold', width=10, command=lambda: self.displaySearch_Window.destroy())
                self.doneButton.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)
                self._bottomFrame.pack(fill=tk.BOTH, padx=10, pady=10)

                self.displaySearch_Window.title('Search Complete')
                self.displaySearch_Window.minsize(400, 225)
                self.displaySearch_Window.config(bg='indianred')
                self.displaySearch_Window.resizable(False, False)
                self.displaySearch_Window.mainloop()

            except ValueError:
                self.ValueError_Window = tk.Tk()
                self.label14 = tk.Label(self.ValueError_Window, text='Could not locate the element:')
                self.label14.config(bg='indianred', fg='white', font='HELVETICA 22 bold')
                self.label14.pack(fill=tk.X, padx=10, pady=(20, 0))
                self.label15 = tk.Label(self.ValueError_Window, text='[' + str(self.indexSearchEntry.get()) + ']')
                self.label15.config(bg='gray24', fg='thistle', font='HELVETICA 20 bold')
                self.label15.pack(fill=tk.X, padx=25, pady=10)
                self.label16 = tk.Label(self.ValueError_Window, text='within the specified array.')
                self.label16.config(bg='indianred', fg='white', font='HELVETICA 20 bold')
                self.label16.pack(fill=tk.X, padx=10)
                self.closeButton = tk.Button(self.ValueError_Window, text='CLOSE', width=20, font='HELVETICA 22 bold', command=lambda: self.ValueError_Window.destroy())
                self.closeButton.pack(fill=tk.X, padx=20, pady=20)
                self.ValueError_Window.title('Value Error:')
                self.ValueError_Window.minsize(400, 225)
                self.ValueError_Window.resizable(False, False)
                self.ValueError_Window.config(bg='indianred')
                self.ValueError_Window.bind('<Return>', lambda cmd: self.ValueError_Window.destroy())
                self.ValueError_Window.mainloop()

        self.alpha = master

        self.label1 = tk.Label(self.alpha, text='Search for element:', bg='gray28', fg='white', font='HELVETICA 20 bold')
        self.label1.pack(fill=tk.X, padx=20, pady=20)
        self.indexSearchEntry = tk.Entry(self.alpha, font='HELVETICA 24 bold', justify='center')
        self.indexSearchEntry.pack(fill=tk.X, padx=20)
        self.indexSearchEntry.focus()

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

    def split_(self, master):
        self.master = master



        self.master.title('Split:')
        self.master.geometry('400x225')
        self.master.resizable(False, False)
        self.master.minsize(400, 225)
        self.master.config(bg='indianred')
        self.master.mainloop()

    # Getter.
    def get_NumDimensions(self):
        return self.numDimensions

    # Getter.
    def get_DataType(self):
        return self.dataType

    # Getter.
    def get_Array(self):
        return self.array

    # Getter.
    def get_NumElements(self):
        return self.numElements

    # Setter.
    def set_NumDimensions(self, val):
        self.numDimensions = val

    # Setter.
    def set_DataType(self, val):
        self.dataType = val

    # Setter.
    def set_NumElements(self, val):
        self.numElements = val


def main():
    # Initialize Visual Array object by passing in a tkinter (Tk()) window into the constructor.
    master = tk.Tk()
    visualArray = VisualArray(master)
    master.mainloop()


# Execute program. 
if __name__ == '__main__':
    main()
