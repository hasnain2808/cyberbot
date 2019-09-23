import subprocess
class searc():
    def __init__(self):
        self.it ="it"
    def initialsearch(self, querystr):
        test = subprocess.Popen(["searchsploit", "--json", "--id",querystr], stdout=subprocess.PIPE)
        output = test.communicate()
        print(output)
        self.output = output
        return output


    def finsearch(self, querystr):
        test = subprocess.Popen(["searchsploit", "--json","--exact", "--id",querystr], stdout=subprocess.PIPE)
        output = test.communicate()
        print(output)
        self.output = output
        return output