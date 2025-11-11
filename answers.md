# CMPS 6610 Problem Set 04
## Answers

**Name:** Abby Ortego


Place all written answers from `problemset-04.md` here for easier grading.

<br>

- **1d.** There seems to be a somewhat consistent trend. The Huffman coding cost continues to be close to 3/4 of the cost of a Fixed-Length coding. 

    | File | Fixed-Length Coding | Huffman Coding | Huffman vs. Fixed-Length |
    | --- | --- | --- | --- |
    | f1.txt    |         1244            |       826         |       0.66 |
    | alice29.txt    |          919071           |        676374        |     0.74 |
    | asyoulik.txt    |          762022           |        606448        |    0.79 |
    | grammar.lsp    |          23248           |        17356        |       0.75 |
    | fields.c    |         72384            |        56206        |      0.78 |

- **1e.** When Huffman coding is applied to an alphabet where each character has equal frequency the results should be similar to that of a Fixed-Length coding. 
    - Since there is no one character with a higher frequency than the others, the number of bits used to represent them will be the same for all and will be determined with the same formula that Fixed-Length coding uses ($\log_2(k)$ where $k$ is the number of characters in the alphabet) for any document. 

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
    - **Work Analysis**: This method yields $W(n) = O(n)$ due to how the nodes are distributed throughout the tree. 
        - The worst case is a node traversing the entire tree before it found its proper spot and it would take $O(\log n)$ work to do so. This could only happen with one node though, the root. 
        - Using this bottom-up approach, each level would increase the depth a misplaced node may have to travel, but the number of possible nodes that could do this would decrease significantly. 
        - This means the overall amount of work would decrease as well and can be bounded by just $O(n)$ work.

- **2b.**
    - **Span Analysis**: For the proposed method the span would be $S(n) = O(\log n)$.
        - In a binary min-heap each node is indepenent from nodes that reside on the same level and so are their subtrees. 
        - Therefore, the subtrees at each level can be validated at the same time. The method proposed above could just take in a level at a time and execute the `construct_min_heap` at once. 
        - This means the span is just dependent on the number of levels. The number of levels in a binary tree is given by $\log n$ which yields a $O(\log n)$ span.

<br>

- **3a.**
    - To exchange $N$ dollars to the local currency while minimizing the number of coins needed...
        - Let $X$ be the set of possible choices for the number of coins or more precisely, the possible values of $k$, sorted from highest to lowest. Let $N$ be the dollars to exchange for Geometrica's currency.
        - ```python
            def greedy_exchange_dollars(X, N):
                # base cases:
                if N <= 0:  # no more dollars to exchange
                    return 0
                elif len(X) == 1 and X[0] >= N:   # hit smallest denomination, and cannot fit more
                    return 0
                # recursive cases:
                else:
                    if len(X) == 1 and X[0] <= N:     # hit smallest denomination, and can fit more
                        new_N = N-X[0]
                        return 1 + greedy_exchange_dollars(X, new_N)
                    elif X[0] <= N:     # if denomination can fit in N dollars
                        new_N = N-X[0]
                        return 1 + greedy_exchange_dollars(X[1:], new_N)
                    else:
                        return 0 + greedy_exchange_dollars(X[1:], N)
                    #
                #
            # greedy_exchange_dollars

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
        - Suppose, $O$ was not optimal and that some other solution, $O'$, is. 
        - By the greedy choice property proven above, $x$ has to be in the optimal solution so $x \in O'$. But, if $x \in O'$, you get the same remainder as before and the same set of subproblems. 
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
    - In Fortuitio, the denominations could be (1, 3, 5, 6). If we're trying to exchange 8 dollars...
        - The greedy solution is $G = {6, 1, 1}$.
            - Greedy would choose 6, remainder 2
            - Greedy would choose 1, remainder 1
            - Greedy would choose 1, remainder 0
        - The optimal solution is $O = {5, 3}$.
        - The greedy solution uses 3 coins while the optimal solution can be done with 2. 

- **4b.**
    - **Optimal Substructure**: This problem still has optimal substructure since an optimal solution for this problem can be constructed from smaller subproblems.
        - Similar to the proof above, let $X$ equal the set of possible denominations and assume you make an optimal choice, $x \in X$, for which denomination to use. 
        - The optimal solution, $O$, will be made up of $x$ and the optimal solution for the remaining amount of dollars to exchange, $N-x$.
        - Suppose, $O$ was not optimal and that some other solution, $O'$, is. 
        - If $x$ is in the optimal solution, however, it has to be in $O'$. But if $x$ is $O'$, you get the same remainder as before and the same set of subproblems. 
        - Therefore, same as before, $O = O'$ and an optimal solution can be created from the optimal solutions to smaller subproblems.
    - Let $OPT(X, N)$ be the optimal solution (smallest number of coins) for any set of denominations, $X$, and any dollar amount, $N$.
        - The optimal substructure is $OPT(X, N) = \min \{1 + OPT(X[1:], N-X[0]), OPT(X[1:], N)\}$.

- **4c.**
    - Let $X$ be the set of possible choices for the number of coins or more precisely, the possible values of $k$. Let $N$ be the dollars to exchange for Fortuito's currency.
    - ```python
        def dp_exchange_dollars(X, N):
            # base cases:
            if N <= 0:  # no more dollars to exchange
                return 0
            elif len(X) == 1 and X[0] >= N:   # hit smallest denomination, and cannot fit more
                return 0
            # recursive cases:
            else:
                if len(X) == 1 and X[0] <= N:     # hit smallest denomination, and can fit more
                    new_N = N-X[0]
                    return 1 + greedy_exchange_dollars(X, new_N)
                elif X[0] <= N:     # if denomination can fit in N dollars, decide to use that denomination or not
                    new_N = N-X[0]
                    use = 1 + greedy_exchange_dollars(X, new_N)
                    dont_use = 0 + greedy_exchange_dollars(X, N)
                    return min(use, dont_use)
                else:
                    return 0 + greedy_exchange_dollars(X[1:], N)
                #
            #
        # dp_exchange_dollars
    - **Work Analysis**: The work is $O(|X| * N)$
        - The denominations must be sorted by highest to lowest first which takes $O(|X| \log |X|)$ work.
        - If memoization was used, each subproblem would be calculated sequentially in constant time and the two recursive calls could be looked-up. There are $O(|X| * N)$ subproblems so $W(n) = O(|X| * N)$.
        - In total, $W(n) = O((|X|*\log |X|) + (|X|*N)) = O(|X| * N)$, assuming the dollars exchanged would end up exceeding the possible denominations.
    - **Span Analysis**: The span is $O(|X| + N)$
        - Similar to the work, the denominations must be sorted by highest to lowest first which takes $O(\log |X|)$ span. 
        - If memoization was used, each subproblem could be calculated in parallel. The span would then just be the longest sequence of dependent subproblems which is just $|X| + N$, so $S(n) = O(|X| + N)$
        - In total, $S(n) = O(\log |X| + |X| + N) = O(|X| + N)$. 

<br>

- **5a.**  
    - **Optimal Substructure**: Yes, the optimal substructure property still holds for weighted task selection. 
        - Let $A$ be the set of tasks to choose from sorted by the task that finish earliest to latest and assume you make an optimal choice, $a \in A$, for which task to choose.
        - The optimal solution, $O$, will be made up of $a$ and the optimal solution for the remaining tasks to choose from that are not $a$ and do not overlap with $a$. 
        - Suppose, $O$ was not optimal and that some other solution, $O'$, is. 
        - If $a$ is in the optimal solution, however, it has to be in $O'$. But if $a$ is $O'$, you get the same remaining tasks as before and the same set of subproblems since tasks cannot overlap. 
        - Therefore, same as before, $O = O'$ and an optimal solution can be created from the optimal solutions to smaller subproblems.
    - Let $OPT(A)$ be the optimal solution (earliest finishing task with maximum value) for any set of tasks, $A$.
        - The optimal substructure is $OPT(A) = \max \{v(a) + OPT(A'), OPT(A-a)\}$ where $A'$ is the set of tasks that strictly come after $a$. 


- **5b.** No, the greedy criterion does not hold. For the two examples below, let $A$ represent a set of tasks with start time ($s$), finish time ($f$), and value ($v$) such that $A = \{(s_0, f_0, v_0), (s_1, f_1, v_1), ..., (s_i, f_i, v_i)\}$.
    - **Greedy Criteria 1**: Pick the task with the maximum value. 
        - Let $A = \{(s=0, f=2, v=2), (s=2, f=3, v=1), (s=3, f=5, v=2), (s=5, f=7, v=3), (s=0, f=7, v=4)\}$
        - The greedy choice would choose the last task, $(s=0, f=7, v=4)$, which overlaps with all other task allowing for no other choice and yielding a value of 4. 
        - The optimal solution would have been picking the rest of the set since that would yield values $2+1+2+3=8$.
        - Therefore, just picking the task with the maximum value will not work. 
    - **Greedy Criteria 2**: Pick the task that finishes the earliest with the maximum value. 
        - Let $A = \{(s=0, f=2, v=2), (s=0, f=2, v=1), (s=3, f=5, v=1), (s=5, f=7, v=1), (s=0, f=7, v=6)\}$. 
        - The greedy choice would choose $\{(s=0, f=2, v=2), (s=3, f=5, v=1), (s=5, f=7, v=1)\}$.
        - The optimal solution would have been picking the the last task, $(s=0, f=7, v=6)$, since $6 > 2+1+1$. 
        - Therefore, just picking the task that finishes first with the highest value will not work, either. 

- **5c.**
    - Let $A$ be the set of tasks to choose from sorted by earliest finish time. 
        - ```python
            def dp_weighted_task_sel(A):
                # base cases:
                if len(A) == 0:   # no more tasks to choose from
                    return 0
                # recursive cases:
                else:
                    if len(A) > 0:      # there are tasks to choose from
                        our_a = A[0]
                        non_overlap_A = a in A that does not overlap with our_a
                        without_A = A with our_A removed
                        
                        run = our_a["v"] + dp_weighted_task_sel(non_overlap_A)
                        dont_run = 0 + dp_weighted_task_sel(without_A)
                        return max(run, dont_run)
                    #
                #
            # dp_weighted_task_sel
    - **Work Analysis**: The work is $O(n \log n)$
        - The tasks must be sorted by finish time first which takes $O(n \log n)$ work.
        - If memoization was used, each subproblem would be calculated sequentially in constant time and the two recursive calls could be looked-up. There are $O(|A|)$ subproblems so $W(n) = O(|A|) = (n)$. 
        - In total, $W(n) = O(n \log n + n) = O(n \log n)$
    - **Span Analysis**: The span is $O(n)$ 
        - Similar to the work, the tasks must be sorted by finish time first which takes $O(\log n)$ span. 
        - If memoization was used, each subproblem could be calculated in parallel. The span would then just be the longest sequence of dependent subproblems which is just $|A|$, so $S(n) = O(|A|) = O(n)$.
        - In total, $S(n) = O(\log n + n) = O(n)$. 
