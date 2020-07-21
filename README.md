# Comparison of ASR systems and their robustness given noise

Automatic speech recognition (ASR) systems come in varying levels of performance. An issue of special importance is their robustness given noisy input—while most ASR systems now handle 'clean' input admirably, they easily 'break' with noise.

The goal of this project is to compare the performance of commercially available and open-source ASR systems under noise. I evaluate five ASR systems: **Mozilla DeepSpeech**, **Amazon Transcribe**, **Microsoft Azure**, **IBM Watson**, and **Google Cloud Text-to-Speech**.

**Datasets**: LibriSpeech for speech, MUSAN for noise

**Methodology**:

* Preprocessing
* Noise addition
* Feed-in
* Evaluation

## Preprocessing

## Noise addition

## Feed-in

## Evaluation

I evaluate the performance of the ASR systems by taking the Levenshtein distance of the output from groundtruth. I report both the absolute percent error rate and the percent change from the *noiseless* to the *noisy* condition.