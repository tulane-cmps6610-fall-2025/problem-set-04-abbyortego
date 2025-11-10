# CMPS 6610 Problem Set 04
## Answers

**Name:** Abby Ortego


Place all written answers from `problemset-04.md` here for easier grading.

<br>

- **1d.**

| File | Fixed-Length Coding | Huffman Coding | Huffman vs. Fixed-Length |
| --- | --- | --- | --- |
| f1.txt    |         1244            |       826         |       0.66 |
| alice29.txt    |          919071           |        676374        |     0.74 |
| asyoulik.txt    |          762022           |        606448        |    0.79 |
| grammar.lsp    |          23248           |        17356        |       0.75 |
| fields.c    |         72384            |        56206        |      0.78 |

There seems to be a somewhat consistent trend. The Huffman coding cost continues to be close to 3/4 of the cost of a Fixed-Length coding.  

- **1e.**
When Huffman coding is applied to an alphabet where each character has equal frequency the results should be similar to that of a Fixed-Length coding. Since there is no one character with a higher frequency than the others, the number of bits used to represent them will be the same for all and will be determined with the same formula that Fixed-Length coding uses ($\log_2(k)$ where $k$ is the number of characters in the alphabet) for any document. 

<br>

- **2a.**
    - If we assume A is already a representation of an almost complete binary tree, where each each level is filled left to right by the order of A's indicies, then all that's left is for it to satisfy the heap property. 
        - This can be done by growing a subtree starting from the bottom, the leaves or the end of the array, and swapping out the root when it violates the heap property (aka the root is larger than its children).
        - If swapped, the subtree where the root is the new value would also need to be recursed on until it satisifies the heap property as well.
    - ```python
        for idx in range(A, -1, -1):
            A = construct_min_heap(A, idx)
        #

        def construct_min_heap(A, idx):
            # get children of A[idx]
            l_child_idx = 2*A[idx] + 1
            r_child_idx = 2*A[idx] + 2

            if l_child_idx >= len(A) and r_child_idx >= len(A):     # looking at a leaf, satifies heap prop
                return A
            elif l_child_idx < len(A) and r_child_idx >= len(A):    # looking at bottom-most subtree, might satisy heap prop
                # pick minimum of the two to be new root
                if A[idx] > A[l_child_idx]:
                    swap A[idx] with A[l_child_idx]
                    return A    # no recursion since we're at the bottom, not needed
                else:
                    return A
                #
            elif A[idx] < A[l_child_idx] and A[idx] < A[r_child_idx]:   # looking at a subtree, satifies heap prop
                return A
            else:   # looking at a subtree, does not satisfy heap prop
                min_idx = idx 
                # pick minimum of the three to be new root
                if A[min_idx] > A[l_child_idx]:
                    min_idx = l_child_idx 
                elif A[min_idx] > A[r_child_idx]:
                    min_idx = r_child_idx
                #

                swap A[min_idx] with A[idx]

                # recurse on subtree with new root (where the other one used to be)
                return construct_min_heap(A, min_idx)
            #
        # construct_min_heap
        ```
    - *Work Analysis*: This method yields $W(n) = O(n)$ due to how the nodes are distributed throughout the tree. 
        - The worst case is a node traversing the entire tree before it found its proper spot and it would take $O(\log n)$ work to do so. This could only happen with one node though, the root. 
        - Using this bottom-up approach, each level would increase the depth a misplaced node may have to travel, but the number of possible nodes that could do this would decrease significantly. 
        - This means the overall amount of work would decrease as well and can be bounded by just $O(n)$ work.

- **2b.**
    - *Span Analysis*: For the proposed method the span would be $S(n) = O(\log n)$.
        - In a binary min-heap each node is indepenent from nodes that reside on the same level and so are their subtrees. 
        - Therefore, the subtrees at each level can be validated at the same time. The method proposed above could just take in a level at a time and execute the `construct_min_heap` at once. 
        - This means the span is just dependent on the number of levels. The number of levels in a binary tree is given by $\log n$ which yields a $O(\log n)$ span.

<br>

- **3a.**
    - To exchange $N$ dollars to the local currency while minimizing the number of coins needed...
        - Let $X$ be the set of possible choices for the number of coins or more precisely, the possible values of $k$. Initialize the solution, $S$, to be empty. 
        - Select $x \in X$ that minimizes $N-2^x$ where $N-2^x \geq 0$ since you cannot get anymore coins without dollars. 
        - Update the solution, $S$, to include $x$, and remove $x$ from the set of possible choices, $X$.
        - Repeat with the new set of possible choices, $X'$, and the new $N$ value, $N-2^x$. 

- **3b.**
    - **Greedy Choice**: The value $x$ with the smallest remainder of $N-2^x$ where $N-2^x \geq 0$ is in the optimal solution.
        - There are $k$ denominations raised to the power of 2. Let $O$ be the optimal solution and $G$ be the greedy solution. 
        - Let $i$ be the choice of $k$ that yields the smallest remainder, $N-2^i$. 
        - Suppose $i \not\in O$. Instead, some other choice of $k$, $j$, is in $O$ and yields a smaller remainder, $N-2^j$. 
        - Now, this means the remainder of choice $i$ is larger than that of choice $j$
            - $N-2^i \geq N-2^j$. 
            - $-2^i \geq -2^j$
            - $2^i \leq 2^j$
        - So, $2^i \leq 2^j$ which means $j$ is larger than $i$. However, $i$ was the largest choice that satisfied $N-2^x \geq 0$ meaning that any choice, like $j$, that is larger than $i$ would yield a remainder, $N-2^x < 0$. 
        - This does not adhere to our greedy choice and is a contradiction. Thus the choice $i$ is in the optimal solution, $O$.
    - **Optimal Substructure**: Let the greedy choice, the value $x$ with the smallest remainder of $N-2^x$ where $N-2^x \geq 0$, be in the optimal solution, $O$. 
        - Then, $O$ contains the greedy choice $x$ and the greedy choice for the remainder, $N-2^x$.
        - Suppose, $O$ was not optimal and that some other solution, $O'$ is. 
        - By the greedy choice property proven above, $x$ has to be in the optimal solution so $x \in O$. But, if $x \in O$, you get the same remainder at before and the same set of subproblems. 
        - Therefore, $O = O'$ and an optimal solution can be created from the optimal solutions to smaller subproblems.

- **3c.**
    - **Work Analysis**: The work is $O(n \log n)$.
        - First, the set of denominations would be sorted highest to lowest which would take $O(n \log n)$ work. 
        - Then, each denominaiton, $k$, would be considered, adding it to the solution if $N-2^k \leq 0$ which would take $O(n)$ work. 
        - This yields the grand total $W(n) = O(n \log n + n) = O(n \log n)$.
    - **Span Analysis**: The span is $O(n)$. 
        - Sorting with an unlimited number of processors takes $O(\log n)$.
        - However, like above, each denomination would have to be considered, costing $O(n)$. 
        - This yields the grand total $S(n) = O(\log n + n) = O(n)$.

<br>

- **4a.**



- **4b.**




- **4c.**


- **5a.**



- **5b.**




- **5c.**
