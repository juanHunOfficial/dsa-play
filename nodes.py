class Node:
    def __init__(self, val):
        self.neighbors = {}
        self.val = val
        
    def add_conn(self, predicate, obj):
        if not self.neighbors.get(predicate):
            self.neighbors[predicate] = []
        self.neighbors[predicate].append(graph.graph[obj])

class Graph:

    def __init__(self):
        self.graph = {}

    def search(self, subject, predicate=None):
        connections = []
        if self.graph.get(subject):
            node = self.graph.get(subject)
            if predicate:
                node = node.neighbors[predicate]
                for obj in node:
                    print(subject, predicate, obj.val)
                    connections.append(obj)
            else:
                for predicate, objs in node.neighbors.items():
                    for obj in objs:
                        print(subject, predicate, obj.val)
                        connections.append(obj)
        else:
            print(f"Sorry that word is not in our knowledge base... {subject.val}")
        return connections

    def add_to_graph(self, triples):
        subject, predicate, obj = triples

        if not self.graph.get(subject):
            self.graph[subject] = Node(subject)
        if not self.graph.get(obj):
            self.graph[obj] = Node(obj)
        self.graph[subject].add_conn(predicate, obj)
        
    def search_with_depth(self, subject, n=3):
        nodes_visited = set()
        nodes = [self.graph.get(subject)]
        print()
        new_nodes = []
        for _ in range(n):
            for node in nodes:
                if node in nodes_visited:
                    continue
                print("-----------------------------------")
                for predicate, objs in node.neighbors.items():
                    for obj in objs:
                        print(node.val, predicate, obj.val)
                        new_nodes.append(obj)
                nodes_visited.add(node)
            nodes = new_nodes
            new_nodes = []
            

graph = Graph()

triplets = [
    # Animals and humans
    ("cat", "chases", "mouse"),
    ("mouse", "eats", "cheese"),
    ("cat", "lives_with", "human"),
    ("dog", "lives_with", "human"),
    ("dog", "chases", "cat"),
    ("bird", "builds", "nest"),
    ("tree", "supports", "nest"),
    ("bird", "eats", "worm"),
    ("worm", "lives_in", "ground"),
    ("fish", "lives_in", "water"),
    ("human", "owns", "dog"),
    ("human", "feeds", "cat"),
    ("human", "feeds", "dog"),
    ("human", "observes", "bird"),

    # Knowledge & learning
    ("human", "reads", "book"),
    ("book", "contains", "pages"),
    ("book", "teaches", "mathematics"),
    ("book", "is_written_in", "language"),
    ("student", "studies", "mathematics"),
    ("student", "writes", "program"),
    ("teacher", "teaches", "student"),
    ("teacher", "uses", "book"),
    ("teacher", "explains", "concept"),
    ("program", "is_written_in", "python"),
    ("python", "is_a", "programming_language"),
    ("programming_language", "is_used_for", "software"),
    ("computer", "executes", "program"),
    ("human", "uses", "computer"),

    # Nature and environment
    ("sun", "provides", "light"),
    ("sun", "is_a", "star"),
    ("star", "produces", "light"),
    ("light", "is_used_by", "tree"),
    ("tree", "produces", "oxygen"),
    ("human", "breathes", "oxygen"),
    ("fire", "requires", "oxygen"),
    ("fire", "produces", "light"),
    ("rain", "falls_on", "ground"),
    ("ground", "absorbs", "water"),
    ("water", "is_required_by", "tree"),
    ("cloud", "produces", "rain"),
    ("river", "contains", "water"),
    ("river", "flows_into", "ocean"),
    ("fish", "lives_in", "river"),

    # Technology
    ("car", "requires", "gasoline"),
    ("car", "transports", "human"),
    ("car", "produces", "emissions"),
    ("emissions", "affect", "air"),
    ("air", "contains", "oxygen"),
    ("computer", "connects_to", "internet"),
    ("internet", "stores", "information"),
    ("information", "is_contained_in", "database"),
    ("database", "is_used_by", "software"),
    ("software", "runs_on", "computer"),
    ("human", "searches", "information"),
    ("human", "creates", "software"),
    ("human", "drives", "car"),
    ("satellite", "orbits", "earth"),
    ("satellite", "provides", "internet"),

    # Society
    ("company", "employs", "human"),
    ("human", "earns", "money"),
    ("money", "buys", "food"),
    ("food", "provides", "energy"),
    ("energy", "is_required_by", "human")
]

for triple in triplets:
    graph.add_to_graph(triple)

graph.search_with_depth("cat")

""" 
video references

in depth overview GHC chat modes - https://www.youtube.com/watch?v=s7Qzq0ejhjg
customize chat mode - https://www.youtube.com/watch?v=rE6svXzyhg0&t=6s
"""

from sentence_transformers import SentenceTransformer, util

# # Pretrained model for embeddings
# model = SentenceTransformer("all-MiniLM-L6-v2")

# # Your fixed list of candidate words
# word_list = ["dog", "cat", "car", "computer", "python", "music", "tree"]

# # Pre-compute embeddings for all words in the list
# word_embeddings = model.encode(word_list, convert_to_tensor=True)

# def find_similar(query: str, top_k: int = 3):
#     """Return top_k semantically similar words to the query."""
#     query_embedding = model.encode(query, convert_to_tensor=True)
#     scores = util.cos_sim(query_embedding, word_embeddings)[0]
#     results = sorted(zip(word_list, scores), key=lambda x: x[1], reverse=True)
#     return results[:top_k]

# # Example usage:
# print(find_similar("animal"))       # likely ['dog', 'cat', ...]
# print(find_similar("programming"))  # likely ['python', 'computer', ...] 

# Pretrained model for embeddings
model = SentenceTransformer("all-MiniLM-L6-v2")

# Pre-compute embeddings for all words in the list
word_embeddings = model.encode(graph.keys(), convert_to_tensor=True)

def find_similar(query: str, top_k: int = 3):
    """Return top_k semantically similar words to the query."""
    query_embedding = model.encode(query, convert_to_tensor=True)
    scores = util.cos_sim(query_embedding, word_embeddings)[0]
    results = sorted(zip(graph.keys(), scores), key=lambda x: x[1], reverse=True)
    return results[:top_k]

# Example usage:
print(find_similar("animal"))       # likely ['dog', 'cat', ...]
print(find_similar("programming"))  # likely ['python', 'computer', ...] 