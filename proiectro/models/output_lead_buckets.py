from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.output_lead_bucket import OutputLeadBucket





T = TypeVar("T", bound="OutputLeadBuckets")



@_attrs_define
class OutputLeadBuckets:
    """ Worklist response — four buckets stacked vertically.

        Attributes:
            overdue (OutputLeadBucket): One bucket of the worklist (overdue / today / untriaged / scheduled).
            today (OutputLeadBucket): One bucket of the worklist (overdue / today / untriaged / scheduled).
            untriaged (OutputLeadBucket): One bucket of the worklist (overdue / today / untriaged / scheduled).
            scheduled (OutputLeadBucket): One bucket of the worklist (overdue / today / untriaged / scheduled).
            total_count (int):
            closed_visible (bool | Unset):  Default: False.
     """

    overdue: OutputLeadBucket
    today: OutputLeadBucket
    untriaged: OutputLeadBucket
    scheduled: OutputLeadBucket
    total_count: int
    closed_visible: bool | Unset = False
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.output_lead_bucket import OutputLeadBucket
        overdue = self.overdue.to_dict()

        today = self.today.to_dict()

        untriaged = self.untriaged.to_dict()

        scheduled = self.scheduled.to_dict()

        total_count = self.total_count

        closed_visible = self.closed_visible


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "overdue": overdue,
            "today": today,
            "untriaged": untriaged,
            "scheduled": scheduled,
            "total_count": total_count,
        })
        if closed_visible is not UNSET:
            field_dict["closed_visible"] = closed_visible

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.output_lead_bucket import OutputLeadBucket
        d = dict(src_dict)
        overdue = OutputLeadBucket.from_dict(d.pop("overdue"))




        today = OutputLeadBucket.from_dict(d.pop("today"))




        untriaged = OutputLeadBucket.from_dict(d.pop("untriaged"))




        scheduled = OutputLeadBucket.from_dict(d.pop("scheduled"))




        total_count = d.pop("total_count")

        closed_visible = d.pop("closed_visible", UNSET)

        output_lead_buckets = cls(
            overdue=overdue,
            today=today,
            untriaged=untriaged,
            scheduled=scheduled,
            total_count=total_count,
            closed_visible=closed_visible,
        )


        output_lead_buckets.additional_properties = d
        return output_lead_buckets

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
