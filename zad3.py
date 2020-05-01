import pandas as pd
file = pd.read_excel('football.xlsx')

drużyny = files['Team']
gole = file['Goals']
golestracone = file['Goals Allowed']

roznica=[]
for i in range (len(file)):
    roz = abs(goals[i]- goals_allowed[i])
    roznica.apeend(roz)

a = roznica.index(min(roznica))

Print("Drużyna z najmniejsza różnicą bramek: ", team[a])
