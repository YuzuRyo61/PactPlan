from typing import Optional

from pydantic import constr

from .base import APBase, http_regex


class APUser(APBase):
    type: str = "Person"
    id: constr(
        regex=http_regex)
    inbox: constr(
        regex=http_regex)
    outbox: Optional[constr(
        regex=http_regex)]
    followers: Optional[constr(
        regex=http_regex)]
    following: Optional[constr(
        regex=http_regex)]
    featured: Optional[constr(
        regex=http_regex)]
    endpoints: Optional[dict]
    url: Optional[constr(
        regex=http_regex)]
    preferredUsername: Optional[str]
    name: Optional[str]
    summary: Optional[str]
    icon: Optional[dict]  # TODO: 仮の型指定。将来的に変更。
    image: Optional[dict]  # TODO: 仮の型指定。将来的に変更。
    tag: Optional[list]  # TODO: 仮の型指定。将来的に変更。
    manuallyApprovesFollows: bool = False
    publicKey: Optional[dict]
