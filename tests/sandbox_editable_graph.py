from pathlib import Path
import sys
import yaml

#sys.pathを弄る。
projectDir=Path(__file__).parent.parent
packageDir=projectDir/"src"
sys.path.append(str(packageDir))

from pgvm import EditableGraph

SANDBOX_DIR=Path(__file__).parent/"editable_graph"/"sandbox"

def test_generateEdge():
  graphFile=SANDBOX_DIR/"graph01.yaml"
  beforeDot=SANDBOX_DIR/"graph01.dot"
  afterDot=SANDBOX_DIR/"test_generate_edge_after.dot"
  with open(graphFile,mode="r",encoding="utf-8") as f:
    graphDict=yaml.safe_load(f)
  eg01=EditableGraph(graphDict,10)
  eg01.visualize(beforeDot)
  eg01.generateEdge(["register"])
  eg01.generateEdge(["register","next"])
  eg01.visualize(afterDot)

def test_deleteEdge():
  graphFile=SANDBOX_DIR/"graph01.yaml"
  beforeDot=SANDBOX_DIR/"graph01.dot"
  afterDot=SANDBOX_DIR/"test_delete_edge_after.dot"
  with open(graphFile,mode="r",encoding="utf-8") as f:
    graphDict=yaml.safe_load(f)
  eg01=EditableGraph(graphDict,10)
  eg01.visualize(beforeDot)
  eg01.deleteEdge(["file","next"])
  eg01.deleteEdge(["file","value"])
  eg01.visualize(afterDot)

def test_changeEdge():
  graphFile=SANDBOX_DIR/"graph01.yaml"
  beforeDot=SANDBOX_DIR/"graph01.dot"
  afterDot=SANDBOX_DIR/"test_change_edge_after.dot"
  with open(graphFile,mode="r",encoding="utf-8") as f:
    graphDict=yaml.safe_load(f)
  eg01=EditableGraph(graphDict,10)
  eg01.visualize(beforeDot)
  eg01.generateEdge(["register"])
  eg01.generateEdge(["register","next"])
  eg01.changeEdgeDestination(["register","value"],["file","next"])
  eg01.deleteEdge(["file","next"])
  eg01.generateEdge(["file","next"])
  eg01.changeEdgeDestination(["file","value"],["register","value"])
  eg01.deleteEdge(["register","value"])
  eg01.generateEdge(["register","value"])
  eg01.visualize(afterDot)

def test_accessNode():
  graphFile=SANDBOX_DIR/"graph01.yaml"
  beforeDot=SANDBOX_DIR/"graph01.dot"
  with open(graphFile,mode="r",encoding="utf-8") as f:
    graphDict=yaml.safe_load(f)
  eg01=EditableGraph(graphDict,10)
  eg01.visualize(beforeDot)
  tup01=eg01.accessNode(["file","next","next","next"])
  print(tup01)

if(__name__=="__main__"):
  # test_accessableNode()
  sandboxFile=Path(__file__).parent/"class01"/"sandbox"/"graph01.yaml"
  with open(sandboxFile,mode="r",encoding="utf-8") as f:
    graphDict=yaml.safe_load(f)
  eg01=EditableGraph(graphDict,10)
  eg01.visualize("mygraph_before.dot")
  tup01=eg01.accessNode(["file","next","next","next"])
  print(tup01)
  eg01.visualize("mygraph_after.dot")

