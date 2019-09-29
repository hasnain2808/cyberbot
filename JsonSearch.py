import json
z = 0
reference_url=[]
reference_name=[]
reference_source=[]
reference_tags=[]
class dessearc:
	def __init__(self, cve):
		self.cve =cve
	def setattr(self):
		with open ("nvdcve-1.1-2019.json") as datafile:
			data = json.load(datafile)
			# CVE = raw_input("Enter CVE: ")
			CVE = self.cve
			for item in data['CVE_Items']:
				if CVE == item.get("cve").get("CVE_data_meta").get("ID"):
					self.CVE_ID = item.get("cve").get("CVE_data_meta").get("ID")
					self.publishDate = item.get("publishedDate")
					self.problemtype = item.get("cve").get("problemtype").get("problemtype_data")[0].get("description")[0].get("value")
					self.reference_url = []
					self.reference_name = []
					self.reference_source = []
					self.reference_tags = []
					for x in range(len(item.get("cve").get("references").get("reference_data"))):
						self.reference_url.insert(x,item.get("cve").get("references").get("reference_data")[x].get("url"))
						self.reference_name.insert(x,item.get("cve").get("references").get("reference_data")[x].get("name"))
						self.reference_source.insert(x,item.get("cve").get("references").get("reference_data")[x].get("refsource"))
						z = 0
						for y in range(len(item.get("cve").get("references").get("reference_data")[x].get("tags"))):
							self.reference_tags.insert(z,item.get("cve").get("references").get("reference_data")[x].get("tags")[y])
							z = z+1
					self.description_lang = item.get("cve").get("description").get("description_data")[0].get("lang")
					self.description = item.get("cve").get("description").get("description_data")[0].get("value")
					self.cvssv3_attackVector = item.get("impact").get("baseMetricV3").get("cvssV3").get("attackVector")
					self.cvssv3_attackComplexity = item.get("impact").get("baseMetricV3").get("cvssV3").get("attackComplexity") 
					self.cvssv3_privilegesRequired = item.get("impact").get("baseMetricV3").get("cvssV3").get("privilegesRequired")
					self.cvssv3_userInteraction = item.get("impact").get("baseMetricV3").get("cvssV3").get("userInteraction")
					self.cvssv3_confidentialityImpact = item.get("impact").get("baseMetricV3").get("cvssV3").get("confidentialityImpact")
					self.cvssv3_integrityImpact = item.get("impact").get("baseMetricV3").get("cvssV3").get("integrityImpact")
					self.cvssv3_availabilityImpact = item.get("impact").get("baseMetricV3").get("cvssV3").get("availabilityImpact")
					self.cvssv3_baseScore = item.get("impact").get("baseMetricV3").get("cvssV3").get("baseScore")
					self.cvssv3_baseSeverity = item.get("impact").get("baseMetricV3").get("cvssV3").get("baseSeverity")
					self.cvssv3_exploitabilityScore = item.get("impact").get("baseMetricV3").get("exploitabilityScore")
					self.cvssv3_impactScore = item.get("impact").get("baseMetricV3").get("impactScore")
					self.cvssv2_accessComplexity = item.get("impact").get("baseMetricV2").get("cvssV2").get("accessComplexity")
					self.cvssv2_authentication = item.get("impact").get("baseMetricV2").get("cvssV2").get("authentication")
					self.cvssv2_confidentialityImpact = item.get("impact").get("baseMetricV2").get("cvssV2").get("confidentialityImpact")
					self.cvssv2_integrityImpact = item.get("impact").get("baseMetricV2").get("cvssV2").get("integrityImpact")
					self.cvssv2_availabilityImpact = item.get("impact").get("baseMetricV2").get("cvssV2").get("availabilityImpact")
					self.cvssv2_baseScore = item.get("impact").get("baseMetricV2").get("cvssV2").get("baseScore")			
					self.cvssv2_severity = item.get("impact").get("baseMetricV2").get("severity")
					self.cvssv2_exploitabilityScore = item.get("impact").get("baseMetricV2").get("exploitabilityScore")
					self.cvssv2_impactScore = item.get("impact").get("baseMetricV2").get("impactScore")
					self.cvssv2_obtainAllPrivilege = item.get("impact").get("baseMetricV2").get("obtainAllPrivilege")
					self.cvssv2_obtainUserPrivilege = item.get("impact").get("baseMetricV2").get("obtainUserPrivilege")
					self.cvssv2_obtainOtherPrivilege = item.get("impact").get("baseMetricV2").get("obtainOtherPrivilege")
					self.cvssv2_userInteractionRequired = item.get("impact").get("baseMetricV2").get("userInteractionRequired")


