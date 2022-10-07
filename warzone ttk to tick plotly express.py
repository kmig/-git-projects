
import plotly.express as px
import math
import pandas as pd

hp=300
bars_names=[]
tick_hs=[]
tick_cs=[]

def tick_calculation(t):
    return (1/t)

def bullets_to_kill(hp, dmg):
    return math.ceil(hp / dmg)

def weapon(rpm, hs, cs, name):
    bars_names.append(name)
    tick_cs.append(math.ceil(((bullets_to_kill(hp,cs)-1)/(rpm/60))/tick_calculation(20)))
    tick_hs.append(math.ceil(((bullets_to_kill(hp,hs)-1)/(rpm/60))/tick_calculation(20)))

weapon(857,51,34,"type 100") #attachments 968,42,28,434 no att 750,44,30,480
weapon(1200,34,23,"ppsh") #952,34,25,
weapon(1053,40,26,"ra225")#845,40,26,
weapon(984,46,27,"armaguerra") #938,40,27,
weapon(1091,38,24,"fennec")
weapon(845,45,30,"welgun")#645,53,36,
weapon(845,45,31,"sten") #667,45,31,
weapon(952,40,25,"mp7") #600,59,36,
weapon(779,49,36,"marco") #667,49,36,
weapon(857,40,29,"mp5cw") #600,59,36,
weapon(750,45,34,"mp5mw") #600,59,36,
weapon(600,55,43,"blixxen") #571,55,38
weapon(779,36,35,"mp40") #600,59,36,
weapon(938,39,26,"ugm")#896,39,26,
weapon(909,36,26,"cooper")#811,37,27,
weapon(732,43,29,"grau")
weapon(600,47,36,"stg")
weapon(619,45,34,"vargo")#659,45,33,
weapon(833,33,24,"automaton")
weapon(833,33,24,"automaton")

x_name = f"{1/tick_calculation(20)} tickrate"
df = pd.DataFrame({x_name:bars_names,"head dmg":tick_hs,"chest dmg":tick_cs})

fig = px.bar(df, x=x_name, y=["head dmg", "chest dmg"], title='ttk to tick', text_auto=True, barmode='group')
fig.show() 