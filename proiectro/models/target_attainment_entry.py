from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.target_band_rung import TargetBandRung
    from ..models.target_band_segment import TargetBandSegment
    from ..models.target_source import TargetSource


T = TypeVar("T", bound="TargetAttainmentEntry")


@_attrs_define
class TargetAttainmentEntry:
    """Attainment of one sales target metric for a report period.

    `target` is the whole period's number (the month for MTD, the quarter for QTD, the year for YTD),
    split from the rows in `sources` by calendar month. Attainment and bands are measured against it.
    `expected_to_date` is the share due by the end of the window -- the "expected by today" marker.

    `attainment_pct` and `band_name` are None whenever the comparison cannot honestly be made, with
    `unavailable` carrying the reason, and while the period has not started (`not_started`). A missing
    target produces no entry at all rather than a zero: a target nobody set is not one somebody missed.

        Attributes:
            metric (str):
            metric_label (str):
            target (float | str):
            scheme_name (str):
            currency (None | str | Unset):
            actual (float | None | str | Unset):
            attainment_pct (float | None | str | Unset):
            band_name (None | str | Unset):
            period_start (datetime.date | None | Unset):
            period_end (datetime.date | None | Unset):
            expected_to_date (float | None | str | Unset):
            expected_pct (float | None | str | Unset):
            pace_gap (float | None | str | Unset):
            elapsed (float | str | Unset):  Default: 0.0.
            period_length (float | str | Unset):  Default: 0.0.
            length_unit (str | Unset):  Default: 'days'.
            not_started (bool | Unset):  Default: False.
            coverage_partial (bool | Unset):  Default: False.
            covered_from (datetime.date | None | Unset):
            covered_until (datetime.date | None | Unset):
            prorated (bool | Unset):  Default: False.
            target_count (int | Unset):  Default: 1.
            sources (list[TargetSource] | Unset):
            unavailable (None | str | Unset):
            bands (list[TargetBandRung] | Unset):
            segments (list[TargetBandSegment] | Unset):
            scale_max_pct (float | str | Unset):  Default: 100.0.
    """

    metric: str
    metric_label: str
    target: float | str
    scheme_name: str
    currency: None | str | Unset = UNSET
    actual: float | None | str | Unset = UNSET
    attainment_pct: float | None | str | Unset = UNSET
    band_name: None | str | Unset = UNSET
    period_start: datetime.date | None | Unset = UNSET
    period_end: datetime.date | None | Unset = UNSET
    expected_to_date: float | None | str | Unset = UNSET
    expected_pct: float | None | str | Unset = UNSET
    pace_gap: float | None | str | Unset = UNSET
    elapsed: float | str | Unset = 0.0
    period_length: float | str | Unset = 0.0
    length_unit: str | Unset = "days"
    not_started: bool | Unset = False
    coverage_partial: bool | Unset = False
    covered_from: datetime.date | None | Unset = UNSET
    covered_until: datetime.date | None | Unset = UNSET
    prorated: bool | Unset = False
    target_count: int | Unset = 1
    sources: list[TargetSource] | Unset = UNSET
    unavailable: None | str | Unset = UNSET
    bands: list[TargetBandRung] | Unset = UNSET
    segments: list[TargetBandSegment] | Unset = UNSET
    scale_max_pct: float | str | Unset = 100.0
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        metric = self.metric

        metric_label = self.metric_label

        target: float | str
        target = self.target

        scheme_name = self.scheme_name

        currency: None | str | Unset
        if isinstance(self.currency, Unset):
            currency = UNSET
        else:
            currency = self.currency

        actual: float | None | str | Unset
        if isinstance(self.actual, Unset):
            actual = UNSET
        else:
            actual = self.actual

        attainment_pct: float | None | str | Unset
        if isinstance(self.attainment_pct, Unset):
            attainment_pct = UNSET
        else:
            attainment_pct = self.attainment_pct

        band_name: None | str | Unset
        if isinstance(self.band_name, Unset):
            band_name = UNSET
        else:
            band_name = self.band_name

        period_start: None | str | Unset
        if isinstance(self.period_start, Unset):
            period_start = UNSET
        elif isinstance(self.period_start, datetime.date):
            period_start = self.period_start.isoformat()
        else:
            period_start = self.period_start

        period_end: None | str | Unset
        if isinstance(self.period_end, Unset):
            period_end = UNSET
        elif isinstance(self.period_end, datetime.date):
            period_end = self.period_end.isoformat()
        else:
            period_end = self.period_end

        expected_to_date: float | None | str | Unset
        if isinstance(self.expected_to_date, Unset):
            expected_to_date = UNSET
        else:
            expected_to_date = self.expected_to_date

        expected_pct: float | None | str | Unset
        if isinstance(self.expected_pct, Unset):
            expected_pct = UNSET
        else:
            expected_pct = self.expected_pct

        pace_gap: float | None | str | Unset
        if isinstance(self.pace_gap, Unset):
            pace_gap = UNSET
        else:
            pace_gap = self.pace_gap

        elapsed: float | str | Unset
        if isinstance(self.elapsed, Unset):
            elapsed = UNSET
        else:
            elapsed = self.elapsed

        period_length: float | str | Unset
        if isinstance(self.period_length, Unset):
            period_length = UNSET
        else:
            period_length = self.period_length

        length_unit = self.length_unit

        not_started = self.not_started

        coverage_partial = self.coverage_partial

        covered_from: None | str | Unset
        if isinstance(self.covered_from, Unset):
            covered_from = UNSET
        elif isinstance(self.covered_from, datetime.date):
            covered_from = self.covered_from.isoformat()
        else:
            covered_from = self.covered_from

        covered_until: None | str | Unset
        if isinstance(self.covered_until, Unset):
            covered_until = UNSET
        elif isinstance(self.covered_until, datetime.date):
            covered_until = self.covered_until.isoformat()
        else:
            covered_until = self.covered_until

        prorated = self.prorated

        target_count = self.target_count

        sources: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.sources, Unset):
            sources = []
            for sources_item_data in self.sources:
                sources_item = sources_item_data.to_dict()
                sources.append(sources_item)

        unavailable: None | str | Unset
        if isinstance(self.unavailable, Unset):
            unavailable = UNSET
        else:
            unavailable = self.unavailable

        bands: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.bands, Unset):
            bands = []
            for bands_item_data in self.bands:
                bands_item = bands_item_data.to_dict()
                bands.append(bands_item)

        segments: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.segments, Unset):
            segments = []
            for segments_item_data in self.segments:
                segments_item = segments_item_data.to_dict()
                segments.append(segments_item)

        scale_max_pct: float | str | Unset
        if isinstance(self.scale_max_pct, Unset):
            scale_max_pct = UNSET
        else:
            scale_max_pct = self.scale_max_pct

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "metric": metric,
                "metric_label": metric_label,
                "target": target,
                "scheme_name": scheme_name,
            }
        )
        if currency is not UNSET:
            field_dict["currency"] = currency
        if actual is not UNSET:
            field_dict["actual"] = actual
        if attainment_pct is not UNSET:
            field_dict["attainment_pct"] = attainment_pct
        if band_name is not UNSET:
            field_dict["band_name"] = band_name
        if period_start is not UNSET:
            field_dict["period_start"] = period_start
        if period_end is not UNSET:
            field_dict["period_end"] = period_end
        if expected_to_date is not UNSET:
            field_dict["expected_to_date"] = expected_to_date
        if expected_pct is not UNSET:
            field_dict["expected_pct"] = expected_pct
        if pace_gap is not UNSET:
            field_dict["pace_gap"] = pace_gap
        if elapsed is not UNSET:
            field_dict["elapsed"] = elapsed
        if period_length is not UNSET:
            field_dict["period_length"] = period_length
        if length_unit is not UNSET:
            field_dict["length_unit"] = length_unit
        if not_started is not UNSET:
            field_dict["not_started"] = not_started
        if coverage_partial is not UNSET:
            field_dict["coverage_partial"] = coverage_partial
        if covered_from is not UNSET:
            field_dict["covered_from"] = covered_from
        if covered_until is not UNSET:
            field_dict["covered_until"] = covered_until
        if prorated is not UNSET:
            field_dict["prorated"] = prorated
        if target_count is not UNSET:
            field_dict["target_count"] = target_count
        if sources is not UNSET:
            field_dict["sources"] = sources
        if unavailable is not UNSET:
            field_dict["unavailable"] = unavailable
        if bands is not UNSET:
            field_dict["bands"] = bands
        if segments is not UNSET:
            field_dict["segments"] = segments
        if scale_max_pct is not UNSET:
            field_dict["scale_max_pct"] = scale_max_pct

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.target_band_rung import TargetBandRung
        from ..models.target_band_segment import TargetBandSegment
        from ..models.target_source import TargetSource

        d = dict(src_dict)
        metric = d.pop("metric")

        metric_label = d.pop("metric_label")

        def _parse_target(data: object) -> float | str:
            return cast(float | str, data)

        target = _parse_target(d.pop("target"))

        scheme_name = d.pop("scheme_name")

        def _parse_currency(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        currency = _parse_currency(d.pop("currency", UNSET))

        def _parse_actual(data: object) -> float | None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | str | Unset, data)

        actual = _parse_actual(d.pop("actual", UNSET))

        def _parse_attainment_pct(data: object) -> float | None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | str | Unset, data)

        attainment_pct = _parse_attainment_pct(d.pop("attainment_pct", UNSET))

        def _parse_band_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        band_name = _parse_band_name(d.pop("band_name", UNSET))

        def _parse_period_start(data: object) -> datetime.date | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                period_start_type_0 = isoparse(data).date()

                return period_start_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.date | None | Unset, data)

        period_start = _parse_period_start(d.pop("period_start", UNSET))

        def _parse_period_end(data: object) -> datetime.date | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                period_end_type_0 = isoparse(data).date()

                return period_end_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.date | None | Unset, data)

        period_end = _parse_period_end(d.pop("period_end", UNSET))

        def _parse_expected_to_date(data: object) -> float | None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | str | Unset, data)

        expected_to_date = _parse_expected_to_date(d.pop("expected_to_date", UNSET))

        def _parse_expected_pct(data: object) -> float | None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | str | Unset, data)

        expected_pct = _parse_expected_pct(d.pop("expected_pct", UNSET))

        def _parse_pace_gap(data: object) -> float | None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | str | Unset, data)

        pace_gap = _parse_pace_gap(d.pop("pace_gap", UNSET))

        def _parse_elapsed(data: object) -> float | str | Unset:
            if isinstance(data, Unset):
                return data
            return cast(float | str | Unset, data)

        elapsed = _parse_elapsed(d.pop("elapsed", UNSET))

        def _parse_period_length(data: object) -> float | str | Unset:
            if isinstance(data, Unset):
                return data
            return cast(float | str | Unset, data)

        period_length = _parse_period_length(d.pop("period_length", UNSET))

        length_unit = d.pop("length_unit", UNSET)

        not_started = d.pop("not_started", UNSET)

        coverage_partial = d.pop("coverage_partial", UNSET)

        def _parse_covered_from(data: object) -> datetime.date | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                covered_from_type_0 = isoparse(data).date()

                return covered_from_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.date | None | Unset, data)

        covered_from = _parse_covered_from(d.pop("covered_from", UNSET))

        def _parse_covered_until(data: object) -> datetime.date | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                covered_until_type_0 = isoparse(data).date()

                return covered_until_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.date | None | Unset, data)

        covered_until = _parse_covered_until(d.pop("covered_until", UNSET))

        prorated = d.pop("prorated", UNSET)

        target_count = d.pop("target_count", UNSET)

        _sources = d.pop("sources", UNSET)
        sources: list[TargetSource] | Unset = UNSET
        if _sources is not UNSET:
            sources = []
            for sources_item_data in _sources:
                sources_item = TargetSource.from_dict(sources_item_data)

                sources.append(sources_item)

        def _parse_unavailable(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        unavailable = _parse_unavailable(d.pop("unavailable", UNSET))

        _bands = d.pop("bands", UNSET)
        bands: list[TargetBandRung] | Unset = UNSET
        if _bands is not UNSET:
            bands = []
            for bands_item_data in _bands:
                bands_item = TargetBandRung.from_dict(bands_item_data)

                bands.append(bands_item)

        _segments = d.pop("segments", UNSET)
        segments: list[TargetBandSegment] | Unset = UNSET
        if _segments is not UNSET:
            segments = []
            for segments_item_data in _segments:
                segments_item = TargetBandSegment.from_dict(segments_item_data)

                segments.append(segments_item)

        def _parse_scale_max_pct(data: object) -> float | str | Unset:
            if isinstance(data, Unset):
                return data
            return cast(float | str | Unset, data)

        scale_max_pct = _parse_scale_max_pct(d.pop("scale_max_pct", UNSET))

        target_attainment_entry = cls(
            metric=metric,
            metric_label=metric_label,
            target=target,
            scheme_name=scheme_name,
            currency=currency,
            actual=actual,
            attainment_pct=attainment_pct,
            band_name=band_name,
            period_start=period_start,
            period_end=period_end,
            expected_to_date=expected_to_date,
            expected_pct=expected_pct,
            pace_gap=pace_gap,
            elapsed=elapsed,
            period_length=period_length,
            length_unit=length_unit,
            not_started=not_started,
            coverage_partial=coverage_partial,
            covered_from=covered_from,
            covered_until=covered_until,
            prorated=prorated,
            target_count=target_count,
            sources=sources,
            unavailable=unavailable,
            bands=bands,
            segments=segments,
            scale_max_pct=scale_max_pct,
        )

        target_attainment_entry.additional_properties = d
        return target_attainment_entry

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
