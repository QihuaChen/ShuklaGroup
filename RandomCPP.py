List = open("randomSelect", 'r')
w = open("SelectedExtract.sh", 'w')

for line in List:
	newline = line.split(" ")
	print(newline)
	filename = newline[0].replace(".mdcrd", "")
	number = newline[1].replace("\n", "")
	newfilename = filename+"-frame"+str(number)
	newcpptrajname = newfilename+".in"
	w.write('echo "parm striga-5CBK-Apo.prmtop"> ')
	w.write(newcpptrajname+"\n")
	w.write('echo "trajin ')
	w.write(newline[0])
	w.write('">> ')
	w.write(newcpptrajname+"\n")
	w.write('echo "autoimage">> ')
	w.write(newcpptrajname+"\n")
	w.write('echo "trajout ')
	w.write(newfilename)
	w.write('.rst restart onlyframes ')
	w.write(str(number))
	w.write('">> ')
	w.write(newcpptrajname+"\n")
	w.write('echo "go">> ')
	w.write(newcpptrajname+"\n")
	w.write('echo "quit">> ')
	w.write(newcpptrajname+"\n")
	w.write('cpptraj -i ')
	w.write(newcpptrajname+"\n")


w.close()
List.close()