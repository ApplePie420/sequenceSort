# sequenceSort
It is pretty simple:
You pass an unsorted array, it will find the biggest number and iterate over all elements in unsorted array with another nested loop, which loops over all numbers in range from 0 to the biggest found, and compares. If it matches, append to new array. Repeat and return. 
Simple, not efficient, dumb and why.
I just made it coz i was bored. It actually works pretty fast with relatively large datasets that containt pretty small ranges.
# big O
So since it have to iterate over array twice, and then over biggest number (B), it's O notation is:

__O(B*(2n))__
# tests
I'm running i5-5470 CPU (non OC) with 16GB of 2800MHz RAM with __64b python 3.8.1.__

Obviously, I disabled `print(result)` because in most occasions, printing whole array takes a lot more than actually sorting it.

So i ran few tests to determine best use case scenario for this algo _(sorted by fastest)_:

| # of Numbers | Biggest Number | Time |
| :---: | :---: | :--- |
| 100 | 100 | 0.0s* |
| 1 000 | 10 | 0.001s |
| 1 000 | 1 000 | 0.034s |
| 1 000 000 | 10 | 1.156s |
| 100 |  1 000 000 | 3.198s |
| 100 000 | 1 000 | 3.393s |
| 1 000 | 1 000 000 | 33.142s |
| 1 000 000 | 1 000 | 34.248s |
| 100 000 | 100 000 | 5.561min |
| 1 000 000 000 | 10 | 22.851min | 

_*couldn't measure even with 15 decimal points_

So by calculating t/O(B*(2n)), we've got approximate speed of 17.3M sorts per second. Not bad I guess?

# things i observed
So running a few tests, i observed following:
- With relatively large datasets with small number range, you get pretty decent speeds
- By using 64b version of python insted of 32b, you can get performance improvements of up to few minutes (with largest tested dataset. Few seconds or tens of seconds in others. Only relatively insignificant difference was in first 5 tests)
