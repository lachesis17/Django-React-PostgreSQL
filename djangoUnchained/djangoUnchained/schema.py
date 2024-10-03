import graphene
from graphene_django import DjangoObjectType
from core.models import Item

class ItemType(DjangoObjectType):
    class Meta:
        model = Item
        fields = ("id", "name", "description")

class Query(graphene.ObjectType):
    all_items = graphene.List(ItemType)

    def resolve_all_items(self, info):
        return Item.objects.all()

schema = graphene.Schema(query=Query)
