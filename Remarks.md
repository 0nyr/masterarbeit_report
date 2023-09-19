# Remarks

> 19.09.2023

* [X] Assumption: Hearders can be detected from started
* [ ] Refactor background and related work.
* [ ] Assumption: Clibrary on alloc
* [ ] Add this https://sourceware.org/glibc/wiki/MallocInternals to backgroud/ method
* [ ] Complete the dataset exploration with a drawing of head dump composition
* [ ] https://www.gnu.org/software/libc/manual/html_node/The-GNU-Allocator.html
* [ ] Add negative vspace to make latex better
* [ ] How can we parse a head dump so as to generate a graph from it.

## Json annotation verification

* [ ] Write a part of JSON annotation verification

`HEAP_START`

`SSH_STRUCT_ADDR`

`SESSION_STATE_ADDR`

And for each key:

* size
* value
* address

taille valeur address

* [X] Vérifier que la taille annoncée correspond à la taille de la valeur effective de la clé.
* [X] stats about nb of keys per annotation file
* [X] total number of missannotated keys
* [X] nb of annotation files with problems

Generate a CSV with all problematic annotation file path, containing

* full path
* nb of malformed keys
* nb of keys in the file
* pour chaque fichier, bool for `HEAP_START`, `SSH_STRUCT_ADDR`, `SESSION_STATE_ADDR`
