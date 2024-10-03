import graphene
from graphene_django import DjangoObjectType
from core.models import CptData

class CptDataType(DjangoObjectType):
    class Meta:
        model = CptData
        fields = ("depth", "qc", "fs")

class Query(graphene.ObjectType):
    all_cpt_data = graphene.List(CptDataType)

    def resolve_all_cpt_data(self, info, **kwargs):
        return CptData.objects.all()

schema = graphene.Schema(query=Query)