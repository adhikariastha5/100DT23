Some Takeover from the machine translation algorithm I learned today:
1. To convert a sentence in one language to another, you need to first of all summarize the sentence of one language, then this summary can be translated to another language.
2. Two summarization: abstract and extractive. Extractive means extracting same sentences and abstract means forming new sentences using past sentences.
3. Next is how Sequence2Sequence model actually works using LSTM for both encoder and decoder.
4. There is training as well as inference phase involved in Encoder-Decoder architecture.
5. In the encoder for training phase, first of all the inputs are given which eventually gives out the summary. This reads entire input sequence. But in each timestep, one word is fed into the encoder. They capture contextual information present in input sequence.
6. Hidden state and cell state of last time step are used to initialize the decoder. Decoder also reads the entire sequence word-by-word and predicts the same sequence. There are < start> and < end> special tokens added to target before feeding it into the decoder.
7. Inference phase is the one in which a model after training is fed with new data or unknown. This works by encoding entire sequence and initialize decoder by internal states of encoder.< start> as input to decoder. Run for states and output will be next word probability. The one with maximum probability will be selected. Repeat the steps by updating internal states until it reach max < end>.

8. Limitation of this Seq2Seq is if the words or reviews are long, to memorize this long is not possible. So its limites for short sequences only.
9. So there comes attention Mechanism. The intution behind this is how much attention we must pay to each word in input sequence. So here rather than reading all the words, it only selects those which have more emphasis.

These are just my readings. More to come for maths and codes in attention mechanism.
