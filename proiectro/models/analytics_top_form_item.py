from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
from typing import Literal, cast






T = TypeVar("T", bound="AnalyticsTopFormItem")



@_attrs_define
class AnalyticsTopFormItem:
    """ One form ranked by submission volume

        Attributes:
            name (str):
            form_id (str):
            count (int):
            percent_of_total (float | str):
            prev_count (int | None | Unset):
            change_pct (float | Literal['new'] | None | Unset):
     """

    name: str
    form_id: str
    count: int
    percent_of_total: float | str
    prev_count: int | None | Unset = UNSET
    change_pct: float | Literal['new'] | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        name = self.name

        form_id = self.form_id

        count = self.count

        percent_of_total: float | str
        percent_of_total = self.percent_of_total

        prev_count: int | None | Unset
        if isinstance(self.prev_count, Unset):
            prev_count = UNSET
        else:
            prev_count = self.prev_count

        change_pct: float | Literal['new'] | None | Unset
        if isinstance(self.change_pct, Unset):
            change_pct = UNSET
        else:
            change_pct = self.change_pct


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "name": name,
            "form_id": form_id,
            "count": count,
            "percent_of_total": percent_of_total,
        })
        if prev_count is not UNSET:
            field_dict["prev_count"] = prev_count
        if change_pct is not UNSET:
            field_dict["change_pct"] = change_pct

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        form_id = d.pop("form_id")

        count = d.pop("count")

        def _parse_percent_of_total(data: object) -> float | str:
            return cast(float | str, data)

        percent_of_total = _parse_percent_of_total(d.pop("percent_of_total"))


        def _parse_prev_count(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        prev_count = _parse_prev_count(d.pop("prev_count", UNSET))


        def _parse_change_pct(data: object) -> float | Literal['new'] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            change_pct_type_1 = cast(Literal['new'] , data)
            if change_pct_type_1 != 'new':
                raise ValueError(f"change_pct_type_1 must match const 'new', got '{change_pct_type_1}'")
            return change_pct_type_1
            return cast(float | Literal['new'] | None | Unset, data)

        change_pct = _parse_change_pct(d.pop("change_pct", UNSET))


        analytics_top_form_item = cls(
            name=name,
            form_id=form_id,
            count=count,
            percent_of_total=percent_of_total,
            prev_count=prev_count,
            change_pct=change_pct,
        )


        analytics_top_form_item.additional_properties = d
        return analytics_top_form_item

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
