import base64
from functools import partial
import tkinter as tk
#intitalize the actual encoding
def call_result(label_result,n1):
	num1=(n1.get())
	crypt = num1.encode()
	result = base64.b64encode(crypt)
	mod =  len(result)
	z = mod - 1
	label_result.config(text="encode complete:%s" % result)

	return
root = tk.Tk()
root.geometry('400x200+100+200')
number1=tk.StringVar()
root.title('casper')
labelNum1 = tk.Label(root,text='input').grid(row=1,column=0)
labelResult = tk.Label(root)
labelResult.grid(row=7,column=2)
entryNum1 = tk.Entry(root,textvariable=number1).grid(row=1,column=2)
call_result=partial(call_result,labelResult,number1)
buttonCal= tk.Button(root,text="encode",command=call_result).grid(row=3,column=0)
root.mainloop()

