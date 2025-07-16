from typing import List

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

class InputEvent(Event):
    input: list[ChatMessage]

class ModelResponseEvent(Event):
    response: str


class ExecutePlan(Event):
    pass

class TaskFailedEvent(Event):
    task_description: str
    reason: str

