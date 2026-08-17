from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.output_lead_summary import OutputLeadSummary





T = TypeVar("T", bound="OutputLeadBucket")



@_attrs_define
class OutputLeadBucket:
    """ One bucket of the worklist (overdue / today / untriaged / scheduled).

        Attributes:
            name (str):
            label (str):
            count (int):
            leads (list[OutputLeadSummary]):
            has_more (bool | Unset):  Default: False.
            next_cursor (None | str | Unset):
     """

    name: str
    label: str
    count: int
    leads: list[OutputLeadSummary]
    has_more: bool | Unset = False
    next_cursor: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.output_lead_summary import OutputLeadSummary
        name = self.name

        label = self.label

        count = self.count

        leads = []
        for leads_item_data in self.leads:
            leads_item = leads_item_data.to_dict()
            leads.append(leads_item)



        has_more = self.has_more

        next_cursor: None | str | Unset
        if isinstance(self.next_cursor, Unset):
            next_cursor = UNSET
        else:
            next_cursor = self.next_cursor


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "name": name,
            "label": label,
            "count": count,
            "leads": leads,
        })
        if has_more is not UNSET:
            field_dict["has_more"] = has_more
        if next_cursor is not UNSET:
            field_dict["next_cursor"] = next_cursor

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.output_lead_summary import OutputLeadSummary
        d = dict(src_dict)
        name = d.pop("name")

        label = d.pop("label")

        count = d.pop("count")

        leads = []
        _leads = d.pop("leads")
        for leads_item_data in (_leads):
            leads_item = OutputLeadSummary.from_dict(leads_item_data)



            leads.append(leads_item)


        has_more = d.pop("has_more", UNSET)

        def _parse_next_cursor(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        next_cursor = _parse_next_cursor(d.pop("next_cursor", UNSET))


        output_lead_bucket = cls(
            name=name,
            label=label,
            count=count,
            leads=leads,
            has_more=has_more,
            next_cursor=next_cursor,
        )


        output_lead_bucket.additional_properties = d
        return output_lead_bucket

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
