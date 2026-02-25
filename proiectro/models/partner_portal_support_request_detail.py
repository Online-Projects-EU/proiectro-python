from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PartnerPortalSupportRequestDetail")


@_attrs_define
class PartnerPortalSupportRequestDetail:
    """Detailed view of single support request - matches customer portal structure

    Attributes:
        bridge_id (str):
        id (str):
        title (str):
        description (str):
        public_reference (str):
        status_lifecycle (str):
        request_status (str):
        request_type (None | str):
        request_severity (None | str):
        assignee_name (None | str):
        project_name (None | str):
        product_name (None | str):
        resolution_display (None | str):
        closure_reason (None | str):
        author_info (str):
        created_info (str):
        updated_info (str):
        solution_pending (bool):
        can_reopen (bool):
        is_requester (bool | Unset):  Default: False.
    """

    bridge_id: str
    id: str
    title: str
    description: str
    public_reference: str
    status_lifecycle: str
    request_status: str
    request_type: None | str
    request_severity: None | str
    assignee_name: None | str
    project_name: None | str
    product_name: None | str
    resolution_display: None | str
    closure_reason: None | str
    author_info: str
    created_info: str
    updated_info: str
    solution_pending: bool
    can_reopen: bool
    is_requester: bool | Unset = False
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        bridge_id = self.bridge_id

        id = self.id

        title = self.title

        description = self.description

        public_reference = self.public_reference

        status_lifecycle = self.status_lifecycle

        request_status = self.request_status

        request_type: None | str
        request_type = self.request_type

        request_severity: None | str
        request_severity = self.request_severity

        assignee_name: None | str
        assignee_name = self.assignee_name

        project_name: None | str
        project_name = self.project_name

        product_name: None | str
        product_name = self.product_name

        resolution_display: None | str
        resolution_display = self.resolution_display

        closure_reason: None | str
        closure_reason = self.closure_reason

        author_info = self.author_info

        created_info = self.created_info

        updated_info = self.updated_info

        solution_pending = self.solution_pending

        can_reopen = self.can_reopen

        is_requester = self.is_requester

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "bridge_id": bridge_id,
                "id": id,
                "title": title,
                "description": description,
                "public_reference": public_reference,
                "status_lifecycle": status_lifecycle,
                "request_status": request_status,
                "request_type": request_type,
                "request_severity": request_severity,
                "assignee_name": assignee_name,
                "project_name": project_name,
                "product_name": product_name,
                "resolution_display": resolution_display,
                "closure_reason": closure_reason,
                "author_info": author_info,
                "created_info": created_info,
                "updated_info": updated_info,
                "solution_pending": solution_pending,
                "can_reopen": can_reopen,
            }
        )
        if is_requester is not UNSET:
            field_dict["is_requester"] = is_requester

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        bridge_id = d.pop("bridge_id")

        id = d.pop("id")

        title = d.pop("title")

        description = d.pop("description")

        public_reference = d.pop("public_reference")

        status_lifecycle = d.pop("status_lifecycle")

        request_status = d.pop("request_status")

        def _parse_request_type(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        request_type = _parse_request_type(d.pop("request_type"))

        def _parse_request_severity(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        request_severity = _parse_request_severity(d.pop("request_severity"))

        def _parse_assignee_name(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        assignee_name = _parse_assignee_name(d.pop("assignee_name"))

        def _parse_project_name(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        project_name = _parse_project_name(d.pop("project_name"))

        def _parse_product_name(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        product_name = _parse_product_name(d.pop("product_name"))

        def _parse_resolution_display(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        resolution_display = _parse_resolution_display(d.pop("resolution_display"))

        def _parse_closure_reason(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        closure_reason = _parse_closure_reason(d.pop("closure_reason"))

        author_info = d.pop("author_info")

        created_info = d.pop("created_info")

        updated_info = d.pop("updated_info")

        solution_pending = d.pop("solution_pending")

        can_reopen = d.pop("can_reopen")

        is_requester = d.pop("is_requester", UNSET)

        partner_portal_support_request_detail = cls(
            bridge_id=bridge_id,
            id=id,
            title=title,
            description=description,
            public_reference=public_reference,
            status_lifecycle=status_lifecycle,
            request_status=request_status,
            request_type=request_type,
            request_severity=request_severity,
            assignee_name=assignee_name,
            project_name=project_name,
            product_name=product_name,
            resolution_display=resolution_display,
            closure_reason=closure_reason,
            author_info=author_info,
            created_info=created_info,
            updated_info=updated_info,
            solution_pending=solution_pending,
            can_reopen=can_reopen,
            is_requester=is_requester,
        )

        partner_portal_support_request_detail.additional_properties = d
        return partner_portal_support_request_detail

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
