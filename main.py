import tkinter as tk
import numpy as np


# Class represents a Numpy array being visualized through a Tkinter window.
class VisualArray:

    # Constructor; Prompts user for for number of dimensions for array.
    def __init__(self, master):

        # Array attributes.
        self.numDimensions = None
        self.dataType = None
        self.array = []
        self.shape = 1   # Shape of array = (numDimensions, shape); Default=1

        # Tkinter attributes.
        self.master = master
        self.listBox = tk.Listbox()
        self.arrayFrame = tk.Frame()
        self.methodsFrame = tk.Frame()
        self.scrollbar = tk.Scrollbar()
        self.insertButton = tk.Button()
        self.deleteButton = tk.Button()
        self.searchButton = tk.Button()
        self.splitButton = tk.Button()
        self.sortButton = tk.Button()
        self.filterButton = tk.Button()
        self.newArrayButton = tk.Button()
        self.arrayAttributeLabel = tk.Label()
        self.msg = None
        self.shapeScale = tk.Scale()

        # Method checks to ensure that the number of dimensions entered by the user is between (1-3).
        # If valid, direct user to next screen; Else, display a notice window.
        def valid_Dimension():
            try:
                self.dimension = int(self.dimEntry.get())

                # Check to ensure the entered dimensions are between (1-3).
                if 1 <= self.dimension <= 3:
                    self.set_NumDimensions(self.dimension)
                    self.master.destroy()
                    self.master.quit()

                    # Direct user to the next GUI to receive the data type for the array.
                    root = tk.Tk()
                    self.prompt_DataType(root)
                    root.mainloop()

                else:
                    # The entry was a valid int, but not within the range (1-3); Direct user to notice window.
                    raise ValueError

            except ValueError:
                # Otherwise, display notice window to user. 
                self.noticeWindow = tk.Tk()
                self.label1_ = tk.Label(self.noticeWindow, text='Invalid Dimension Selected!', font='HELVETICA 26 bold', bg='gray20', fg='white').pack(fill=tk.X, pady=20, padx=20)
                self.label2_ = tk.Label(self.noticeWindow, text='Please select a dimension between 1 and 3.', font='HELVETICA 18', bg='salmon', fg='white').pack()
                self.label3_ = tk.Label(self.noticeWindow, text='You have entered: ' + self.dimEntry.get(), bg='gray20', fg='white', font='HELVETICA 14 italic').pack(pady=20)
                self.closeButton = tk.Button(self.noticeWindow, text='CLOSE', font='HELVETICA 24 bold', command=lambda: self.noticeWindow.destroy())
                self.closeButton.pack(fill=tk.X, padx=10, pady=10)

                # Notice window attributes.
                self.noticeWindow.configure(bg='salmon')
                self.noticeWindow.geometry('400x250')
                self.noticeWindow.resizable(False, False)
                self.noticeWindow.bind('<Return>', lambda: self.noticeWindow.destroy())
                self.noticeWindow.title('Notice!')
                self.noticeWindow.mainloop()

        self.master = master

        # Frame holding text above entry bar.
        self.frame = tk.Frame(self.master, bg='indianred')
        self.label1 = tk.Label(self.frame, text='Enter number of dimensions:', font='Helvetica 40 bold', bg='indianred3', fg='white').pack()
        self.label2 = tk.Label(self.frame, text='Please select between 1 to 3 dimensions.', bg='indianred3', fg='lightcyan', font='Helvetica 12 bold').pack(padx=90)
        self.frame.pack(pady=(40, 20), fill=tk.X)

        # Entry to hold the number of dimensions from user.
        self.dim = tk.StringVar()
        self.dimEntry = tk.Entry(self.master, font=('Helvetica', 90, 'bold'), justify='center', textvariable=self.dim)
        self.dimEntry.pack(fill=tk.X)
        self.dimEntry.focus()

        # Button to direct user to next GUI.
        self.nextButton = tk.Button(self.master, text='NEXT', font='Helvetica 60 bold', command=lambda: valid_Dimension()).pack(fill=tk.X, padx=20, pady=25)

        # dimension_PromptWindow attributes.
        self.master.title('Visual Array')
        self.master.configure(bg='indianred3')
        self.master.geometry('600x400')
        self.master.minsize(600, 400)
        self.master.bind("<Return>", lambda cmd: valid_Dimension())
        self.master.mainloop()

    # Prompts user for data Type for array.
    def prompt_DataType(self, master):

        # Method fetches the selected data type from the listbox.
        # Then, method directs user to next screen to the fetch array shape.
        def selection():
            self.set_DataType(self.listBox.get(self.listBox.curselection()))
            self.master.destroy()
            self.master.quit()

            # Direct user to the next screen.
            root = tk.Tk()
            self.prompt_ArrayShape(root)
            root.mainloop()

        self.master = master

        # Frame holding text above entry bar.
        self.frame = tk.Frame(self.master, bg='indianred3')
        self.label1 = tk.Label(self.frame, text='Select datatype:', font='Helvetica 40 bold', bg='indianred3', fg='white').pack()

        # Present user with list of options of data types to select from.
        self.listBox = tk.Listbox(self.frame, justify='center', cursor='dot', bg='mintcream', fg='lightslateblue', font='HELVETICA 20 bold')
        self.listBox.config(selectbackground='oldlace', relief='raised', selectmode='single', height=4)
        self.listBox.insert(1, 'Integer')
        self.listBox.insert(2, 'Boolean')
        self.listBox.insert(3, 'Float')
        self.listBox.insert(4, 'String')
        self.listBox.select_set(0)
        self.listBox.pack(fill=tk.BOTH, pady=10)
        self.frame.pack(pady=(40, 20), fill=tk.X)
        self.listBox.focus()

        # Button to direct user to next GUI.
        self.nextButton = tk.Button(self.master, text='NEXT', font='Helvetica 60 bold', command=lambda: selection()).pack(fill=tk.X, padx=20, pady=10)

        # dataTypePrompt_Window window attributes.
        self.master.title('Visual Array')
        self.master.configure(bg='indianred3')
        self.master.minsize(600, 375)
        self.master.bind("<Return>", lambda cmd: selection())
        self.master.mainloop()

    # Method prompts user for the shape of the array.
    def prompt_ArrayShape(self, master):

        # Method transfers the user from the array Shape GUI to the array hub GUI.
        def transfer():
            self.master.destroy()
            self.master.quit()
            root = tk.Tk()
            self.arrayHub(root)
            root.mainloop()

        self.master = master

        self.label1 = tk.Label(self.master, text='SELECT THE NUMBER OF ELEMENTS PER DIMENSION:', font='HELVETICA 20 bold', bg='salmon', fg='white')
        self.label1.pack(fill=tk.X, padx=20, pady=(25, 0))

        shapeScale = tk.Scale(self.master, from_=1, to=10, orient=tk.HORIZONTAL, activebackground='yellow', tickinterval=9, relief=tk.GROOVE)
        shapeScale.config(command=self.set_Shape)
        shapeScale.config(background='gray25', fg='white', font='HELVETICA 24 bold', relief=tk.GROOVE, sliderlength=100, sliderrelief=tk.RAISED)
        shapeScale.pack(fill=tk.X, padx=20, pady=(0, 25))
        shapeScale.focus()

        # Button to direct user to next GUI.
        self.nextButton = tk.Button(self.master, text='NEXT', font='Helvetica 60 bold', command= lambda: transfer()).pack(fill=tk.X, padx=20, pady=25)

        # dimension_PromptWindow attributes.
        self.master.title('Visual Array')
        self.master.configure(bg='indianred3')
        self.master.geometry('600x300')
        self.master.minsize(600, 300)
        self.master.bind("<Return>", lambda cmd: transfer())
        master.mainloop()

    # Method displays the array alongside the methods and tasks that can be performed on the array. 
    def arrayHub(self, master):
        self.master = master

        # Method destroys array hub window and restarts application.
        def restart():
            self.master.destroy()
            self.master.quit()
            root = tk.Tk()
            self.__init__(root)
            root.mainloop()

        # Frame to listbox containing array elements.
        self.arrayFrame = tk.Frame(self.master, bg='indianred')
        self.label1 = tk.Label(self.arrayFrame, text='Array Contents:', fg='white', bg='black', font='Helvetica 24 bold').pack(fill=tk.X, pady=(10, 30))

        # Listbox to hold the contents of the array.
        self.listBox = tk.Listbox(self.arrayFrame, justify='center', font='TIMES 26 bold', width=20, height=10, selectborderwidth=1, bg='lavenderblush')
        self.listBox.config(relief='sunken', selectbackground='oldlace')

        for key in self.array:
            self.listBox.insert(tk.END, key)

        self.listBox.pack(side=tk.RIGHT)
        self.listBox.focus()

        # If the content of the array exceeds 11, then insert a scroll bar left of the listbox.
        if self.listBox.size() >= 11:
            # Add scrollbar to listbox.
            self.scrollbar = tk.Scrollbar(self.arrayFrame, orient="vertical", command=self.listBox.yview)
            self.listBox.config(yscrollcommand=self.scrollbar.set)
            self.scrollbar.pack(side=tk.LEFT, fill=tk.Y)

        self.arrayFrame.grid(row=0, column=0)
        self.master.columnconfigure(0, weight=1)
        self.master.rowconfigure(0, weight=1)

        # Frame containing buttons with methods to perform on the given array.
        self.methodsFrame = tk.Frame(self.master, bg='indianred')

        label2 = tk.Label(self.methodsFrame, text='Array Methods:', fg='white', bg='black', font='Helvetica 24 bold')
        label2.pack(fill=tk.X, pady=10)

        # Array Method Buttons.
        self.insertButton = tk.Button(self.methodsFrame, text='INSERT', font='HELVETICA 30 bold', width=20, command=lambda: self.insert()).pack(fill=tk.X, pady=10)
        self.deleteButton = tk.Button(self.methodsFrame, text='DELETE', font='HELVETICA 30 bold', width=20, command=lambda: self.delete()).pack(fill=tk.X, pady=10)
        self.searchButton = tk.Button(self.methodsFrame, text='SEARCH', font='HELVETICA 30 bold', width=20, command=lambda: self.search()).pack(fill=tk.X, pady=10)
        self.splitButton = tk.Button(self.methodsFrame, text='SPLIT', font='HELVETICA 30 bold', width=20).pack(fill=tk.X, pady=10)
        self.sortButton = tk.Button(self.methodsFrame, text='SORT', font='HELVETICA 30 bold', width=20).pack(fill=tk.X, pady=10)
        self.filterButton = tk.Button(self.methodsFrame, text='FILTER', font='HELVETICA 30 bold', width=20).pack(fill=tk.X, pady=10)
        self.newArrayButton = tk.Button(self.master, text='NEW ARRAY', font='HELVETICA 30 bold', width=20, command=lambda: restart()).grid(row=1, column=1)

        self.methodsFrame.grid(row=0, column=1)
        self.master.columnconfigure(1, weight=1)
        self.master.rowconfigure(1, weight=1)

        # Label containing attributes of the array.
        self.msg = 'Number of Dimensions: '+str(self.get_NumDimensions())+'\nType of data: '+str(self.get_DataType())+'\n['+str(self.listBox.size())+'] # of elements.'
        self.arrayAttributeLabel = tk.Label(self.master, text=self.msg, bg='indianred', font='HELVETICA 18').grid(row=1, column=0)

        # dimensionPrompt_Window attributes.
        self.master.config(bg='indianred')
        self.master.title('Visual Array Hub')
        self.master.geometry('875x525')
        self.master.minsize(875, 525)
        self.master.mainloop()

    # Method inserts element at given location in array.
    def insert(self):

        def add():
            try:
                self.array.insert(int(int(self.indexEntry.get())), self.elementEntry.get())
                print('Inserted [' + str(self.elementEntry.get()) + '] @ Index ' + str(self.indexEntry.get()))
                self.insertElement_Window.destroy()
                self.insertElement_Window.quit()
                self.arrayHub(1)
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
        self.index = tk.StringVar()

        self.insertElement_Window = tk.Tk()

        self.label6 = tk.Label(self.insertElement_Window, text='Insert Element:', bg='gray28', fg='white', font='HELVETICA 20 bold')
        self.label6.pack(fill=tk.X, padx=20, pady=20)
        self.elementEntry = tk.Entry(self.insertElement_Window, font='HELVETICA 24 bold', justify='center', textvariable=self.element)
        self.elementEntry.pack(fill=tk.X, padx=20)
        self.elementEntry.focus()
        self.label7 = tk.Label(self.insertElement_Window, text='@ Index: ', bg='gray28', fg='white', font='HELVETICA 20 bold', textvariable=self.index)
        self.label7.pack(fill=tk.X, padx=20, pady=20)
        self.indexEntry = tk.Entry(self.insertElement_Window, font='HELVETICA 24 bold', justify='center')
        self.indexEntry.pack(fill=tk.X, padx=20)
        self.insertButton = tk.Button(self.insertElement_Window, text='INSERT', font='HELVETICA 24 bold', command=lambda: add())
        self.insertButton.pack(fill=tk.X, padx=20, pady=20)

        self.insertElement_Window.geometry('400x300')
        self.insertElement_Window.title('INSERT:')
        self.insertElement_Window.config(bg='indianred')
        self.insertElement_Window.minsize(400, 300)
        self.insertElement_Window.bind('<Return>', lambda cmd: add())
        self.insertElement_Window.mainloop()

    # Method removes element at given location in array.
    def delete(self):
        def remove():
            try:
                self.elementRemoved = self.array.pop(int(self.indexDeleteEntry.get()))
                print('Deleted element [' + str(self.elementRemoved) + '] @ Index [' + str(self.indexDeleteEntry.get()) + "]")
                self.deleteIndex_Window.destroy()
                self.deleteIndex_Window.quit()
                self.arrayHub(1)

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

        # String variable holds the index to be deleted.
        self.index = tk.StringVar()

        self.deleteIndex_Window = tk.Tk()

        self.label8 = tk.Label(self.deleteIndex_Window, text='Delete Index:', bg='gray28', fg='white', font='HELVETICA 20 bold')
        self.label8.pack(fill=tk.X, padx=20, pady=20)
        self.indexDeleteEntry = tk.Entry(self.deleteIndex_Window, font='HELVETICA 24 bold', justify='center')
        self.indexDeleteEntry.pack(fill=tk.X, padx=20)
        self.indexDeleteEntry.focus()
        self.deleteButton = tk.Button(self.deleteIndex_Window, text='DELETE', font='HELVETICA 24 bold', command=lambda: remove())
        self.deleteButton.pack(fill=tk.X, padx=20, pady=20)

        self.deleteIndex_Window.geometry('400x225')
        self.deleteIndex_Window.title('INSERT:')
        self.deleteIndex_Window.config(bg='indianred')
        self.deleteIndex_Window.minsize(400, 225)
        self.deleteIndex_Window.bind('<Return>', lambda cmd: remove())
        self.deleteIndex_Window.resizable(False, False)
        self.deleteIndex_Window.mainloop()

    def search(self):

        # Method find's element in given array.
        def find():

            def searchBind():
                self.displaySearch_Window.destroy()
                self.search()

            try:
                self.searchedIndex = self.array.index(self.indexSearchEntry.get())
                self.searchedElement = self.indexSearchEntry.get()
                print('Element [' + str(self.indexSearchEntry.get()) + '] found @ index: ' + str(self.searchedIndex))
                self.searchWindow.destroy()

                self.displaySearch_Window = tk.Tk()

                self.label12 = tk.Label(self.displaySearch_Window, text='Element: ' + str(self.searchedElement), bg='black', fg='white', font='HELVETICA 44 bold')
                self.label12.pack(fill=tk.X, padx=10, pady=(10, 10))

                self.label13 = tk.Label(self.displaySearch_Window, text='Index: ' + str(self.searchedIndex), bg='gray20', fg='white', font='HELVETICA 54 bold')
                self.label13.pack(fill=tk.X, padx=10)

                self.bottomFrame = tk.Frame(self.displaySearch_Window, bg='indianred')

                self.searchAgainButton = tk.Button(self.bottomFrame, text='SEARCH', font='HELVETICA 24 bold', width=10, command=lambda: searchBind())
                self.searchAgainButton.pack(side=tk.LEFT, fill=tk.X)

                self.doneButton = tk.Button(self.bottomFrame, text='DONE', font='HELVETICA 24 bold', width=10, command=lambda: self.displaySearch_Window.destroy())
                self.doneButton.pack(side=tk.RIGHT, fill=tk.X, padx=1)

                self.bottomFrame.pack(fill=tk.BOTH, padx=10, pady=10)

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

        self.searchWindow = tk.Tk()

        self.label11 = tk.Label(self.searchWindow, text='Search for element:', bg='gray28', fg='white', font='HELVETICA 20 bold')
        self.label11.pack(fill=tk.X, padx=20, pady=20)
        self.indexSearchEntry = tk.Entry(self.searchWindow, font='HELVETICA 24 bold', justify='center')
        self.indexSearchEntry.pack(fill=tk.X, padx=20)
        self.indexSearchEntry.focus()
        self.searchButton = tk.Button(self.searchWindow, text='SEARCH', font='HELVETICA 24 bold', command=lambda: find())
        self.searchButton.pack(fill=tk.X, padx=20, pady=20)

        self.searchWindow.geometry('400x225')
        self.searchWindow.title('Search:')
        self.searchWindow.config(bg='indianred')
        self.searchWindow.minsize(400, 225)
        self.searchWindow.bind('<Return>', lambda cmd: find())
        self.searchWindow.resizable(False, False)
        self.searchWindow.mainloop()

    # Getter method.
    def get_NumDimensions(self):
        return self.numDimensions

    # Getter method.
    def get_DataType(self):
        return self.dataType

    # Getter method.
    def get_Array(self):
        return self.array

    # Getter method.
    def get_Shape(self):
        return self.shape

    # Setter method.
    def set_NumDimensions(self, val):
        self.numDimensions = val

    # Setter method.
    def set_DataType(self, val):
        self.dataType = val

    # Setter method.
    def set_Shape(self, val):
        self.shape = val


def main():
    # Initialize the visualArray, by passing a tkinter window object into the constructor.
    master = tk.Tk()
    visualArray = VisualArray(master)
    master.mainloop()


# Execute program. 
if __name__ == '__main__':
    main()
