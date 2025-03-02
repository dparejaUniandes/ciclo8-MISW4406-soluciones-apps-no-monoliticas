from src.bff_web.api.v1.suscripciones import Suscripcion
from strawberry.fastapi import GraphQLRouter
from .consultas import Query
from .mutaciones import Mutation

import strawberry


schema = strawberry.Schema(query=Query, mutation=Mutation, subscription=Suscripcion)
router = GraphQLRouter(schema)
