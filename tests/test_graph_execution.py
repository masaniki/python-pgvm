from pathlib import Path
import sys
from copy import deepcopy

import yaml

#sys.pathを弄る。
projectDir=Path(__file__).parent.parent
packageDir=projectDir/"src"
sys.path.append(str(packageDir))

from pgvm import EditableGraph

def testSuitExecution(suitDir:Path):
  """
  @Summ: suit単位でtestを実行する関数。

  @Desc: isTestのdefault値はtrue.

  @Args:
    suitDir:
      @Summ: test suitのdirectory.
      @Type: Path
  """
  suitInputFile=suitDir/"suit_input.yaml"
  suitOutputFile=suitDir/"suit_output.yaml"
  with open(suitInputFile,mode="r", encoding="utf-8") as f:
    inputDict=yaml.safe_load(f)
  resultDict={"detail":{}}
  abstract=True
  defaultConfig=inputDict.get("default")
  if(defaultConfig is None):
    defaultConfig={}
  for caseDir in suitDir.iterdir():
    if(caseDir.is_file()):
      continue
    caseName=caseDir.name
    # inputDictでfiltering.
    caseValue=inputDict.get(caseName,{})
    caseConfig=deepcopy(defaultConfig)
    for key,value in caseValue.items():
      caseConfig[key]=value
    isTest=caseConfig.get("test",False)
    if(isTest==False):
      continue
    else:
      del caseConfig["test"]
    result=testCaseExecution(caseDir,**caseConfig)
    if(result==False):
      abstract=False
    resultDict["detail"][caseName]=result
  resultDict["abstract"]=abstract
  with open(suitOutputFile,mode="w",encoding="utf-8") as f:
    yaml.safe_dump(resultDict,f)
  return


def testCaseExecution(caseDir:Path,outputName:str="output.yaml",expectedName:str|None=None,isDetail:bool=False)->bool:
  """
  @Summ: caes単位でtestを実行する関数。

  @Args:
    caseDir:
      @Summ: test caseのdirectoryを指定する。
    ouputName:
      @Summ: 出力するfile名。
    expectedName:
      @Summ: 期待する出力file名。
      @Desc: Noneの時は出力飲みする。
    isDetail:
      @Summ: 期待file以外のfileも出力する。
      @Default: false
  @Returns:
    @Summ: 実際出力と期待出力が同じ時にtrue.
    @Desc: 実際出力するだけの時もtrue.
  """
  graphFile=caseDir/"graph.yaml"
  programFile=caseDir/"program.csv"
  beforeDot=caseDir/"before.dot"
  afterDot=caseDir/"after.dot"
  outputFile=caseDir/outputName
  with open(graphFile,mode="r",encoding="utf-8") as f:
    graphDict=yaml.safe_load(f)
  eg01=EditableGraph()
  eg01.importGraph("file",graphDict,10)
  if(isDetail):
    eg01.visualize(beforeDot)
  eg01.loadProgramCSV(programFile)
  eg01.execute()
  with open(outputFile,mode="w",encoding="utf-8") as f:
    yaml.safe_dump(eg01.graph,f)
  if(isDetail):
    eg01.visualize(afterDot)
  # 期待fileと比較する場合。
  if(expectedName is None):
    return True
  else:
    expectedFile=caseDir/expectedName
    with open(expectedFile,mode="r",encoding="utf-8") as f:
      expDict=yaml.safe_load(f)
    # 2つのdict型を比較する。
    return expDict==eg01.graph

if(__name__=="__main__"):
  suitDir=Path(__file__).parent/"graph_execution"
  caseDir=Path(__file__).parent/"graph_execution"/"sandbox"
  # isSuccess=testCaseExecution(caseDir,"expected.yaml",None,True)
  # print(isSuccess)
  testSuitExecution(suitDir)
  # testCaseExecution(caseDir,isDetail=True)

