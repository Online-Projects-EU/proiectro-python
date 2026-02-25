from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="MonthlyProjection")


@_attrs_define
class MonthlyProjection:
    """Monthly cash flow projection data

    Attributes:
        month_name (str):
        inflow (float | str):
        outflow (float | str):
        net (float | str):
        cumulative (float | str):
    """

    month_name: str
    inflow: float | str
    outflow: float | str
    net: float | str
    cumulative: float | str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        month_name = self.month_name

        inflow: float | str
        inflow = self.inflow

        outflow: float | str
        outflow = self.outflow

        net: float | str
        net = self.net

        cumulative: float | str
        cumulative = self.cumulative

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "month_name": month_name,
                "inflow": inflow,
                "outflow": outflow,
                "net": net,
                "cumulative": cumulative,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        month_name = d.pop("month_name")

        def _parse_inflow(data: object) -> float | str:
            return cast(float | str, data)

        inflow = _parse_inflow(d.pop("inflow"))

        def _parse_outflow(data: object) -> float | str:
            return cast(float | str, data)

        outflow = _parse_outflow(d.pop("outflow"))

        def _parse_net(data: object) -> float | str:
            return cast(float | str, data)

        net = _parse_net(d.pop("net"))

        def _parse_cumulative(data: object) -> float | str:
            return cast(float | str, data)

        cumulative = _parse_cumulative(d.pop("cumulative"))

        monthly_projection = cls(
            month_name=month_name,
            inflow=inflow,
            outflow=outflow,
            net=net,
            cumulative=cumulative,
        )

        monthly_projection.additional_properties = d
        return monthly_projection

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
