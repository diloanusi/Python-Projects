#Iloanusi, Dabeluchukwu
#HW 05
#Property Tax

#assessment value = 60% of actual value
#Ex. If an acre of land is valued @ $10,000, its assessement value is $6,000
#Property tax = $0.75 for each $100 of the assessment value
#Ex. Tax of the acre assesed at $6,000 will be $45.00
#Write GUI program that displays the assessment value and property tax
#when a user enters the actual value of a property

import tkinter

class PropertyTaxGUI:
             def __init__(self):

                          # Create the main window.
                          self.main_window = tkinter.Tk()

                          # Create four frames to group widgets.
                          self.top_frame = tkinter.Frame()
                          self.assessment_mid_frame = tkinter.Frame()
                          self.tax_mid_frame = tkinter.Frame()
                          self.bottom_frame = tkinter.Frame()

                          # Create the widgets for the top frame.
                          self.prompt_label = tkinter.Label(self.top_frame,
                                 text="Enter Property's Actual Value: $")
                          self.actualValue_entry = tkinter.Entry(self.top_frame,
                                                     width=10)

                          # Pack the top frame's widgets.
                          self.prompt_label.pack(side="left")
                          self.actualValue_entry.pack(side="left")

                          # Create the widgets for the middle frame.
                          self.descr_label = tkinter.Label(self.assessment_mid_frame,
                                                      text="Assessment value: $")
                          self.descr_label2 = tkinter.Label(self.tax_mid_frame,
                                                      text="Property Tax: $")

                          # We need a StringVar object to associate with
                          # an output label. Use the object's set method
                          # to store a string of blank characters.
                          self.assessment_value = tkinter.StringVar()
                          self.tax_value = tkinter.StringVar()

                          # Create a label and associate it with the
                          # StringVar object. Any value stored in the
                          # StringVar object will automatically be displayed
                          # in the label.
                          self.assessment_label = tkinter.Label(self.assessment_mid_frame,
                                                      textvariable=self.assessment_value)
                          self.tax_label = tkinter.Label(self.tax_mid_frame,
                                                         textvariable = self.tax_value)

                          # Pack the middle frame's widgets.
                          self.descr_label.pack(side='left')
                          self.assessment_label.pack(side='left')
                          self.descr_label2.pack(side = "left")
                          self.tax_label.pack(side = "left")

                          # Create the button widgets for the bottom frame.
                          self.calc_button = tkinter.Button(self.bottom_frame,
                                                       text='Calculate',
                                                       command=self.calculations)
                          self.quit_button = tkinter.Button(self.bottom_frame,
                                                       text='Quit',
                                                       command=self.main_window.destroy)

                          # Pack the buttons.
                          self.calc_button.pack(side='left')
                          self.quit_button.pack(side='left')

                          # Pack the frames.
                          self.top_frame.pack()
                          self.assessment_mid_frame.pack()
                          self.tax_mid_frame.pack()
                          self.bottom_frame.pack()

                          # Enter the tkinter main loop.
                          tkinter.mainloop()

                          # The convert method is a callback function for
                          # the Calculate button.

             def calculations(self):
                          # Get the value entered by the user into the
                          # actualValue widget.
                          actualValue = float(self.actualValue_entry.get())

                          # Calculate the assesment value 
                          assessmentValue = (0.6 * actualValue)

                          # Calculate the tax value 
                          taxValue = format((0.75*(assessmentValue/100)), '.2f')

                          # Convert assessment value to a string and store it
                          # in the StringVar object. This will automatically
                          # update the assesment_label widget.
                          self.assessment_value.set(format(assessmentValue, ".2f"))

                          # Convert tax value to a string and store it
                          # in the StringVar object. This will automatically
                          # update the tax_label widget.
                          self.tax_value.set(taxValue)

# Create an instance of the PropertyTaxGUI class.
PropertyTax = PropertyTaxGUI()
