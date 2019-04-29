# Weight Converter
# Ivan Delgadillo
# 4.28.19
# This program convert pounds weight into grams, kilograms and ounces

from graphics import *
from button import *

""" Message display when user enter the wrong value"""
def wrongValue(grams,kilos,ounces):            
    grams.setText("Please enter a number value")
    kilos.setText("Please enter a number value")  
    ounces.setText("Please enter a number value")
    
    """ Conversion values"""
def weightGrams(pounds):
    grams = (pounds * 453.59)
    return(round(grams, ndigits=2))

def weightOunces(pounds):   
    ounces = (pounds * 16)
    return(round(ounces, ndigits=2))

def weightKilograms(pounds):   
    kilos = (pounds * .4535)
    return(round(kilos, ndigits=2))

def weightC():
    """ The dimension of the display"""
    win = GraphWin("Entry",345,360)
    win.setCoords(0.0,0.0,3.5,3.5)
    win.setBackground("gray")

    """ The title sizes and style"""
    wTitle = Text(Point(1.8,3), "Weight Converter" )
    wTitle.setSize(19)
    wTitle.setStyle("bold")
    wTitle.draw(win)

    """ The pound, grams, kilogras and ounces dimensions"""
    Text(Point(3.0,2.45),"lb").draw(win)
    input = Entry(Point(1.82,2.5),15)
    input.setSize(19)
    input.setFill("white")
    input.draw(win)

    Text(Point(1.0,2.13),"Grams").draw(win)
    grams = Entry(Point(1.8,1.9),23)
    grams.setText(" 0.0")
    grams.setFill("white")
    grams.draw(win)
    
    Text(Point(1.1,1.58),"Kilograms").draw(win)
    kilos = Entry(Point(1.8,1.35),23)
    kilos.setText(" 0.0")
    kilos.setFill("white")
    kilos.draw(win)
    
    Text(Point(1.0,1.05),"Ounces").draw(win)
    ounces = Entry(Point(1.8,.8),23)
    ounces.setText(" 0.0")
    ounces.setFill("white")
    ounces.draw(win)

    """ Button that users use to click and process the conversion."""
    convertButton = Button(win,Point(2.4,.5),0.9,.2,"Convert")
    convertButton.activate() 
    ifClicked = win.getMouse()

    """ The functions of the mouse when clicks"""
    while convertButton.clicked(ifClicked):
        try:
            pounds = eval(input.getText())
            grams.setText(weightGrams(pounds))
            kilos.setText(weightKilograms(pounds))
            ounces.setText(weightOunces(pounds))
            
        except NameError:wrongValue(grams,kilos,ounces)
        except TypeError:wrongValue(grams,kilos,ounces)
        except SyntaxError:wrongValue(grams,kilos,ounces)
        except:wrongValue(grams,kilos,ounces)
                    
        ifClicked = win.getMouse()    
    win.getMouse()
    win.close()
    

weightC()
