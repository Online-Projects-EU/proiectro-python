from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from dateutil.parser import isoparse
from typing import cast
import datetime






T = TypeVar("T", bound="OutputDocument")



@_attrs_define
class OutputDocument:
    """ 
        Attributes:
            id (str):
            title (str):
            status (str):
            locked (bool | Unset):  Default: False.
            full_number (None | str | Unset):
            series (None | str | Unset):
            series_code (None | str | Unset):
            template (None | str | Unset):
            template_name (None | str | Unset):
            context_type (None | str | Unset):
            context_id (None | str | Unset):
            context_label (str | Unset):  Default: ''.
            render_route (None | str | Unset):
            page_route (None | str | Unset):
            org_id (None | str | Unset):
            org_label (str | Unset):  Default: ''.
            data_classification (None | str | Unset):
            finalized_at (datetime.datetime | None | Unset):
            retain_until (datetime.date | None | Unset):
            created_at (datetime.datetime | None | Unset):
     """

    id: str
    title: str
    status: str
    locked: bool | Unset = False
    full_number: None | str | Unset = UNSET
    series: None | str | Unset = UNSET
    series_code: None | str | Unset = UNSET
    template: None | str | Unset = UNSET
    template_name: None | str | Unset = UNSET
    context_type: None | str | Unset = UNSET
    context_id: None | str | Unset = UNSET
    context_label: str | Unset = ''
    render_route: None | str | Unset = UNSET
    page_route: None | str | Unset = UNSET
    org_id: None | str | Unset = UNSET
    org_label: str | Unset = ''
    data_classification: None | str | Unset = UNSET
    finalized_at: datetime.datetime | None | Unset = UNSET
    retain_until: datetime.date | None | Unset = UNSET
    created_at: datetime.datetime | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        id = self.id

        title = self.title

        status = self.status

        locked = self.locked

        full_number: None | str | Unset
        if isinstance(self.full_number, Unset):
            full_number = UNSET
        else:
            full_number = self.full_number

        series: None | str | Unset
        if isinstance(self.series, Unset):
            series = UNSET
        else:
            series = self.series

        series_code: None | str | Unset
        if isinstance(self.series_code, Unset):
            series_code = UNSET
        else:
            series_code = self.series_code

        template: None | str | Unset
        if isinstance(self.template, Unset):
            template = UNSET
        else:
            template = self.template

        template_name: None | str | Unset
        if isinstance(self.template_name, Unset):
            template_name = UNSET
        else:
            template_name = self.template_name

        context_type: None | str | Unset
        if isinstance(self.context_type, Unset):
            context_type = UNSET
        else:
            context_type = self.context_type

        context_id: None | str | Unset
        if isinstance(self.context_id, Unset):
            context_id = UNSET
        else:
            context_id = self.context_id

        context_label = self.context_label

        render_route: None | str | Unset
        if isinstance(self.render_route, Unset):
            render_route = UNSET
        else:
            render_route = self.render_route

        page_route: None | str | Unset
        if isinstance(self.page_route, Unset):
            page_route = UNSET
        else:
            page_route = self.page_route

        org_id: None | str | Unset
        if isinstance(self.org_id, Unset):
            org_id = UNSET
        else:
            org_id = self.org_id

        org_label = self.org_label

        data_classification: None | str | Unset
        if isinstance(self.data_classification, Unset):
            data_classification = UNSET
        else:
            data_classification = self.data_classification

        finalized_at: None | str | Unset
        if isinstance(self.finalized_at, Unset):
            finalized_at = UNSET
        elif isinstance(self.finalized_at, datetime.datetime):
            finalized_at = self.finalized_at.isoformat()
        else:
            finalized_at = self.finalized_at

        retain_until: None | str | Unset
        if isinstance(self.retain_until, Unset):
            retain_until = UNSET
        elif isinstance(self.retain_until, datetime.date):
            retain_until = self.retain_until.isoformat()
        else:
            retain_until = self.retain_until

        created_at: None | str | Unset
        if isinstance(self.created_at, Unset):
            created_at = UNSET
        elif isinstance(self.created_at, datetime.datetime):
            created_at = self.created_at.isoformat()
        else:
            created_at = self.created_at


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "id": id,
            "title": title,
            "status": status,
        })
        if locked is not UNSET:
            field_dict["locked"] = locked
        if full_number is not UNSET:
            field_dict["full_number"] = full_number
        if series is not UNSET:
            field_dict["series"] = series
        if series_code is not UNSET:
            field_dict["series_code"] = series_code
        if template is not UNSET:
            field_dict["template"] = template
        if template_name is not UNSET:
            field_dict["template_name"] = template_name
        if context_type is not UNSET:
            field_dict["context_type"] = context_type
        if context_id is not UNSET:
            field_dict["context_id"] = context_id
        if context_label is not UNSET:
            field_dict["context_label"] = context_label
        if render_route is not UNSET:
            field_dict["render_route"] = render_route
        if page_route is not UNSET:
            field_dict["page_route"] = page_route
        if org_id is not UNSET:
            field_dict["org_id"] = org_id
        if org_label is not UNSET:
            field_dict["org_label"] = org_label
        if data_classification is not UNSET:
            field_dict["data_classification"] = data_classification
        if finalized_at is not UNSET:
            field_dict["finalized_at"] = finalized_at
        if retain_until is not UNSET:
            field_dict["retain_until"] = retain_until
        if created_at is not UNSET:
            field_dict["created_at"] = created_at

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        title = d.pop("title")

        status = d.pop("status")

        locked = d.pop("locked", UNSET)

        def _parse_full_number(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        full_number = _parse_full_number(d.pop("full_number", UNSET))


        def _parse_series(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        series = _parse_series(d.pop("series", UNSET))


        def _parse_series_code(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        series_code = _parse_series_code(d.pop("series_code", UNSET))


        def _parse_template(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        template = _parse_template(d.pop("template", UNSET))


        def _parse_template_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        template_name = _parse_template_name(d.pop("template_name", UNSET))


        def _parse_context_type(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        context_type = _parse_context_type(d.pop("context_type", UNSET))


        def _parse_context_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        context_id = _parse_context_id(d.pop("context_id", UNSET))


        context_label = d.pop("context_label", UNSET)

        def _parse_render_route(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        render_route = _parse_render_route(d.pop("render_route", UNSET))


        def _parse_page_route(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        page_route = _parse_page_route(d.pop("page_route", UNSET))


        def _parse_org_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        org_id = _parse_org_id(d.pop("org_id", UNSET))


        org_label = d.pop("org_label", UNSET)

        def _parse_data_classification(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        data_classification = _parse_data_classification(d.pop("data_classification", UNSET))


        def _parse_finalized_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                finalized_at_type_0 = isoparse(data)



                return finalized_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        finalized_at = _parse_finalized_at(d.pop("finalized_at", UNSET))


        def _parse_retain_until(data: object) -> datetime.date | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                retain_until_type_0 = isoparse(data).date()



                return retain_until_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.date | None | Unset, data)

        retain_until = _parse_retain_until(d.pop("retain_until", UNSET))


        def _parse_created_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                created_at_type_0 = isoparse(data)



                return created_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        created_at = _parse_created_at(d.pop("created_at", UNSET))


        output_document = cls(
            id=id,
            title=title,
            status=status,
            locked=locked,
            full_number=full_number,
            series=series,
            series_code=series_code,
            template=template,
            template_name=template_name,
            context_type=context_type,
            context_id=context_id,
            context_label=context_label,
            render_route=render_route,
            page_route=page_route,
            org_id=org_id,
            org_label=org_label,
            data_classification=data_classification,
            finalized_at=finalized_at,
            retain_until=retain_until,
            created_at=created_at,
        )


        output_document.additional_properties = d
        return output_document

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
