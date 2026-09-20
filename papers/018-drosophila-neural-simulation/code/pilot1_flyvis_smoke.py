#!/usr/bin/env python3
"""ARIS4C018 Pilot 1A: minimal pinned flyvis connectome reproduction."""

from flyvis import ConnectomeFromAvgFilters, connectome_file


def main():
    config = dict(file=connectome_file.name, extent=1, n_syn_fill=1)
    connectome = ConnectomeFromAvgFilters(config)

    nodes = connectome.nodes.to_df()
    edges = connectome.edges.to_df()
    cell_types = nodes["type"].nunique()

    assert len(nodes) > 0
    assert len(edges) > 0
    assert cell_types > 0

    print("ARIS4C018 flyvis smoke PASS")
    print(f"connectome_file={connectome_file.name}")
    print(f"extent={config['extent']}")
    print(f"nodes={len(nodes)}")
    print(f"edges={len(edges)}")
    print(f"cell_types={cell_types}")


if __name__ == "__main__":
    main()
