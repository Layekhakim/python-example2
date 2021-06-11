
file = open("teams.txt","w")
teams = ['Chelsea', 'Manchester City','Arsenal','Liverpool', 'Manchester United']
for name in teams: 
    file.write(name+"/n")
    file.close()

    file = open("teams.txt","r")
    lines_to_read =[0,3]


 