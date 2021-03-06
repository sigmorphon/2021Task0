# Task0: SIGMORPHON–UniMorph Shared Task on Generalization in Morphological Inflection Generation

SIGMORPHON’s sixth installment of its inflection generation shared task focuses on two aspects: (a) generalization across typologically diverse languages;  (b) cognitive plausibility of morphological inflection systems.

Please join our [Google Group](https://groups.google.com/forum/#!forum/sigmorphon2021-sharedtask0/join) to stay up to date.

[Register for the task!](https://forms.gle/tu4tX648F9kA9eps7)

## Shared Task Description

In this shared task, participants will design a model that learns to generate morphological inflections from a lemma and a set of morphosyntactic features of the target form. Each language in the task has its own training, development, and test splits. Training and development splits contain triples, each consisting of a lemma, a target form, and a set of morphological features, provided in the UniMorph format (the “Data” section below provides an example of input format). Test splits only provide lemmas and morphological tags: your model will need to predict the missing target form.

The model should be general enough to work for natural languages of any typological patterning. For example, Tagalog verbs exhibit [circumfixation](https://en.wikipedia.org/wiki/Circumfix); thus, a model with a strong inductive bias towards suffixing will likely not work well for Tagalog.

The task will be divided in two parts, the first forcuses on the inflection models' generalization across typologically diverse languages, while the second focuses on how human-like their generalization is (i.e. how cognitively plausible their outputs are).

### Part 1: Generalization across Languages

This task will proceed in three phases: a Development Phase, a Generalization Phase, and an Evaluation Phase. As the task progresses, more data and more languages will be released.

In the Development Phase, we will provide training and development splits that should be used to *develop* your system.
We will refer to them as the *development languages*. The list of languages will be announced shortly.

In the Generalization Phase, we will provide training and development splits for new languages where approximately half are genetically related (belong to the same family) and half are genetically *unrelated* (are isolates or belong to a different family) to the development languages. We will keep the languages in the Generalization Phase a surprise until April 2021. We will also keep the genetically unrelated language *families* a surprise, though some languages will come from the same families as those in the Development Phase.

In the Evaluation Phase, the participants’ models will be evaluated on held-out forms from all of the languages from the previous phases. The languages from the Development Phase and the Generalization Phase are evaluated simultaneously. The only difference is that there has been more time to construct a model for those languages released in the Development Phase. It follows that a model could easily overfit to or favor phenomena that are more frequent in languages presented in the Development Phase, especially if parameters are shared across languages. For instance, a model based on the morphological patterning of the Indo-European languages may end up with a bias towards suffixing and will struggle to learn prefixing or circumfixation, the degree to which only becomes apparent during experimentation on other languages whose inflectional morphology patterns differ. Of course, the model architecture itself could explicitly or implicitly favor certain word formation types (suffixing, prefixing, etc.).

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
|Itelmen |Chukotko-Kamchatkan | itl | https://github.com/unimorph/itl| Karina Mischenkova, Maria Ryskina | 
|Chukchi |Chukotko-Kamchatkan | ckt | https://github.com/unimorph/ckt | Karina Mischenkova, Maria Ryskina | 
|Evenki |Tungusic | evn | https://github.com/unimorph/evn| Elena Klyachko|
|Central Kurdish (Sorani) |Indo-European | ckb | https://github.com/unimorph/ckb| Ali Salehi | 
| Southern Kurdish (Kurdiy Xwarîn) |Indo-European | sdh | https://github.com/unimorph/sdh | Ali Salehi | 
| Polish | Indo-European | pol | https://github.com/unimorph/pol | Witold Kieraś, Marcin Wolinski | 
| Russian | Indo-European | rus | https://github.com/unimorph/rus | Wiktionary | 
| Czech | Indo-European | ces | https://github.com/unimorph/ces | Wiktionary| 
| Braj | Indo-European | bra | https://github.com/unimorph/bra |Ritesh Kumar | 
| Magahi | Indo-European | mag | https://github.com/unimorph/mag | Ritesh Kumar | 
| Indonesian | Austronesian| ind | https://github.com/unimorph/ind   | Clara Vania | 
| Kodi | Austronesian| kod | https://github.com/unimorph/kod | Yustinus Ghanggo Ate | 
| Eibela | Trans–New Guinea | ail | https://github.com/unimorph/ail | Grant Aiton |
| Veps | Uralic | vep | https://github.com/unimorph/vep | Andrew and Natalia Krizhanovsky | 
| Karelian | Uralic | krl | https://github.com/unimorph/krl | Andrew and Natalia Krizhanovsky | 
| Ludic | Uralic | lud | https://github.com/unimorph/lud | Andrew and Natalia Krizhanovsky | 
| Livvi | Uralic | olo | https://github.com/unimorph/olo | Andrew and Natalia Krizhanovsky | 

Organizers: Tiago Pimentel, Brian Leonard, Eleanor Chodroff,  Maria Ryskina, Sabrina Mielke, Garrett Nicolai, Yustinus Ghanggo Ate, Francis Tyers, Edoardo M. Ponti, Niklas Stoehr, Ritesh Kumar, Kairit Sirts, Zoey Liu, Mans Hulden, David Yarowsky, Ryan Cotterell, Ekaterina Vylomova, Ben Ambridge

Annotators: Salam Khalifa, Nizar Habash, Charbel El-Khaissi, Omer Goldman, Michael Gasser, William Lane, Matt Coler, Arturo Oncevay, Jaime Rafael Montoya Samame, Gema Celeste Silva Villegas, Zoey Liu, Richard J. Hatcher, Emily Prud'hommeaux, Maria Ryskina, Karina Mischenkova, Elena Klyachko, Ali Salehi, Andrew and Natalia Krizhanovsky, Ritesh Kumar, Clara Vania, Yustinus Ghanggo Ate, Witold Kieraś, Marcin Wolinski, Totok Suhardijanto, Zahroh Nuriah, Mohit Raj, Shyam Ratan



### Part 2: Human-like Generalization

We selected four high resource languages for this task with varying degrees of morphological complexity: English, German, Portuguese, and Russian.
Systems will be trained on real words from these languages on the task of morphological inflection, but will then be evaluated on a selection of wug wordforms --- they will be compared to both human plausibility judgements and productions.

For training models, we provide participants with inflection data from [UniMorph](https://unimorph.github.io/).
The training data has been converted into phonemes and is composed of <lemma, inflected_form, inflection_tags> triples.

The evaluation will be conducted on a new set of wug word forms.
Wugs were generated in each language so as to cover a diverse subset of the language’s phonotactic space.
The steps to generate these wugs were:
1. Transduce Unimorph’s word lists into IPA using the baseline encoder-decoder from SIGMORPHON 2020 task 1 (https://github.com/sigmorphon/2020/tree/master/task1/baselines/encoder-decoder) , filtering out any word whose 'concept' has a zipf frequency of 3 or lower using the wordfreq package(https://doi.org/10.5281/zenodo.1443582)
2. Choose a tagset in the given language that is likely to be irregular, e.g. V;PST in English or N;ACC;PL for German.
3. Train an LSTM on each language, conditioning it on the inflection tag.
4. Sample new wug lemmas from the LSTM, removing already existing word forms.
5. Subsample a diverse set of wugs based on their likelihood to be irregular, lexical neighborhood, and phonotactic probability (this step relies on several factors and will be described in detail at a later point).
6. Train a neural transducer on IPA UniMorph.
7. Generate inflections for chosen wugs.

We then presented inflections to a group of native speakers to get plausibility judgements, while we asked another group to inflect the lemmas directly to get production probabilities. We will later release a subset of this wug data so participants can validate their systems with them.


## Timeline
(Estimated Dates)

**Stage 1: Development Phase**
* February TBA, 2021: Training and development splits for development languages released; we invite participants to report errors.
* February TBA, 2021: Neural and non-neural baselines for development languages released.
* March 1, 2021: Development language data are frozen.

**Stage 2: Generalization Phase**
* April 20, 2021: Training and development splits for surprise languages released.
(This is not a zero-shot learning task. Participants will be given training data for all languages.)

**Stage 3: Evaluation Phase**
* April 27, 2021: Test splits for all languages (both development and surprise) released.
* May 4, 2021: Participants submit test predictions on all languages.


**Stage 4: Write-up Phase**
* May 8, 2021: Participants’ system description papers due.
* May 15, 2021: Participants’ system description papers camera ready due.


## Data
The training and development data are provided in a simple utf-8 encoded text format for both the development and surprise languages. Each line in a file is an example that consists of word forms and corresponding morphosyntactic descriptions (MSDs) provided as a set of features, separated by semicolons. We refer to the MSDs as (morphological) tags for simplicity. The fields on a line are TAB-separated.
The fields are: lemma, target form, tag. Here we present an example from the Akan training data (the Akan verb “bisa” means “to ask” in English):

```
bisa     mmbisa     V;PRS;HAB;NEG
```

In the training data, we give all three fields. In the test phase, we omit field 2.

We will provide varying amounts of labeled training data, depending on the language, to assess models’ ability to generalize to novel forms, in addition to information about each language’s family and sub-family, and WALS features which participants may optionally use. For each language, the possible inflections are taken from a finite set of morphological tags, presented in the UniMorph schema.



## Evaluation

The language generalization evaluation will follow last year's design. We will simultaneously evaluate models for both the Development languages, whose training and development sets will be available for an elongated period of time, and the Surprise languages, whose training and development sets will only be available for a short time prior to submission, which precludes extensive tuning. To be officially ranked, you must submit results for **all** evaluation languages. Thus, to succeed, your class of models (e.g. neural sequence-to-sequence models or weighted finite-state transducers with hand-crafted features) must generalize well to the group of Surprise languages that are typologically distinct from the Development languages you performed model selection on. To repeat: This is not a zero-shot learning task, but rather our evaluation set-up is designed to test the inherent inductive bias in the participants' chosen model class.

We will simultaneously evaluate the accuracy on held-out forms for languages from the following three categories of languages separately: 1) held-out forms from the Development languages, 2) held-out forms from genetically related Surprise languages, and 3) held-out forms from genetically unrelated Surprise languages. This tripartite split should give the field insight into how reliable performance of certain classes of models are on typologically distinct languages.

The human-like generalization part of this shared task will be evaluated based on a morphological inflection system's output correlation with both human plausibility scores and production probabilities. These outputs will be evaluated at multiple data glanuralities. They will be separately evaluated based on wugs which are similar to regular existing words, similar to irregulars, to both, or to neither.


## Baselines

The organizers will provide one neural baseline for the participants’ consumption.
Its use is optional and is provided to help the participants develop their own models faster.
This baseline is a multilingual transformer ([Vaswani et al., 2017](https://papers.nips.cc/paper/7181-attention-is-all-you-need.pdf)). The version of this model adopted for character-level tasks currently holds the state-of-the-art on the 2017 SIGMORPHON shared task data. The transformer takes the lemma and morphological tags as input and outputs the target inflection. Given the low-resource setup, a single model will be trained on all languages. Additionally, we consider the data augmentation technique used by [Anastasopoulos and Neubig (2019)](https://www.aclweb.org/anthology/D19-1091/) as another baseline.

## References

Anastasopoulos and Neubig. [“Pushing the Limits of Low-Resource Morphological Inflection.”](https://www.aclweb.org/anthology/D19-1091/) Proceedings of EMNLP 2019.

Vaswani et al. [“Attention is All You Need.”](https://papers.nips.cc/paper/7181-attention-is-all-you-need.pdf) Proceedings of NeurIPS 2017.
