
# Latex

### compiling

`latexmk main.tex`

### compiling glossary / acronyms

`pdflatex main.tex`

`makeglossaries main`

`pdflatex main.tex`

# What is a KG?

## intro
> include the basic idea presented in the papers

Reading of 3 differents articles, mainly based on (KG21)(.


## development
> summarize the papers

##### A bit of history
The history and evolution of the knowledge engineering discipline has seen significant transformation since its inception during the expert systems development phase in the 1980s. We can distinguish 4 periods ranging from 1955 to the present day, with each period introducing new requirements for knowledge production processes to overcome the limitations of systems developed in preceding periods.

* Dawn of AI: initial focus on reliable and effective processes.
* Expert Systems Era: Feigenbaum stressed the need for domain-specific focus for automated knowledge production, leading to the creation of expert systems. However, these systems proved to be brittle and hard to maintain, thus the need for scalable, globally distributed, and interoperable systems arose.
* Semantic Web Era: Tim Berners-Lee advocated for a “Web of Data” based on linked data principles, standard ontologies, and data sharing protocols. This period saw the development of a globally federated open linked data cloud and techniques for ontology engineering. However, wider adoption was slow and led to the call for more developer-friendly tools and methods to deal with data noise and incompleteness.
* Language Model Era: LLM are now everywhere (ChatGPT, Bard) due to recent advancements in neural network architectures and graphical processing hardware. Language models can either serve as knowledge bases that are queryable using natural language prompts or as a component in a knowledge production workflow.

########## knowledge & graph
Not easy to define what knowledge is, so focus on "explicit knowledge": "something that is known and can be written down" (p4), composed of statements such as sentences, that are essentially sequences of words that draw relationship between concepts and data.

Graph theory: Theory ranging between computer science and mathematics that interests itself to the study of graphs. A graph is a kind of data structure consisting of nodes (aka vertices) and edges (arcs) that connect pairs of nodes. Based on the field and the shape of the graph, many properties can be deduced such as connectedness, cyclicity, planarity, as well as the presence of specific substructures like cliques or independent sets. These properties can provide valuable insights into the nature and characteristics of the system or network being modeled, enabling more effective analysis and decision-making. This theory is used to model and analyze various types of relationships and structures in a wide range of fields, including computer networks, social networks, biological networks, and many others.

Knowledge graph?: "a graph of data intended to accumulate and convey knowledge of the real world, whose nodes represent entities of interest and whose edges represent potentially different relations between these entities." (p3).

"Knowledge graphs serve as a common substrate of knowledge within an organisation or com-
munity, enabling the representation, accumulation, curation, and dissemination of knowledge
over time." (p31)

########## what is KG: basic understanding
"At the foundation of any knowledge graph is the principle of first modelling data as a graph" (p4)

"Graphs offer a flexible way to conceptualise, represent, and integrate diverse and incomplete data." p5

"Knowledge graphs use a graph-based data model to capture knowledge in application scenar-
ios that involve integrating, managing and extracting value from diverse sources of data at large scale (p2)"

"has a number of benefits when compared with a relational model or NoSQL alternatives" p2
data to evolve in a more flexible manner p2

flexible way to organize data (not hierarchical, can represent incomplete information, no need for a precise schema 

"Although the term knowledge graph goes back as far as 1973 [14], it gained popularity through the 2012 blog post1 about the Google KG. Afterwards, several related definitions of knowledge graphs were proposed, either in research papers [7, 9, 15–17] or by companies using or supporting KGs (OpenLink, Ontotext, Neo4J, TopQuadrant, Amazon, Diffbot2 , Google). Ehrlinger et al. [16] give a comprehensive overview of KG definitions and provide their
own: "A knowledge graph acquires and integrates information into an ontology and applies a reasoner to derive new knowledge." Hogan et. al. [18] argue that this definition is very specific and excludes various industrial KGs which helped to popularize the concept. We therefore define KGs more inclusively as a graph of data consisting of semantically described entities and relations of different types that are integrated from different sources. Entities have a unique identifier. KG entities and relations are semantically described using an ontology or, more clearly, an ontological representation [19]. An ontological theory can define formal naming, category systems, properties, and relations between concepts, data, and entities that encompass one or several domains of discourse." [CKH23]

########## types of KG
different types of graphs:
NB: "data can typically be converted from one model to another; in our view, a knowledge graph can thus adopt any such graph data model" (p6)
* Directed Edge-labelled Graphs (DEL): the classic graph, set of nodes and edges that connect the nodes with in certain way. RDF is a popular DEL data model.
* Heterogeneous Graphs: where each node and edge is assigned one type (p5), allow for partitioning nodes according to their type (for ML) (p6)
* Property Graphs: allows a set of property–value pairs and a label to be associated with nodes and edges (think of it as a kind of DB tables). Used in Neo4j (p6), great flexibility but harder to handle / query.
* Graph Dataset: set of named graphs, with a default graph with no ID. Useful when working with different sources.
* hypergraphs: allow edges that connect sets rather than pairs of nodes. 

##### storing and distributing KG
See (KG21, 2.1.6 p7)
relational databases either as a single relation of arity three (triple table),
as a binary relation for each property (vertical partitioning), or as n-ary relations for entities of a given type (property tables)
custom storage technique also exist

##### uses
open and entreprise KG
* open: BabelNet [90], DBpedia [76], Freebase [14], Wikidata [138], YAGO
* closed: Google KG
used for: Web search, commerce, social networks, finance, among others:
"Prominent industries using enterprise knowledge graphs include Web search, commerce, social
networks, finance, among others, where applications include search, recommendations, informa-
tion extraction, personal agents, advertising, business analytics, risk assessment, automation, and more besides (p4)

##### construction / creation / extraction
> Based on CKG23

Knowledge Graphs (KGs) are physical data integration systems that combine information from different sources into a new, logically centralized, graph-like representation. "Creation often involves integrating data from diverse sources, including direct human input; extraction from existing text, markup, legacy file formats, relational databases, other knowledge graphs; and so on." (KG21 p7)

Knowledge Graphs (KGs) are physical data integration systems that combine information from different sources into a new, logically centralized, graph-like representation. Knowledge Graphs (KGs) are physical data integration systems that combine information from different sources into a new, logically centralized, graph-like representation.

Requirements for quality KG construction:
    * Input Data requirements: It should be possible to integrate a large number of data sources as well as a high amount of data. There should also be support for heterogeneous and potentially low-quality input data of different kinds such as structured, semi-structured, and multimodal unstructured data.
    * Support for incremental KG updates: It should be possible to process the input data both in a batch-like mode where all (new) input data is processed at the same time or in a streaming manner where new data items can continuously be ingested.
    * Tooling/pipelining: A toolset for KG construction should be able to define and execute different pipelines depending on the data sources to be integrated and specific requirements, e.g., for incremental updates.
    * Quality assurance: The correctness (accuracy, consistency) aspect implies that each entity, concept, relation, and property is canonicalized by having a unique identifier and being included exactly once. The freshness aspect requires a continuous update of the instance and ontological information in a KG to incorporate all relevant data source changes.

KG construction tasks and approaches:
* Data Acquisition & Preprocessing: This task involves the selection of relevant sources, acquisition and transformation of relevant source data, and initial data cleaning. Source selection and filtering are typically manual steps but can be supported by data catalogs providing descriptive metadata about sources and their contents.

* Metadata Management: This task involves the acquisition and management of different kinds of metadata, such as provenance of entities, structural metadata, temporal information, quality reports, and process logs.

* Ontology Management: This task involves the creation and incremental evolution of a KG ontology.

* Knowledge Extraction (KE): This task involves the derivation of structured information and knowledge from unstructured or semi-structured data. Techniques used include named entity recognition, entity linking, and relation extraction. If necessary, this also entails the canonicalization of entity and relation identifiers.

* Entity Resolution (ER) and Fusion: This task involves the identification of matching entities and their fusion within the KG.

* Quality Assurance (QA): This task involves identifying and repairing data quality problems in the KG. Quality problems can relate to the ontological consistency, the data quality of entities and relations (comprehensiveness), or domain coverage.

* Knowledge Completion: This task involves extending a given KG, for example, by learning missing type information, predicting new relations, and enhancing domain-specific data (polishing).

The paper emphasizes that a construction pipeline does not necessarily follow a fixed execution order for the individual tasks and that not all steps may be required depending on the KG use case. This is because the required tasks depend on the type of source input. Furthermore, data and metadata management play a special role compared to the other tasks, since they are necessary throughout the entire pipeline, representing a cross-cutting task.


##### querying
* SPARQL query language for RDF graphs
* Cypher [34], Gremlin [112], and G-CORE for property graphs

important concepts related to querying graphs
* Graph Patterns: a graph similar to the data being queried that can contain variables so that the it can be evaluated to retreive information from constants in the KG.
	* homomorphism-based semantics: multiple variables to be mapped to the same term
	* isomorphism-based semantics: requires variables on nodes and/or edges to be mapped to unique terms
* Complex Graph Patterns: combines several graph patterns with operators (union, filter, where...). Powerful but can generate duplicates in the answer.
* Navigational Graph Patterns: regular expression for matching paths with support to more complex querying similar to using regex (disjunction, concatenation, set of possible values...). Can generate infinite number of paths, so it can be better to only return nodes (finite number).

"Graph query languages may support other features beyond those we have discussed, such as aggregation, complex filters and datatype operators, sub-queries, federated queries, graph updates, entailment regimes, and so on." (p9)

########## validation
Graphs are poweful du to being able to represent incomplete data, however it is sometimes necessary to ensure certain properties in the graph depending on its uses.

important concepts related to graph validation:
* Shapes Graphs: selected subset of nodes, with specified constraints, usually expressed using UML diagrams (which is by itself a kind of property graph).
	* open shape: "allows the node to have additional properties not specified by the shape" (p10)
	* closed shape: "no possible additional properties for target nodes".
* Conformance: "A node conforms to a shape if it satisfies all of the constraints of the shape." (p9). A valid graph is such that every node conforms to a given shape. Different shape langages extensions to RDF are available (ShEx, SHACL).
* context: every piece of information exists with respect to a context. The context, alonside with origin/provenance and time frame all define the "scope of truth" (p11). A context can be implicit or explicit. 
	* Direct Representation: consider context information as any other data (for instance, include dates, origin...). Different onthologies can help to better define relevant way to include the context.
	* Reification: describe edges of a graph in another graph to represent the context. Several forms of reification exist such as "RDF reification, n-ary relations and singleton properties, [...] NdFluents" (p11)
	* Higher-arity Representation: modify the graph with context annotation direclty on the graph. Different approaches exists like RDF*, (edges can be defined as nodes), named graph containing context, properties...
	* annotations: annotate directly edges or nodes with metadata, context informations or other useful related information. Several annotation model exists like Temporal RDF (time), Fuzzy RDF (degree of confidence)...
	* other more complex solutions exists like using subgraphs with partially ordered dimensions...

########## Onthologies
p13/37
"In computing, an ontology is then a concrete, formal representation—a convention—on what
terms mean within the scope in which they are used" (p13)
Shared ontologies make KG that use them more interoperable, but many onthologies exists depending on the context and use cases: Web Ontology Language (OWL) by W3C (RDF compatible), Open Biomedical Ontologies Format (OBOF).

* Interpretations: The real-world knowledge we human understand is call the "domain graph". It's an abstract notion, contrary to KG that are concrete. So every KG can be interpreted (understood) by mapping its nodes and edges to entities and relations. But many interpretations are possible (depending on who reads the KG for instance).
* Assumptions: assumptions we make on KG is going to dictate how they can be interpreted
	* Closed World Assumption: "what is not known is assumed false" (p14)
	* Open World Assumption: "it is possible for the relation to exist without being described by the graph" (p14)
	* Unique Name Assumption: "no two nodes can map to the same entity" (p14)
	* No Unique Name Assumption: it is possible that two nodes designate the same entity.
Since KG are often incomplete, Open World Assumption and No Unique Name Assumption are generally the considered assumptions.
* Semantic Conditions: case-specific assumptions that can make reasoning and entailment in the graph easier, by stating that if certain patterns are respected, then we can deduce some knowledge from it.
* Individuals: refers to real life entities. It is possible to apply rules for instance to try to distinguish nodes that refer to similar or different entities
* Properties:  "terms that can be used as edge-labels" (p14). It's possible to define a range of caracteristics on properties, like range, domain, equivalence, inverse, disjoinction, transitivity, symmetricity, reflexiveness, multiplicity... A property can also be a part of a chain, "such that pairs of entities related by the chain are also related by the given property" (p15)
* Classes: regroupment of nodes under a similar type (basically another property). Classes can also have caracteristics like equivalence, intersection, disjunction, complement... Classes can also have features with specified cardinality (think of it as Java classes or UML class diagram). One can also specify reasoning on classes, or rules 

Onthologies can be very complexe, with many more features like datatype facets ("defining new datatypes by applying restrictions to existing datatypes" (p15))

########## deduction, inference and entailment
> I have choosen to regroup some sections here
* Deduction: Process of deriving new data from what is already given and some implicit or explicit rules " allowing us to know more than what is explicitly given to us by the
data." (p12)
* Inference: Inference refers to the process of deriving or deducing new facts or knowledge from the existing data in the graph. This is typically achieved through logical reasoning based on the relationships and rules defined within the graph, or even context and additional external information.

"These deductions may serve a range of applications, such as improving query answering (deductive) classification, finding inconsistencies, and so on." (p13)

Inference in KGs is a powerful tool for enriching the graph with additional information, improving the quality of search and query results, and enabling more sophisticated data analysis and decision-making processes. It's a fundamental aspect of many applications of KGs, including semantic search, recommendation systems, and natural language processing.

* Entailment: deductive process where a relationship between statements or sets of statements where the truth of one statement or set necessarily implies the truth of another. By extension, "We say that one graph entails another if and only if any model of the for-
mer graph is also a model of the latter graph" (p17). In short, two graphs are entailed if they mean the same.
* Model-theoretic Semantics: Adding property axioms which define truth conditions, means that only certain interpretations become possible. "interpretations that satisfy a graph are called 'models' of the graph" (p16). 
* Reasoning: Once working with big graphs, the process of knowing if one graph entails the other second is undecidable. So we can only rely on practical algorithms whose properties depend on the KG and onthology, and that cannot be guarantied to be always correct of able to complete.
* Inference Rules: If-then (body-head) like statements with body and head being graph patterns. Predefined sets of rules exists for popular onthologies like "OWL 2 RL/RDF". Languages for expressing rules over KG also exists like Rule Interchange Format (RIF) or Semantic Web Rule Language.
* Description Logics (DLs): DLs comes from First Oder Logic (FOL), and are based on three types of elements:
	* Individuals: These are specific instances or objects, such as 'Santiago'.
	* Classes: (or concepts) categories or types of objects, such as 'City'.
	* Properties: (or roles), represent relationships between individuals, such as 'flight'.
DLs allow for making claims (known as axioms) about these elements. Axioms can be unary class relations on individuals (e.g., City(Santiago)) or binary property relations on individuals. Web Ontology Language (OWL) was heavily influenced by DLs, with OWL 2 DL language being a restricted fragment of OWL with decidable entailment.

########## inductive reasoning and learning
Inductive reasoning is a process that involves making generalizations based on observed patterns. "Inductive reasoning generalises patterns from input observations, which are used to generate novel but potentially imprecise predictions." (p20) This could involve using machine learning techniques to predict missing links or infer new knowledge. The paper also discusses the challenges associated with inductive reasoning, such as the difficulty of handling noise, incompleteness and uncertainty in the data.

Different processing framework for large-scale graph processing exists like "Apache Spark (GraphX) [26, 148], GraphLab [78], Pregel [80], Signal–Collect [126], Shark [149], and so on." (p22)

Induction techniques regroup:
* graph analytics: " well-known algorithms are used to detect communities or clusters, find central nodes and edges, and so on, in a graph" (p20). Regroup many popular analytical algorithms, on the following categories
	* centrality analysis: algorithms focused on identifying the most important nodes of a graph: PageRank, HITS...
	* community detection: identify densely-connected subgraphs (communities): minimum-cut algorithms, label propagation, Louvain modularity...
	* connectivity analysis: analysis on the graph connectiveness, with a range of metrics and algorithmns like graph density, strongly or weakly connected components, spanning trees, minimum cuts...
	* node similarity: identify similar nodes, for instance, based on their connected neighbourhood. Many metrics exists like structural equivalence, random walks, diffusion kernels...
	* graph summarisation: identify high-level structures, useful for getting an overview of a big graph

* knowledge graph embeddings: "learn a low-dimensional numerical model of elements of a knowledge graph" (p20). ML techniques can be used on KG for a wide range of applications: "recommendation [155], information extraction [135], question answering [60], query relaxation [139], query approximation [45], and so on." (p23). The issue is that ML often requires working with numerical values like vectors, not graphs. Going from graphs to vector is known as embedding. 
	* adjascency sparse matrix: matrix for every node, of its connections with other nodes. Impractical as mostly full of zeros, and huge. What we want is a dense, low dimensionality representation of the graph. 
	* plausibility embedding: vectors for nodes (entity embedding) and for edge labels (relation embedding), and a scoring function learned from the graph that determines the plausibility (possible existence) of a given edge, like DistMult method: "The resulting embeddings can then be seen as models learned through self-supervision that encode (latent) features of the graph, mapping input edges to output plausibility scores." (p23) A drawback is that "DistMult does not capture edge direction." (p25)
	* translational models: "interpret edge labels as transformations from
subject nodes" (p23). The embedding trys to learn distances of transformations by summing vectors. But this doesn't works well due to the curse of dimensionality so other approches have been developped using different spaces like distinct hyperplanes or hyperbolic space thag give more "space" to distinguish entities.
	* tensor decomposition models: A tensor is a generalization of scalars, vectors and matrices to higher dimensionalities. Tensor decomposition is the process of capturing latent factor of high dimensional tensors to smaller dimensional tensors. Several approches exist like RESCAL that relies on rank decomposition similar to plausibility embedding (like DistMul), but using matrices instead of vectors. This helps to capture edge direction by combining values of many dimensions (many edges). Other methods: ComplEx (complex vectors), HolE (circular correlation operator), SimplE (CP-decomposition), TuckEr (Trucker Decomposition...).
	* neural models: Use of neural networks for learning non-linear scoring (plausibility) functions. A range of networks can be used like the now classical Multi Layer Perceptron or more specific implementations like Multi Layer Perceptron that tries to learn parameters by computing two scoring function and comparing their dot-product. New approaches take advantage of the powerful convolutional kernels.
	* language models: Range of techniques that tend to transform a graph into text so as to take advantage of powerful NLP ML techniques. For instance, "RDF2Vec performs biased random walks on the graph and records the paths traversed as “sentences,” which are then fed as input into the word2vec [83] model." 
	* entailment-aware models: It is possible to take advantage of ontologies and sets of rule for embedding, so as to refine predictions or scoring functions. "More recent approaches rather propose joint embeddings that consider both the data graph and rules." (p26). For instance, KALE uses TransE emdedding with fuzzy logic to integrate the rules to its embedding. 
p27

* graph neural networks: supervised learning using the graph structure itself. A Neural network is by nature a "directed weighted graph, where nodes serve as artificial neurons, and edges serve as weighted connections (axons)." (p27). GNN (Graph Neural Network) is a kind of neural network where "where nodes are connected to their neighbours in the data graph." "GNNs have been used to perform classification over graphs encoding compounds, objects in images, documents, and so on;" (p27)
	* Recursive graph neural networks (RecGNNs): Every node and label is associated with a vector encapsulating features, and every node has also a state vector that is updated with each recursion loop from the information of its neighbours. The recursion uses two functions called the *transition function* that gets information from a node neighbours and the *output function* that takes results from the previous function as well as the node's own state vector and features. "Both parametric functions can be learned using neural networks given a partial set of labelled nodes in the graph." (p27). The recursion is generally applied until a fixpoint is reached.
	* Convolutional Graph Neural Networks (ConvGNNs): Convolutional neural networks (CNNs) are now a popular family of machine learning models that rely on the idea of applying small filters (kernels) over local regions of the dataset, for instance on subparts of images. The idea behing ConvGNNs is to implement the *transition function* as a convolution, however, the challenge here is that contrary to images where each pixel neighbourhood is easily predictable, this is not as straightforward for node neighbourhood. Different approaches are possible to tackle this issue, like "working with spectral or spatial reference representations of graphs that induce a more regular structure from the graph." (p28). Convolution layers can be diverses and applied generally a specified number of times.

* symbolic learning: "learn symbolic models—i.e., logical formulae in the form of rules or
axioms—from a graph in a self-supervised manner." (p20) This makes possible to learn logic rules and reasoning, such that the decision making can rely on a well-defined explaination prodived by the model rather than on numerical values like it is the case with RecGNNs or ConvGNNs. Thoses models suffer from what is known as *out-of-vocabulary problem* which describe the issue that those models struggle to provide accurate results for unseen nodes or edges labels. By using symbolic learning, we focus the learning process on the hypotheses as explainable rules which works on a broader set of situations.
 	* Rule mining: The idea is to learn meaningful rules as logical patterns. Those patterns do no need to be always verified, but rather must be associated with a measure of how well they are verified in the graph. What we try to do is to find the rules that are well-verified and that have few exceptions. Several techniques exixts like AMIE.
 	* Axiom mining: axioms are a similar to rules but are intended to be more general. For instance, determining what are impossible cases from the graph. Thoses are called *disjointness constraints*. Other axioms can be found using more complex strategies like *disjointness constraints* ("given a set of positive nodes and negative nodes, the goal is to find a logical class description that divides the positive and negative sets." (p31)



## KG in real life
> Show example of how I use KG in my masterarbeit.

I have been using a Heterogeneous Directed Edge-labelled Graph for representing the heap-dump memory of different versions of OpenSSH. Each node represents an annotated block of bytes. The annotation is encapsulated in a type that can represent Data Structures, SSH Keys, pointers and so on. Thoses types are then being used for generating samples and labels used in the feature engineering and ML part.

## points raised during presentation
> include the points raised in the seminar by the moderator (collaborate with the opponents if necessary)

## paper evaluations
> Identify strengths and weaknesses, question the assumptions, criticize the bad decisions in the papers

[KG21]:
+ do not assume that readers have specific expertise on knowledge graphs, and as such can be very informative for readers that want to grasp a good overview of what are KG.
+ meta-analysis: 13 external papers and books reviewed
+ extended online version
+ concrete examples (many) on GitHub: https://github.com/knowledge-graphs-tutorial/examples
+ in-depth concept discussion: The paper covers many crucial complex topics with a deep understanding. It also discusses how these concepts are applied in the context of knowledge graphs.
+ has "article structure" section
+ still recent paper (2021)
+ Provide some recommendations: "allows edges to be defined as nodes..." (p11). Also provide useful bibliography and further readings for topics that are not covered in depth.
- Only focused on DEL graphs
- Focused on core theorical concepts: It would benefit from more practical examples or case studies showing how these concepts are applied in real-world settings.
- KG creation: very little (5 lines) on KG creation or extraction, but covered in extended version
- content complexity: While still comprehensive for newcomers, it is challenging for readers who are new to the field due to the complexity and profusion of topics discussed. The paper could benefit from a more gradual introduction to these complex topics.
- Imbalanced topic discussion: While some crucial topics for newcomers like KG creation are not covered, other more advanced ones are presented with a lot of details like inductive reasoning or learning methods such as graph kernels and graph neural networks. While these are important subjects, the choice for such a focus is odd considering the targeted audience.
- Lack of discussion on challenges: Too few discussions (on conclusion) on challenges associated with  knowledge graphs, such as issues related to scalability, data quality, diversity ("managing contextual or multi-modal data" (p31), dynamicity (temporal and streaming data), usability and the complexity of reasoning tasks. 
- Some unclear explainations: p22, the explaination example of PageRank is really unclear, with no scheme, as well as mathematical expressions directly in the text with some symbols like |V| being unspecified (and have to be guessed by the reader, here, number of nodes in the graph). The distinction between rule mining and axiom mining is also very shallow and unclear, on p31.
- mistake in a sentence: p29: "In more detail, we call the edges entailed by a rule and the set of positive edges (not including the entailed edge itself) the positive entailments of that rule. The number of entailments that are positive is called the support for the rule, while the ratio of a rule’s entailments that are positive is called the confidence for the rule [127]." (p29) -> Missing some words: "...we call the edges entailed by a rule <the entailments of the rule> and the set of positive edges (not including the entailed edge itself) the positive entailments of that rule."
- Would benefit from a clearer presentation of the differences between deductive and inductive reasoning. The paper consider that the reader is already familiar with thoses differences and dives directly into advances concepts.

[CKG23]
+ state of the art
+ extensive documentation and references (more than 250 references)
- preprint, available on Arxiv


Paper Overview
Contributions
Improvements to the State-of-the-Art
Main Results

## conclusion
> include the important results and conclusions

In conclusion, a knowledge graph is a powerful tool for modeling, storing, organizing and accessing complex information. By representing data as a network of interconnected nodes and edges, knowledge graphs enable us to navigate through the data in a natural and intuitive way. They are becoming increasingly important in today's data-driven world, and have a wide range of applications across many different industries and domains. As the amount of data we generate and collect continues to grow, knowledge graphs will become even more important in helping us to make sense of it all.


(KG21) 
This paper provides a comprehensive and in-depth exploration of knowledge graphs (KGs), structures, applications, and many related concepts. KGs are a structured form of data representation that uses a graph-based structure to depict real-world entities and the relationships between them. They are particularly useful for handling complex and interconnected data, providing a way to integrate, organize, and manage data from different sources while maintaining the semantic context and relationships between data points.

Key elements to consider when working with KGs, as discussed in the paper, include Description Logics (DLs), which provide a logical formalization of KGs, and ontologies, which enable entailment and provide a precise definition of terms used in KGs. The paper also delves into the concept of inductive reasoning over KGs, discussing various methods such as graph kernels, graph neural networks, label propagation, and multi-modal learning.

As for the quality of the paper, it stands out for its comprehensive coverage and clear explanations of complex concepts. It provides a valuable resource for anyone interested in understanding KGs, from beginners to experts in the field. However, the paper could benefit from more practical examples or case studies to illustrate the application of these concepts in real-world settings.

In terms of readability, while the paper is well-structured and the content is clearly presented, the complexity of the topics discussed might make it challenging for readers who are new to the field. Nonetheless, for those with a background in the subject matter, the paper offers a deep and insightful exploration of KGs and their applications.

Overall, the paper is a significant contribution to the field, offering a thorough and detailed examination of KGs that will likely prove useful for researchers and practitioners alike.


# Question for moderator
Andreas Einwiller: How is inductive and deductive reasoning related to ML and Ontologies/Rules?

Notes from presentation:
Slide: Inductive and deductive reasoning: What is that ?
Source: [Wikipedia]
Types of Reasoning
2 fundamental methods: Deductive and Inductive reasoning
Different in process and results
Importance of Reasoning in KGs
Essential for enhancing the utility of KGs.
Enable predictions: missing links,
○ discovery of new knowledge, rules
○ improvement of the overall quality and completeness
Facilitate complex queries and advanced analytics on the graph.

Slide: Deductive Reasoning
Top-down logical flow: General to specific
Conclusion is certain if premises are true
Example:
1. All men are mortal. (General premise)
2. Socrates is a man. (Specific premise)
3. Therefore, Socrates is mortal. (Specific
conclusion)
Used to test theories and hypotheses
Used to “deduce” new knowledge

Slide: Importance of Reasoning in KGs

Both deductive and inductive reasoning are essential for enhancing the utility of KGs.
They enable the prediction of missing links, discovery of new knowledge, and improvement of the overall quality and completeness of the graph.
They also facilitate complex queries and advanced analytics on the graph.

Slide: Deductive Reasoning in KGs
Infer new facts based on existing facts and rules in the graph.
Follows a logical process: if all premises are true, then the conclusion must also be true.
Example: If we know that "Paris is a city" (fact) and "All cities are populated areas" (rule),
we can deduce that "Paris is a populated area" (new fact).
This process is also known as "knowledge graph completion" or "link prediction".

Slide: A range of methods
Ontologies
Definition: An ontology is a formal representation of what terms mean within the scope in which they are used.
Shared ontologies make KGs more interoperable.
Examples: Web Ontology Language (OWL) by W3C, Open Biomedical Ontologies Format (OBOF).
Deduction, Inference, and Entailment

Deduction: Process of deriving new data from what is already given and some implicit or explicit rules.
Inference: Process of deriving or deducing new facts or knowledge from the existing data in the graph.
Entailment: Deductive process where a relationship between statements or sets of statements where the truth of one
statement or set necessarily implies the truth of another.
Inference Rules and Description Logics (DLs)

Inference Rules: If-then (body-head) like statements with body and head being graph patterns.
Description Logics (DLs): DLs come from First Order Logic (FOL), based on 3 types: Individuals, Classes, Properties
DLs allow for making claims (known as axioms) about these elements.

Slide: Inductive Reasoning
Bottom-up logical ﬂow: Speciﬁc to general
Conclusion is probable, based on truth of
premises
Example:
○ The sun has risen in the east every
morning so far. (Speciﬁc observation)
○ Therefore, the sun will rise in the east
tomorrow. (General conclusion)
Used in the formation of hypotheses and
theories

Slide: Inductive Reasoning in KGs
Inductive reasoning in KGs is about learning new rules based on patterns observed in the
data.
It follows a probabilistic process: speciﬁc observations are generalized into rules, which are
likely but not guaranteed to be true.
Example: If we observe many instances of a relationship like "Person works at Company"
and "Company is located in City", we might induce a rule like "Person lives in City".
This process is often used in "rule mining" or "entity prediction" in KGs.

Slide: A range of methods



Amandeep Gill:  How do knowledge graphs handle scalability issues, and what are the associated trade-offs?

Chirag: Could you explain a bit more as to how exactly knowledge graph is best suitable for machine learning?



## bibliography
(KG21) [Hogan, Aidan, et al. &#34;Knowledge graphs.&#34; ACM Computing Surveys (CSUR) 54.4 (2021): 1-37](https://dl.acm.org/doi/abs/10.1145/3447772)

(KGKE22) [Knowledge Graphs and their Role in the Knowledge Engineering of the 21st Century](https://drops.dagstuhl.de/opus/volltexte/2023/17810/pdf/dagrep_v012_i009_p060_22372.pdf)

(CKG23) [Marvin Hofer, Daniel Obraczka, Alieh Saeedi, Hanna Köpcke and Erhard Rahm. "Construction of Knowledge Graphs: State and Challenges" (2023)](https://arxiv.org/pdf/2302.11509.pdf)






## TODO: go further
A number of systems further allow for distributing graphs over multiple
machines based on popular NoSQL stores or custom partitioning schemes [63, 146]. For further
details, we refer to the book chapter by Janke and Staab [63] and the survey by Wylot et al. [146] dedicated to this topic.




