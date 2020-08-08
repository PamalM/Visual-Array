import tkinter as tk
import numpy as np


# Class represents a Numpy array being visualized through a Tkinter window.
# noinspection PyAttributeOutsideInit
class VisualArray:

    # Constructor; Prompts user for for number of dimensions for the array.
    def __init__(self, master):

        # Array attributes (Initially set to None/Empty).
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
                self._label = tk.Label(self._noticeWindow, text='Invalid Dimension Selected!', font='HELVETICA 26 bold', bg='gray20', fg='white').pack(fill=tk.X, pady=20, padx=20)
                self._label2 = tk.Label(self._noticeWindow, text='Please select a dimension between 1 and 3.', font='HELVETICA 18', bg='salmon', fg='white').pack()
                self._label3 = tk.Label(self._noticeWindow, text='You have entered: ' + self._dimEntry.get(), bg='gray20', fg='white', font='HELVETICA 14 italic').pack(pady=20)
                self._closeButton = tk.Button(self._noticeWindow, text='CLOSE', font='HELVETICA 24 bold', command=lambda: self._noticeWindow.destroy())
                self._closeButton.pack(fill=tk.X, padx=10, pady=10)

                # Notice window attributes.
                self._noticeWindow.configure(bg='salmon')
                self._noticeWindow.geometry('400x250')
                self._noticeWindow.resizable(False, False)
                self._noticeWindow.bind('<Return>', lambda cmd: self._noticeWindow.destroy())
                self._noticeWindow.title('Notice!')
                self._noticeWindow.mainloop()

        # Tkinter attributes.
        self.master = master

        # Frame holding contents of the window.
        self._frame = tk.Frame(self.master, bg='indianred3')
        self._frame.grid_columnconfigure(0, weight=1)
        self._frame.grid_rowconfigure(0, weight=1)
        self._frame.grid_rowconfigure(1, weight=1)
        self._frame.grid_rowconfigure(2, weight=1)
        self._frame.grid_rowconfigure(3, weight=1)

        self._label1 = tk.Label(self._frame, text='Enter number of dimensions:', font='Helvetica 40 bold', bg='indianred3', fg='white', relief=tk.FLAT)
        self._label1.grid(row=0, column=0, sticky='nsew', padx=10, pady=5)

        # Dimension entry to hold the number of dimensions from user.
        self._dimEntry = tk.Entry(self._frame, font=('Helvetica', 90, 'bold'), justify='center', textvariable=tk.StringVar(), relief=tk.RAISED)
        self._dimEntry.grid(row=1, column=0, sticky='nsew', padx=20, pady=20)

        # Set the focus of the window to the entry bar.
        self._dimEntry.focus()

        self._label2 = tk.Label(self._frame, text='(Please select between 1 to 3 dimensions.)', bg='indianred3', fg='lightcyan', font='Helvetica 12 bold', relief=tk.FLAT)
        self._label2.grid(row=2, column=0, sticky='nsew', padx=20, pady=5)

        # Button to direct user to next GUI.
        self._nextButton = tk.Button(self._frame, text='NEXT', font='Helvetica 60 bold', relief=tk.RAISED, command=lambda: transfer())
        self._nextButton.grid(row=3, column=0, sticky='nsew', padx=20, pady=20)

        # Pack/Draw the frame into the window.
        self._frame.pack(fill=tk.BOTH, padx=14, pady=14, expand=True)

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

        self.master = master
        self._frame = tk.Frame(self.master, bg='indianred3')

        self._label1 = tk.Label(self._frame, text='SELECT THE NUMBER OF ELEMENTS PER DIMENSION:', font='HELVETICA 20 bold', bg='salmon', fg='white', relief=tk.FLAT)
        self._label1.pack(expand=True, fill=tk.BOTH, padx=10, pady=10)

        self._shapeScale = tk.Scale(self._frame, from_=1, to=10, orient=tk.HORIZONTAL, activebackground='yellow', tickinterval=9, relief=tk.RAISED)
        self._shapeScale.config(background='gray20', fg='white', font='HELVETICA 24 bold', sliderlength=100, sliderrelief=tk.GROOVE)
        self._shapeScale.pack(expand=True, fill=tk.BOTH, padx=10, pady=10)
        self._shapeScale.focus()

        # Button to direct user to next GUI.
        self._nextButton = tk.Button(self._frame, text='NEXT', font='Helvetica 60 bold', command= lambda: transfer(), relief=tk.RAISED)
        self._nextButton.pack(expand=True, fill=tk.BOTH, padx=10, pady=10)

        self._frame.pack(fill=tk.BOTH, padx=14, pady=14, expand=True)

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
        def transfer():
            self.set_DataType(self._listBox.get(self._listBox.curselection()))
            self.master.destroy()
            self.master.quit()

            # Dictionary to hold the numpy data types and translates user selection from listbox to numpy data type.
            typeConv = {'Integer': 'i', 'Boolean': 'b', 'Float': 'f', 'String': 'S'}

            # Initiate and create the array with user specified attributes; (Create the array before entering the arrayHub.)
            self.array = np.zeros(shape=(int(self.get_NumDimensions()), int(self.get_NumElements())), dtype=int)

            # Direct user to the next screen.
            root = tk.Tk()
            self.arrayHub(root)
            root.mainloop()

        self.master = master
        self._frame = tk.Frame(self.master, bg='indianred3')
        self._frame.grid_columnconfigure(0, weight=1)
        self._frame.grid_rowconfigure(0, weight=1)
        self._frame.grid_rowconfigure(1, weight=1)
        self._frame.grid_rowconfigure(2, weight=1)

        self._label1 = tk.Label(self._frame, text='Select Data Type:', font='Helvetica 40 bold', bg='indianred3', fg='white')
        self._label1.grid(row=0, column=0, sticky='nsew', padx=20, pady=20)

        # Present user with list of options of data types to select from.
        self._listBox = tk.Listbox(self._frame, justify='center', cursor='dot', bg='mintcream', fg='lightslateblue', font='HELVETICA 20 bold')
        self._listBox.config(selectbackground='oldlace', relief='raised', selectmode='single', height=4)
        self._listBox.insert(1, 'Integer')
        self._listBox.insert(2, 'Boolean')
        self._listBox.insert(3, 'Float')
        self._listBox.insert(4, 'String')
        self._listBox.select_set(0)
        self._listBox.grid(row=1, column=0, sticky='nsew', padx=20, pady=20)
        self._listBox.focus()

        # Button to direct user to next GUI.
        self._nextButton = tk.Button(self._frame, text='NEXT', font='Helvetica 60 bold', command=lambda: transfer())
        self._nextButton.grid(row=2, column=0, sticky='nsew', padx=20, pady=20)

        self._frame.pack(fill=tk.BOTH, padx=14, pady=14, expand=True)

        # Window attributes.
        self.master.title('Visual Array')
        self.master.configure(bg='gray25')
        self.master.minsize(600, 375)
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

        # Method destroys array hub window and restarts application.
        def restart():
            self.master.destroy()
            self.master.quit()
            root = tk.Tk()
            self.__init__(root)
            root.mainloop()

        self.master = master
        self._frame = tk.Frame(self.master, bg='indianred3')

        # Frame holds the listBoxes for each dimension. (Displays array's contents)
        self._arrayFrame = tk.Frame(self._frame, bg='indianred')
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

        # Pack in other listbox widgets depending on dimensions specified by user.
        if self.get_NumDimensions() == 1:
            # Fill the first dimensional listBox with content from self.array[0].
            for element in np.nditer(self.array):
                self._listBox.insert(tk.END, element)

            self._label1.pack(fill=tk.X, expand=True)
            self._listBox.pack(fill=tk.BOTH, expand=True)

            self.msg2 = "You selected: array[" + str(list(self.array.flatten()).index(int(self._listBox.get('active')))) + "]"
            self.selectionLabel = tk.Label(self._frame, text=self.msg2, font='HELVETICA 14 bold', bg='lightyellow', fg='black')

        elif self.get_NumDimensions() == 2:
            for element in self.array[0]:
                self._listBox.insert(tk.END, element)
            for element in self.array[1]:
                self._listBox2.insert(tk.END, element)

            self._label1.pack(fill=tk.X, expand=True)
            self._listBox.pack(side=tk.LEFT, expand=True, fill=tk.BOTH)
            self._listBox2.pack(side=tk.RIGHT, expand=True, fill=tk.BOTH)

            self.msg2 = "You selected: array[0][" + str(list(self.array.flatten()).index(int(self._listBox.get('active')))) + "]"
            self.selectionLabel = tk.Label(self._frame, text=self.msg2, font='HELVETICA 14 bold', bg='lightyellow', fg='black')

        else:
            for element in self.array[0]:
                self._listBox.insert(tk.END, element)
            for element in self.array[1]:
                self._listBox2.insert(tk.END, element)
            for element in self.array[2]:
                self._listBox3.insert(tk.END, element)

            self._label1.grid(row=0, column=0, columnspan=3, sticky='ew')
            self._listBox.grid(row=1, column=0, sticky='nsew', columnspan=1)
            self._listBox2.grid(row=1, column=1, sticky='nsew', columnspan=1)
            self._listBox3.grid(row=1, column=2, sticky='nsew', columnspan=1)

            self.msg2 = "You selected: array[0][" + str(list(self.array.flatten()).index(int(self._listBox.get('active')))) + "]"
            self.selectionLabel = tk.Label(self._frame, text=self.msg2, font='HELVETICA 14 bold', bg='lightyellow', fg='black')

        self._arrayFrame.pack(fill=tk.BOTH, padx=20, expand=True, pady=5)
        self.selectionLabel.pack(fill=tk.BOTH, padx=20, pady=5, expand=True)

        # Frame containing buttons with methods to perform on the given array.
        self._methodsFrame = tk.Frame(self._frame, bg='indianred3')

        self._label2 = tk.Label(self._methodsFrame, text='Array Methods:', fg='white', bg='black', font='Helvetica 24 bold')
        self._label2.grid(row=0, column=0, columnspan=3, sticky='ew')

        self._methodsFrame.grid_columnconfigure(0, weight=1)
        self._methodsFrame.grid_columnconfigure(1, weight=1)
        self._methodsFrame.grid_columnconfigure(2, weight=1)
        self._methodsFrame.grid_rowconfigure(0, weight=1)
        self._methodsFrame.grid_rowconfigure(1, weight=1)
        self._methodsFrame.grid_rowconfigure(2, weight=1)

        # Array Method Buttons.
        self.insertButton = tk.Button(self._methodsFrame, text='INSERT', font='HELVETICA 30 bold', width=20, command=lambda: terminal(1)).grid(row=1, column=0, sticky='nsew')
        self.deleteButton = tk.Button(self._methodsFrame, text='DELETE', font='HELVETICA 30 bold', width=20, command=lambda: terminal(2)).grid(row=2, column=0, sticky='nsew')
        self.searchButton = tk.Button(self._methodsFrame, text='SEARCH', font='HELVETICA 30 bold', width=20, command=lambda: terminal(3)).grid(row=1, column=1, sticky='nsew')
        self.splitButton = tk.Button(self._methodsFrame, text='SPLIT', font='HELVETICA 30 bold', width=20, command=lambda: terminal(4)).grid(row=2, column=1, sticky='nsew')
        self.sortButton = tk.Button(self._methodsFrame, text='SORT', font='HELVETICA 30 bold', width=20).grid(row=1, column=2, sticky='nsew')
        self.filterButton = tk.Button(self._methodsFrame, text='FILTER', font='HELVETICA 30 bold', width=20).grid(row=2, column=2, sticky='nsew')

        self._methodsFrame.pack(fill=tk.BOTH, padx=20, expand=True, pady=5)

        # Pre-select the first item in the first dimension from listbox.
        self._listBox.select_set(0)

        # Bottom frame containing array's attributes and a new array button.
        self._bottomFrame = tk.Frame(self._frame, bg='gray25')
        self.newArrayButton = tk.Button(self._bottomFrame, text='NEW ARRAY', font='HELVETICA 30 bold', width=20, command=lambda: restart())
        self.newArrayButton.pack(side=tk.RIGHT, padx=60)

        # Label containing attributes of the array.
        self.msg = 'Number of Dimensions: ' + str(self.get_NumDimensions()) + '\nType of data: ' + str(self.get_DataType()) + '\n[' + str(self._listBox.size()) + '] # of elements.'
        self.arrayAttributeLabel = tk.Label(self._bottomFrame, text=self.msg, bg='gray25', fg='white', font='HELVETICA 18')
        self.arrayAttributeLabel.pack(side=tk.LEFT, padx=60)

        self._bottomFrame.pack(fill=tk.BOTH, padx=20, expand=True, pady=5)

        self._frame.pack(fill=tk.BOTH, padx=14, pady=14, expand=True)

        # Window attributes.
        self.master.config(bg='gray25')
        self.master.title('Visual Array Hub')
        self.master.geometry('875x525')
        self.master.minsize(875, 660)
        # These bindings to the window ensure that the window is being updated immediately, and displaying the correct selection from listBoxes.
        self._listBox.bind('<<ListboxSelect>>', lambda cmd: tagger(1))
        self._listBox2.bind('<<ListboxSelect>>', lambda cmd: tagger(2))
        self._listBox3.bind('<<ListboxSelect>>', lambda cmd: tagger(3))
        self.master.mainloop()

    # Method inserts element at given location in array.
    def insert(self, master):

        def add():
            try:
                np.insert(self.array, int(self.indexEntry.get()), int(self.elementEntry.get()))
                print('Inserted [' + str(self.elementEntry.get()) + '] @ Index ' + str(self.indexEntry.get()))
                print(self.array)
                self.master.destroy()
                self.master.quit()
                root = tk.Tk()
                self.arrayHub(root)
                root.mainloop()
            except ValueError:
                # Display an error window if the entered element/index cannot be added into the array.
                self.valError_Window = tk.Tk()

                self.label9 = tk.Label(self.valError_Window, text='You have entered a value for the element \nor index that cannot be inserted into the array.')
                self.label9.config(bg='indianred', fg='white', font='HELVETICA 14 bold')
                self.label9.pack(fill=tk.X, padx=30, pady=(25, 10))
                self.label10 = tk.Label(self.valError_Window, text='Please try again, using a different value.', bg='indianred', fg='white', font='HELVETICA 14 bold')
                self.label10.pack(fill=tk.X, padx=30)

                self.closeButton = tk.Button(self.valError_Window, text='CLOSE', font='HELVETICA 24 bold', command=lambda: self.valError_Window.destroy())
                self.closeButton.pack(fill=tk.X, padx=20, pady=(10, 0))

                self.valError_Window.config(bg='indianred')
                self.valError_Window.geometry('375x175')
                self.valError_Window.minsize(300, 175)
                self.valError_Window.title('Value Error!')
                self.valError_Window.resizable(False, False)
                self.valError_Window.bind('<Return>', lambda cmd: self.valError_Window.destroy())
                self.valError_Window.mainloop()

        # String variables to hold given array and element entered by user.
        self.element = tk.StringVar()
        self.dimension = tk.StringVar()
        self.index = tk.StringVar()

        self.alpha = master

        self.label1 = tk.Label(self.alpha, text='Insert Element:', bg='gray28', fg='white', font='HELVETICA 20 bold')
        self.label1.pack(fill=tk.X, padx=20, pady=20)
        self.elementEntry = tk.Entry(self.alpha, font='HELVETICA 24 bold', justify='center', textvariable=self.element)
        self.elementEntry.pack(fill=tk.X, padx=20)
        self.elementEntry.focus()

        if self.get_NumDimensions() != 1:
            self.alpha.after(1, self.alpha.minsize(400, 400))
            self.tkvar = tk.StringVar()
            self.options = []
            x = 0
            while x < int(self.get_NumDimensions()):
                x += 1
                self.options.insert(x-1, str('Dimension [' + str(x) + "]"))
            self.label2 = tk.Label(self.alpha, text='Select Dimension: ', bg='gray28', fg='white', font='HELVETICA 20 bold', )
            self.label2.pack(fill=tk.X, padx=20, pady=20)
            self.dimensionBox = tk.OptionMenu(self.alpha, self.tkvar, self.options).pack(fill=tk.X, padx=20)

        self.label3 = tk.Label(self.alpha, text='@ Index: ', bg='gray28', fg='white', font='HELVETICA 20 bold', )
        self.label3.pack(fill=tk.X, padx=20, pady=20)
        self.indexEntry = tk.Entry(self.alpha, font='HELVETICA 24 bold', justify='center', textvariable=self.index)
        self.indexEntry.pack(fill=tk.X, padx=20)
        self.insertButton = tk.Button(self.alpha, text='INSERT', font='HELVETICA 24 bold', command=lambda: add())
        self.insertButton.pack(fill=tk.X, padx=20, pady=20)

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
                self.elementRemoved = self.array.pop(int(self.indexDeleteEntry.get()))
                print('Deleted element [' + str(self.elementRemoved) + '] @ Index [' + str(self.indexDeleteEntry.get()) + "]")
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
                self.valError_Window = tk.Tk()

                self.label9 = tk.Label(self.valError_Window, text='You have entered an index value\nthat cannot be removed from the array.')
                self.label9.config(bg='indianred', fg='white', font='HELVETICA 14 bold')
                self.label9.pack(fill=tk.X, padx=30, pady=(25, 10))
                self.label10 = tk.Label(self.valError_Window, text='Please try a different value again.')
                self.label10.config(bg='indianred', fg='white', font='HELVETICA 14 bold')
                self.label10.pack(fill=tk.X, padx=30)

                self.closeButton = tk.Button(self.valError_Window, text='CLOSE', font='HELVETICA 24 bold', command=lambda: self.valError_Window.destroy())
                self.closeButton.pack(fill=tk.X, padx=20, pady=(10, 0))

                self.valError_Window.config(bg='indianred')
                self.valError_Window.geometry('375x175')
                self.valError_Window.minsize(300, 175)
                self.valError_Window.title('Value Error!')
                self.valError_Window.resizable(False, False)
                self.valError_Window.bind('<Return>', lambda cmd: self.valError_Window.destroy())
                self.valError_Window.mainloop()

        self.alpha = master

        # String variable holds the index to be deleted.
        self.index = tk.StringVar()

        self.label1 = tk.Label(self.alpha, text='Delete Index:', bg='gray28', fg='white', font='HELVETICA 20 bold')
        self.label1.pack(fill=tk.X, padx=20, pady=20)
        self.indexDeleteEntry = tk.Entry(self.alpha, font='HELVETICA 24 bold', justify='center')
        self.indexDeleteEntry.pack(fill=tk.X, padx=20)
        self.indexDeleteEntry.focus()
        self.deleteButton = tk.Button(self.alpha, text='DELETE', font='HELVETICA 24 bold', command=lambda: remove())
        self.deleteButton.pack(fill=tk.X, padx=20, pady=20)

        self.alpha.geometry('400x225')
        self.alpha.title('INSERT:')
        self.alpha.config(bg='indianred')
        self.alpha.minsize(400, 225)
        self.alpha.bind('<Return>', lambda cmd: remove())
        self.alpha.resizable(False, False)
        self.alpha.mainloop()

    # Method searches array for specified element from user.
    def search(self, master):
        # Method find's element in given array.
        def find():

            def searchBind():
                self.displaySearch_Window.destroy()
                self.search()

            try:
                self.searchedIndex = self.array.index(self.indexSearchEntry.get())
                self.searchedElement = self.indexSearchEntry.get()
                print('Element [' + str(self.indexSearchEntry.get()) + '] found @ index: ' + str(self.searchedIndex))
                self.alpha.destroy()

                self.displaySearch_Window = tk.Tk()

                self.label12 = tk.Label(self.displaySearch_Window, text='Element: ' + str(self.searchedElement), bg='black', fg='white', font='HELVETICA 44 bold')
                self.label12.pack(fill=tk.X, padx=10, pady=(10, 10))

                self.label13 = tk.Label(self.displaySearch_Window, text='Index: ' + str(self.searchedIndex), bg='gray20', fg='white', font='HELVETICA 54 bold')
                self.label13.pack(fill=tk.X, padx=10)

                self._bottomFrame = tk.Frame(self.displaySearch_Window, bg='indianred')

                self.searchAgainButton = tk.Button(self._bottomFrame, text='SEARCH', font='HELVETICA 24 bold', width=10, command=lambda: searchBind())
                self.searchAgainButton.pack(side=tk.LEFT, fill=tk.X)

                self.doneButton = tk.Button(self._bottomFrame, text='DONE', font='HELVETICA 24 bold', width=10, command=lambda: self.displaySearch_Window.destroy())
                self.doneButton.pack(side=tk.RIGHT, fill=tk.X, padx=1)

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
        self.searchButton = tk.Button(self.alpha, text='SEARCH', font='HELVETICA 24 bold', command=lambda: find())
        self.searchButton.pack(fill=tk.X, padx=20, pady=20)

        # Search window attributes.
        self.alpha.geometry('400x225')
        self.alpha.title('Search:')
        self.alpha.config(bg='indianred')
        self.alpha.minsize(400, 225)
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
