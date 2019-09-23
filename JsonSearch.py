import json
z = 0
reference_url=[]
reference_name=[]
reference_source=[]
reference_tags=[]
with open ("/home/anonnick/CVE/nvdcve-1.1-2019.json") as datafile:
	data = json.load(datafile)
	CVE = raw_input("Enter CVE: ")
	for item in data['CVE_Items']:
		if CVE == item.get("cve").get("CVE_data_meta").get("ID"):
			CVE_ID = item.get("cve").get("CVE_data_meta").get("ID")
			publishDate = item.get("publishedDate")
			problemtype = item.get("cve").get("problemtype").get("problemtype_data")[0].get("description")[0].get("value")
			for x in range(len(item.get("cve").get("references").get("reference_data"))):
				reference_url.insert(x,item.get("cve").get("references").get("reference_data")[x].get("url"))
				reference_name.insert(x,item.get("cve").get("references").get("reference_data")[x].get("name"))
				reference_source.insert(x,item.get("cve").get("references").get("reference_data")[x].get("refsource"))
				for y in range(len(item.get("cve").get("references").get("reference_data")[x].get("tags"))):
					reference_tags.insert(z,item.get("cve").get("references").get("reference_data")[x].get("tags")[y])
					z = z+1
			description_lang = item.get("cve").get("description").get("description_data")[0].get("lang")
			description = item.get("cve").get("description").get("description_data")[0].get("value")
			cvssv3_attackVector = item.get("impact").get("baseMetricV3").get("cvssV3").get("attackVector")
			cvssv3_attackComplexity = item.get("impact").get("baseMetricV3").get("cvssV3").get("attackComplexity") 
			cvssv3_privilegesRequired = item.get("impact").get("baseMetricV3").get("cvssV3").get("privilegesRequired")
			cvssv3_userInteraction = item.get("impact").get("baseMetricV3").get("cvssV3").get("userInteraction")
			cvssv3_confidentialityImpact = item.get("impact").get("baseMetricV3").get("cvssV3").get("confidentialityImpact")
			cvssv3_integrityImpact = item.get("impact").get("baseMetricV3").get("cvssV3").get("integrityImpact")
			cvssv3_availabilityImpact = item.get("impact").get("baseMetricV3").get("cvssV3").get("availabilityImpact")
			cvssv3_baseScore = item.get("impact").get("baseMetricV3").get("cvssV3").get("baseScore")
			cvssv3_baseSeverity = item.get("impact").get("baseMetricV3").get("cvssV3").get("baseSeverity")
			cvssv3_exploitabilityScore = item.get("impact").get("baseMetricV3").get("exploitabilityScore")
			cvssv3_impactScore = item.get("impact").get("baseMetricV3").get("impactScore")
			cvssv2_accessComplexity = item.get("impact").get("baseMetricV2").get("cvssV2").get("accessComplexity")
			cvssv2_authentication = item.get("impact").get("baseMetricV2").get("cvssV2").get("authentication")
			cvssv2_confidentialityImpact = item.get("impact").get("baseMetricV2").get("cvssV2").get("confidentialityImpact")
			cvssv2_integrityImpact = item.get("impact").get("baseMetricV2").get("cvssV2").get("integrityImpact")
			cvssv2_availabilityImpact = item.get("impact").get("baseMetricV2").get("cvssV2").get("availabilityImpact")
			cvssv2_baseScore = item.get("impact").get("baseMetricV2").get("cvssV2").get("baseScore")			
			cvssv2_severity = item.get("impact").get("baseMetricV2").get("severity")
			cvssv2_exploitabilityScore = item.get("impact").get("baseMetricV2").get("exploitabilityScore")
			cvssv2_impactScore = item.get("impact").get("baseMetricV2").get("impactScore")
			cvssv2_obtainAllPrivilege = item.get("impact").get("baseMetricV2").get("obtainAllPrivilege")
			cvssv2_obtainUserPrivilege = item.get("impact").get("baseMetricV2").get("obtainUserPrivilege")
			cvssv2_obtainOtherPrivilege = item.get("impact").get("baseMetricV2").get("obtainOtherPrivilege")
			cvssv2_userInteractionRequired = item.get("impact").get("baseMetricV2").get("userInteractionRequired")


