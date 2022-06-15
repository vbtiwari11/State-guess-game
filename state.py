# -*- coding: utf-8 -*-
"""
Created on Mon May  2 13:21:29 2022

@author: vaitiwar
"""
'''
import pandas as pd
state_data=pd.read_csv("indian_state.csv")
state_names=state_data['Place Name']
lattitude=state_data['Latitude']
longitude=state_data['Longitude']
print(lattitude)
'''
import pandas as pd
import turtle
import pandas as pd
screen=turtle.Screen()
screen.title("Indian State game")
image="inblst.gif"
screen.addshape(image)

turtle.shape(image)
'''
def get_mouse_cor(x,y):
    print(x,y)

turtle.onscreenclick(get_mouse_cor)
turtle.mainloop()
#screen.exitonclick()
'''
t=turtle.Turtle()
guess_count=0
state_data=pd.read_csv("indian_state.csv")
state_names=state_data['Place Name'].to_list()
answer=screen.textinput(title="Guess the state", prompt="Enter the state name:")
guessed_state=[]
state_to_learn=[]
guess_count=len(guessed_state)
while guess_count<=23:
    
    answer=answer.title()
    if answer=='Exit':
        for state in state_names:
            if state not in guessed_state:
                state_to_learn.append(state)
        missed_state=pd.DataFrame(state_to_learn)
        missed_state.to_csv("State_to_learn.csv")
        
        break
    if answer in state_names:
            #print("Correct Guess")
            t.hideturtle()
            t.penup()
            state=state_data[state_data.state==answer]
            t.goto(int(state.Latitude),int(state.Longitude))
            t.write(answer) #t.write(state_data.state.item())
            guessed_state.append(answer)
            
            guess_count+=1
    answer=screen.textinput(title=f"{guess_count}/50", prompt="Enter the next state name:")
        
    
#screen.exitonclick()   
    

        


