import pandas as pd
import turtle
import pandas as pd
screen=turtle.Screen()
screen.title("U.S State game")
image="blank_states_img.gif"
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
state_data=pd.read_csv("50_states.csv")
state_names=state_data['state'].to_list()
answer=screen.textinput(title="Guess the state", prompt="Enter the state name:")
guessed_state=[]
state_to_learn=[]
guess_count=len(guessed_state)
while guess_count<=50:
    
    answer=answer.title()
    if answer=='Exit':
        #missed_state=[state for state in state_names if state not in guessed_state]
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
            t.goto(int(state.x),int(state.y))
            t.write(answer) #t.write(state_data.state.item())
            guessed_state.append(answer)
            
            guess_count+=1
    answer=screen.textinput(title=f"{guess_count}/50", prompt="Enter the next state name:")
        
    
#screen.exitonclick()   
    

        


