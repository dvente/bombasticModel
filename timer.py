import subprocess as sub
import os
import re

solutionPatern = re.compile("solution")
paramFilePatern = re.compile(r'.*\.param$')
timePatern = re.compile(r'(\d+\.\d+)')
solutionLengthPatern = re.compile(r'letting moveCol be \[([-?\d,? ?]+)')
logFile = "compTimes.log"


optFlags = ['-O' + str(x) for x in range(4)]

sub.call("rm -f " + logFile + " && touch " + logFile + " && echo \"file,optLevel,foundSolution,lenthOfSolution,compTime\" >> "+logFile,shell=True)


for root, dirs, files in os.walk("."):
	for file in files:
		filePath = os.path.join(root,file)
		if not paramFilePatern.match(filePath) or re.search(r'stac', filePath):
			continue
		else:
			for flag in optFlags:
				print(file,flag)
				subOut = sub.check_output("TIMEFORMAT='%U'; { time ../savilerow Bombastic.eprime "+filePath+" -run-solver "+flag+"; } 2>&1",shell=True)
				lineOut = str(filePath)
				lineOut += " , " + flag[-1]
				if solutionPatern.search(subOut):
					lineOut += ",true, "
					solutionOutput = sub.check_output("cat " + filePath + ".solution",shell=True)
					solutionSearch = solutionLengthPatern.search(solutionOutput)
					solutionLine = solutionSearch.group()
					solutionLength = len(re.findall(',',solutionLine)) + 1
					lineOut += str(solutionLength) + ","
				else:
					lineOut += ",false,NaN, "
				match = timePatern.search(subOut)
				lineOut += match.group(0)
				sub.call("echo \"" + lineOut + "\" >> "+logFile,shell=True)

