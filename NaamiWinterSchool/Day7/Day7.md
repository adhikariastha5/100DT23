# NLP by Asutosh Modi
- Communication with machines: gives rise to NLP. Computational technique to analyze and understand language.
- app like pers assist like siri,alexa. Dearch engine like Google,Bing.

- why nlp is hard? #almost 60 years back but not succeed.
- challenge that language is complex.
- just by change of one word meaning changes completely
- language is ambiguous, syntatic,semantic.
- language evolves not static. Usage of words changes plus slang or mixup languages like hinglish..
- language is challenging. Poems,sarcasm.

- NLP Pipeline
- input text,segment text into sentence,want to tokenize(word level),pos tagging,lemmatization,syntatic parsing(grammar associated with grammar),parse and extract rules(dobj,nsubj and root or verb----->depended parsing), another step is Named Entity Recognition(NER)(helps to build knowledge graph), coreference resolution(It and so on...what is it refering to),q/a,sent analysis,then to model then in higher nlp task.

- Sequence Models
- language is sequential, sentences are composed of words in a sequence, eg POS tag,NER,Speech Recognition.
- HMM,.... ---> sequence models

- HMM(Hidden Markov Model)
- consider POS tag
- step 1: select a part of speech category
- step 2: based on pos select word
- step 3: select next category and go on from step 2
- 3 question: Learning Problem: Decoding Problem: Likelihood problem(estimate parameter distrib...)
- Supervised Learning(given observed text and then a pos tag)
- graphical model (probability with graph). Start state then go to next step, go on and on until you reach the stop. start prob (y1,y0) and we have end prob, transition,ambission probability.
- Markov Property ---> yi you are and in condition to all previous state we have, last two state also, if we become huge it becomes complex so people only use first order.
- another assump is independence, only depend on the hidden state which generate this word not before or after word.
- another is homogenity, the transition,ambition propertyu remains same, it does not change over time.
- joint distribution (words generated along with hidden layer) start stop club the transition and ambition together ---> probability of each.

- Learning Problem: we would do maximum likehood distribution. we find out the p init then Ptrans, Pemiss, Pfina and so on (convert to log domain rather than only probability since it becomes too low and round off cretaes a problem)
- Decoding Problem: we wnat to do pos tagging, Posterior decodeing: every step you generate most liking(context is a problem---> loosing context; not optimum by doing 1 by 1 not as a whole), Viterbi decoding:
- bayes, marginal(throat property) take all possib value and add them together
- independence: Joint probability and y1 is independent to all others...
- Trellis Diagram: 
- So problem is: overall all possible sequences is in the denominator. k to the power N , just for 1 sentence we do more than 10 million. That's why this approach is not good. Its complexity is exponential.
- dynamic probability:: divide prob into sub prob and store it so it lavarises the problem.
- forward probability: marginalized then condition probability with bayes, now apply bayes rule again for second term, independece on first and second term. Then we get the equation of emission and transition. for stop we get p(x) since one term is always stop so it has prob 1.
- brute force approach. from k state you get information. we consider previous state too. We reduce complexity. Tackle exponential large programs
- In backward we go reverse of forward. Start from stop, prob of observing xi from 1 to xn. 
- we have emission from end then transit to forward state.
- we do marginal with y+1 then we apply bayes rule then again bayes rule, then independence
- Need to play with these slides and formulas to know more
- backward(0,start) is p(x) since you start from start only then its always 1.
- p(x)-forward(n+1,stop)
- backward(0,start)=p(x)
- same probability both
- if we have both forw, back together then we take product of both forw and back and add to get the result.

- Decoding Problem: find less possible state
- Posterior decoding into forward and backward. We apply bayes rule firstly then bayes rule again then we get forw and back.
- take some database and implement in forward and backward and so on.
- viterbi decoding trans multiply with viterbi then emmision. Difference here is we are taking max.
- backward pass is keeping things in buffer when doing backward pass.

- Likelihood Problem: p(x) is forw, back then product it
- every step p(x) is same , so it can be used as debugging. If we do not have pos tag for many like hidden layer(annotator).

- Unsupervised Seq Modeling
- Expectation Maximization(EM) algorithm
- Jurasics book ....look

- Dependency Parsing
- Parsing is tring to get syntax of language.
- Book recommended ( see the slide)
- Dependency grammar: words are related to each other via binary relations called dependency relations. labels directed graph. nodes--> words
- for every head word we have a root word which tells this sentence is trying to convey.
- useful in ambiguous resolving.

- Constituent Parsing
- based on context free grammar rules. Use this rules to form a sentence.
- Given sent with words graph to labeled graph
- relation are predifined, nodes are weights,arcs are cardisian product of nodes relation
- if wi to wj we cannot have reverse - constraint
- only one relation, another not allowed - constraint
- basically set of all node set: spanning node set. Projective, non-projective dependency
- language that have free order like neplai , sanskrit have non-projective dependancy
- dp approaches: grammar, data driven, hybrid
- grammar(formal)---> context-free, constraints-based
- data driven---> unsup,sup(based on finite state), sup ----> transition based and graph based
- dependency parsing model has set of constraints,set of parameters, parsing algorithm.
- computational problems: Learning problem, parsing problem.
- Transition based system, we transit from initial state go to different state and get to the final state.
- Sentence configuration
- transition based parsing, apply on config and give config.
- transition in shift reduce parsing
- left arc transit---> stack of words, buffer with words, (stack should not be empty)top word from the stack, take head r from buffer and put it in relation. relation of h of buffer and top of stack
- right transit---> stack take out the top,put in the head of the buffer and combine with head of the buffer and put into relation
- shift transition, put head of buffer to top of the stack
- (visualize---imp)
- we need kind of oracle in order to perform deterministic parsing. Oracle gives nice transition. Apply oracle to do operation. (in constraint time, like linear alagebra)
- difficult to get oracles in real time. So we need ML.
- we want to learn mapping from transition to racle. For each transition each classifier tell what to do.
- take features from this connfiguration... many possible vectors. feature predict the transition.
- how do we derive the treebanks? Tken lot of text,annotated, make dependency tree known as tree bank.
- we need dataset that takes feature vector along with transition. We need interiem transition data.
- sentences alnong with dependency map. Given configuration, we need to predict what we desire? , config features and the transitions.
- look at tree, and guess what that leads to training set.
- how do we represent this feature. m-dim feature vector. DEsign template, give feature and get feature vector.
- based on attributes of words or tree nodes, and are identified by their pos in config.
- mannualy created these features. Time consuming is the feature part in NLP.
- neural dependency parser, use word embeddings for words,pos tag, arc labels...we donot have to define feature.. so it is much easier.
- refer to paper
- evaluated matrics(UAS)
- label Attention layer,hpsg,xlnet

# Topics in NLP: Word Embeddings, Sequencs models, Attention and Dialogues systems by Suresh Manandhar
- autoencoder in language: In NLP,They have almost no 0 elements in embedding
- Cluster the words in context so they can give the meaning . This is word embedding
- compute the vector of words along aside of words left right.(5 to left and 5 to 5 to left and then put it into dictionary to make massive product)
- we use condn probability by just counting. Pointwise mutual inf, insensitive to direction. Positively shifted PMI.
- vocabulary avoid stop words and normalize it.
- lang have property, from one word we see smth related to context that is narrow eg. resturant we see food, menu... 
- cosine similarity, k-l divergence, without any label data we can find the similarity.
- high dim probability have issue and poorly generalise
- count the sililar words in corpus and increase its counting 
- VSM for words, 
- we can create lot of task that require sematic interpretation.
- See slide for eg The dog ---- the cat(high frequency is chases)
- Predict next word.
- unrelated, contradicts,entail 
- +ve and -ve data set, to train world embedding
- initialize weights randomly to each words ... feed to neural network and then predict the correct output and from back propgation we again continue the network unless some criteria is reached.
- transfer learning: word2Vec ::: words itself, context words, randomly generated context words, each word embedded with 2 different meaning, one as target word one as context word. So we assosciate with the pairs.
- skip gram embeddings:: probability maximize and then again minimize. (likelihood)
- meaning of w and c to be high, context word guessing what word will it be.(assume w and c tog prob is same as context and word embedding; intialized randomly)
- derivative -----look through in the slide(H/W)
- Stochastic gradient descent algorithm
- directional similarity like china to beijing and so on.
- low dim projection of this high dimensional.
- analaogy between words: woman -man is same as queen-king
- skipgram embeddings (high dim and generate 2 low dim matrix)
- Omer levvy, word embedding metrics and context. (approx to represent fact)
- It is shifted by global constant k
- word replace with vector, push through machine learning representation. Encapsulate
- problem that length is not same 
- sum the vector divide by sentence(average)
- sentence level class. Apect based sentiment analysis.
- Subjectivity classification.
- word2vec take the cnn

- Sequence modeling:: popular is rnn. POS is seqm modeling task.
- NER does comb of 'New York' as a tag.
- we have a single cell, with single set of parameter. This is known as unrolling of RNN.If we update 1, it updates everywhere.
- we have inp, output and hidden output  which is the latent or memory which is passed to the next cell(or next input). Parameters same so it is called recurrent.
- we sum up the weights and inputs  and activation and softmax 
- as model increases it becomes complex and memory becomes a problem.(robust mechanism for storing long term sensitive information; sequences)
- LSTM- self state, hidden state, input gate,....
- It has got 2 memories, how much previous cell state to forget is decided by forget gate. It has some value so it define vector for most. 
- Then pass to tanh which scle through it, -1 to 1 range and it decides how much inf to be propagated by input gate, modified cell gate. Then this inf pass through sigmoid then again tanh and then it gets tweeted. (need to see)
- gru they have many sigmoid joined together. Efficiency(look through it)
- character embedding are not semantic but it is trainable. It has shown accurate result.
- Embedding table is less so download our model.(in slide)(read this paper)
- Encoder/Decoder has 2 LSTM.
- input whole input sentence and end with whole nepali sentence for eg.

- If sequence becomes more long, packing all inf becomes hard, we human being translate easily do not remember after doing it. Only some bits so we can use that for some training nn.
- In attention we use decoder which only depends on some part of encoder.
- output from decoder and take similarity with encoder, and measure how imp this word is and this we feed to softmax and then it gives probability or weights, and is multiplied with hidden layer itself.

- machine translation system-blue score(look at n grams and no of truth betn ground truth and words). So better is to rate.
- they collected data, look at db and provide ans, example is the time and event....
- retrieve right one to get from db, they need not look to knowledge base but for some part they need to.
- key value knowledge base concatenate the value. We then finally take key-value and create embedding table in memory.
- look the dialogue and replace values with keys.
- we don't care about values, we replace with keys and then train with it.
- treat knowledge based and things added then create attenuate. decoder gets corresponding values.
- we have keys as a sum of many keys. We have keys and previous hidden. Standard 2 layer network.
- this vj together with the yt,ot then with softmax create a single probability. We treat as if encoder has output(like extra inputs and rest is just standard), In vocabulary dimension we have extra dimension. output 101 we get 8 p.m. and so on.
- to accomodate add knowledhe based we make like extention of vocabulary, then our new vocab is 1k.. this is dynamic as it is changing dynamically.......


- 

