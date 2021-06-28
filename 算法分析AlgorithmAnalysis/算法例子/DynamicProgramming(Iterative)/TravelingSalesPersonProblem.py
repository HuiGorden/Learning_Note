#!python3
import re
import json
# Calculate optimal tour bases on ajacent matrix

nodes = ["V0", "V1", "V2", "V3"]
ajacentMatrix = [
    [0, 2, 9, float('inf')],
    [1, 0, 6, 4],
    [float('inf'), 7, 0, 8],
    [6, 3, float('inf'), 0]
]
DistanceDict = {eachNode: {} for eachNode in nodes}
routeRecorder = {eachNode: {} for eachNode in nodes}


def subsetGenerator(fullList, elementNumber):
    fullList = [element for element in fullList if element != "V0"]
    if elementNumber == 0:
        return ["Empty"]
    elif elementNumber == 1:
        return fullList
    else:
        subsetList = [
            ["Empty"],
            [element for element in fullList]
        ]
        # each loop add base element
        # starting result with element length = 1
        for i in range(2, elementNumber + 1):
            previousLevelResult = subsetList[i - 1]
            result = []
            # baseElement looping over [v1, v2,v3...]
            for baseElement in subsetList[1]:
                for index in range(len(previousLevelResult)):
                    if baseElement not in previousLevelResult[index]:
                        newElement = re.findall(r"(V\d)", previousLevelResult[index])
                        newElement.append(baseElement)
                        newElement = "".join(sorted(newElement))
                        if newElement not in result:
                            result.append(newElement)
            subsetList.append(result)
        return subsetList[elementNumber]


def outputShortestPath():
    path = "V0 ->"
    # notTravel: "V1V2V3"
    notTravel = "".join(nodes).replace("V0", "")
    goingTo = "V0"
    while notTravel:
        nextReach = routeRecorder[goingTo][notTravel]
        path += f" {nextReach} ->"
        notTravel = notTravel.replace(nextReach, "")
        goingTo = nextReach
    path += " V0"
    print(path)


# base case
for eachNode in DistanceDict:
    eachNodeIndex = int(eachNode.replace("V", ""))
    DistanceDict[eachNode]["Empty"] = ajacentMatrix[eachNodeIndex][0]
    routeRecorder[eachNode]["Empty"] = "V0"
# iterative
subsetSize = 1
while subsetSize <= len(nodes) - 1:
    for eachNode in DistanceDict:
        # print(f"1:eachNode:{eachNode}")
        subset = subsetGenerator(nodes, subsetSize)
        # print(f"2:subset:{subset}")
        for eachSubset in subset:
            minValue = float("inf")
            if eachNode not in eachSubset:
                nextReachNodeList = re.findall(r"(V\d)", eachSubset)
                for nextReachNode in nextReachNodeList:
                    eachNodeIndex = int(eachNode.replace("V", ""))
                    nextReachNodeIndex = int(nextReachNode.replace("V", ""))
                    # print(f"3:eachNode:{eachNode}")
                    # print(f"4:eachSubset:{eachSubset}")
                    # print(f"5:nextReachNode:{nextReachNode}")
                    if len(nextReachNodeList) == 1:
                        value = ajacentMatrix[eachNodeIndex][nextReachNodeIndex] + DistanceDict[nextReachNode]["Empty"]
                    else:
                        value = ajacentMatrix[eachNodeIndex][nextReachNodeIndex] + DistanceDict[nextReachNode][eachSubset.replace(nextReachNode, "")]
                    if value < minValue:
                        minValue = value
                        recordNextNode = nextReachNode
                DistanceDict[eachNode]["".join(eachSubset)] = minValue
                routeRecorder[eachNode]["".join(eachSubset)] = recordNextNode
    subsetSize += 1
print(f"Optimal Cost:{DistanceDict['V0'][''.join(nodes).replace('V0', '')]}")
outputShortestPath()

