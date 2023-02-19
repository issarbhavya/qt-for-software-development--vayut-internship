"""
so basically the ocde for this is to open dialog box that takes input
without making a qmessagebox or line edit and all and an ok and cancel button
to use there clicked/triggered function    




def button_clicked(self):
    text, ok =QInputDialog.getText(self,"get text dialog box",
                        ,"Enter your name :")
    if (ok and not (text=="")):
        
        than you can use the value inputed as per your requiremrnt

#there are even functions like 


getDouble
It allows integer/double input,
there you can set a default value, minimum and maximum value as well


getItems
It allows user to select the items of a list through comboBox

items=["a","b"]
i,ok =QInputDialog.getItem(self,"title of dialogBox","text to be mentioned",items)

if (ok):
    self.label.setText(i)
"""