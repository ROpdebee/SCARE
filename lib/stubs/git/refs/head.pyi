from .reference import Reference
from .symbolic import SymbolicReference
from .remote import RemoteReference
from ..objects.commit import Commit
Repo = Any # from ..repo import Repo
from ..config import GitConfigParser
from typing import Any, Optional, Union, List

class HEAD(SymbolicReference):
    def __init__(self, repo: Repo, path: str = ...) -> None: ...
    def orig_head(self) -> SymbolicReference: ...
    def reset(self, commit: Union[str, Commit, SymbolicReference] = ..., index: bool = ..., working_tree: bool = ..., paths: Optional[Union[List[str], str]] = ..., **kwargs: Any) -> HEAD: ...

class Head(Reference):
    k_config_remote: str = ...
    k_config_remote_ref: str = ...
    @classmethod
    def delete(cls, repo: Repo, *heads: Head, **kwargs: Any) -> None: ...
    def set_tracking_branch(self, remote_reference: RemoteReference) -> Head: ...
    def tracking_branch(self) -> RemoteReference: ...
    def rename(self, new_path: str, force: bool = ...) -> Head: ...  # type: ignore[override]
    def checkout(self, force: bool = ..., **kwargs: Any) -> SymbolicReference: ...
    def config_reader(self) -> GitConfigParser: ...
    def config_writer(self) -> GitConfigParser: ...