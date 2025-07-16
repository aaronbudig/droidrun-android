# Guarded import: allow this module to load even when `llama_index` is absent
# (e.g., on Android where Rust wheels cannot be built). If the real package
# isn't present, we create lightweight stubs so the rest of the codebase can
# still import this module without raising `ModuleNotFoundError`.
try:
    from llama_index.core.llms import ChatMessage
    from llama_index.core.workflow import Event
except ModuleNotFoundError:  # pragma: no cover
    class _Stub:
        def __getattr__(self, name):
            raise ModuleNotFoundError("llama_index is not installed") from None
        def __call__(self, *args, **kwargs):
            raise ModuleNotFoundError("llama_index is not installed") from None
    ChatMessage = _Stub()
    Event = _Stub
from typing import Any, Optional

from pydantic import PrivateAttr


class InputEvent(Event):
    input: list[ChatMessage]

class ModelOutputEvent(Event):
    thoughts: Optional[str] = None
    code: Optional[str] = None  

class ExecutionEvent(Event):
    code: str
    globals: dict[str, str] = {}
    locals: dict[str, str] = {}

class ExecutionResultEvent(Event):
    output: str

class FinalizeEvent(Event):
    _result: Any = PrivateAttr(default=None)

    def __init__(self, result: Any = None, **kwargs: Any) -> None:
        # forces the user to provide a result
        super().__init__(_result=result, **kwargs)

    def _get_result(self) -> Any:
        """This can be overridden by subclasses to return the desired result."""
        return self._result

    @property
    def result(self) -> Any:
        return self._get_result()