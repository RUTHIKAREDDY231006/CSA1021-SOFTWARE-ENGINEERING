"""Cyclomatic complexity cross-check (Experiment 8)."""

def vg_edges_nodes(edges: int, nodes: int, components: int = 1) -> int:
    return edges - nodes + 2 * components

def vg_predicates(predicates: int) -> int:
    return predicates + 1

if __name__ == "__main__":
    e, n, p = 17, 13, 5
    a, b = vg_edges_nodes(e, n), vg_predicates(p)
    print(f"V(G) = E - N + 2 = {e} - {n} + 2 = {a}")
    print(f"V(G) = P + 1     = {p} + 1 = {b}")
    assert a == b == 6
