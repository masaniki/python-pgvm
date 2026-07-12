from pathlib import Path
import sys
import yaml

#sys.pathを弄る。
projectDir=Path(__file__).parent.parent
packageDir=projectDir/"src"
sys.path.append(str(packageDir))

from edge_assembler import EditableGraph

if(__name__=="__main__"):
  graphFile=Path(__file__).parent/"class01"/"sandbox02"/"test01.yaml"
  programFile=Path(__file__).parent/"class01"/"sandbox02"/"ifTest03.csv"
  with open(graphFile,mode="r",encoding="utf-8") as f:
    graphDict=yaml.safe_load(f)
  eg01=EditableGraph(graphDict,10)
  eg01.visualize("mygraph_before.dot")
  eg01.loadProgramCSV(str(programFile))
  print(eg01.program)
  eg01.execute()
  # tup01=eg01.accessNode(["file","next","next","next"])
  # print(tup01)
  eg01.visualize("mygraph_after.dot")

