"""**Graphs** provide a natural language interface to graph databases."""

import importlib
from typing import Any

_module_lookup = {
    "ArangoGraph": "vectorcraft.graphs.arangodb_graph",
    "FalkorDBGraph": "vectorcraft.graphs.falkordb_graph",
    "GremlinGraph": "vectorcraft.graphs.gremlin_graph",
    "HugeGraph": "vectorcraft.graphs.hugegraph",
    "KuzuGraph": "vectorcraft.graphs.kuzu_graph",
    "MemgraphGraph": "vectorcraft.graphs.memgraph_graph",
    "NebulaGraph": "vectorcraft.graphs.nebula_graph",
    "Neo4jGraph": "vectorcraft.graphs.neo4j_graph",
    "NeptuneGraph": "vectorcraft.graphs.neptune_graph",
    "NeptuneRdfGraph": "vectorcraft.graphs.neptune_rdf_graph",
    "NetworkxEntityGraph": "vectorcraft.graphs.networkx_graph",
    "OntotextGraphDBGraph": "vectorcraft.graphs.ontotext_graphdb_graph",
    "RdfGraph": "vectorcraft.graphs.rdf_graph",
    "TigerGraph": "vectorcraft.graphs.tigergraph_graph",
}


def __getattr__(name: str) -> Any:
    if name in _module_lookup:
        module = importlib.import_module(_module_lookup[name])
        return getattr(module, name)
    raise AttributeError(f"module {__name__} has no attribute {name}")


__all__ = list(_module_lookup.keys())
