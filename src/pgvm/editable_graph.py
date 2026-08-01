import graphviz

class EditableGraph():
  """
  @Summ: 編集可能なgraph構造を与えるclass.

  @Desc:
  - node番号は非負整数である。負の値はerror用。
  """
  PATH_DELIMITER="/"

  def __init__(self,graph,rootNode:int,program:list=None):
    """
    @Summ: constructor.

    @InsVars:
      data:
        @Summ: {node番号(int):{edgeLabel(str):node番号(int)}}。
        @Type: Dict
      rootNode:
        @Summ: root nodeのnode番号。
        @Type: Int
      maxNodeIdx:
        @Summ: node番号の最大値を記録する。
        @Type: Int
      program:
        @Summ: programのdataを入れる。
        @Type: Str型二次元配列。
      programCounter:
        @Summ: 次に実行するprogramの行番号を記録する。
        @Desc: 例外messageを出すために必要。
        @Type: Int
      programLength:
        @Summ: 次に実行するprogramの行数を記録する。
        @Type: Int
    """
    self.graph=graph
    self.rootNode=rootNode
    self.maxNodeIdx=None
    self.program=program
    self.programCounter=0
    if(program is None):
      self.programLength=0
    else:
      self.programLength=len(program)

  def loadProgramCSV(self,csvFile):
    """
    @Summ: programが書かれたCSV fileをloadする関数。

    @Args:
      csvFile:
        @Summ: programが書かれたcsv file名。
        @SemType: str型の二次元配列。
    """
    with open(csvFile,mode="r",encoding="utf-8") as f:
      lineList=f.readlines()
    programData=[]
    for line in lineList:
      if(line[-1]=="\n"):
        notBreakLine=line[:-1]
      else:
        notBreakLine=line
      argList=notBreakLine.split(",")
      programData.append(argList)
    self.program=programData
    self.programLength=len(programData)

  def visualizeProgram(self,filename):
    """
    @Summ: programをgraph構造で可視化する関数。
    """
    digraph=graphviz.Digraph()
    digraph.filename=filename
    digraph.format="svg"
    digraph.attr("graph",rankdir="LR")
    digraph.node(name="start")
    digraph.node(name="end")
    digraph.edge("start","row_0:command")
    for i in range(self.programLength):
      argList=self.program[i]
      command=argList[0]
      match command:
        case "gn":
          nodeLabel=f"<command> {command}|{argList[1]}|<jump1> {argList[2]}"
          if(int(argList[2])<self.programLength):
            digraph.edge(tail_name=f"row_{i}:jump1",head_name=f"row_{argList[2]}:head")
          else:
            digraph.edge(tail_name=f"row_{i}:jump1",head_name="end")
        case "ge":
          nodeLabel=f"<command> {command}|{argList[1]}|{argList[2]}|<jump1> {argList[3]}"
          if(int(argList[3])<self.programLength):
            digraph.edge(tail_name=f"row_{i}:jump1",head_name=f"row_{argList[3]}:head")
          else:
            digraph.edge(tail_name=f"row_{i}:jump1",head_name="end")
        case "se":
          nodeLabel=f"<command> {command}|{argList[1]}|{argList[2]}|<jump1> {argList[3]}"
          if(int(argList[3])<self.programLength):
            digraph.edge(tail_name=f"row_{i}:jump1",head_name=f"row_{argList[3]}:head")
          else:
            digraph.edge(tail_name=f"row_{i}:jump1",head_name="end")
        case "del":
          nodeLabel=f"<command> {command}|{argList[1]}|<jump1> {argList[2]}"
          if(int(argList[2])<self.programLength):
            digraph.edge(tail_name=f"row_{i}:jump1",head_name=f"row_{argList[2]}:head")
          else:
            digraph.edge(tail_name=f"row_{i}:jump1",head_name="end")
        case "if":
          nodeLabel=f"<command> {command}|{argList[1]}|{argList[2]}|<jump1> {argList[3]}|<jump2> {argList[4]}"
          if(int(argList[3])<self.programLength):
            digraph.edge(tail_name=f"row_{i}:jump1",head_name=f"row_{argList[3]}:head")
          else:
            digraph.edge(tail_name=f"row_{i}:jump1",head_name="end")
          if(int(argList[4])<self.programLength):
            digraph.edge(tail_name=f"row_{i}:jump2",head_name=f"row_{argList[4]}:head")
          else:
            digraph.edge(tail_name=f"row_{i}:jump2",head_name="end")
        case _:
          raise RuntimeError
      digraph.node(name=f"row_{i}",label=nodeLabel, shape="record")
    digraph.render()


  def __issueNewNode(self):
    """
    @Summ: 新しいnode番号を発行する関数。

    @Desc: 最大値を利用して新しい番号を生成している。

    @Returns:
      @Summ: 新しいnode番号。
      @Type: Int
    """
    if(self.maxNodeIdx is None):
      self.maxNodeIdx=max(self.graph.keys())
    newNodeIdx=self.maxNodeIdx+1
    self.maxNodeIdx=newNodeIdx
    self.graph[newNodeIdx]={}
    return newNodeIdx

  def visualize(self,filename):
    """
    @Summ: graphvizで可視化する関数。
    """
    digraph=graphviz.Digraph()
    digraph.filename=filename
    digraph.format="svg"
    digraph.attr("graph",rankdir="LR")
    for nodeIdx,edgeDict in self.graph.items():
      # print(nodeIdx)
      digraph.node(str(nodeIdx))
      for edgeLabel,destNode in edgeDict.items():
        digraph.edge(tail_name=str(nodeIdx), head_name=str(destNode), label=edgeLabel)
    digraph.render()

  def accessNode(self,path:list):
    """
    @Summ: pathからedgeを参照する関数。

    @Args:
      path:
        @Summ: 参照するedge.
        @SemType: Str型List.
    @Returns:
    - @Summ: nodeの到達履歴。
      @Desc: 到達不可能になったらそこで終了する。
      @Type: Int型List
    - @Summ: 使わなかったedgeLabelの数。この数字を未到達度と呼ぶ。
      @Desc: 0で到達完了を表す。
      @Type: Int
    """
    history=[self.rootNode]
    curEdgeDict=self.graph[self.rootNode]
    pathLength=len(path)
    unreached=pathLength
    for i in range(pathLength):
      edgeLabel=path[i]
      curNode=curEdgeDict.get(edgeLabel)
      if(curNode is None):
        break
      history.append(curNode)
      curEdgeDict=self.graph[curNode]
      unreached-=1
    return history,unreached


  def execute(self):
    """
    @Summ: programを実行する関数。
    """
    self.programCounter=0
    while(True):
      if(self.programLength<=self.programCounter):
        break
      argList=self.program[self.programCounter]
      command=argList[0]
      arglen=len(argList)
      match command:
        case "se":
          if(arglen!=4):
            raise RuntimeError(f"line: {self.programCounter}:\n\t the argument count is should be 4.")
          self.switchEdge(argList[1],argList[2])
          self.programCounter=int(argList[3])
        case "del":
          if(arglen!=3):
            raise RuntimeError(f"line: {self.programCounter}:\n\t the argument count is should be 3.")
          self.executeDeletion(argList[1])
          self.programCounter=int(argList[2])
        case "gn":
          if(arglen!=3):
            raise RuntimeError(f"line: {self.programCounter}:\n\t the argument count is should be 3.")
          self.generateNode(argList[1])
          self.programCounter=int(argList[2])
        case "ge":
          if(arglen!=4):
            raise RuntimeError(f"line: {self.programCounter}:\n\t the argument count is should be 4.")
          self.generateEdge(argList[1],argList[2])
          self.programCounter=int(argList[3])
        case "if":
          if(arglen!=5):
            raise RuntimeError(f"line: {self.programCounter}:\n\t the argument count is should be 5.")
          isSame=self.executeIf(argList[1],argList[2])
          if(isSame):
            self.programCounter=int(argList[3])
          else:
            self.programCounter=int(argList[4])
        case _:
          raise RuntimeError(f"line: {self.programCounter}:\n\t unknown command.")
    return

  def executeDeletion(self,path:str):
    """
    @Summ: 到達可能なedgeを削除する関数。

    @Args:
      path:
        @Summ: 既存のpath。このedgeを削除する。
        @Type: Str
    """
    edgeList=path.split(self.PATH_DELIMITER)
    lastNodePath=edgeList[:-1]
    lastEdge=edgeList[-1]
    history,unreached=self.accessNode(lastNodePath)
    if(unreached==0):
      lastNode=history[-1]
      del self.graph[lastNode][lastEdge]
    else:
      raise RuntimeError(f"line: {self.programCounter}:\n\t{path} is not accessable.")

  def generateNode(self,path):
    """
    @Summ: 未知のnodeへの新しいedgeを生成する関数。

    @Args:
      path:
        @Summ: 新規生成するpathを表す。
        @Desc: 未到達度=1である必要がある。
        @Type: Str
    """
    edgeList=path.split(self.PATH_DELIMITER)
    history,unreached=self.accessNode(edgeList)
    if(unreached!=1):
      raise RuntimeError(f"line: {self.programCounter}:\n\t{path} is not accessable.")
    lastEdge=edgeList[-1]
    lastNode=history[-1]
    newNode=self.__issueNewNode()
    self.graph[lastNode][lastEdge]=newNode

  def generateEdge(self,path1,path2):
    """
    @Summ: 既知のnodeへの新しいedgeを生成する関数。

    @Args:
      path1:
        @Summ: 終点を動かすpathを指定する。
        @Desc: 未知のpathしか受け付けない。
        @Type: Str
      path2:
        @Summ: edgeの新しい終着点を指定する。
        @Desc: 既知のpathしか受け付けない。
        @Type: Str
    """
    path1EdgeList=path1.split(self.PATH_DELIMITER)
    path2EdgeList=path2.split(self.PATH_DELIMITER)
    # self.changeEdgeDestination(path1EdgeList,path2EdgeList)
    path1history,unused1=self.accessNode(path1EdgeList)
    lastEdgeLabel=path1EdgeList[-1]
    if(unused1!=1):
      raise RuntimeError(f"line: {self.programCounter}:\n\t{path1} is not accessable.")
    edgeStartNode=path1history[-1]
    path2history,unused2=self.accessNode(path2EdgeList)
    if(unused2>0):
      raise RuntimeError(f"line: {self.programCounter}:\n\t{path2} is not accessable.")
    newEndNode=path2history[-1]
    self.graph[edgeStartNode][lastEdgeLabel]=newEndNode

  def switchEdge(self,path1,path2):
    """
    @Summ: 既知のpathの終点を既知のnodeに切り替える関数。

    @Desc: 始点と終点が同じ辺(二重辺)は禁止。

    @Args:
      path1:
        @Summ: 終点を動かすpathを指定する。
        @Desc: 既知のpathしか受け付けない。
        @Type: Str
      path2:
        @Summ: edgeの新しい終着点を指定する。
        @Desc: 既知のpathしか受け付けない。
        @Type: Str
    """
    path1EdgeList=path1.split(self.PATH_DELIMITER)
    path2EdgeList=path2.split(self.PATH_DELIMITER)
    path1history,unused1=self.accessNode(path1EdgeList)
    lastEdge=path1EdgeList[-1]
    if(unused1>0):
      raise RuntimeError(f"line: {self.programCounter}:\n\t{path1} is not accessable.")
    newStartNode=path1history[-2]
    path2history,unreached2=self.accessNode(path2EdgeList)
    if(unreached2>0):
      raise RuntimeError(f"line: {self.programCounter}:\n\t{path2} is not accessable.")
    newEndNode=path2history[-1]
    edgeInfo=self.graph[newStartNode]
    if(newEndNode in edgeInfo.values()):
      raise RuntimeError(f"line: {self.programCounter}:\n\t Edge endpoint is duplicated.")    #既存のedgeの終端が被る。
    self.graph[newStartNode][lastEdge]=newEndNode

  def executeIf(self,path1,path2):
    """
    @Summ: if文を実行する関数。

    @Args:
      path1:
        @Summ: if文の第一引数。比較するpathその1。
        @Type: Str
      path2:
        @Summ: if文の第二引数。比較するpathその2。
        @Type: Str
    @Returns:
      @Summ: 同じ値の時にTrue.
      @Type: Bool
    """
    path1EdgeList=path1.split(self.PATH_DELIMITER)
    path1History,path1unreached=self.accessNode(path1EdgeList)
    path2EdgeList=path2.split(self.PATH_DELIMITER)
    path2History,path2unreached=self.accessNode(path2EdgeList)
    if(path1unreached!=0):
      raise RuntimeError(f"line {self.programCounter}:\n\t{path1} is not accessable.")
    if(path2unreached!=0):
      raise RuntimeError(f"line {self.programCounter}:\n\t{path2} is not accessable.")
    path1LastNode=path1History[-1]
    path2LastNode=path2History[-1]
    if(path1LastNode==path2LastNode):
      return True
    else:
      return False

