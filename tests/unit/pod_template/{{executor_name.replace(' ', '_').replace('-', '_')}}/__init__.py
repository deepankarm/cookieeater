from jina.executors.{{ kind | lower}}s import Base{{ kind }}

class {{ executor_name | replace(' ', '_') | replace('-', '_') }}(Base{{ kind }}):
    """
    :class:`{{ executor_name }}` {{ description }}.
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # your customized __init__ below
        raise NotImplementedError

    {% if kind == 'Crafter' %}

    def craft(self, *args, **kwargs):
        raise NotImplementedError

    {% elif kind == 'Encoder' %}

    def encode(self, data, *args, **kwargs):
        raise NotImplementedError

    {% elif kind == 'Indexer' %}

    def query(self, keys, *args, **kwargs):
        raise NotImplementedError

    def add(self, keys, vectors, *args, **kwargs):
        raise NotImplementedError

    {% elif kind == 'Ranker' %}

    def score(self, *args, **kwargs):
        raise NotImplementedError

    {% elif kind == 'Evaluator' %}

    def evaluate(self, *args, **kwargs):
        raise NotImplementedError

    {% elif kind == 'Segmenter' %}

    def segment(self, *args, **kwargs):
        raise NotImplementedError

    {% elif kind == 'Classifier' %}

    def predict(self, *args, **kwargs):
        raise NotImplementedError

    {% endif %}
