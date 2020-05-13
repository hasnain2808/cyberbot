# cyberbot
A bot that can give you information about various vulnerabilities in natural language<br />
the bot uses bert for qa <br />
the bot has a state machine<br />
<br />
run the project<br />
go to the nvd website and download all the json fiels for each year of vulnerability and save it in root of the project.
<br />
install cdqa on python3.6 using pip<br />
running python main.py would now turn on the bot<br />
now choose a domain like windows<br />
now send the ebe-id of the vulnerability you want to know from the list displayed.<br />
now you can ask about the attributes from nvd about this vulnerability.<br />
type qa to switch to bert powered natural language bot<br />
<br />
<br />
[Click here to read the report](https://github.com/hasnain2808/cyberbot/blob/master/AIHNV.pdf)

A file by the name AINHV.pdf in the repository is the project report<br />
please read it for full details of the project.<br />

The flow of the code follows the flowchart available on page 8 of the report
The state management of the bot follows the finite automata available on page 12 of the report

