from __future__ import annotations

from uuid import UUID

from pydantic import BaseModel, ConfigDict


class NodeData(BaseModel):
	model_config = ConfigDict(extra='allow')


class Node(BaseModel):
	id: UUID
	type: str
	data: NodeData
