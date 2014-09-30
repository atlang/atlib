"""The standard library for atlang, an extensible static type system for Python."""
import atlang

class fn(atlang.FnType):
  @classmethod
  def init_ctx(cls, ctx):
    # TODO: initialize assignables
    pass

  def init_ctx(self, ctx):
    # TODO: initialize assignables
    pass

  def ana_FunctionDef_TopLevel(self, ctx, tree, static_env):
    # TODO: iterate over statements?
    pass

  @classmethod
  def syn_FunctionDef_TopLevel(self, ctx, tree, static_env):
    # TODO: iterate over statements?
    pass

  @classmethod
  def check_Pass(cls, ctx, tree):
    pass

