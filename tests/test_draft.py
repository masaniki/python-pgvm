from pathlib import Path
import sys
import yaml

#sys.pathを弄る。
projectDir=Path(__file__).parent.parent
packageDir=projectDir/"src"
sys.path.append(str(packageDir))

from pgvm import EditableGraph

def testCaseExecution(testDir:Path,outputName:str,expectedName:str|None=None,isDetail:bool=False)->bool:
  """
  @Summ: caes単位でtestを実行する関数。

  @Args:
    testDir:
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
  graphFile=testDir/"graph.yaml"
  programFile=testDir/"program.csv"
  beforeDot=testDir/"before.dot"
  afterDot=testDir/"after.dot"
  outputFile=testDir/outputName
  with open(graphFile,mode="r",encoding="utf-8") as f:
    graphDict=yaml.safe_load(f)
  eg01=EditableGraph(graphDict,10)
  if(isDetail):
    eg01.visualize(beforeDot)
  eg01.loadProgramCSV(programFile)
  eg01.execute()
  with open(outputFile,mode="w",encoding="utf-8") as f:
    yaml.safe_dump(eg01.data,f)
  if(isDetail):
    eg01.visualize(afterDot)
  # 期待fileと比較する場合。
  if(expectedName is None):
    return True
  else:
    expectedFile=testDir/expectedName
    with open(expectedFile,mode="r",encoding="utf-8") as f:
      expDict=yaml.safe_load(f)
    for key,outValue in eg01.data.items():
      expValue=expDict.get(key)
      if(expValue is None):
        return False
      if(outValue!=expValue):
        return False
    return True

if(__name__=="__main__"):
  test_gn=Path(__file__).parent/"graph_execution"/"test_gn"
  isSuccess=testCaseExecution(test_gn,"output.yaml","expected.yaml",True)
  print(isSuccess)
