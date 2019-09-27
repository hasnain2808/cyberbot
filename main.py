from searchspl import searc
import json
inp0=input('-->')
if inp0 == 'hello' or 'hi' or 'hey' or 'sup' or 'wasup':
	#print('Hello! Enter your query')
	obj1= searc()
	#inp1=input('-->')
	in1=str(obj1.initialsearch("afd windows local")[0])[1:]
#	print(in1[0])
	in1 = in1.replace('\\n','').replace('\\t','').replace('\\','')[1:-1]
#	print(in1)
	in1_j=json.loads(in1)
	print(in1_j["SEARCH"])
#	print(in1_j)
