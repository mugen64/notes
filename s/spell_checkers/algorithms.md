# Levenshtein Distance
Given two words the levenshtein distance is the number of operations needed to turn one into the other
Operations include:-
- Deletion
- Insertion
- Substitution

## Levenshtein algorithm
- Given two words a,b
```js

function lev(a, b) {
    edits = 0

    if(len(a) == 0) return

    if(len(b) == 0) return

    if(head(a) == head(b)) return

    edits = 1 + min(
        // deletion
        lev(tail(a), b),
        // insertion
        lev(a, tail(b)),
        // substitution
        lev(tail(a), tail(b)),
     )

    return edits;
}



```