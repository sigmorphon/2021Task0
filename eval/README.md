## Evaluation script

To evaluate your part2 system run the command:
```bash
$ Rscript eval/sigmorphon_evaluation_part2.R <human_ratings> <model_ratings>
```

So this should give you the scores of a perfect model:
```bash
$ Rscript eval/sigmorphon_evaluation_part2.R part2/eng.judgements.dev  part2/eng.judgements.dev
```
