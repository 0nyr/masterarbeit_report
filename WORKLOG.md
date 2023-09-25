# Logs

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

### Tue 8 Aug 2023

Started to create the report template.
