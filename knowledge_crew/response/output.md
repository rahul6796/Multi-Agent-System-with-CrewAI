# Scoring Functions Used in the Paper

The paper discusses various scoring functions crucial for estimating the likelihood of answers predicted by language models. Below is the summary of different scoring functions mentioned:

* **Direct Method**
  - Describes the conditional probability of candidate answers based on the model’s vocabulary.
  - The answer with the highest probability is selected.
  - Restriction: Requires answer tokens to be positioned at the end of input sequences.

* **Perplexity (PPL)**
  - Computes the perplexity of the entire input sequence that combines demonstration examples, input queries, and candidate labels.
  - More flexible than the Direct method as it does not restrict token positions.
  - It requires additional computation time.

* **Channel Model**
  - Estimates the likelihood of an input query given the label, computing the conditional probability in reverse.
  - Particularly useful under imbalanced data situations.
  
* **Summary Table of Scoring Functions**
  - **Efficiency, Coverage, Stability** metrics are assessed, each with qualitative evaluations.
  
| **Method** | **Target**                          | **Efficiency** | **Coverage** | **Stability** |
|------------|-------------------------------------|----------------|--------------|---------------|
| Direct     | M(yj | C, x)                       | +++            | +            | +             |
| PPL        | PPL(Sj)                            | +              | +++          | +             |
| Channel    | M(x | C, yj)                      | +              | +            | ++            |

* **Key Insights**
  - Direct and PPL methods are sensitive to the demonstration surface.
  - There is limited research on calibrating bias and mitigating sensitivity through scoring strategies.
  - The choice of scoring function has implications on template design and performance metrics.

* **Conclusion**
  - The scoring function serves as a bridge between model predictions and the final answer estimation, influencing the overall performance of the in-context learning methodology.