import tkinter as tk
import numpy as np


# Class represents a numpy array being visualized through a tkinter window.
class VisualArray:

    # Constructor; Prompts user for for number of dimensions for array.
    def __init__(self):

        # Numpy array attributes.
        self.numDimensions = None
        self.dataType = None
        self.array = []

        # Check to see if user dimension entry is valid.
        # Method direct's user to dataTypePrompt_Window if entry is valid.
        def valid_Dimension():
            try:
                # Attempt to convert given dimension to int, if error than display notice window. 
                self.dimension = int(self.dimEntry.get())
                
                if 1 <= self.dimension <= 3:
                    # Proceed user to next GUI, to receive the data type for the array.
                    self.set_NumDimensions(self.dimension)
                    # Destroy the current GUI.
                    self.dimension_PromptWindow.destroy()
                    self.dimension_PromptWindow.quit()

                    # Proceed to next GUI.
                    self.prompt_DataType()

                else:
                    # Direct user to notice window below.
                    # The entry was a valid int, but not within the range (1-3).
                    raise ValueError

            except ValueError as VE:

                # Method binds <Return> key press to close noticeWindow.
                def keyBind1(event):
                    self.noticeWindow.destroy()
                
                # Otherwise, display notice window to user. 
                self.noticeWindow = tk.Tk()
                self.label1_ = tk.Label(self.noticeWindow, text='Invalid Dimension Selected!', font='HELVETICA 26 bold',
                                   bg='gray20', fg='white')
                self.label1_.pack(fill=tk.X, pady=20, padx=20)
                self.label2_ = tk.Label(self.noticeWindow, text='Please select a dimension between 1 and 3.',
                                   font='HELVETICA 18', bg='salmon', fg='white')
                self.label2_.pack()
                self.label3_ = tk.Label(self.noticeWindow, text='You have entered: ' + self.dimEntry.get(), bg='gray20',
                                   fg='white', font='HELVETICA 14 italic')
                self.label3_.pack(pady=20)
                self.closeButton = tk.Button(self.noticeWindow, text='CLOSE', font='HELVETICA 24 bold', command=lambda: self.noticeWindow.destroy())
                self.closeButton.pack(fill=tk.X, padx=10, pady=10)
                self.noticeWindow.configure(bg='salmon')
                self.noticeWindow.geometry('400x250')
                self.noticeWindow.resizable(False, False)
                self.noticeWindow.bind('<Return>', keyBind1)
                self.noticeWindow.title('Notice!')
                self.noticeWindow.mainloop()

        # Create tkinter window object.
        self.dimension_PromptWindow = tk.Tk()

        # Function binds <Return> key press to nextButton command.
        def keyBind(event):
            valid_Dimension()

        # Frame holding text above entry bar.
        self.frame = tk.Frame(self.dimension_PromptWindow, bg='indianred')
        self.label1 = tk.Label(self.frame, text='Enter number of dimensions:', font='Helvetica 40 bold', bg='indianred3', fg='white')
        self.label1.pack()
        self.label2 = tk.Label(self.frame, text='Please select between 1 to 3 dimensions.', bg='indianred3', fg='lightcyan', font='Helvetica 12 bold')
        self.label2.pack(padx=90)
        self.frame.pack(pady=(40, 20), fill=tk.X)

        # Entry to hold the number of dimensions from user.
        self.dim = tk.StringVar()
        self.dimEntry = tk.Entry(self.dimension_PromptWindow, font=('Helvetica', 90, 'bold'), justify='center', textvariable=self.dim)
        self.dimEntry.pack(fill=tk.X)

        # Button to direct user to next GUI.
        self.nextButton = tk.Button(self.dimension_PromptWindow, text='NEXT', font='Helvetica 60 bold', command=lambda: valid_Dimension())
        self.nextButton.pack(fill=tk.X, padx=20, pady=25)

        # dimension_PromptWindow attributes.
        self.dimension_PromptWindow.title('Visual Array')
        self.dimension_PromptWindow.configure(bg='indianred3')
        self.dimension_PromptWindow.geometry('600x400')
        self.dimension_PromptWindow.minsize(600, 400)
        self.dimension_PromptWindow.bind("<Return>", keyBind)
        self.dimension_PromptWindow.mainloop()

    # Prompts user for data Type for array.
    def prompt_DataType(self):

        # Method fetches the selected data type from the listbox. 
        def selected_DataType():
            self.set_DataType(self.listBox.get(self.listBox.curselection()))
            self.dataTypePrompt_Window.destroy()
            self.dataTypePrompt_Window.quit()
            self.arrayHub(0)
        
        # Bind the <Return> key to the button press command.
        def keyBind2(event):
            selected_DataType()

        # Create tkinter window object.
        self.dataTypePrompt_Window = tk.Tk()

        # Frame holding text above entry bar.
        self.frame = tk.Frame(self.dataTypePrompt_Window, bg='indianred3')
        self.label3 = tk.Label(self.frame, text='Select datatype:', font='Helvetica 40 bold', bg='indianred3', fg='white')
        self.label3.pack()

        # Present user with list of options of datatypes to select from.
        self.listBox = tk.Listbox(self.frame, justify='center', cursor='dot', bg='mintcream', fg='lightslateblue', font='HELVETICA 20 bold')
        self.listBox.config(selectbackground='oldlace', relief='raised', selectmode='single', height=4)
        self.listBox.insert(1, 'Integer')
        self.listBox.insert(2, 'Boolean')
        self.listBox.insert(3, 'Float')
        self.listBox.insert(4, 'String')
        self.listBox.select_set(0)
        self.listBox.pack(fill=tk.BOTH, pady=10)
        self.frame.pack(pady=(40, 20), fill=tk.X)

        # Button to direct user to next GUI.
        self.nextButton = tk.Button(self.dataTypePrompt_Window, text='NEXT', font='Helvetica 60 bold', command=lambda: selected_DataType())
        self.nextButton.pack(fill=tk.X, padx=20, pady=10)

        # dataTypePrompt_Window window attributes.
        self.dataTypePrompt_Window.title('Visual Array')
        self.dataTypePrompt_Window.configure(bg='indianred3')
        self.dataTypePrompt_Window.minsize(600, 375)
        self.dataTypePrompt_Window.bind("<Return>", keyBind2)
        self.dataTypePrompt_Window.mainloop()

    # Method displays the array alongside the methods and tasks that can be performed on the array. 
    def arrayHub(self, tag):

        # The tag parameter determines whether we load arrayHub as a fresh empty canvas, or refreshing after a method has been performed.
        # Tag 0 = Fresh Canvas, Tag 1 = Refreshing Canvas; Re-Draw canvas.
        # I had to do it this way because i couldn't access the arrayHub window from the insert method.
        if tag == 1:
            self.arrayHubWindow.destroy()
            self.arrayHubWindow.quit()
            self.arrayHub(0)

        else:
            # dimensionPrompt_Window displays the list's contents and buttons to respective methods that can be performed on array.
            self.arrayHubWindow = tk.Tk()

            # Method destroys current GUI and restarts application.
            def restart():
                self.arrayHubWindow.destroy()
                self.arrayHubWindow.quit()
                self.__init__()

            # Frame to listbox containing array elements.
            self.arrayFrame = tk.Frame(self.arrayHubWindow, bg='indianred')
            self.label4 = tk.Label(self.arrayFrame, text='Array Contents:', fg='white', bg='black', font='Helvetica 24 bold')
            self.label4.pack(fill=tk.X, pady=(10,30))

            # Listbox to hold the contents of the array.
            self.listBox = tk.Listbox(self.arrayFrame, justify='center', font='TIMES 26 bold', width=20, height=10, selectborderwidth=1, bg='lavenderblush',
                                 relief='sunken', selectbackground='oldlace')

            for key in self.array:
                self.listBox.insert(tk.END, key)

            self.listBox.pack(side=tk.RIGHT)

            # If the content of the array exceeds 11, then insert a scroll bar left of the listbox.
            if self.listBox.size() >= 11:
                # Add scrollbar to listbox.
                self.scrollbar = tk.Scrollbar(self.arrayFrame, orient="vertical", command=self.listBox.yview)
                self.listBox.config(yscrollcommand=self.scrollbar.set)
                self.scrollbar.pack(side=tk.LEFT, fill=tk.Y)

            self.arrayFrame.grid(row=0, column=0)
            self.arrayHubWindow.columnconfigure(0, weight=1)
            self.arrayHubWindow.rowconfigure(0, weight=1)

            # Frame containing buttons with methods to perform on the given array.
            self.methodsFrame = tk.Frame(self.arrayHubWindow, bg='indianred')

            label5 = tk.Label(self.methodsFrame, text='Array Methods:', fg='white', bg='black', font='Helvetica 24 bold').pack(fill=tk.X, pady=10)

            # Array Method Buttons.
            self.insertButton = tk.Button(self.methodsFrame, text='INSERT', font='HELVETICA 30 bold', width=20, command=lambda: self.insert()).pack(fill=tk.X, pady=10)
            self.deleteButton = tk.Button(self.methodsFrame, text='DELETE', font='HELVETICA 30 bold', width=20, command=lambda: self.delete()).pack(fill=tk.X, pady=10)
            self.searchButton = tk.Button(self.methodsFrame, text='SEARCH', font='HELVETICA 30 bold', width=20).pack(fill=tk.X, pady=10)
            self.splitButton = tk.Button(self.methodsFrame, text='SPLIT', font='HELVETICA 30 bold', width=20).pack(fill=tk.X, pady=10)
            self.sortButton = tk.Button(self.methodsFrame, text='SORT', font='HELVETICA 30 bold', width=20).pack(fill=tk.X, pady=10)
            self.filterButton = tk.Button(self.methodsFrame, text='FILTER', font='HELVETICA 30 bold', width=20).pack(fill=tk.X, pady=10)
            self.newArrayButton = tk.Button(self.arrayHubWindow, text='NEW ARRAY', font='HELVETICA 30 bold', width=20, command=lambda: restart()).grid(row=1, column=1)

            self.methodsFrame.grid(row=0, column=1)
            self.arrayHubWindow.columnconfigure(1, weight=1)
            self.arrayHubWindow.rowconfigure(1, weight=1)

            # Label containing attributes of the array.
            self.msg = 'Number of Dimensions: ' + str(self.get_NumDimensions()) + '\nType of data: ' + str(self.get_DataType()) + '\n[' + str(self.listBox.size()) + '] # of elements.'
            self.arrayAttributeLabel = tk.Label(self.arrayHubWindow, text=self.msg, bg='indianred', font='HELVETICA 18').grid(row=1, column=0)

            # dimensionPrompt_Window attributes.
            self.arrayHubWindow.config(bg='indianred')
            self.arrayHubWindow.title('Visual Array Hub')
            self.arrayHubWindow.geometry('875x525')
            self.arrayHubWindow.minsize(875, 525)
            self.arrayHubWindow.mainloop()

    # Method inserts element at given location in array.
    def insert(self):

        def add():

            # Method binds <Return> key press to closing valueError window popup.
            def bind3(event):
                self.valError_Window.destroy()

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
                self.label10 = tk.Label(self.valError_Window, text='Please try again, using a different value.')
                self.label10.config(bg='indianred', fg='white', font='HELVETICA 14 bold')
                self.label10.pack(fill=tk.X, padx=30)

                self.closeButton = tk.Button(self.valError_Window, text='CLOSE', font='HELVETICA 24 bold', command=lambda: self.valError_Window.destroy())
                self.closeButton.pack(fill=tk.X, padx=20, pady=(10, 0))

                self.valError_Window.config(bg='indianred')
                self.valError_Window.geometry('375x175')
                self.valError_Window.minsize(300, 175)
                self.valError_Window.title('Value Error!')
                self.valError_Window.resizable(False, False)
                self.valError_Window.bind('<Return>', bind3)
                self.valError_Window.mainloop()

        # Method binds <Return> press to closing insert Window GUI.
        def bind4(event):
            add()

        # String variables to hold given array and element entered by user.
        self.element = tk.StringVar()
        self.index = tk.StringVar()

        self.insertElement_Window = tk.Tk()

        self.label6 = tk.Label(self.insertElement_Window, text='Insert Element:', bg='gray28', fg='white', font='HELVETICA 20 bold')
        self.label6.pack(fill=tk.X, padx=20, pady=20)
        self.elementEntry = tk.Entry(self.insertElement_Window, font='HELVETICA 24 bold', justify='center', textvariable=self.element)
        self.elementEntry.pack(fill=tk.X, padx=20)
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
        self.insertElement_Window.bind('<Return>', bind4)
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
                def bind7(event):
                    self.indexError_Window.destroy()

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
                self.indexError_Window.bind('<Return>', bind7)
                self.indexError_Window.mainloop()

            except ValueError:

                def bind7(event):
                    self.valError_Window.destroy()

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
                self.valError_Window.bind('<Return>', bind7)
                self.valError_Window.mainloop()

        # Method binds <Return> press to closing deleteIndex_Window GUI.
        def bind5(event):
            remove()

        # String variable holds the index to be deleted.
        self.index = tk.StringVar()

        self.deleteIndex_Window = tk.Tk()

        self.label8 = tk.Label(self.deleteIndex_Window, text='Delete Index:', bg='gray28', fg='white', font='HELVETICA 20 bold')
        self.label8.pack(fill=tk.X, padx=20, pady=20)
        self.indexDeleteEntry = tk.Entry(self.deleteIndex_Window, font='HELVETICA 24 bold', justify='center')
        self.indexDeleteEntry.pack(fill=tk.X, padx=20)
        self.deleteButton = tk.Button(self.deleteIndex_Window, text='DELETE', font='HELVETICA 24 bold', command=lambda: remove())
        self.deleteButton.pack(fill=tk.X, padx=20, pady=20)

        self.deleteIndex_Window.geometry('400x225')
        self.deleteIndex_Window.title('INSERT:')
        self.deleteIndex_Window.config(bg='indianred')
        self.deleteIndex_Window.minsize(400, 225)
        self.deleteIndex_Window.bind('<Return>', bind5)
        self.deleteIndex_Window.resizable(False, False)
        self.deleteIndex_Window.mainloop()

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
