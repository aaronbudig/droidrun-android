"""
Android stubs for llama_index LLM provider modules.

They register empty modules so imports like
`import llama_index.llms.stub` or `...openai` succeed even though the
real Rust-backed packages are not present on Android.
"""
import sys, types

# Ensure parent packages exist.
llama_index_pkg = sys.modules.setdefault("llama_index", types.ModuleType("llama_index"))
llms_pkg        = sys.modules.setdefault("llama_index.llms", types.ModuleType("llama_index.llms"))

class DummyLLM:
    """Placeholder so code can instantiate OpenAI() or StubLLM() without crashing."""
    def __init__(self, *_, **__):
        pass
    def complete(self, *_, **__):
        return "stub"

# openai provider path
openai_mod = types.ModuleType("llama_index.llms.openai")
openai_mod.OpenAI = DummyLLM
sys.modules["llama_index.llms.openai"] = openai_mod

# stub provider path
tub_mod = types.ModuleType("llama_index.llms.stub")
stub_mod = types.ModuleType("llama_index.llms.stub")
stub_mod.StubLLM = DummyLLM
sys.modules["llama_index.llms.stub"] = stub_mod