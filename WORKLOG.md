# TODO

* [ ] Write a paragraph on repartition of training and testing files.

```
 ❮onyr ★ nixos❯ ❮phdtrack_data_clean❯❯ find ./Performance_Test/ -type f -name '*-heap.raw' | wc -l
1503
 ❮onyr ★ nixos❯ ❮phdtrack_data_clean❯❯ find ./Training/ -type f -name '*-heap.raw' | wc -l
20953
 ❮onyr ★ nixos❯ ❮phdtrack_data_clean❯❯ find ./Validation/ -type f -name '*-heap.raw' | wc -l
3735
```

* [ ] Correct chunk filtering
* [ ] correct mem graph construction
* [X] Write SUMMARY result section in Conclusion

* Identifying a key is equivalent to identifying its chunk
* We can filter out chunks based on the entropy of the 12 first bytes of their user data, their connectivity to other chunks, or their size.
* We can build a directed graph representing every block and every chunk from a heap dump
* We can perform embeddings on those graph via manual feature engineering, or automated techniques like Node2Vec
* ML and Deep Learning models are efficient at identifying keys from thoses embeddings, but hyperparam tuning and model fitting is time and compute intensive.

* [X] Write future work

* Leverage the work done in this masterarbeit and generalize it to other programs based on GLibC
* Study the impact of different C libraries on the algorithms developped here
* Integrate the models into a new Rust program, able to do the full graph parsing and ML predictions.
* Improve hyperparameter tuning
* Test more model of ML and DL
* Add new custom embeddings to mem2graph program.

* [X] Correct shema graphs to be using CHN instead of DTN.

# Logs

### Thu 26 Oct 2023

* [ ] Intégrer les notes de Clem, particulièrement les embeddings
* [ ] Remplir les sections vides
* [ ] Graphiques de résultats (pour les 4 métriques, par classifier)

### Sat 21 Oct 2023

`python run_pipelines.py -k -i /home/onyr/code/phdtrack/phdtrack_data_clean/ -p graph-with-embedding-comments`: In mem2graph, launcher script params.

### Fri 20 Oct 2023

Started launching the dataset generation on the server.

```shell
[2023-10-20T10:41:06 UTC][INFO mem_to_graph::exe_pipeline::pipeline]  🟢 [t: worker-25] [N°16771 / 26202 files] [fid: 6017-1644319566]    (Nb samples: 0)
[2023-10-20T10:41:06 UTC][INFO mem_to_graph::exe_pipeline::pipeline]  🟢 [t: worker-55] [N°20331 / 26202 files] [fid: 12821-1644324152]    (Nb samples: 0)
[2023-10-20T10:41:06 UTC][INFO mem_to_graph::exe_pipeline::pipeline]  🟢 [t: worker-77] [N°16751 / 26202 files] [fid: 6862-1644319566]    (Nb samples: 0)
[2023-10-20T10:41:06 UTC][INFO mem_to_graph::exe_pipeline::pipeline]  🟢 [t: worker-70] [N°20326 / 26202 files] [fid: 12432-1644324152]    (Nb samples: 0)
[2023-10-20T10:41:06 UTC][INFO mem_to_graph::exe_pipeline::pipeline]  ⏱️  total pipeline time: 518.97s]
🟢 Finished compute instance: cargo run -- -d /root/phdtrack/phdtrack_data_cleaned -o /root/phdtrack/mem2graph/data/48_graph_with_embedding_comments_-e_none_-a_chunk-header-node -p graph-with-embedding-comments -e none -a chunk-header-node
100%|█████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 1/1 [08:39<00:00, 519.31s/it]
Total time: 0 hours, 8 minutes, 39 seconds
```

### Thu 28 Sep 2023

NOTE: Since we are only predicting first block of chunks, this is equivalent to predict the chunk itself.

`cargo run -- -d /home/onyr/code/phdtrack/phdtrack_data_clean/ -o /home/onyr/code/phdtrack/mem2graph/data/chunk_semantic_no_vn -p chunk-semantic-embedding -e only-max-entropy -a chunk-header-node -v`

Lot of work.

> **NOTE**: WE DISCOVERED THAT KEYS ARE ALWAYS AT THE START OF THE USER DATA OF A CHUNK! THIS HOLDS TRUE FOR ALL ANNOTATIONS (KEYS, SSH_STRUCT, SESSION_STATE).

`/home/onyr/code/phdtrack/phdtrack_data_clean/Training/Training/basic/V_7_1_P1/24/17016-1643962152-heap.raw`

### Wed 27 Sep 2023

Continued to work on Chunk exploration script in Python.

```shell
find ~/code/phdtrack/phdtrack_data_clean/ -type f -name "*-heap.raw" | wc -l
```

### Mon 25 Sep 2023

* [ ] write script to check GLIBC allocation processes. Count nb of allocated and unallocated data structures
* [ ] write script to count nb of files in each subdirectories of the cleaned dataset
* [ ] Create RUST pipeline for semantic embedding with entropy filtering. Just keep blocks that are inside chunks with highest entropy. Add a check to verify that first key blocks are all included.
* [ ] Finished KG-construction part.
* [ ] Finish Dataset data structure exploration part.

The following command was used to find the example file from `phdtrack_data_clean`:

```shell
 ❮onyr ★ nixos❯ ❮mem2graph❯❯ find ~/code/phdtrack/phdtrack_data_clean/ -type f -name "17016-1643962152-heap.raw"
/home/onyr/code/phdtrack/phdtrack_data_clean/Training/Training/basic/V_7_1_P1/24/17016-1643962152-heap.raw
```

#### notes:

The last block is only composed of zeros, and the heap is truncated 2 blocks before the real end. This chunk should be removed.

### Fri 22 Sep 2023

Generating graph examples.

`sfdp -Gsize=30! -Goverlap=ortho -Tpng test.gv > test.png`

Testing chunk detection and annotation algorithms on cleaned dataset:

`python src/data_structure_detection.py --input /home/onyr/code/phdtrack/phdtrack_data_clean`

##### error with file `14814-1644921072-heap.raw`

I have a weird error with file `/home/onyr/code/phdtrack/phdtrack_data_clean/Training/Training/client/V_7_8_P1/24/14814-1644921072-heap.raw`. Memory increases until processed get killed, just for this file.

Actually, this was because of a block with size=0. I had an infinite loop. In this situation, the heap chunk flow is broken. Skip file.

### Tue 8 Aug 2023

Started to create the report template.
