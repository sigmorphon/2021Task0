# SIGMORPHON–UniMorph Shared Task on Generalization in Morphological Inflection Generation

SIGMORPHON’s sixth installment of its inflection generation shared task will be divided into two parts: 

+ ***Part 1***: [Generalization Across Typologically Diverse Languages](https://github.com/sigmorphon/2021Task0#part-1-generalization-across-typologically-diverse-languages)
+ ***Part 2***: [Are We There Yet? A Shared Task on Cognitively Plausible Morphological Inflection](https://github.com/sigmorphon/2021Task0#part-2-are-we-there-yet1-a-shared-task-on-cognitively-plausible-morphological-inflection)

Please join our [Google Group](https://groups.google.com/forum/#!forum/sigmorphon2021-sharedtask0/join) to stay up to date.

Click here to [register for the task!](https://forms.gle/tu4tX648F9kA9eps7)


## Part 1: Generalization Across Typologically Diverse Languages


### Task Summary


In this shared task, participants will design a model that learns to generate morphological inflections from a lemma and a set of morphosyntactic features of the target form. Each language in the task has its own training, development, and test splits. Training and development splits contain triples, each consisting of a lemma, a target form, and a set of morphological features, provided in the UniMorph format (the “Data” section below provides an example of input format). Test splits only provide lemmas and morphological tags: your model will need to predict the missing target form.

The model should be general enough to work for natural languages of any typological patterning. For example, Tagalog verbs exhibit [circumfixation](https://en.wikipedia.org/wiki/Circumfix); thus, a model with a strong inductive bias towards suffixing will likely not work well for Tagalog.

The task will be divided in two parts, the first forcuses on the inflection models' generalization across typologically diverse languages, while the second focuses on how human-like their generalization is (i.e. how cognitively plausible their outputs are).


### Task Details
This task will proceed in three phases: the ***Development Phase***, the ***Generalization Phase***, and the ***Evaluation Phase**. As the task progresses, more data and more languages will be released.

In the ***Development Phase***, we will provide training and development splits that should be used to *develop* your system.
We will refer to them as the *development languages*. The list of languages will be announced shortly.

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


### Timeline


**Stage 1: Development Phase**
* ***February 28, 2021***: Training and development splits for development languages released; we invite participants to report errors.
* ***February 28, 2021***: Neural and non-neural baselines for development languages released.
* ***March 6, 2021***: Development language data are frozen. (may be updated.)

**Stage 2: Generalization Phase**
* ***April 20, 2021***: Training and development splits for surprise languages released.
(This is not a zero-shot learning task. Participants will be given training data for all languages.)

**Stage 3: Evaluation Phase**
* ***April 27, 2021***: Test splits for all languages (both development and surprise) released.
* ***May 4, 2021***: Participants submit test predictions on all languages.

**Stage 4: Write-up Phase**
* ***May 8, 2021***: Participants’ system description papers due.
* ***May 15, 2021***: Participants’ system description papers camera ready due.


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


### Baselines

The organizers will provide one neural baseline for the participants’ consumption.
Its use is optional and is provided to help the participants develop their own models faster.
This baseline is a multilingual transformer ([Vaswani et al., 2017](https://papers.nips.cc/paper/7181-attention-is-all-you-need.pdf)). The version of this model adopted for character-level tasks currently holds the state-of-the-art on the 2017 SIGMORPHON shared task data. The transformer takes the lemma and morphological tags as input and outputs the target inflection. Given the low-resource setup, a single model will be trained on all languages. Additionally, we consider the data augmentation technique used by [Anastasopoulos and Neubig (2019)](https://www.aclweb.org/anthology/D19-1091/) as another baseline.

### References

Anastasopoulos and Neubig. [“Pushing the Limits of Low-Resource Morphological Inflection.”](https://www.aclweb.org/anthology/D19-1091/) Proceedings of EMNLP 2019.

Vaswani et al. [“Attention is All You Need.”](https://papers.nips.cc/paper/7181-attention-is-all-you-need.pdf) Proceedings of NeurIPS 2017.



## Part 2: Are We There Yet?<sup>1</sup> A Shared Task on Cognitively Plausible Morphological Inflection

### Task Description
An open question in the use of neural networks for the study of language is to what degree they resemble human-like language production. In the realm of morphology, this question goes back 40 years to the infamous past-tense debate of the 1980s where one camp argued humans use rule-based mechanisms and another argued that humans inflect words with a process closer to neural networks. See Gary Marcus’ book [The Algebraic Mind](https://mitpress.mit.edu/books/algebraic-mind) for an overview or several recent papers in the ACL community on the topic, e.g. [Kirov and Cotterell (2018)](https://arxiv.org/abs/1807.04783), [Corkery et al. (2019)](https://arxiv.org/abs/1906.01280) and [McCurdy et al. (2020)](https://www.aclweb.org/anthology/2020.acl-main.159/). 


This shared task adopts the experimental paradigm introduced by [Albright and Hayes (2003)](https://linguistics.ucla.edu/people/hayes/papers/AlbrightHayes2003RulesVsAnalogy.pdf). In four languages (English, German, Portuguese and Russian) we have created a large number of new nonce words. To the best of our knowledge, this will be the largest and most multilingual collection of nonce words in existence. The goal of the participants in the shared task is to design a model that morphologically inflects the nonce words according to the grammar of the given languages. As an example, consider the following nonce verbs that obey English phonotactics:

+ blad /blæd/
+ crast /kɹæst/
+ flink /flɪŋk/
+ pide /paɪd/
+ sprake /spɹeɪk/

In many cases, there is arguably more than one “correct” way to inflect these verbs according to English grammar because they are unattested. For instance, who is to say that the past tense of “fink” should be “finked” and not “fank”. For that reason, we have elicited human judgements (on [Amazon’s Mechanical Turk](https://www.mturk.com/) that tell native speakers’ preferences towards specific past tense inflections. The candidate set of potential inflections were generated through a linguist-in-the-loop procedure that made use of the state-of-the-art neural inflector from [Wu et al. (2021)](https://arxiv.org/abs/2005.10213). 

### Timeline

* ***February 25th, 2021***: Training data for English, German, Portuguese and Russian are released. In contrast to previous year’s shared tasks, the data are in IPA. We invite participants to report errors.
* ***March 8th, 2021***: Neural and non-neural baselines for development languages released.
* ***May 1st, 2021***: Development data for nonce inflections are released. (This includes human judgements.)
* ***May 23rd, 2021***: Test data for the nonce inflections are released. (This includes human judgements.)
* ***June 1th, 2021***: Users submit their system output.
* ***June 7th, 2021***: Users submit their system description paper. 

### Data

The training data are attested inflections in four languages (English, German, Portuguese and Russian) in. You may download them [here](https://github.com/sigmorphon/2021Task0/tree/main/part2). The data are in the standard UniMorph triple file format:


<div class="language-plaintext highlighter-rouge">
<div class="highlight">
<pre class="highlight"><code>talk talking V;V.PTCP;PRS</code></pre>
</div>
</div>


In contrast to the example above, the words are encoded in the [International Phonetic Alphabet (IPA)](https://en.wikipedia.org/wiki/International_Phonetic_Alphabet) not in the standard orthography for the given language. 

The **development** and **test data** are in a different format. They are quadruples 

````
fink  finked  V;PST   3.2
fink  fank    V;PST   4.1
fink  funk    V;PST   1.5
````

where the fourth column is a native-speaker rating on a [Likert scale](https://en.wikipedia.org/wiki/Likert_scale). As stated above, these rankings were given by native speakers on Amazon’s Mechanical Turk. 

### Evaluation

The task is evaluated in the following manner. Having trained a model on the training data, the participants are asked to provide scores for each inflection of the novel word. For instance, if the model is probabilistic (which is not a requirement!), the participants are asked to provide -log(finking | fink, V;V.PTCP;PRS) and -log(fank | fink, V;V.PTCP;PRS) for the examples above.
For each wug lemma a micro-correlation is computed ([Spearman's ρ](https://en.wikipedia.org/wiki/Spearman%27s_rank_correlation_coefficient)). Then, a macro-average is computed by averaging the micro-correlations. Systems will be ranked by the final macro-average. A script will be provided for system evaluation. 

### Organizers

* Tiago Pimentel (University of Cambridge) 
* Brian Leonard (Brian Leonard Consulting)
* Maria Ryskina (Carnegie Mellon University)
* Sabrina Mielke (Johns Hopkins University)
* Eleanor Chodroff (University of York)
* Ryan Cotterell (ETH Zürich)
* Ekaterina Vylomova (University of Melbourne)
* Ben Ambridge (University of Liverpool)


### References


Albright, A., & Hayes, B. (2003). [Rules vs. analogy in English past tenses: A computational/experimental study](https://linguistics.ucla.edu/people/hayes/papers/AlbrightHayes2003RulesVsAnalogy.pdf). Cognition, 90(2), 119-161.

Marcus, G. F. (2001). [The Algebraic Mind: Integrating Connectionism and Cognitive Science](https://mitpress.mit.edu/books/algebraic-mind). MIT Press.

Corkery, M., Matusevych, Y., & Goldwater, S. (2019). [Corkery et al. (2019)](https://arxiv.org/abs/1906.01280). Proceedings of ACL 2019.

Kirov, C. and Cotterell, R. (2018). [Recurrent Neural Networks in Linguistic Theory: Revisiting Pinker and Prince (1988) and the Past Tense Debate](https://arxiv.org/abs/1807.04783). TACL 2018. 

Kirov, C., Cotterell, R., Sylak-Glassman, J., Walther, G., Vylomova, E., Xia, P., Faruqui, M., Mielke, S., McCarthy, A., Kübler, S., Yarowsky, D., Eisner, J., and Hulden, M. (2018). [UniMorph 2.0: Universal Morphology](https://arxiv.org/abs/1810.11101). Proceedings of LREC 2018. 

McCurdy, K., Goldwater, S., and Lopez, A. (2020). [Inflecting When There’s No Majority: Limitations of Encoder-Decoder Neural Networks as Cognitive Models for German Plurals](https://www.aclweb.org/anthology/2020.acl-main.159/). Proceedings of ACL 2020.

Wu, S., Cotterell, R., and Hulden, M. (2021). [Applying the Transformer to Character-level Transduction](https://arxiv.org/abs/2005.10213). Proceedings of EACL 2021.



<sup>1</sup>Our title is inspired by [Corkery et al. (2019)](https://arxiv.org/abs/1906.01280).

