#Exercise: 2
p = open("esercizio_sui_file", "r")
print(p.read())

#Exercise: 3 
i = open("esercizio_sui_file", "a")
i.write("This line was appended.")
i.close()

#Exercise: 4
s = open("esercizio_sui_file")
print(s.read())
s.close()

#Exercixse: 5 
i = open("esercizio_sui_file", "w")
i = open("esercizio_sui_file", "r")
for i in i:
    copy.write(str(1))
i.close()






