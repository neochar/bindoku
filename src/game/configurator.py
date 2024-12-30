from typing import Self


class Configurator:
    def __init__(self, config: dict):
        self.config = self.validate(config)

    @staticmethod
    def validate(config):
        assert isinstance(config, dict)
        assert 'puzzleable' in config

        return config

    @classmethod
    def dev(cls) -> Self:
        return Configurator({
            'puzzleable': True,
        })
