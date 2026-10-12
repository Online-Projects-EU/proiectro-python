from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="PydanticDetailItem")


@_attrs_define
class PydanticDetailItem:
    """One per-field error inside a 422 ``detail`` array.

    Attributes:
        type_ (str):
        loc (list[str]):
        msg (str):
    """

    type_: str
    loc: list[str]
    msg: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_

        loc = self.loc

        msg = self.msg

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
                "loc": loc,
                "msg": msg,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        type_ = d.pop("type")

        loc = cast(list[str], d.pop("loc"))

        msg = d.pop("msg")

        pydantic_detail_item = cls(
            type_=type_,
            loc=loc,
            msg=msg,
        )

        pydantic_detail_item.additional_properties = d
        return pydantic_detail_item

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
