from tkinter import *

root=Tk()
root.title("Calculator")
root.resizable(False, False)
myframe=Frame(root)
myframe.pack(fill="x")
myframe.config(bg="white")


expression=""

def value_assign(number):
  
  global expression

  expression=expression+str(number)
  print (equation)
  equation.set(expression)
  


def equalpress():
    # Try and except statement is used
    # for handling the errors like zero
    # division error etc.
 
    # Put that code inside the try block
    # which may generate the error
    try:
 
        global expression
 
        # eval function evaluate the expression
        # and str function convert the result
        # into string
        total = str(eval(expression))
        print (total)
        equation.set(total)
 
        # initialize the expression variable
        # by empty string
        expression = ""
 
    # if error is generate then handle
    # by the except block
    except:
 
        equation.set(" error ")
        expression = ""
  

def clear_entry():
  expression=""
  main_label.delete(0, END)
  equation=""



equation = StringVar()


main_label=Entry(myframe,width=10,textvariable=equation)
main_label.grid(row=0,column=0,padx=1,pady=5,sticky="w")
main_label.config(width=15)


#creamos el bloque de botones de los numeros
number_seven_buton=Button(myframe,text="7",command=lambda: value_assign(7))
number_seven_buton.grid(row=1,column=0,sticky="w")
number_eight_button=Button(myframe,text="8",command=lambda:value_assign(8))
number_eight_button.grid(row=1,column=0,sticky="w",padx=40)
number_nine_buton=Button(myframe,text="9",command=lambda:value_assign(9))
number_nine_buton.grid(row=1,column=0,sticky="w",padx=80)
number_four_button=Button(myframe,text="4",command=lambda:value_assign(4))
number_four_button.grid(row=2,column=0,sticky="w")
number_five_button=Button(myframe,text="5",command=lambda:value_assign(5))
number_five_button.grid(row=2,column=0,sticky="W",padx=40)
number_six_button=Button(myframe,text="6",command=lambda:value_assign(6))
number_six_button.grid(row=2,column=0,sticky="W",padx=80)
number_one_button=Button(myframe,text="1",command=lambda:value_assign(1))
number_one_button.grid(row=3,column=0,sticky="W")
number_two_button=Button(myframe,text="2",command=lambda:value_assign(2))
number_two_button.grid(row=3,column=0,sticky="w",padx=40)
number_tree_button=Button(myframe,text="3",command=lambda:value_assign(3))
number_tree_button.grid(row=3,column=0,sticky="W",padx=80)
number_cero_button=Button(myframe,text="0",command=lambda:value_assign(0))
clear_button=Button(myframe,text="C", command=lambda:clear_entry())
clear_button.grid(row=4,column=0,sticky="w")
number_cero_button.grid(row=4,column=0,sticky="w",padx=40)
equal_button=Button(myframe,text="=",command=equalpress)
equal_button.grid(row=4,column=0,sticky="w",padx=80)

#creamos los botones de operaciones fundamentales.
division_button=Button(myframe,text="÷",command=lambda:value_assign("÷"))
division_button.grid(row=1,column=0,sticky="W",padx=(115,1))
multiplication_button=Button(myframe,text="x",command=lambda:value_assign("x"))
multiplication_button.grid(row=2,column=0,padx=(72,1))
substraction_button=Button(myframe,text="−",command=lambda:value_assign("−"))
substraction_button.grid(row=3,column=0,padx=(72,1))
add_button=Button(myframe,text="+",command=lambda:value_assign("+"))
add_button.grid(row=4,column=0,padx=(72,1))

#en este text iran los creditos del programa
creditos=Text(myframe,text="made by: Jerick Abril")

creditos.grid(row=5,column=0) 


root.mainloop()


