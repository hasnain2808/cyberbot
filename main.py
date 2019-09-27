from searchspl import searc
import json
inp0=input('-->')
if inp0 == 'hello' or 'hi' or 'hey' or 'sup' or 'wasup':
	print('Hello! Enter your query')
	obj1= searc()
	inp1=input('-->')
	in1=obj1.initialsearch(inp1)
	in1_j=json.loads(in1)
	
