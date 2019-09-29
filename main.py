from searchspl import searc
import json
from scr import CVE
from JsonSearch import dessearc
import requests 

URLtr = "http://127.0.0.1:5000/train"
URLpr = "http://127.0.0.1:5000/predict"
state = "q1"
cve = 0
global attrlis

def q1(inp):
	if inp0 == 'hello' or 'hi' or 'hey' or 'sup' or 'wasup':
		global state 
		state = 'q2'
		# print(state)
		print("q1")
		return "hey whats your domain ?"
	else :
		return "I wasn't able to understand please reframe"

def q2(inp):
	obj1= searc()
	#inp1=input('-->')
	#"afd windows local"
	print("q2")
	in1=str(obj1.initialsearch(inp)[0])[1:]
	in1 = in1.replace('\\n','').replace('\\t','').replace('\\','')[1:-1]
	in1_j=json.loads(in1)
	global state 
	state = "q3"
	return in1

def q3(inp):
	print("q3")
	ebd = CVE(inp)
	cve = ebd.find()
	global state
	state = "q4"
	global attrlis
	# attrlis = dessearc('CVE-'+str(cve))
	# 2019-0013
	attrlis = dessearc('CVE-'+str("2019-0013"))
	attrlis.setattr()
	return cve

def q4(inp):
	print("q4")
	global state
	global attrlis

	if inp == "qa":
		desc = attrlis.description + ',' + attrlis.description
		PARAMS = {'tr':desc} 
		requests.get(url = URLtr, params = PARAMS) 
		state = "q5"
		return "transfer learning..."
	# state = "q5"
	if inp == "publishDate":
		return attrlis.publishDate
	if inp == "problemtype":
		return attrlis.problemtype
	if inp == "reference_url":
		return attrlis.reference_url
	if inp == "reference_name":
		return attrlis.reference_name
	if inp == "reference_source":
		return attrlis.reference_source
	if inp == "reference_tags":
		return attrlis.reference_tags 
	if inp == "description_lang":
		return attrlis.description_lang
	if inp == "description":
		return attrlis.description
	if inp == "cvssv3_attackVector":
		return attrlis.cvssv3_attackVector
	if inp == "cvssv3_attackComplexity":
		return attrlis.cvssv3_attackComplexity
	if inp == "cvssv3_privilegesRequired":
		return attrlis.cvssv3_privilegesRequired
	if inp == "cvssv3_userInteraction":
		return attrlis.cvssv3_userInteraction
	if inp == "cvssv3_confidentialityImpact":
		return attrlis.cvssv3_confidentialityImpact
	if inp == "cvssv3_integrityImpact":
		return attrlis.cvssv3_integrityImpact
	if inp == "cvssv3_availabilityImpact":
		return attrlis.cvssv3_availabilityImpact
	if inp == "cvssv3_baseScore":
		return attrlis.cvssv3_baseScore
	if inp == "cvssv3_baseSeverity":
		return attrlis.cvssv3_baseSeverity
	if inp == "cvssv3_exploitabilityScore":
		return attrlis.cvssv3_exploitabilityScore
	if inp == "cvssv3_impactScore":
		return attrlis.cvssv3_impactScore
	if inp == "cvssv2_accessComplexity":
		return attrlis.cvssv2_accessComplexity
	if inp == "cvssv2_authentication":
		return attrlis.cvssv2_authentication
	if inp == "cvssv2_confidentialityImpact":
		return attrlis.cvssv2_confidentialityImpact
	if inp == "cvssv2_integrityImpact":
		return attrlis.cvssv2_integrityImpact
	if inp == "cvssv2_availabilityImpact":
		return attrlis.cvssv2_availabilityImpact
	if inp == "cvssv2_baseScore":
		return attrlis.cvssv2_baseScore
	if inp == "cvssv2_severity":
		return attrlis.cvssv2_severity
	if inp == "cvssv2_exploitabilityScore":
		return attrlis.cvssv2_exploitabilityScore
	if inp == "cvssv2_impactScore":
		return attrlis.cvssv2_impactScore
	if inp == "cvssv2_obtainAllPrivilege":
		return attrlis.cvssv2_obtainAllPrivilege
	if inp == "cvssv2_obtainUserPrivilege":
		return attrlis.cvssv2_obtainUserPrivilege
	if inp == "cvssv2_obtainOtherPrivilege":
		return attrlis.cvssv2_obtainOtherPrivilege
	if inp == "cvssv2_userInteractionRequired":
		return attrlis.cvssv2_userInteractionRequired
	return "attribute not found"

def q5(inp):
	if inp == "bye":
		state = "q9"
		return "Bye"
	PARAMS = {'tr':inp} 
	rr = requests.get(url = URLpr, params = PARAMS) 
	return rr.content


while True:
	# global state
	inp0=input('-->')
	print("sta ",state)
	if state == "q1":
		out0 = q1(inp0)
		print(out0)
	elif state == "q2":
		out0 = q2(inp0)
		print(out0)
	elif state == "q3":
		out0 = q3(inp0)
		print("enter what attribute you want, enter qa to enter qa mode")
	elif state == "q4":
		out0 = q4(inp0)
		print(out0)
	elif state == "q5":
		out0 = q5(inp0)
		print(out0)
	else:
		print("thanks and bbye")