from fixtures.common_fixtures import COMMON_FIXTURES


PAUSE_BOT_FIXTURES = {
    'eth_call': (
        (({'to': '0x710B3303fB508a84F10793c1106e32bE873C24cd', 'data': '0xc7062e98'}, 'latest'), {'jsonrpc': '2.0', 'id': 11, 'result': '0x00000000000000000000000000000000000000000000000000000000000019f6'}),
        (({'to': '0x0000000000000000000000000000000000000000', 'data': '0x6608b11b0000000000000000000000000000000000000000000000000000000000000001'}, '0xd17320'), {'jsonrpc': '2.0', 'id': 16, 'result': '0x0000000000000000000000000000000000000000000000000000000000000000'}),
        (({'to': '0x710B3303fB508a84F10793c1106e32bE873C24cd', 'data': '0xa50833d6'}, 'latest'), {'jsonrpc': '2.0', 'id': 0, 'result': '0xd225b544f236c424d88abf1dd1a58e20df146bb6c02d916809b75d7a72bccb10'}),
        (({'to': '0x710B3303fB508a84F10793c1106e32bE873C24cd', 'data': '0x4acd54c30000000000000000000000000000000000000000000000000000000000d1731f0000000000000000000000000000000000000000000000000000000000000001baa668505cd496caaf7117dd074338197200175057909ab73a04463656bdb0fad4933925f5f97a9632b4b1bc621a1c2771d58eaf6eee27dcf915eac8af010537'}, 'latest'), {'jsonrpc': '2.0', 'id': 0, 'error': {'code': 3, 'data': '0x08c379a000000000000000000000000000000000000000000000000000000000000000200000000000000000000000000000000000000000000000000000000000000011696e76616c6964207369676e6174757265000000000000000000000000000000', 'message': 'execution reverted: invalid signature'}}),
    ),
    **COMMON_FIXTURES,
}


PAUSED_PROTOCOL_FIXTURES = {
    'eth_call': (
        (({'to': '0x710B3303fB508a84F10793c1106e32bE873C24cd', 'data': '0xc7062e98'}, 'latest'), {'jsonrpc': '2.0', 'id': 15, 'result': '0x00000000000000000000000000000000000000000000000000000000000019f6'}),
        (({'to': '0x0000000000000000000000000000000000000000', 'data': '0x6608b11b0000000000000000000000000000000000000000000000000000000000000001'}, '0xd17320'), {'jsonrpc': '2.0', 'id': 14, 'result': '0x0000000000000000000000000000000000000000000000000000000000000001'}),
        (({'to': '0x710B3303fB508a84F10793c1106e32bE873C24cd', 'data': '0xa50833d6'}, 'latest'), {'jsonrpc': '2.0', 'id': 0, 'result': '0xd225b544f236c424d88abf1dd1a58e20df146bb6c02d916809b75d7a72bccb10'})
    ),
    **COMMON_FIXTURES,
}
