from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.my_pipeline_money import MyPipelineMoney
    from ..models.my_pipeline_stage import MyPipelineStage


T = TypeVar("T", bound="MyPipelineFunnel")


@_attrs_define
class MyPipelineFunnel:
    """
    Attributes:
        id (str):
        name (str):
        count (int):
        values (list[MyPipelineMoney]):
        stages (list[MyPipelineStage]):
    """

    id: str
    name: str
    count: int
    values: list[MyPipelineMoney]
    stages: list[MyPipelineStage]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        count = self.count

        values = []
        for values_item_data in self.values:
            values_item = values_item_data.to_dict()
            values.append(values_item)

        stages = []
        for stages_item_data in self.stages:
            stages_item = stages_item_data.to_dict()
            stages.append(stages_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "count": count,
                "values": values,
                "stages": stages,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.my_pipeline_money import MyPipelineMoney
        from ..models.my_pipeline_stage import MyPipelineStage

        d = dict(src_dict)
        id = d.pop("id")

        name = d.pop("name")

        count = d.pop("count")

        values = []
        _values = d.pop("values")
        for values_item_data in _values:
            values_item = MyPipelineMoney.from_dict(values_item_data)

            values.append(values_item)

        stages = []
        _stages = d.pop("stages")
        for stages_item_data in _stages:
            stages_item = MyPipelineStage.from_dict(stages_item_data)

            stages.append(stages_item)

        my_pipeline_funnel = cls(
            id=id,
            name=name,
            count=count,
            values=values,
            stages=stages,
        )

        my_pipeline_funnel.additional_properties = d
        return my_pipeline_funnel

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
