from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.pydantic_detail_item import PydanticDetailItem


T = TypeVar("T", bound="PydanticDetail")


@_attrs_define
class PydanticDetail:
    """Field-level validation errors: one entry per field that was refused.

    Attributes:
        detail (list[PydanticDetailItem]):
    """

    detail: list[PydanticDetailItem]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        detail = []
        for detail_item_data in self.detail:
            detail_item = detail_item_data.to_dict()
            detail.append(detail_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "detail": detail,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.pydantic_detail_item import PydanticDetailItem

        d = dict(src_dict)
        detail = []
        _detail = d.pop("detail")
        for detail_item_data in _detail:
            detail_item = PydanticDetailItem.from_dict(detail_item_data)

            detail.append(detail_item)

        pydantic_detail = cls(
            detail=detail,
        )

        pydantic_detail.additional_properties = d
        return pydantic_detail

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
