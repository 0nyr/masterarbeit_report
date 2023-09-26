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

Testing chunk detection and annotation algorithms on cleaned dataset:

`python src/data_structure_detection.py --input /home/onyr/code/phdtrack/phdtrack_data_clean`

##### error with file `14814-1644921072-heap.raw`

I have a weird error with file `/home/onyr/code/phdtrack/phdtrack_data_clean/Training/Training/client/V_7_8_P1/24/14814-1644921072-heap.raw`. Memory increases until processed get killed, just for this file.

Actually, this was because of a block with size=0. I had an infinite loop. In this situation, the heap chunk flow is broken. Skip file.


### Tue 8 Aug 2023

Started to create the report template.
