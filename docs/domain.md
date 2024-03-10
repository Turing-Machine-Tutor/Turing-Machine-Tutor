# Formal languages

An **alphabet** $\Sigma$ is a finite collection of elements called **characters**. A character does not have to be represented by a single character in a computer - for example, the alphabet $\Sigma=\{ a,b,a',b' \}$ may be represented by the strings `"a", "b", "a'", "b'"` - notice the last two are represented by two computer characters each.

A **word** $w$ over $\Sigma$ is a possibly-empty finite sequence of characters from $\Sigma$, and its size is denoted $|w|$. The set of all possible words over $\Sigma$ is denoted $\Sigma^*$. The empty word is denoted $\varepsilon$

A **language** $L$ over $\Sigma$ is a subset of the collection of possible words: $L\subseteq \Sigma^*$. 

# Turing machines

A Turing machine is a model that "runs" over words in $\Sigma^*$. It consists of:

*  $\Sigma$ - the input alphabet
* $B$ a blank character that is not in $\Sigma$.
* $\Gamma$ a tape alphabet, such that $\Gamma \supseteq \Sigma \uplus \{ B \}$
* $Q$ a set of states
* $q_0\in Q$ an initial state
* $q_{acc}, q_{rej}\in Q$ distinct states that are called accepting and rejecting. Collectively, these two are called the terminal states, and the rest are called non-terminal states.
* A transition function $\delta: \;\; (Q/\{ q_{acc},q_{rej} \})\times \Gamma \;\; \rightarrow \;Q\times \Gamma \times \{  L, R,S\}\\$

A **configuration** of a Turing machine is a triplet of a tape, a head position, and a state.

A **tape** is a sequence of cells that can contain letters of $\Gamma$ that has a left end but is infinite on the right, such that exists some cell that has a $B$ on it and every cell right of it also has a $B$ on it. In that way, we can say that the word written on the tape $w$ is the sequence of letters from $\Gamma$ until the point from which there is only $B$.

The **head position** is a position on the tape.

The **state** is a state $q\in Q$.

A **configuration** can also be represented as a triplet $(w_L, q, w_R)$ where $w=w_Lw_R$ , with $w_L$ is the word up to and including the position of the head, and $w_R$ is the rest of the word.

**The initial configuration** of a run of the machine over $w$ is $(\varepsilon, q_0, w)$. That is, the tape has $w$ written on it, the state is $q_0$ and the head position is in the left end.

The transition function defines what is the next configuration for each non-terminal configuration. A terminal configuration is such that the state is final.

A run of the machine over a word $w$ is a series of configurations that starts with the initial configuration and is updated by $\delta$ until a terminal one is found. If the series is finite and reaches a terminal configuration, then the machine **halts** over $w$. In that scenario, the machine either **accepts** or **rejects** the word, depending on whether the state is $q_{acc}$ or $q_{rej}$.

The **language** of a machine is the set $L$ of words it accepts. The machine is then said to **accept** $L$ (also: semi-decide). The language $L$ is then said to be semi-decidable. The set of languages that have a Turing machine that accepts them is denoted $RE$.

If for every $w\notin L$ the machine *rejects* the word, then the machine is also said to **decide** L. The set of languages that have a Turing machine that decides them is denoted $R$ (decidable languages).

This project only concerns languages in $R$. Languages in $RE/R$ or not in $RE$ do not interest us in this project.

