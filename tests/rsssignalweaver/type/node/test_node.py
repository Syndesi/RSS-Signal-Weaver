from __future__ import annotations

from rsssignalweaver.type.node import Node

payload = {
	'id': '567cb7ba-cbb2-40fd-ac96-05372feeaff2',
	'type': 'Node',
	'data': {
		'name': 'name',
		'string': 'some string',
		'int': 1234,
		'float': 4.321,
		'boolean': True,
	},
}


def test_node_parsing():
	node = Node.model_validate(payload)

	assert node.type == 'Node'
	assert str(node.id) == '567cb7ba-cbb2-40fd-ac96-05372feeaff2'

	assert hasattr(node.data, 'name')
	assert node.data.name == 'name'
