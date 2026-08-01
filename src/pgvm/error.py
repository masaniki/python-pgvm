
class PGVMRuntimeError(RuntimeError):
  """
  @Summ: PGNM用の例外class.
  """
  def __init__(self, line:int, message:str):
    super().__init__()
    self.line=line
    self.message=message
  
  def __str__(self):
    return f"line: {self.line}:\n\t{self.message}"

class PGVMInvalidPath(PGVMRuntimeError):
  """
  @Summ: pathが参照できない時のerror.
  """
  def __init__(self, line:int, path:str):
    super().__init__(line,message=f"{path} is not accesible.")
    self.line=line
    self.path=path

class PGVMSyntaxError(PGVMRuntimeError):
  """
  @Summ: PGLの構文解析上のerror.
  """
  def __init__(self, line:int, message:str):
    super().__init__(line,message)
