from random import randrange
import copy

def load_graph():
    edges = []
    vertices = []
    with open('kargerMinCut_input.txt', 'r') as source:
        for line in source:
            line = line.strip().split(('\t'))  # ensure each line doesn't contain \n then split by tab
            vertices.append(line[0])
            for j in line[1:]:
                if [j, line[0]] not in edges and [line[0],j] not in edges:
                    edges.append([line[0], j])
    return edges, vertices


def contract_edges(es, vs):
    while len(vs) > 2:  # Keep contracting till 2 nodes left
        rand = randrange(0, len(es))  # Pick a random edge to contract
        [u, v] = es.pop(rand)
        vs.remove(v)  # Merge vertex v into u

        for e in es[:]:  # Loop through a copy of es since es.remove(e) will disrupt the index
            # Replace all existence of v with u
            if e[0] == v:
                e[0] = u
            elif e[1] == v:
                e[1] = u
            if (e[0]==u) and (e[1]==u):  # remove self loop
                es.remove(e)

    return len(es)  # Return the count of the crossing edges


def kargers_contraction():
    min_cuts = []
    e_s, v_s = load_graph()
    for k in range(100):  # Ideally, loop n^2*ln(n) to achieve: P(all_fail) < 1/n
        # "Deepcopy" the graph since contract_edges will change v_s (since list is mutable)
        v = copy.deepcopy(v_s)
        e = copy.deepcopy(e_s)
        crossing_edges = contract_edges(e, v)
        min_cuts.append(crossing_edges)

    return min(min_cuts)

if __name__ == '__main__':
    ans = kargers_contraction()
    print(ans)
