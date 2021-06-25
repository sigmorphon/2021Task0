# SIGMORPHON–UniMorph Shared Task on Generalization in Morphological Inflection Generation

SIGMORPHON’s sixth installment of its inflection generation shared task will be divided into two parts:

+ ***Part 1***: [Generalization Across Typologically Diverse Languages](https://github.com/sigmorphon/2021Task0#part-1-generalization-across-typologically-diverse-languages)
+ ***Part 2***: [Are We There Yet? A Shared Task on Cognitively Plausible Morphological Inflection](https://github.com/sigmorphon/2021Task0#part-2-are-we-there-yet1-a-shared-task-on-cognitively-plausible-morphological-inflection)

Please join our [Google Group](https://groups.google.com/forum/#!forum/sigmorphon2021-sharedtask0/join) to stay up to date.

Click here to [register for the task](https://forms.gle/tu4tX648F9kA9eps7)!


## Part 1: Generalization Across Typologically Diverse Languages


### Task Summary


In this shared task, participants will design a model that learns to generate morphological inflections from a lemma and a set of morphosyntactic features of the target form. Each language in the task has its own training, development, and test splits. Training and development splits contain triples, each consisting of a lemma, a target form, and a set of morphological features, provided in the UniMorph format (the “Data” section below provides an example of input format). Test splits only provide lemmas and morphological tags: your model will need to predict the missing target form.

The model should be general enough to work for natural languages of any typological patterning. For example, Tagalog verbs exhibit [circumfixation](https://en.wikipedia.org/wiki/Circumfix); thus, a model with a strong inductive bias towards suffixing will likely not work well for Tagalog.


### Task Details
This task will proceed in three phases: the ***Development Phase***, the ***Generalization Phase***, and the ***Evaluation Phase***. As the phases advance, more data and more languages will be released.

In the ***Development Phase***, we will provide training and development splits that should be used to *develop* your system.
We will refer to them as the *development languages*. The list of languages is below.

In the ***Generalization Phase***, we will provide training and development splits for new languages where approximately half are genetically related (belong to the same family) and half are genetically *unrelated* (are isolates or belong to a different family) to the development languages. We will keep the languages in the Generalization Phase a surprise until April 2021. We will also keep the genetically unrelated language *families* a surprise, though some languages will come from the same families as those in the Development Phase.

In the ***Evaluation Phase***, the participants’ models will be evaluated on held-out forms from all of the languages from the previous phases. The languages from the Development Phase and the Generalization Phase are evaluated simultaneously. The only difference is that there has been more time to construct a model for those languages released in the Development Phase. It follows that a model could easily overfit to or favor phenomena that are more frequent in languages presented in the Development Phase, especially if parameters are shared across languages. For instance, a model based on the morphological patterning of the Indo-European languages may end up with a bias towards suffixing and will struggle to learn prefixing or circumfixation, the degree to which only becomes apparent during experimentation on other languages whose inflectional morphology patterns differ. Of course, the model architecture itself could explicitly or implicitly favor certain word formation types (suffixing, prefixing, etc.).


#### Development Languages

| Language | Family| code | UM | Annotators  |
|---|---|---|---|---|
|Egyptian Arabic |Afro-Asiatic | arz  | https://github.com/unimorph/arz/  | Salam Khalifa and Nizar Habash  |
|Gulf Arabic |Afro-Asiatic | afb | https://github.com/unimorph/afb/  |Salam Khalifa and Nizar Habash  |
|Modern Standard Arabic |Afro-Asiatic | ara | https://github.com/unimorph/ara| Salam Khalifa and Nizar Habash  |
|Classic Syriac | Afro-Asiatic | syc | https://github.com/unimorph/syc| Charbel El-Khaissi   |
|Hebrew (Vocalized) |Afro-Asiatic | heb | https://github.com/unimorph/heb| Omer Goldman   |
|Amharic | Afro-Asiatic | amh| https://github.com/unimorph/amh| Michael Gasser   |
|Kunwinjku |Arnhem (AU) | gup | https://github.com/unimorph/gup| William Lane |
|Aymara |Aymaran | aym | https://github.com/unimorph/aym| Matt Coler, Eleanor Chodroff |
|Ashaninka |Arawakan | cni | https://github.com/unimorph/cni| Arturo Oncevay, Jaime Rafael Montoya Samame |
|Yanesha |Arawakan | ame | https://github.com/unimorph/ame| Arturo Oncevay, Gema Celeste Silva Villegas |
|Seneca |Iroquoian | see | https://github.com/unimorph/see| Zoey Liu, Richard J. Hatcher, Emily Prud'hommeaux |
|Sakha |Turkic | sah | https://github.com/unimorph/sah| Maria Ryskina |
|Tuvan |Turkic | tyv | https://github.com/unimorph/tyv| Maria Ryskina |
|Itelmen |Chukotko-Kamchatkan | itl | https://github.com/unimorph/itl| Karina Mishchenkova, Sofya Ganieva, Matvey Plugaryov |
|Chukchi |Chukotko-Kamchatkan | ckt | https://github.com/unimorph/ckt | Karina Mishchenkova, Maria Ryskina |
|Evenki |Tungusic | evn | https://github.com/unimorph/evn| Elena Klyachko|
|Central Kurdish (Sorani) |Indo-European | ckb | https://github.com/unimorph/ckb| Alexina project  and Ali Salehi |
| Northern Kurdish (Kurmanji) |Indo-European | kmr | https://github.com/unimorph/kmr | Alexina project  |
| Polish | Indo-European | pol | https://github.com/unimorph/pol | Witold Kieraś, Marcin Wolinski |
| Russian | Indo-European | rus | https://github.com/unimorph/rus | Wiktionary |
| Czech | Indo-European | ces | https://github.com/unimorph/ces | Wiktionary|
| Bulgarian | Indo-European | bul | https://github.com/unimorph/bul | Wiktionary |
| German | Indo-European | deu | https://github.com/unimorph/deu | Wiktionary |
| Dutch | Indo-European | nld | https://github.com/unimorph/nld | Wiktionary |
| Spanish | Indo-European | spa | https://github.com/unimorph/spa | Wiktionary |
| Portuguese | Indo-European | por | https://github.com/unimorph/por | Wiktionary |
| Braj | Indo-European | bra | https://github.com/unimorph/bra |Ritesh Kumar |
| Magahi | Indo-European | mag | https://github.com/unimorph/mag | Ritesh Kumar |
| Indonesian | Austronesian| ind | https://github.com/unimorph/ind   | Clara Vania |
| Kodi | Austronesian| kod | https://github.com/unimorph/kod | Yustinus Ghanggo Ate |
| Eibela | Trans–New Guinea | ail | https://github.com/unimorph/ail | Grant Aiton |
| Veps | Uralic | vep | https://github.com/unimorph/vep | Andrew and Natalia Krizhanovsky |
| Karelian | Uralic | krl | https://github.com/unimorph/krl | Andrew and Natalia Krizhanovsky |
| Ludic | Uralic | lud | https://github.com/unimorph/lud | Andrew and Natalia Krizhanovsky |
| Livvi | Uralic | olo | https://github.com/unimorph/olo | Andrew and Natalia Krizhanovsky |


#### Surprise Languages

| Language | Family| code | UM | Annotators  |
|---|---|---|---|---|
|Turkish |Turkic | tur  | https://github.com/unimorph/tur/  | Omer Goldman and Duygu Ataman |
|Xibe* |Tungusic | sjo  | https://github.com/unimorph/sjo/  | Elena Klyachko  |
|Võro |Uralic| vro  | https://github.com/unimorph/vro/  | Ekaterina Vylomova  |

* -- For Xibe you might need to install fonts (Mongolian Baiti, from https://www.manchustudiesgroup.org/typing-manchu/)
### Timeline


**Stage 1: Development Phase**
* ***February 28, 2021***: Training and development splits for development languages released; we invite participants to report errors.
* ***February 28, 2021***: Neural and non-neural baselines for development languages released.
* ***March 7, 2021***: Development language data are frozen.

**Stage 2: Generalization Phase**
* ***~~April 20~~ May 16, 2021***: Training and development splits for surprise languages released.
(This is not a zero-shot learning task. Participants will be given training data for all languages.)

**Stage 3: Evaluation Phase**
* ***~~April 27~~ May 16, 2021***: Test splits for all languages (both development and surprise) released.
* ***~~May 4~~ May 23, 2021***: Participants submit test predictions on all languages.

**Stage 4: Write-up Phase**
* ***June 7, 2021***: Participants’ system description papers due.

### Data

The training and development data are provided in a simple utf-8 encoded text format for both the development and surprise languages. Each line in a file is an example that consists of word forms and corresponding morphosyntactic descriptions (MSDs) provided as a set of features, separated by semicolons. We refer to the MSDs as (morphological) tags for simplicity. The fields on a line are TAB-separated.
The fields are: lemma, target form, tag. Here we present an example from the Akan training data (the Akan verb “bisa” means “to ask” in English):

```
bisa     mmbisa     V;PRS;HAB;NEG
```

In the training data, we give all three fields. In the test phase, we omit field 2.

We will provide varying amounts of labeled training data, depending on the language, to assess models’ ability to generalize to novel forms, in addition to information about each language’s family and sub-family, and WALS features which participants may optionally use. For each language, the possible inflections are taken from a finite set of morphological tags, presented in the UniMorph schema.

### Evaluation


The language generalization evaluation will follow last year's design. We will simultaneously evaluate models for both the Development languages, whose training and development sets will be available for an elongated period of time, and the Surprise languages, whose training and development sets will only be available for a short time prior to submission, which precludes extensive tuning. To be officially ranked, you must submit results for **all** evaluation languages. Thus, to succeed, your class of models (e.g. neural sequence-to-sequence models or weighted finite-state transducers with hand-crafted features) must generalize well to the group of Surprise languages that are typologically distinct from the Development languages you performed model selection on. To repeat: This is not a zero-shot learning task, but rather our evaluation set-up is designed to test the inherent inductive bias in the participants' chosen model class.

We will simultaneously evaluate the accuracy on held-out forms for languages from the following three categories of languages separately: 1) held-out forms from the Development languages, 2) held-out forms from genetically related Surprise languages, and 3) held-out forms from genetically unrelated Surprise languages. This tripartite split should give the field insight into how reliable performance of certain classes of models are on typologically distinct languages.

The human-like generalization part of this shared task will be evaluated based on a morphological inflection system's output correlation with both human plausibility scores and production probabilities. These outputs will be evaluated at multiple data glanuralities. They will be separately evaluated based on wugs which are similar to regular existing words, similar to irregulars, to both, or to neither.

### Submission Instructions 

Please submit your team's results to ryan.cotterell@gmail.com CCing your team mates by May 23rd, 2021. 


### Baselines

The organizers will provide one non-neural and one neural baseline for the participants’ consumption.
Its use is optional and is provided to help the participants develop their own models faster.
The neural baseline is a multilingual transformer ([Vaswani et al., 2017](https://papers.nips.cc/paper/7181-attention-is-all-you-need.pdf)). The version of this model adopted for character-level tasks currently holds the state-of-the-art on the 2017 SIGMORPHON shared task data. The transformer takes the lemma and morphological tags as input and outputs the target inflection. Given the low-resource setup, a single model will be trained on all languages. Additionally, we consider the data augmentation technique used by [Anastasopoulos and Neubig (2019)](https://www.aclweb.org/anthology/D19-1091/) as another baseline.

To run the non-neural baseline use command:
```bash
$ python baselines/nonneural/baseline.py --path part1/development_languages/
```

To run the neural baseline first download and augment [(Anastasopoulos and Neubig, 2019)](https://arxiv.org/abs/1908.05838) the data
```bash
$ mkdir part1/original
$ cp part1/development_languages/* part1/original

$ bash baselines/neural/example/sigmorphon2021-shared-tasks/augment.sh
$ python baselines/neural/example/sigmorphon2021-shared-tasks/task0-build-dataset.py all
```

Then, to run the transducer [(Wu et al, 2021)](https://arxiv.org/abs/2005.10213), one model per language.
```bash
$ bash baselines/neural/example/sigmorphon2021-shared-tasks/task0-launch.sh
```

**Baseline Results** : https://docs.google.com/spreadsheets/d/1n91nUeV72-sGKyQr6-iSO3u39E1Ho9LHSfeYAf7HYxY/edit?usp=sharing


### Organizers
**Task Logistics**: Tiago Pimentel, Brian Leonard, Eleanor Chodroff,  Maria Ryskina, Sabrina Mielke, Garrett Nicolai, Yustinus Ghanggo Ate, Francis Tyers, Edoardo M. Ponti, Niklas Stoehr, Ritesh Kumar, Kairit Sirts, Zoey Liu, Mans Hulden, David Yarowsky, Ryan Cotterell, Ekaterina Vylomova, Ben Ambridge

**Annotators**: Salam Khalifa, Nizar Habash, Charbel El-Khaissi, Omer Goldman, Michael Gasser, William Lane, Matt Coler, Arturo Oncevay, Jaime Rafael Montoya Samame, Gema Celeste Silva Villegas, Zoey Liu, Richard J. Hatcher, Emily Prud'hommeaux, Maria Ryskina, Karina Mishchenkova, Sofya Ganieva, Matvey Plugaryov, Elena Klyachko, Ali Salehi, Andrew and Natalia Krizhanovsky, Ritesh Kumar, Clara Vania, Yustinus Ghanggo Ate, Witold Kieraś, Marcin Wolinski, Totok Suhardijanto, Zahroh Nuriah, Mohit Raj, Shyam Ratan



### References

Anastasopoulos, A. and Neubig, G. (2019) [“Pushing the Limits of Low-Resource Morphological Inflection.”](https://www.aclweb.org/anthology/D19-1091/) Proceedings of EMNLP 2019.

Vaswani, A., Shazeer, N., Parmar, N., Uszkoreit, J., Jones, L., Gomez, A., Kaiser, Ł. and Polosukhin, I. (2007) [“Attention is All You Need.”](https://papers.nips.cc/paper/7181-attention-is-all-you-need.pdf) Proceedings of NeurIPS 2017.



## Part 2: Are We There Yet?<sup>1</sup> A Shared Task on Cognitively Plausible Morphological Inflection

### Task Description
An open question in the use of neural networks for the study of language is to what degree they resemble humans in how they generate language. In the realm of morphology, this question goes back 40 years to the infamous past-tense debate of the 1980s where one camp argued humans use rule-based mechanisms and another argued that humans inflect words with a process closer to neural networks. See Gary Marcus’ book [The Algebraic Mind](https://mitpress.mit.edu/books/algebraic-mind) for an overview or several recent papers in the ACL community on the topic, e.g. [Kirov and Cotterell (2018)](https://arxiv.org/abs/1807.04783), [Corkery et al. (2019)](https://arxiv.org/abs/1906.01280) and [McCurdy et al. (2020)](https://www.aclweb.org/anthology/2020.acl-main.159/).


This shared task adopts the experimental paradigm introduced by [Albright and Hayes (2003)](https://linguistics.ucla.edu/people/hayes/papers/AlbrightHayes2003RulesVsAnalogy.pdf). We have created a large number of new nonce words in four languages: English, German, Dutch and Russian. To the best of our knowledge, this will be the largest and most multilingual collection of nonce words in existence. The goal of the participants in the shared task is to design a model that morphologically inflects the nonce words according to the grammar of the given languages. As an example, consider the following nonce verbs that obey English phonotactics:

+ blad /blæd/
+ crast /kɹæst/
+ flink /flɪŋk/
+ pide /paɪd/
+ sprake /spɹeɪk/

In many cases, there is arguably more than one “correct” way to inflect these verbs according to English grammar because they are unattested. For instance, who is to say that the past tense of “fink” should be “finked” and not “fank”. For that reason, we have elicited human judgements (on [Amazon’s Mechanical Turk](https://www.mturk.com/)) that tell native speakers’ preferences towards specific past tense inflections. The candidate set of potential inflections was generated through a linguist-in-the-loop procedure that made use of the state-of-the-art neural inflector from [Wu et al. (2021)](https://arxiv.org/abs/2005.10213).

### Timeline

* ***February 25, 2021***: Training data for English, German, ~~Portuguese~~ Dutch and Russian are released. In contrast to previous year’s shared tasks, the data are in IPA. We invite participants to report errors.
* ***March 8, 2021***: Neural and non-neural baselines for development languages released.
* ***May 1, 2021***: Development data for nonce inflections are released. (This includes human judgements.)
* ***May 23, 2021***: Test data for the nonce inflections are released. (This excludes human judgements.)
* ***June 1, 2021***: Users submit their system output.
* ***June 7, 2021***: Users submit their system description paper.

### Data and Evaluation

The training data are attested inflections in English, German, Dutch and Russian. You may download them [here](https://github.com/sigmorphon/2021Task0/tree/main/part2). We have also released development sets so all of participants tune their models on the same data. At evaluation time we will release test sets of attested words so we correlate quality of the trained inflectors with performance on the wug data.

The data are in the standard UniMorph triple file format:


<div class="language-plaintext highlighter-rouge">
<div class="highlight">
<pre class="highlight"><code>talk talking V;V.PTCP;PRS</code></pre>
</div>
</div>


In contrast to the example above, the words are encoded in the [International Phonetic Alphabet (IPA)](https://en.wikipedia.org/wiki/International_Phonetic_Alphabet) not in the standard orthography for the given language. This is true for the training, development and test data, even though we present examples here in standard orthography.

The **development data** are in a different format. They are quadruples

````
flink  flinked  V;PST   3.2
flink  flank    V;PST   4.1
flink  flunk    V;PST   1.5
````

where the fourth column is a native-speaker rating on a [Likert scale](https://en.wikipedia.org/wiki/Likert_scale). As stated above, these rankings were given by native speakers on Amazon’s

The task will be evaluated in the following manner. Having trained a model on the training data, the participants are asked to provide model scores for each inflection of the novel word. For instance, if the model is probabilistic (which is not a requirement!), the participants could provide the log-probability of each inflection under their model as the score. To use the example given above, the particpants could provide log p(flinked | flink, V;V.PTCP;PRS), log p(flank | flink, V;V.PTCP;PRS) and log p(flunk | flink, V;V.PTCP;PRS).
For each wug lemma, e.g. "flink", a micro-correlation is computed using ([Spearman's ρ](https://en.wikipedia.org/wiki/Spearman%27s_rank_correlation_coefficient)) between the human judgements and the provided model scores. Then, a macro-average is computed by arithmetically averaging the micro-correlations. Systems will be ranked by the final macro-average.

As an evaluation example, consider the following potential **test entries**:
````
flink  flinked  V;PST
flink  flank    V;PST
flink  flunk    V;PST
````

An hypothetical submitted system output would be:

````
flink  flinked  V;PST   -0.87
flink  flank    V;PST   -0.92
flink  flunk    V;PST   -6.21
````
where the foruth column is the log-probability under the participant's model. The micro-correlation here is ρ=0.5. These per-paradigm micro-correlations would then be arithmetically averaged to produce the final macro-average. The organizers will release an evaluation script for system evaluation along with the development data, which is the first data release where there are human judgements in the TSV.

### Submission Instructions 

Please submit your team's results to ryan.cotterell@gmail.com CCing your team mates by June 1st, 2021. 


### Organizers

* Tiago Pimentel (University of Cambridge)
* Brian Leonard (Brian Leonard Consulting)
* Maria Ryskina (Carnegie Mellon University)
* Sabrina Mielke (Johns Hopkins University)
* Coleman Haley (Johns Hopkins University)
* Eleanor Chodroff (University of York)
* Johann-Mattis List (Max Planck Institute)
* Adina Williams (Facebook AI Research)
* Ryan Cotterell (ETH Zürich; primary contact)
* Ekaterina Vylomova (University of Melbourne)
* Ben Ambridge (University of Liverpool)


### References


Albright, A., and Hayes, B. (2003). [Rules vs. analogy in English past tenses: A computational/experimental study](https://linguistics.ucla.edu/people/hayes/papers/AlbrightHayes2003RulesVsAnalogy.pdf). Cognition, 90(2), 119-161.

Marcus, G. F. (2001). [The Algebraic Mind: Integrating Connectionism and Cognitive Science](https://mitpress.mit.edu/books/algebraic-mind). MIT Press.

Corkery, M., Matusevych, Y., and Goldwater, S. (2019). [Are we there yet? Encoder-decoder neural networks as cognitive models of English past tense inflection](https://arxiv.org/abs/1906.01280). Proceedings of ACL 2019.

Kirov, C. and Cotterell, R. (2018). [Recurrent Neural Networks in Linguistic Theory: Revisiting Pinker and Prince (1988) and the Past Tense Debate](https://arxiv.org/abs/1807.04783). TACL 2018.

Kirov, C., Cotterell, R., Sylak-Glassman, J., Walther, G., Vylomova, E., Xia, P., Faruqui, M., Mielke, S., McCarthy, A., Kübler, S., Yarowsky, D., Eisner, J., and Hulden, M. (2018). [UniMorph 2.0: Universal Morphology](https://arxiv.org/abs/1810.11101). Proceedings of LREC 2018.

McCurdy, K., Goldwater, S., and Lopez, A. (2020). [Inflecting When There’s No Majority: Limitations of Encoder-Decoder Neural Networks as Cognitive Models for German Plurals](https://www.aclweb.org/anthology/2020.acl-main.159/). Proceedings of ACL 2020.

Wu, S., Cotterell, R., and Hulden, M. (2021). [Applying the Transformer to Character-level Transduction](https://arxiv.org/abs/2005.10213). Proceedings of EACL 2021.



<sup>1</sup>Our title is inspired by [Corkery et al. (2019)](https://arxiv.org/abs/1906.01280).

# Participation Policy

We do not tolerate harassment in our shared task. Anyone who has been previously found to have harassed one of the organizers cannot participate in our task in any capacity. There are too few organizers for us to accomodate the harasser in a manner that ensures the safety of their victims. (This policy was written on June 22nd and cannot be applied retroactively, but will be in place for all future iterations of the task.)

