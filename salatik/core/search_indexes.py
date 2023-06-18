from elasticsearch_dsl import Document, fields
from elasticsearch_dsl import registry
from core.models import Salad


@registry.register_document
class SaladDocument(Document):
    name = fields.TextField()
    description = fields.TextField()
    ingredients = fields.NestedField(properties={
        'name': fields.TextField(),
        'quantity': fields.FloatField(),
    })

    class Index:
        name = 'salad_index'
        settings = {
            'number_of_shards': 1,
            'number_of_replicas': 0
        }

    def get_queryset(self):
        return self.get_model().objects.all()

    def get_instances_from_related(self, related_instance):
        if isinstance(related_instance, Salad):
            return related_instance
        return None
