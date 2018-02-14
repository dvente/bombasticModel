import subprocess as sub
import os
import re

solutionPatern = re.compile("solution")
paramFilePatern = re.compile(r'.*\.param$')
timePatern = re.compile(r'(\d+\.\d+)')
fileNamePatern = re.compile(r'.*Bombastic(\d+)\_(\d+).*')
logFile = "compTimes.log"


optFlags = ['-O' + str(x) for x in range(4)]

sub.call("rm -f " + logFile + " && touch " + logFile + " && echo \"instance_id,steps,optLevel,foundSolution,compTime\" >> "+logFile,shell=True)


for root, dirs, files in os.walk("."):
	for file in files:
		filePath = os.path.join(root,file)
		if not paramFilePatern.match(filePath) or re.search(r'stac', filePath):
			continue
		else:
			fileSearch = fileNamePatern.search(filePath)
                        instance_id = fileSearch.group(1)
                        steps  = fileSearch.group(2)

			for flag in optFlags:
				lineOut = str(instance_id) + "," + str(steps) + ","
				print(file,flag)
				subOut = sub.check_output("TIMEFORMAT='%U'; { time ../savilerow Bombastic.eprime "+filePath+" -run-solver "+flag+"; } 2>&1",shell=True)
				lineOut += flag[-1] + ","
				if solutionPatern.search(subOut):
					lineOut += "true,"
				else:
					lineOut += "false,"

				#solutionOutput = sub.check_output("cat " + filePath,shell=True)
                                #solutionSearch = solutionLengthPatern.search(solutionOutput)
                                #solutionLength = solutionSearch.group(1)
                                #lineOut += str(solutionLength) + ",

				match = timePatern.search(subOut)
				lineOut += match.group(0)
				sub.call("echo \"" + lineOut + "\" >> "+logFile,shell=True)

