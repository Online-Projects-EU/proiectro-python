from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="ReassignLeadsInList")



@_attrs_define
class ReassignLeadsInList:
    """ Admin cross-owner bulk reassign within a single list.

        Attributes:
            to_owner (str):
            from_owner (None | str | Unset):
     """

    to_owner: str
    from_owner: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        to_owner = self.to_owner

        from_owner: None | str | Unset
        if isinstance(self.from_owner, Unset):
            from_owner = UNSET
        else:
            from_owner = self.from_owner


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "to_owner": to_owner,
        })
        if from_owner is not UNSET:
            field_dict["from_owner"] = from_owner

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        to_owner = d.pop("to_owner")

        def _parse_from_owner(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        from_owner = _parse_from_owner(d.pop("from_owner", UNSET))


        reassign_leads_in_list = cls(
            to_owner=to_owner,
            from_owner=from_owner,
        )


        reassign_leads_in_list.additional_properties = d
        return reassign_leads_in_list

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
