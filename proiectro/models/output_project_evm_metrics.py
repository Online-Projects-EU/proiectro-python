from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.evm_warning import EVMWarning
    from ..models.output_project_evm_metrics_chart_series_item import (
        OutputProjectEVMMetricsChartSeriesItem,
    )


T = TypeVar("T", bound="OutputProjectEVMMetrics")


@_attrs_define
class OutputProjectEVMMetrics:
    """Earned Value Management (EVM) metrics for a project

    Attributes:
        pv (str):
        ev (str):
        ac (str):
        spi (str):
        cpi (str):
        cv (str):
        sv (str):
        bac (str):
        eac (str):
        etc (str):
        vac (str):
        eac_method1 (str):
        etc_method1 (str):
        vac_method1 (str):
        eac_method2 (str):
        etc_method2 (str):
        vac_method2 (str):
        eac_method3 (str):
        etc_method3 (str):
        vac_method3 (str):
        eac_method4 (str):
        etc_method4 (str):
        vac_method4 (str):
        currency_symbol (str):
        percent_complete (str):
        spi_status (str):
        cpi_status (str):
        project_id (str):
        project_name (str):
        has_evm_data (bool):
        warnings (list[EVMWarning] | Unset):
        chart_categories (list[str] | Unset):
        chart_series (list[OutputProjectEVMMetricsChartSeriesItem] | Unset):
    """

    pv: str
    ev: str
    ac: str
    spi: str
    cpi: str
    cv: str
    sv: str
    bac: str
    eac: str
    etc: str
    vac: str
    eac_method1: str
    etc_method1: str
    vac_method1: str
    eac_method2: str
    etc_method2: str
    vac_method2: str
    eac_method3: str
    etc_method3: str
    vac_method3: str
    eac_method4: str
    etc_method4: str
    vac_method4: str
    currency_symbol: str
    percent_complete: str
    spi_status: str
    cpi_status: str
    project_id: str
    project_name: str
    has_evm_data: bool
    warnings: list[EVMWarning] | Unset = UNSET
    chart_categories: list[str] | Unset = UNSET
    chart_series: list[OutputProjectEVMMetricsChartSeriesItem] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        pv = self.pv

        ev = self.ev

        ac = self.ac

        spi = self.spi

        cpi = self.cpi

        cv = self.cv

        sv = self.sv

        bac = self.bac

        eac = self.eac

        etc = self.etc

        vac = self.vac

        eac_method1 = self.eac_method1

        etc_method1 = self.etc_method1

        vac_method1 = self.vac_method1

        eac_method2 = self.eac_method2

        etc_method2 = self.etc_method2

        vac_method2 = self.vac_method2

        eac_method3 = self.eac_method3

        etc_method3 = self.etc_method3

        vac_method3 = self.vac_method3

        eac_method4 = self.eac_method4

        etc_method4 = self.etc_method4

        vac_method4 = self.vac_method4

        currency_symbol = self.currency_symbol

        percent_complete = self.percent_complete

        spi_status = self.spi_status

        cpi_status = self.cpi_status

        project_id = self.project_id

        project_name = self.project_name

        has_evm_data = self.has_evm_data

        warnings: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.warnings, Unset):
            warnings = []
            for warnings_item_data in self.warnings:
                warnings_item = warnings_item_data.to_dict()
                warnings.append(warnings_item)

        chart_categories: list[str] | Unset = UNSET
        if not isinstance(self.chart_categories, Unset):
            chart_categories = self.chart_categories

        chart_series: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.chart_series, Unset):
            chart_series = []
            for chart_series_item_data in self.chart_series:
                chart_series_item = chart_series_item_data.to_dict()
                chart_series.append(chart_series_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "pv": pv,
                "ev": ev,
                "ac": ac,
                "spi": spi,
                "cpi": cpi,
                "cv": cv,
                "sv": sv,
                "bac": bac,
                "eac": eac,
                "etc": etc,
                "vac": vac,
                "eac_method1": eac_method1,
                "etc_method1": etc_method1,
                "vac_method1": vac_method1,
                "eac_method2": eac_method2,
                "etc_method2": etc_method2,
                "vac_method2": vac_method2,
                "eac_method3": eac_method3,
                "etc_method3": etc_method3,
                "vac_method3": vac_method3,
                "eac_method4": eac_method4,
                "etc_method4": etc_method4,
                "vac_method4": vac_method4,
                "currency_symbol": currency_symbol,
                "percent_complete": percent_complete,
                "spi_status": spi_status,
                "cpi_status": cpi_status,
                "project_id": project_id,
                "project_name": project_name,
                "has_evm_data": has_evm_data,
            }
        )
        if warnings is not UNSET:
            field_dict["warnings"] = warnings
        if chart_categories is not UNSET:
            field_dict["chart_categories"] = chart_categories
        if chart_series is not UNSET:
            field_dict["chart_series"] = chart_series

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.evm_warning import EVMWarning
        from ..models.output_project_evm_metrics_chart_series_item import (
            OutputProjectEVMMetricsChartSeriesItem,
        )

        d = dict(src_dict)
        pv = d.pop("pv")

        ev = d.pop("ev")

        ac = d.pop("ac")

        spi = d.pop("spi")

        cpi = d.pop("cpi")

        cv = d.pop("cv")

        sv = d.pop("sv")

        bac = d.pop("bac")

        eac = d.pop("eac")

        etc = d.pop("etc")

        vac = d.pop("vac")

        eac_method1 = d.pop("eac_method1")

        etc_method1 = d.pop("etc_method1")

        vac_method1 = d.pop("vac_method1")

        eac_method2 = d.pop("eac_method2")

        etc_method2 = d.pop("etc_method2")

        vac_method2 = d.pop("vac_method2")

        eac_method3 = d.pop("eac_method3")

        etc_method3 = d.pop("etc_method3")

        vac_method3 = d.pop("vac_method3")

        eac_method4 = d.pop("eac_method4")

        etc_method4 = d.pop("etc_method4")

        vac_method4 = d.pop("vac_method4")

        currency_symbol = d.pop("currency_symbol")

        percent_complete = d.pop("percent_complete")

        spi_status = d.pop("spi_status")

        cpi_status = d.pop("cpi_status")

        project_id = d.pop("project_id")

        project_name = d.pop("project_name")

        has_evm_data = d.pop("has_evm_data")

        _warnings = d.pop("warnings", UNSET)
        warnings: list[EVMWarning] | Unset = UNSET
        if _warnings is not UNSET:
            warnings = []
            for warnings_item_data in _warnings:
                warnings_item = EVMWarning.from_dict(warnings_item_data)

                warnings.append(warnings_item)

        chart_categories = cast(list[str], d.pop("chart_categories", UNSET))

        _chart_series = d.pop("chart_series", UNSET)
        chart_series: list[OutputProjectEVMMetricsChartSeriesItem] | Unset = UNSET
        if _chart_series is not UNSET:
            chart_series = []
            for chart_series_item_data in _chart_series:
                chart_series_item = OutputProjectEVMMetricsChartSeriesItem.from_dict(
                    chart_series_item_data
                )

                chart_series.append(chart_series_item)

        output_project_evm_metrics = cls(
            pv=pv,
            ev=ev,
            ac=ac,
            spi=spi,
            cpi=cpi,
            cv=cv,
            sv=sv,
            bac=bac,
            eac=eac,
            etc=etc,
            vac=vac,
            eac_method1=eac_method1,
            etc_method1=etc_method1,
            vac_method1=vac_method1,
            eac_method2=eac_method2,
            etc_method2=etc_method2,
            vac_method2=vac_method2,
            eac_method3=eac_method3,
            etc_method3=etc_method3,
            vac_method3=vac_method3,
            eac_method4=eac_method4,
            etc_method4=etc_method4,
            vac_method4=vac_method4,
            currency_symbol=currency_symbol,
            percent_complete=percent_complete,
            spi_status=spi_status,
            cpi_status=cpi_status,
            project_id=project_id,
            project_name=project_name,
            has_evm_data=has_evm_data,
            warnings=warnings,
            chart_categories=chart_categories,
            chart_series=chart_series,
        )

        output_project_evm_metrics.additional_properties = d
        return output_project_evm_metrics

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
