## Non-neural baseline system for the SIGMORPHON shared task 2021 (task 0)

This system was first released as a [baseline](https://github.com/sigmorphon2020/task0-baselines/tree/master/nonneural) SIGMORPHON's shared task 2020.

This is a very simple Python 3 baseline algorithm for solving task 0 without external dependencies. The system has a strong bias toward only accounting for prefix and suffix changes when inflecting a form from a given lemma.

When run with the `-o` option, the program writes its outputs into files.  The default behavior is to just run the algorithm on all tasks and languages and print out accuracy on the dev set.

The default relative path to the train/dev files language family directory (`./../../task0-data/`) can be changed with the `-p` flag. The system is also tested with PyPy and runs significantly faster.

To run:

```
python baseline.py
```

This assumes the data is found in `./../../task0-data/`.

## Details: learning

As a first step, the system aligns input/output training examples using Levenshtein distance.  For example, the example

```
schielen        geschielt       V.PTCP;PST
```

is aligned as follows:

```
__schielen
geschielt_
```

The system now assumes that each input-output pair can be broken up into a prefixation part, a stem part, and a suffixation part, based on where the inputs or outputs have initial or trailing zeroes:

```
Pr   St   Su
__|schiele|n
ge|schielt|_
```

After this, the system extracts a set of prefix-changing rules based on the Pr pairings, and a set of suffix-changing rules based on St+Su pairings.

In this example, the following suffix-changing rules are extracted:

```
n$ > $
en$ > t$
len$ > lt$
elen$ > elt$
ielen$ > ielt$
hielen$ > hielt$
chielen$ > chielt$
schielen$ > schielt$
```

Likewise, the only prefix-changing rule extracted is the following:

```
$ > $ge
```

For languages with few prefix changes, the only prefix rule will often be `$ > $`, i.e. no change.

All these rules are associated with the complete MSD of an example, in this case `V.PTCP;PST`.

## Details: generation

At generation time, the longest suffix rule that applies to a lemma form to be inflected is used.  For example, if we're asked to inflect `kaufen` into `V.PTCP;PST`, we may find that, for example, `en$ > t$` is the longest-matching suffix rule among all rules for `V.PTCP;PST`, which transforms:

```
$kaufen$ > $kauft$
```

and, following this, we find the most frequently seen prefix-changing rule for the target MSD in question that is applicable, in this case `$ > $ge` and apply that:

```
$kaufen$ > $gekauft$
```

### Unseen MSD strings

If no rule has been associated with a particular MSD combination, the lemma form is simply repeated.

### Prefixing languages

There is a heuristic to decide if a language is largely prefixing or largely suffixing.  This is done by simply counting how often there is a prefix-change vs. suffix-change in going from the lemma form to the inflected form.  Whenever a language is found to be largely prefixing, the system works with reversed strings throughout.
