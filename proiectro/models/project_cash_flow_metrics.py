from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.monthly_projection import MonthlyProjection


T = TypeVar("T", bound="ProjectCashFlowMetrics")


@_attrs_define
class ProjectCashFlowMetrics:
    """Cash flow metrics for a project.
    Extensible schema for future additions like margin, ROI, etc.

        Attributes:
            project_id (str):
            project_name (str):
            currency_symbol (str):
            total_inflow (float | str):
            total_outflow (float | str):
            net_cash_flow (float | str):
            monthly_projections (list[MonthlyProjection] | Unset):
    """

    project_id: str
    project_name: str
    currency_symbol: str
    total_inflow: float | str
    total_outflow: float | str
    net_cash_flow: float | str
    monthly_projections: list[MonthlyProjection] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        project_id = self.project_id

        project_name = self.project_name

        currency_symbol = self.currency_symbol

        total_inflow: float | str
        total_inflow = self.total_inflow

        total_outflow: float | str
        total_outflow = self.total_outflow

        net_cash_flow: float | str
        net_cash_flow = self.net_cash_flow

        monthly_projections: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.monthly_projections, Unset):
            monthly_projections = []
            for monthly_projections_item_data in self.monthly_projections:
                monthly_projections_item = monthly_projections_item_data.to_dict()
                monthly_projections.append(monthly_projections_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "project_id": project_id,
                "project_name": project_name,
                "currency_symbol": currency_symbol,
                "total_inflow": total_inflow,
                "total_outflow": total_outflow,
                "net_cash_flow": net_cash_flow,
            }
        )
        if monthly_projections is not UNSET:
            field_dict["monthly_projections"] = monthly_projections

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.monthly_projection import MonthlyProjection

        d = dict(src_dict)
        project_id = d.pop("project_id")

        project_name = d.pop("project_name")

        currency_symbol = d.pop("currency_symbol")

        def _parse_total_inflow(data: object) -> float | str:
            return cast(float | str, data)

        total_inflow = _parse_total_inflow(d.pop("total_inflow"))

        def _parse_total_outflow(data: object) -> float | str:
            return cast(float | str, data)

        total_outflow = _parse_total_outflow(d.pop("total_outflow"))

        def _parse_net_cash_flow(data: object) -> float | str:
            return cast(float | str, data)

        net_cash_flow = _parse_net_cash_flow(d.pop("net_cash_flow"))

        _monthly_projections = d.pop("monthly_projections", UNSET)
        monthly_projections: list[MonthlyProjection] | Unset = UNSET
        if _monthly_projections is not UNSET:
            monthly_projections = []
            for monthly_projections_item_data in _monthly_projections:
                monthly_projections_item = MonthlyProjection.from_dict(
                    monthly_projections_item_data
                )

                monthly_projections.append(monthly_projections_item)

        project_cash_flow_metrics = cls(
            project_id=project_id,
            project_name=project_name,
            currency_symbol=currency_symbol,
            total_inflow=total_inflow,
            total_outflow=total_outflow,
            net_cash_flow=net_cash_flow,
            monthly_projections=monthly_projections,
        )

        project_cash_flow_metrics.additional_properties = d
        return project_cash_flow_metrics

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
