from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="OutputExternalSupportRequest")


@_attrs_define
class OutputExternalSupportRequest:
    """Output schema for external support request detail card

    Attributes:
        external_id_str (str):
        public_reference (str):
        title (str):
        description (str):
        status_lifecycle (str):
        status_name (str):
        type_name (str):
        severity_name (str):
        has_assignee (bool):
        requester_external_id (str):
        request_type (str):
        card_title (str):
        author_info (str):
        created_info (str):
        updated_info (str):
        assignee_name (None | str | Unset):
        can_assign_to_self (bool | Unset):  Default: False.
        queue_name (None | str | Unset):
        queue_id (None | str | Unset):
        resource_name (None | str | Unset):
        project_name (None | str | Unset):
        project_customer_name (None | str | Unset):
        customer_name (None | str | Unset):
        work_item_name (None | str | Unset):
        work_item_hierarchy_id (None | str | Unset):
        can_reopen (bool | Unset):  Default: False.
        resolution (None | str | Unset):
        resolution_display (None | str | Unset):
        closure_reason (None | str | Unset):
        solution_pending (bool | Unset):  Default: False.
    """

    external_id_str: str
    public_reference: str
    title: str
    description: str
    status_lifecycle: str
    status_name: str
    type_name: str
    severity_name: str
    has_assignee: bool
    requester_external_id: str
    request_type: str
    card_title: str
    author_info: str
    created_info: str
    updated_info: str
    assignee_name: None | str | Unset = UNSET
    can_assign_to_self: bool | Unset = False
    queue_name: None | str | Unset = UNSET
    queue_id: None | str | Unset = UNSET
    resource_name: None | str | Unset = UNSET
    project_name: None | str | Unset = UNSET
    project_customer_name: None | str | Unset = UNSET
    customer_name: None | str | Unset = UNSET
    work_item_name: None | str | Unset = UNSET
    work_item_hierarchy_id: None | str | Unset = UNSET
    can_reopen: bool | Unset = False
    resolution: None | str | Unset = UNSET
    resolution_display: None | str | Unset = UNSET
    closure_reason: None | str | Unset = UNSET
    solution_pending: bool | Unset = False
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        external_id_str = self.external_id_str

        public_reference = self.public_reference

        title = self.title

        description = self.description

        status_lifecycle = self.status_lifecycle

        status_name = self.status_name

        type_name = self.type_name

        severity_name = self.severity_name

        has_assignee = self.has_assignee

        requester_external_id = self.requester_external_id

        request_type = self.request_type

        card_title = self.card_title

        author_info = self.author_info

        created_info = self.created_info

        updated_info = self.updated_info

        assignee_name: None | str | Unset
        if isinstance(self.assignee_name, Unset):
            assignee_name = UNSET
        else:
            assignee_name = self.assignee_name

        can_assign_to_self = self.can_assign_to_self

        queue_name: None | str | Unset
        if isinstance(self.queue_name, Unset):
            queue_name = UNSET
        else:
            queue_name = self.queue_name

        queue_id: None | str | Unset
        if isinstance(self.queue_id, Unset):
            queue_id = UNSET
        else:
            queue_id = self.queue_id

        resource_name: None | str | Unset
        if isinstance(self.resource_name, Unset):
            resource_name = UNSET
        else:
            resource_name = self.resource_name

        project_name: None | str | Unset
        if isinstance(self.project_name, Unset):
            project_name = UNSET
        else:
            project_name = self.project_name

        project_customer_name: None | str | Unset
        if isinstance(self.project_customer_name, Unset):
            project_customer_name = UNSET
        else:
            project_customer_name = self.project_customer_name

        customer_name: None | str | Unset
        if isinstance(self.customer_name, Unset):
            customer_name = UNSET
        else:
            customer_name = self.customer_name

        work_item_name: None | str | Unset
        if isinstance(self.work_item_name, Unset):
            work_item_name = UNSET
        else:
            work_item_name = self.work_item_name

        work_item_hierarchy_id: None | str | Unset
        if isinstance(self.work_item_hierarchy_id, Unset):
            work_item_hierarchy_id = UNSET
        else:
            work_item_hierarchy_id = self.work_item_hierarchy_id

        can_reopen = self.can_reopen

        resolution: None | str | Unset
        if isinstance(self.resolution, Unset):
            resolution = UNSET
        else:
            resolution = self.resolution

        resolution_display: None | str | Unset
        if isinstance(self.resolution_display, Unset):
            resolution_display = UNSET
        else:
            resolution_display = self.resolution_display

        closure_reason: None | str | Unset
        if isinstance(self.closure_reason, Unset):
            closure_reason = UNSET
        else:
            closure_reason = self.closure_reason

        solution_pending = self.solution_pending

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "external_id_str": external_id_str,
                "public_reference": public_reference,
                "title": title,
                "description": description,
                "status_lifecycle": status_lifecycle,
                "status_name": status_name,
                "type_name": type_name,
                "severity_name": severity_name,
                "has_assignee": has_assignee,
                "requester_external_id": requester_external_id,
                "request_type": request_type,
                "card_title": card_title,
                "author_info": author_info,
                "created_info": created_info,
                "updated_info": updated_info,
            }
        )
        if assignee_name is not UNSET:
            field_dict["assignee_name"] = assignee_name
        if can_assign_to_self is not UNSET:
            field_dict["can_assign_to_self"] = can_assign_to_self
        if queue_name is not UNSET:
            field_dict["queue_name"] = queue_name
        if queue_id is not UNSET:
            field_dict["queue_id"] = queue_id
        if resource_name is not UNSET:
            field_dict["resource_name"] = resource_name
        if project_name is not UNSET:
            field_dict["project_name"] = project_name
        if project_customer_name is not UNSET:
            field_dict["project_customer_name"] = project_customer_name
        if customer_name is not UNSET:
            field_dict["customer_name"] = customer_name
        if work_item_name is not UNSET:
            field_dict["work_item_name"] = work_item_name
        if work_item_hierarchy_id is not UNSET:
            field_dict["work_item_hierarchy_id"] = work_item_hierarchy_id
        if can_reopen is not UNSET:
            field_dict["can_reopen"] = can_reopen
        if resolution is not UNSET:
            field_dict["resolution"] = resolution
        if resolution_display is not UNSET:
            field_dict["resolution_display"] = resolution_display
        if closure_reason is not UNSET:
            field_dict["closure_reason"] = closure_reason
        if solution_pending is not UNSET:
            field_dict["solution_pending"] = solution_pending

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        external_id_str = d.pop("external_id_str")

        public_reference = d.pop("public_reference")

        title = d.pop("title")

        description = d.pop("description")

        status_lifecycle = d.pop("status_lifecycle")

        status_name = d.pop("status_name")

        type_name = d.pop("type_name")

        severity_name = d.pop("severity_name")

        has_assignee = d.pop("has_assignee")

        requester_external_id = d.pop("requester_external_id")

        request_type = d.pop("request_type")

        card_title = d.pop("card_title")

        author_info = d.pop("author_info")

        created_info = d.pop("created_info")

        updated_info = d.pop("updated_info")

        def _parse_assignee_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        assignee_name = _parse_assignee_name(d.pop("assignee_name", UNSET))

        can_assign_to_self = d.pop("can_assign_to_self", UNSET)

        def _parse_queue_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        queue_name = _parse_queue_name(d.pop("queue_name", UNSET))

        def _parse_queue_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        queue_id = _parse_queue_id(d.pop("queue_id", UNSET))

        def _parse_resource_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        resource_name = _parse_resource_name(d.pop("resource_name", UNSET))

        def _parse_project_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        project_name = _parse_project_name(d.pop("project_name", UNSET))

        def _parse_project_customer_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        project_customer_name = _parse_project_customer_name(
            d.pop("project_customer_name", UNSET)
        )

        def _parse_customer_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        customer_name = _parse_customer_name(d.pop("customer_name", UNSET))

        def _parse_work_item_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        work_item_name = _parse_work_item_name(d.pop("work_item_name", UNSET))

        def _parse_work_item_hierarchy_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        work_item_hierarchy_id = _parse_work_item_hierarchy_id(
            d.pop("work_item_hierarchy_id", UNSET)
        )

        can_reopen = d.pop("can_reopen", UNSET)

        def _parse_resolution(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        resolution = _parse_resolution(d.pop("resolution", UNSET))

        def _parse_resolution_display(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        resolution_display = _parse_resolution_display(
            d.pop("resolution_display", UNSET)
        )

        def _parse_closure_reason(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        closure_reason = _parse_closure_reason(d.pop("closure_reason", UNSET))

        solution_pending = d.pop("solution_pending", UNSET)

        output_external_support_request = cls(
            external_id_str=external_id_str,
            public_reference=public_reference,
            title=title,
            description=description,
            status_lifecycle=status_lifecycle,
            status_name=status_name,
            type_name=type_name,
            severity_name=severity_name,
            has_assignee=has_assignee,
            requester_external_id=requester_external_id,
            request_type=request_type,
            card_title=card_title,
            author_info=author_info,
            created_info=created_info,
            updated_info=updated_info,
            assignee_name=assignee_name,
            can_assign_to_self=can_assign_to_self,
            queue_name=queue_name,
            queue_id=queue_id,
            resource_name=resource_name,
            project_name=project_name,
            project_customer_name=project_customer_name,
            customer_name=customer_name,
            work_item_name=work_item_name,
            work_item_hierarchy_id=work_item_hierarchy_id,
            can_reopen=can_reopen,
            resolution=resolution,
            resolution_display=resolution_display,
            closure_reason=closure_reason,
            solution_pending=solution_pending,
        )

        output_external_support_request.additional_properties = d
        return output_external_support_request

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
