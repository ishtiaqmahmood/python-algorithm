# Python Data Structures and Algorithms

A comprehensive collection of 120+ professional, PEP 8-compliant implementations of fundamental and advanced data structures and algorithms in Python.

## Table of Contents

- [Data Structures](#data-structures)
  - [Linked Lists](#linked-lists)
  - [Stacks](#stacks)
  - [Queues](#queues)
  - [Trees](#trees)
  - [Heaps](#heaps)
  - [Hash Tables](#hash-tables)
  - [Disjoint Set](#disjoint-set)
  - [Trie](#trie)
- [Algorithms](#algorithms)
  - [Recursion](#recursion)
  - [Search](#search)
  - [Sort](#sort)
  - [Graphs](#graphs)
  - [Dynamic Programming](#dynamic-programming)
  - [Greedy](#greedy)
  - [Backtracking](#backtracking)
  - [Strings](#strings)
  - [Bit Manipulation](#bit-manipulation)
  - [Math](#math)

## Data Structures

### Linked Lists
- **Singly Linked List**: Basic implementation.
- **Doubly Linked List**: Bidirectional links.
- **Circular Singly Linked List**: Last node points to head.
- **Circular Doubly Linked List**: Circular and bidirectional.
- **Cycle Detection**: Floyd's Cycle-Finding Algorithm.
- **Reverse Linked List**: Iterative reversal.

### Stacks
- **Stack (List-based)**: Built-in list.
- **Stack (Linked List-based)**: Linked list structure.
- **Limited Stack**: Fixed capacity.
- **Min Stack**: O(1) minimum retrieval.

### Queues
- **Queue (Linked List-based)**: Efficient operations.
- **Circular Queue**: Fixed-capacity circular buffer.
- **Queue using Stacks**: Queue implementation using two stacks.
- **Stack using Queues**: Stack implementation using a queue.
- **Deque**: Double-ended queue implementation.

### Trees
- **Binary Tree**: Fundamental binary tree with traversals.
- **Binary Search Tree (BST)**: Efficient search/insert/delete.
- **AVL Tree**: Self-balancing BST.
- **Red-Black Tree**: Balanced BST (insertion).
- **Segment Tree**: Range sum queries and updates.
- **Fenwick Tree**: Binary Indexed Tree for prefix sums.

### Heaps
- **Binary Heap**: Min and Max Heaps.
- **Priority Queue**: Implementation using `heapq`.

### Hash Tables
- **Linear Probing**: Collision resolution via linear search.
- **Chaining**: Collision resolution via linked lists.
- **Bloom Filter**: Probabilistic data structure for set membership.

### Disjoint Set
- **DSU**: Basic Union-Find.
- **DSU Path Compression**: Optimized with path compression and union by rank.

### Trie
- **Trie Implementation**: Prefix tree for string operations.

## Algorithms

### Graphs
- **BFS/DFS**: Fundamental traversals.
- **Dijkstra's Algorithm**: Shortest path in weighted graphs.
- **Bellman-Ford**: Shortest path with negative weights.
- **Floyd-Warshall**: All-pairs shortest paths.
- **Topological Sort**: Ordering of DAG vertices.
- **Cycle Detection**: Directed and Undirected graphs.
- **Bridges & Articulation Points**: Graph connectivity.
- **Strongly Connected Components**: Kosaraju's and Tarjan's algorithms.

### Dynamic Programming
- **Fibonacci**: Memoization and Tabulation.
- **LCS/LIS**: Longest Common/Increasing Subsequence.
- **Knapsack**: 0/1 Knapsack problem.
- **Edit Distance**: Minimum edit operations.
- **Coin Change**: Minimum coins for amount.
- **Matrix Chain Multiplication**: Optimal multiplication order.
- **Rod Cutting**: Maximum value from cutting a rod.
- **Egg Dropping**: Minimum trials for critical floor.
- **Word Break**: Segmenting strings into words.
- **Max Subarray Sum**: Kadane's Algorithm.
- **Min Path Sum**: Minimal path in grid.
- **Unique Paths**: Counting grid paths.
- **Subset Sum**: Checking for subset with target sum.
- **Partition Equal Subset Sum**: Splitting list into equal sum subsets.
- **Palindromes**: Longest palindromic substring/subsequence.
- **Wildcard/Regex Matching**: Pattern matching implementations.

### Greedy
- **Fractional Knapsack**: Greedy knapsack.
- **Activity Selection**: Non-overlapping activities.
- **Huffman Coding**: Data compression.
- **Job Sequencing**: Max profit with deadlines.
- **Prim's/Kruskal's**: Minimum Spanning Tree.
- **Gas Station**: Circuit completion.
- **Lemonade Change**: Greedy change providing.
- **Min Platforms**: Minimum platforms for trains.
- **Police and Thieves**: Catching maximum thieves.

### Backtracking
- **N-Queens**: Placing N queens on a board.
- **Sudoku Solver**: Solving 9x9 Sudoku.
- **Rat in a Maze**: Pathfinding in a maze.
- **Permutations/Combinations**: Generating all arrangements.
- **Subset Generation**: Power set creation.
- **M-Coloring**: Graph coloring.
- **Hamiltonian Path**: Visiting all vertices once.
- **Knight's Tour**: Knight visiting all board squares.
- **Word Search**: Finding words in a character grid.

### Strings
- **Pattern Matching**: KMP, Rabin-Karp, Z-Algorithm, Naive.
- **Manipulation**: Reversal, Anagrams, Palindrome check.
- **Common Prefix**: Longest prefix among strings.
- **Compression**: Basic string compression.
- **Group Anagrams**: Categorizing anagrams.

### Bit Manipulation
- **Basics**: Set bits count, Power of two, Odd/Even check.
- **Problems**: Single number, Reverse bits, Sum of two integers.
- **Range AND**: Bitwise AND of range.
- **Hamming Distance**: Bit difference.
- **Counting Bits**: Bits for 0 to n.
- **Subsets**: Generating subsets via bitmasking.

### Math
- **Primes**: Sieve of Eratosthenes, Prime check, Prime factorization.
- **Number Theory**: GCD, LCM, Divisors.
- **Properties**: Perfect, Armstrong, Palindrome numbers.
- **Calculations**: Fast exponentiation, Square root.

## How to Run

Most files include a `if __name__ == "__main__":` block with example usage. You can run any script directly using Python:

```bash
python3 sort/merge_sort.py
python3 graph/graph.py
python3 dynamic_programming/knapsack_01.py
```

## License

This project is open-source and available under the [MIT License](LICENSE).


## Recently Added Algorithms

- **Combination Sum**: `backtracking/combination_sum.py`
- **Combination Sum Ii**: `backtracking/combination_sum_ii.py`
- **Combination Sum Iii**: `backtracking/combination_sum_iii.py`
- **Combinations**: `backtracking/combinations.py`
- **Hamiltonian Path**: `backtracking/hamiltonian_path.py`
- **Knight Tour**: `backtracking/knight_tour.py`
- **M Coloring**: `backtracking/m_coloring.py`
- **N Queens**: `backtracking/n_queens.py`
- **N Queens Optimized**: `backtracking/n_queens_optimized.py`
- **Palindrome Partitioning Backtracking**: `backtracking/palindrome_partitioning_backtracking.py`
- **Permutations**: `backtracking/permutations.py`
- **Permutations Ii**: `backtracking/permutations_ii.py`
- **Rat In Maze**: `backtracking/rat_in_maze.py`
- **Restore Ip Addresses**: `backtracking/restore_ip_addresses.py`
- **Subset Generation**: `backtracking/subset_generation.py`
- **Sudoku Solver**: `backtracking/sudoku_solver.py`
- **Sudoku Solver Optimized**: `backtracking/sudoku_solver_optimized.py`
- **Word Search**: `backtracking/word_search.py`
- **Binary Watch**: `bit_manipulation/binary_watch.py`
- **Bitwise And Range**: `bit_manipulation/bitwise_and_range.py`
- **Check Odd Even**: `bit_manipulation/check_odd_even.py`
- **Count Set Bits**: `bit_manipulation/count_set_bits.py`
- **Counting Bits**: `bit_manipulation/counting_bits.py`
- **Divide Integers**: `bit_manipulation/divide_integers.py`
- **Hamming Distance**: `bit_manipulation/hamming_distance.py`
- **Power Of Four**: `bit_manipulation/power_of_four.py`
- **Power Of Two**: `bit_manipulation/power_of_two.py`
- **Reverse Bits**: `bit_manipulation/reverse_bits.py`
- **Single Number**: `bit_manipulation/single_number.py`
- **Single Number Ii**: `bit_manipulation/single_number_ii.py`
- **Single Number Iii**: `bit_manipulation/single_number_iii.py`
- **Subsets Bitmasking**: `bit_manipulation/subsets_bitmasking.py`
- **Sum Of Two Integers**: `bit_manipulation/sum_of_two_integers.py`
- **Total Hamming Distance**: `bit_manipulation/total_hamming_distance.py`
- **Circular Buffer**: `data_structures/circular_buffer.py`
- **Disjoint Set Union By Size**: `data_structures/disjoint_set_union_by_size.py`
- **Fenwick Tree 2D**: `data_structures/fenwick_tree_2d.py`
- **Monotonic Queue**: `data_structures/monotonic_queue.py`
- **Monotonic Stack**: `data_structures/monotonic_stack.py`
- **Persistent Stack**: `data_structures/persistent_stack.py`
- **Randomized Set**: `data_structures/randomized_set.py`
- **Sparse Table**: `data_structures/sparse_table.py`
- **Boolean Parenthesization**: `dynamic_programming/boolean_parenthesization.py`
- **Burst Balloons**: `dynamic_programming/burst_balloons.py`
- **Coin Change**: `dynamic_programming/coin_change.py`
- **Count Subsets Sum**: `dynamic_programming/count_subsets_sum.py`
- **Dice Roll**: `dynamic_programming/dice_roll.py`
- **Edit Distance**: `dynamic_programming/edit_distance.py`
- **Egg Dropping**: `dynamic_programming/egg_dropping.py`
- **Fibonacci Memoization**: `dynamic_programming/fibonacci_memoization.py`
- **Fibonacci Tabulation**: `dynamic_programming/fibonacci_tabulation.py`
- **Frog Jump**: `dynamic_programming/frog_jump.py`
- **House Robber Ii**: `dynamic_programming/house_robber_ii.py`
- **Interleaving String Dp**: `dynamic_programming/interleaving_string_dp.py`
- **Job Scheduling Dp**: `dynamic_programming/job_scheduling_dp.py`
- **Knapsack 01**: `dynamic_programming/knapsack_01.py`
- **Knight Probability**: `dynamic_programming/knight_probability.py`
- **Largest Divisible Subset**: `dynamic_programming/largest_divisible_subset.py`
- **Longest Arithmetic Subseq**: `dynamic_programming/longest_arithmetic_subseq.py`
- **Longest Common Subsequence**: `dynamic_programming/longest_common_subsequence.py`
- **Longest Common Substring**: `dynamic_programming/longest_common_substring.py`
- **Longest Palindromic Subsequence**: `dynamic_programming/longest_palindromic_subsequence.py`
- **Longest Palindromic Substring**: `dynamic_programming/longest_palindromic_substring.py`
- **Matrix Chain Multiplication**: `dynamic_programming/matrix_chain_multiplication.py`
- **Max Sum 3 Subarrays**: `dynamic_programming/max_sum_3_subarrays.py`
- **Min Cost Climbing**: `dynamic_programming/min_cost_climbing.py`
- **Min Cost Merge Stones**: `dynamic_programming/min_cost_merge_stones.py`
- **Min Difficulty Job Schedule**: `dynamic_programming/min_difficulty_job_schedule.py`
- **Min Swaps Increasing**: `dynamic_programming/min_swaps_increasing.py`
- **New 21 Game**: `dynamic_programming/new_21_game.py`
- **Optimal Bst**: `dynamic_programming/optimal_bst.py`
- **Palindrome Partitioning**: `dynamic_programming/palindrome_partitioning.py`
- **Palindrome Partitioning Iii**: `dynamic_programming/palindrome_partitioning_iii.py`
- **Partition Equal Subset Sum**: `dynamic_programming/partition_equal_subset_sum.py`
- **Perfect Squares**: `dynamic_programming/perfect_squares.py`
- **Predict Winner**: `dynamic_programming/predict_winner.py`
- **Race Car**: `dynamic_programming/race_car.py`
- **Regular Expression Matching**: `dynamic_programming/regular_expression_matching.py`
- **Rod Cutting**: `dynamic_programming/rod_cutting.py`
- **Shopping Offers**: `dynamic_programming/shopping_offers.py`
- **Stock I**: `dynamic_programming/stock_i.py`
- **Stock Ii**: `dynamic_programming/stock_ii.py`
- **Subset Sum**: `dynamic_programming/subset_sum.py`
- **Super Egg Drop**: `dynamic_programming/super_egg_drop.py`
- **Triangle Path**: `dynamic_programming/triangle_path.py`
- **Unique Paths**: `dynamic_programming/unique_paths.py`
- **Wild Card Matching**: `dynamic_programming/wild_card_matching.py`
- **Word Break**: `dynamic_programming/word_break.py`
- **Word Break Ii**: `dynamic_programming/word_break_ii.py`
- **A Star**: `graph/a_star.py`
- **All Pairs Shortest Paths Matrix**: `graph/all_pairs_shortest_paths_matrix.py`
- **Articulation Points**: `graph/articulation_points.py`
- **Bellman Ford**: `graph/bellman_ford.py`
- **Bfs**: `graph/bfs.py`
- **Biconnected Components**: `graph/biconnected_components.py`
- **Boruvkas Algorithm**: `graph/boruvkas_algorithm.py`
- **Bridges In Graph**: `graph/bridges_in_graph.py`
- **Bron Kerbosch**: `graph/bron_kerbosch.py`
- **Cycle Detection Directed**: `graph/cycle_detection_directed.py`
- **Cycle Detection Undirected**: `graph/cycle_detection_undirected.py`
- **Dfs**: `graph/dfs.py`
- **Dijkstra Sssp**: `graph/dijkstra_sssp.py`
- **Edmonds Karp**: `graph/edmonds_karp.py`
- **Floyd Warshall**: `graph/floyd_warshall.py`
- **Ford Fulkerson**: `graph/ford_fulkerson.py`
- **Gale Shapley**: `graph/gale_shapley.py`
- **Graph**: `graph/graph.py`
- **Graph Center**: `graph/graph_center.py`
- **Graph Diameter**: `graph/graph_diameter.py`
- **Hierholzer**: `graph/hierholzer.py`
- **Hopcroft Karp**: `graph/hopcroft_karp.py`
- **Is Planar**: `graph/is_planar.py`
- **Johnsons Algorithm**: `graph/johnsons_algorithm.py`
- **Kahns Algorithm**: `graph/kahns_algorithm.py`
- **Kosaraju Scc**: `graph/kosaraju_scc.py`
- **Lca Binary Lifting**: `graph/lca_binary_lifting.py`
- **Lca Rmq**: `graph/lca_rmq.py`
- **Max Bipartite Matching**: `graph/max_bipartite_matching.py`
- **Max Independent Set**: `graph/max_independent_set.py`
- **Mcmf**: `graph/mcmf.py`
- **Min Cut**: `graph/min_cut.py`
- **Min Vertex Cover**: `graph/min_vertex_cover.py`
- **Push Relabel**: `graph/push_relabel.py`
- **Sssp**: `graph/sssp.py`
- **Tarjan Scc**: `graph/tarjan_scc.py`
- **Topological Sort**: `graph/topological_sort.py`
- **Tree Isomorphism**: `graph/tree_isomorphism.py`
- **Tsp Dp**: `graph/tsp_dp.py`
- **Two Sat**: `graph/two_sat.py`
- **Add Two Nums**: `linked_list/add_two_nums.py`
- **Add Two Nums Ii**: `linked_list/add_two_nums_ii.py`
- **Circular Doubly Linked List**: `linked_list/circular_doubly_linked_list.py`
- **Circular Singly Linked List**: `linked_list/circular_singly_linked_list.py`
- **Copy List Random**: `linked_list/copy_list_random.py`
- **Delete Node**: `linked_list/delete_node.py`
- **Detect Cycle Linked List**: `linked_list/detect_cycle_linked_list.py`
- **Dll Cycle**: `linked_list/dll_cycle.py`
- **Doubly Linked List**: `linked_list/doubly_linked_list.py`
- **Doubly Linked List Ops**: `linked_list/doubly_linked_list_ops.py`
- **Flatten Iterator**: `linked_list/flatten_iterator.py`
- **Flatten Multilevel Dll**: `linked_list/flatten_multilevel_dll.py`
- **Insertion Sort Ll**: `linked_list/insertion_sort_ll.py`
- **Intersection Ll**: `linked_list/intersection_ll.py`
- **Ll Cycle Ii**: `linked_list/ll_cycle_ii.py`
- **Merge Sorted Ll**: `linked_list/merge_sorted_ll.py`
- **Mid Ll**: `linked_list/mid_ll.py`
- **Odd Even Ll**: `linked_list/odd_even_ll.py`
- **Palindrome Ll**: `linked_list/palindrome_ll.py`
- **Partition Ll**: `linked_list/partition_ll.py`
- **Remove Dup Sorted**: `linked_list/remove_dup_sorted.py`
- **Remove Dup Sorted Ii**: `linked_list/remove_dup_sorted_ii.py`
- **Remove Nth Node**: `linked_list/remove_nth_node.py`
- **Reorder Ll**: `linked_list/reorder_ll.py`
- **Reverse K Group**: `linked_list/reverse_k_group.py`
- **Reverse Linked List**: `linked_list/reverse_linked_list.py`
- **Rotate Ll**: `linked_list/rotate_ll.py`
- **Self Organizing Ll**: `linked_list/self_organizing_ll.py`
- **Singly Linked List**: `linked_list/singly_linked_list.py`
- **Skip List**: `linked_list/skip_list.py`
- **Sort Ll**: `linked_list/sort_ll.py`
- **Split Ll Parts**: `linked_list/split_ll_parts.py`
- **Swap Nodes Pairs**: `linked_list/swap_nodes_pairs.py`
- **Add Binary**: `math/add_binary.py`
- **Area Of Polygon**: `math/area_of_polygon.py`
- **Armstrong Number**: `math/armstrong_number.py`
- **Automorphic Number**: `math/automorphic_number.py`
- **Bell Numbers**: `math/bell_numbers.py`
- **Catalan Numbers**: `math/catalan_numbers.py`
- **Check Prime**: `math/check_prime.py`
- **Chinese Remainder Theorem**: `math/chinese_remainder_theorem.py`
- **Collatz Conjecture**: `math/collatz_conjecture.py`
- **Distance Formulas**: `math/distance_formulas.py`
- **Euler Number**: `math/euler_number.py`
- **Euler Totient**: `math/euler_totient.py`
- **Extended Euclidean**: `math/extended_euclidean.py`
- **Fast Exponentiation**: `math/fast_exponentiation.py`
- **Fft**: `math/fft.py`
- **Fibonacci Closed Form**: `math/fibonacci_closed_form.py`
- **Find Divisors**: `math/find_divisors.py`
- **Fraction To Decimal**: `math/fraction_to_decimal.py`
- **Goldbach Conjecture**: `math/goldbach_conjecture.py`
- **Gray Code Math**: `math/gray_code_math.py`
- **Hamming Weight**: `math/hamming_weight.py`
- **Happy Number**: `math/happy_number.py`
- **Harshad Number**: `math/harshad_number.py`
- **Integer To Roman**: `math/integer_to_roman.py`
- **Kaprekar Constant**: `math/kaprekar_constant.py`
- **Karatsuba**: `math/karatsuba.py`
- **Line Intersection**: `math/line_intersection.py`
- **Linear Diophantine**: `math/linear_diophantine.py`
- **Lucas Theorem**: `math/lucas_theorem.py`
- **Miller Rabin**: `math/miller_rabin.py`
- **Modular Exponentiation**: `math/modular_exponentiation.py`
- **Modular Inverse**: `math/modular_inverse.py`
- **Multiply Strings**: `math/multiply_strings.py`
- **Palindrome Number**: `math/palindrome_number.py`
- **Pascals Triangle**: `math/pascals_triangle.py`
- **Perfect Number**: `math/perfect_number.py`
- **Perfect Square**: `math/perfect_square.py`
- **Pi Calculation**: `math/pi_calculation.py`
- **Point In Polygon**: `math/point_in_polygon.py`
- **Pollards Rho**: `math/pollards_rho.py`
- **Power Of Four**: `math/power_of_four.py`
- **Power Of Three**: `math/power_of_three.py`
- **Prime Factorization**: `math/prime_factorization.py`
- **Rectangle Overlap**: `math/rectangle_overlap.py`
- **Roman To Integer**: `math/roman_to_integer.py`
- **Segmented Sieve**: `math/segmented_sieve.py`
- **Self Dividing Numbers**: `math/self_dividing_numbers.py`
- **Sieve Of Eratosthenes**: `math/sieve_of_eratosthenes.py`
- **Sum Of Squares**: `math/sum_of_squares.py`
- **Valid Number**: `math/valid_number.py`
- **Volume Formulas**: `math/volume_formulas.py`
- **Wilsons Theorem**: `math/wilsons_theorem.py`
- **Gradient Descent**: `ml/gradient_descent.py`
- **Kmeans**: `ml/kmeans.py`
- **Knn**: `ml/knn.py`
- **Linear Regression**: `ml/linear_regression.py`
- **Logistic Regression**: `ml/logistic_regression.py`
- **Naive Bayes**: `ml/naive_bayes.py`
- **Factorial**: `recursion/factorial.py`
- **Fibonacci**: `recursion/fibonacci.py`
- **Gcd**: `recursion/gcd.py`
- **Power Of Num**: `recursion/power_of_num.py`
- **Tower Of Hanoi**: `recursion/tower_of_hanoi.py`
- **Binary Search**: `search/binary_search.py`
- **Fibonacci Search**: `search/fibonacci_search.py`
- **Interpolation Search**: `search/interpolation_search.py`
- **Jump Search**: `search/jump_search.py`
- **Linear Search**: `search/linear_search.py`
- **Ternary Search**: `search/ternary_search.py`
- **Bitonic Sort**: `sort/bitonic_sort.py`
- **Bogo Sort**: `sort/bogo_sort.py`
- **Bubble Sort**: `sort/bubble_sort.py`
- **Bucket Sort**: `sort/bucket_sort.py`
- **Comb Sort**: `sort/comb_sort.py`
- **Counting Sort**: `sort/counting_sort.py`
- **Cycle Sort**: `sort/cycle_sort.py`
- **Gnome Sort**: `sort/gnome_sort.py`
- **Insertion Sort**: `sort/insertion_sort.py`
- **Merge Sort**: `sort/merge_sort.py`
- **Pancake Sort**: `sort/pancake_sort.py`
- **Quick Sort**: `sort/quick_sort.py`
- **Radix Sort**: `sort/radix_sort.py`
- **Selection Sort**: `sort/selection_sort.py`
- **Shell Sort**: `sort/shell_sort.py`
- **Tim Sort**: `sort/tim_sort.py`
- **Aho Corasick**: `strings/aho_corasick.py`
- **Anagram Check**: `strings/anagram_check.py`
- **Basic Calculator**: `strings/basic_calculator.py`
- **Bwt**: `strings/bwt.py`
- **Count And Say**: `strings/count_and_say.py`
- **Decode String**: `strings/decode_string.py`
- **Distinct Subsequences**: `strings/distinct_subsequences.py`
- **Group Anagrams**: `strings/group_anagrams.py`
- **Group Shifted Strings**: `strings/group_shifted_strings.py`
- **Horspool**: `strings/horspool.py`
- **Interleaving String**: `strings/interleaving_string.py`
- **Isomorphic Strings**: `strings/isomorphic_strings.py`
- **Itoa**: `strings/itoa.py`
- **Jaro Winkler**: `strings/jaro_winkler.py`
- **Knuth Morris Pratt**: `strings/knuth_morris_pratt.py`
- **Lcp Array**: `strings/lcp_array.py`
- **Length Of Last Word**: `strings/length_of_last_word.py`
- **Levenshtein Distance**: `strings/levenshtein_distance.py`
- **Long Common Prefix**: `strings/long_common_prefix.py`
- **Longest Substring No Repeat**: `strings/longest_substring_no_repeat.py`
- **Longest Valid Parentheses**: `strings/longest_valid_parentheses.py`
- **Manachers Algorithm**: `strings/manachers_algorithm.py`
- **Metaphone**: `strings/metaphone.py`
- **Min Window Substring**: `strings/min_window_substring.py`
- **Naive Pattern Matching**: `strings/naive_pattern_matching.py`
- **Palindrome Pairs**: `strings/palindrome_pairs.py`
- **Palindromic Substrings**: `strings/palindromic_substrings.py`
- **Rabin Karp**: `strings/rabin_karp.py`
- **Repeated Dna**: `strings/repeated_dna.py`
- **Restore Ip**: `strings/restore_ip.py`
- **Reverse String**: `strings/reverse_string.py`
- **Scramble String**: `strings/scramble_string.py`
- **Shortest Palindrome**: `strings/shortest_palindrome.py`
- **Soundex**: `strings/soundex.py`
- **String Compression**: `strings/string_compression.py`
- **String Hashing**: `strings/string_hashing.py`
- **Suffix Array**: `strings/suffix_array.py`
- **Suffix Automaton**: `strings/suffix_automaton.py`
- **Suffix Tree**: `strings/suffix_tree.py`
- **Text Justification**: `strings/text_justification.py`
- **Valid Anagram**: `strings/valid_anagram.py`
- **Valid Palindrome**: `strings/valid_palindrome.py`
- **Valid Parentheses**: `strings/valid_parentheses.py`
- **Word Pattern**: `strings/word_pattern.py`
- **Word Search Ii**: `strings/word_search_ii.py`
- **Z Algorithm**: `strings/z_algorithm.py`
- **Zigzag Conversion**: `strings/zigzag_conversion.py`
- **Aa Tree**: `tree/aa_tree.py`
- **B Plus Tree**: `tree/b_plus_tree.py`
- **B Tree**: `tree/b_tree.py`
- **Binary Search Tree**: `tree/binary_search_tree.py`
- **Binary Tree**: `tree/binary_tree.py`
- **Bt From Post In**: `tree/bt_from_post_in.py`
- **Bt From Pre In**: `tree/bt_from_pre_in.py`
- **Cartesian Tree**: `tree/cartesian_tree.py`
- **Centroid Decomposition**: `tree/centroid_decomposition.py`
- **Fenwick Tree**: `tree/fenwick_tree.py`
- **Flatten Bt**: `tree/flatten_bt.py`
- **Hld**: `tree/hld.py`
- **Interval Tree**: `tree/interval_tree.py`
- **Invert Bt**: `tree/invert_bt.py`
- **Kd Tree**: `tree/kd_tree.py`
- **Kth Smallest Bst**: `tree/kth_smallest_bst.py`
- **Lca Bst**: `tree/lca_bst.py`
- **Lca Bt**: `tree/lca_bt.py`
- **Link Cut Tree**: `tree/link_cut_tree.py`
- **Morris Inorder**: `tree/morris_inorder.py`
- **Morris Preorder**: `tree/morris_preorder.py`
- **Path Sum Ii**: `tree/path_sum_ii.py`
- **Persistent Segment Tree**: `tree/persistent_segment_tree.py`
- **Populate Next Right**: `tree/populate_next_right.py`
- **Quad Tree**: `tree/quad_tree.py`
- **Radix Tree**: `tree/radix_tree.py`
- **Red Black Tree**: `tree/red_black_tree.py`
- **Right Side View**: `tree/right_side_view.py`
- **Rsq Mutable**: `tree/rsq_mutable.py`
- **Serialize Bt**: `tree/serialize_bt.py`
- **Splay Tree**: `tree/splay_tree.py`
- **Symmetric Tree**: `tree/symmetric_tree.py`
- **Treap**: `tree/treap.py`
- **Tst**: `tree/tst.py`
- **Two Three Tree**: `tree/two_three_tree.py`
- **Validate Bst**: `tree/validate_bst.py`
- **Zigzag Level Order**: `tree/zigzag_level_order.py`
