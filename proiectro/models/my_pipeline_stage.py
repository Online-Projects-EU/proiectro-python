from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.my_pipeline_money import MyPipelineMoney


T = TypeVar("T", bound="MyPipelineStage")


@_attrs_define
class MyPipelineStage:
    """
    Attributes:
        id (str):
        name (str):
        stage_type (str):
        count (int):
        values (list[MyPipelineMoney]):
    """

    id: str
    name: str
    stage_type: str
    count: int
    values: list[MyPipelineMoney]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        stage_type = self.stage_type

        count = self.count

        values = []
        for values_item_data in self.values:
            values_item = values_item_data.to_dict()
            values.append(values_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "stage_type": stage_type,
                "count": count,
                "values": values,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.my_pipeline_money import MyPipelineMoney

        d = dict(src_dict)
        id = d.pop("id")

        name = d.pop("name")

        stage_type = d.pop("stage_type")

        count = d.pop("count")

        values = []
        _values = d.pop("values")
        for values_item_data in _values:
            values_item = MyPipelineMoney.from_dict(values_item_data)

            values.append(values_item)

        my_pipeline_stage = cls(
            id=id,
            name=name,
            stage_type=stage_type,
            count=count,
            values=values,
        )

        my_pipeline_stage.additional_properties = d
        return my_pipeline_stage

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
