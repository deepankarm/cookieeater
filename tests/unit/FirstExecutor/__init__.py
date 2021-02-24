from jina.executors.encoders import BaseEncoder


class FirstExecutor(BaseEncoder):
    """
    :class:`FirstExecutor` Encoder executor.
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # your customized __init__ below
        raise NotImplementedError

    def encode(self, data, *args, **kwargs):
        raise NotImplementedError

