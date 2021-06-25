#!/usr/bin/env python
"""
Official Evaluation Script for SIGMORPHON 2020 Task 0.
Returns accuracy and mean Levenshtein distance.

Last Update: 02/28/2020
"""

import numpy as np
import codecs

def distance(str1, str2):
    """Simple Levenshtein implementation for eval."""
    m = np.zeros([len(str2)+1, len(str1)+1])
    for x in range(1, len(str2) + 1):
        m[x][0] = m[x-1][0] + 1
    for y in range(1, len(str1) + 1):
        m[0][y] = m[0][y-1] + 1
    for x in range(1, len(str2) + 1):
        for y in range(1, len(str1) + 1):
            if str1[y-1] == str2[x-1]:
                dg = 0
            else:
                dg = 1
            m[x][y] = min(m[x-1][y] + 1, m[x][y-1] + 1, m[x-1][y-1] + dg)
    return int(m[len(str2)][len(str1)])

def read(fname):
    """ read file name """
    D = {}
    with codecs.open(fname, 'rb', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            lemma, word, tag = line.split("\t")
            if lemma not in D:
                D[lemma] = {}
            D[lemma][tag] = word
    return D

def read_input(fname):
    """ read in the uncovered file to ignore paradigm slots """
    ignore = set()
    with codecs.open(fname, 'rb', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            lemma, word, tag = line.split("\t")
            if word != u"":
                ignore.add((lemma, tag))
    return ignore

def eval_form(gold, guess, ignore=set()):
    """ compute average accuracy and edit distance for task 1 """
    correct, dist, total = 0., 0., 0.
    for lemma, D in gold.items():
        for tag, str1 in D.items():
            if (lemma, tag) in ignore:
                continue
            
            str2 = u"" # empty string if no guess
            if lemma in guess and tag in guess[lemma]:
                str2 = guess[lemma][tag]
            if str1 == str2:
                correct += 1
            dist += distance(str1, str2)
            total += 1
    return (round(correct/total*100, 2), round(dist/total, 2))

def eval_paradigm(gold, guess):
    """ compute the accuracy (form and paradigm) and edit distance (form) for task 2 """
    correct, total = 0., 0.
    for lemma, D in gold.items():
        correct += 1
        total += 1
        for tag, str1 in D.items():
            str2 = u"" # empty string if no guess
            if lemma in guess and tag in guess[lemma]:
                str2 = guess[lemma][tag]
            if str1 != str2:
                correct -= 1
                break
    return round(correct/total*100, 2)
                
if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description='SIGMORPHON 2020 Task 0 Evaluation')
    parser.add_argument("--ref", help="Gold data", required=True, type=str)
    parser.add_argument("--hyp", help="Model output", required=True, type=str)
    args = parser.parse_args()    

    D_gold  = read(args.ref)
    D_guess = read(args.hyp)

    print("accuracy:\t{0:.2f}\nlevenshtein:\t{1:.2f}".format(*eval_form(D_gold, D_guess)))
