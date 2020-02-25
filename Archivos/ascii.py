f = open ("ascii.txt","w")

#f.write(chr(1))
for i in range(33,125):
    f.write(chr(i))

f.close()