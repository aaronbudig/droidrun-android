import sys, types

# ------------------------------------------------------------------
# 1.  Fake base class `LLM`
# ------------------------------------------------------------------
_LLMBase = type("LLM", (), {})        # empty shell satisfies issubclass

# Register fake module path: llama_index.core.llms.llm
llm_mod = types.ModuleType("llama_index.core.llms.llm")
llm_mod.LLM = _LLMBase
sys.modules["llama_index.core.llms.llm"] = llm_mod

# Ensure parent packages exist
llama_index_pkg = sys.modules.setdefault("llama_index", types.ModuleType("llama_index"))
llms_pkg        = sys.modules.setdefault("llama_index.llms", types.ModuleType("llama_index.llms"))

# ------------------------------------------------------------------
# 2.  Provider stubs
# ------------------------------------------------------------------
class DummyLLM(_LLMBase):             # <-- now subclasses the fake LLM
    """Minimal no-op LLM used on Android when real back-ends are unavailable."""

    def __init__(self, *args, **kwargs):
        # Accept any constructor signature without exploding.
        super().__init__()
        # Store kwargs for debugging if you like.
        self._init_kwargs = kwargs
    def complete(self, *_, **__): return "stub"

# openai provider
openai_mod = types.ModuleType("llama_index.llms.openai")
openai_mod.OpenAI = DummyLLM
sys.modules["llama_index.llms.openai"] = openai_mod

# stub provider
stub_mod = types.ModuleType("llama_index.llms.stub")
stub_mod.StubLLM = DummyLLM
stub_mod.stub    = DummyLLM      # lower-case
stub_mod.Stub    = DummyLLM      # title-case
sys.modules["llama_index.llms.stub"] = stub_mod