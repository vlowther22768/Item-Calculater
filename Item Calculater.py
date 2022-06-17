from breezypythongui import EasyFrame
from tkinter.font import Font
#other imports
class final(EasyFrame):
#AppilcationName will change from project to project

#defintion of the __init__() method which is our class constructor

	def __init__(self):

		EasyFrame.__init__(self, title = "Cost Calculater", background = "lightskyblue")
		self.setResizable(True)
		#Creating the font variables
		titleFont = Font(family = "Goergia", size = 24, weight = "bold")
		questionFont = Font(family = "Optima", size = 14)
		
		#the basic structure for the questions 
		self.addLabel(foreground ="DimGray", font = titleFont, text = "Cost Calculater", row = 0, column = 0, sticky = "NSEW", columnspan = 2, background = "lightskyblue")
		self.addLabel(foreground = "SeaShell", font = questionFont, text = "What item are you buying?", row = 1, column = 0, columnspan = 2, background = "lightskyblue")
		self.item = self.addTextField(text = "", row = 1, column = 2)
		self.addLabel(foreground = "SeaShell", font = questionFont, text = "How many are you buying?", row = 2, column = 0, columnspan = 2, background = "lightskyblue")
		self.quantity = self.addIntegerField(value = 0, row = 2, column = 2)
		self.addLabel(foreground ="SeaShell", font = questionFont, text = "How much does it cost?", row = 3, column = 0, columnspan = 2, background = "lightskyblue")
		self.cost = self.addFloatField(value = 0.0, row = 3, column = 2, precision = 2)
		self.button = self.addButton(text = "Caculate Cost", row = 4, column = 2, command = self.calc)
		self.button["background"] = "LightCoral"
	
	# the defintion of the button command
	def calc(self):
		#made another font variable
		answerFont = Font(family = "Optima", size = 20, weight = "bold")
		price = self.cost.getNumber()
		quant = self.quantity.getNumber()
		total = quant * price
		userInput = self.item.getText()
		stringtotal = str('%.2f'%total)
		self.addLabel(foreground = "DimGray", font = answerFont, text = "The total cost of your " + userInput + " is $" + stringtotal , row = 5, column = 0, columnspan = 2, sticky = "NSEW", background = "lightskyblue")




def main():
	# instance an object from the class into mainloop
	final().mainloop()
#global call to trigger he main() method
main()		  