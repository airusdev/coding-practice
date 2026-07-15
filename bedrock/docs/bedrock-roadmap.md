# The Bedrock Curriculum

Pattern-drilling roadmap — Strings → Arrays → Stacks/Queues → Dictionaries → Trees → Linked Lists → Mixed.
One problem per session per day. No starter code — design the interface yourself.

---

## Phase 0 — Computational Thinking (one-time, folded into the 7-step protocol)

Write each step out, answer it, then move to the next — don't write all 7 upfront.

1. Understand the problem step-by-step given some input
2. In 1–3 sentences, explain the program's core logic
3. Figure out the essential data structure
4. Think of specific cases/conditions and what to do in each
5. Think of edge cases and what to do to accommodate them
6. Merge cases + edges into ordered steps
7. Code

---

## Phase 1 — Strings

**Core patterns:** Frequency/Hashmap → Two Pointers → Sliding Window

### Tier 1 — Foundation
- [x] 1. Vowel Census — Count vowels in a string
- [x] 2. Mirror Check — Is string a palindrome (brute force)
- [x] 3. The Duplicate Detector — Find first repeated character
- [ ] 4. Case Flip — Swap case of every letter
- [ ] 5. The Counter — Count occurrences of a given character
- [ ] 6. Longest Word — Find longest word in a sentence
- [ ] 7. Reverse Words — Reverse word order in a sentence
- [ ] 8. The Deduplicator — Remove consecutive duplicate characters
- [ ] 9. Title Case — Capitalize first letter of each word
- [ ] 10. Frequency Map Builder — Build a full char-frequency dict of a string

### Tier 2 — Single Pattern
- [ ] 1. Anagram Verifier — Same letter frequency between two strings *(Frequency)*
- [ ] 2. Two-Ended Palindrome — Palindrome check, no extra space *(Two pointers)*
- [ ] 3. Character Budget — Longest substring with only K distinct chars *(Sliding window)*
- [ ] 4. First Unique Character — Index of first non-repeating char *(Frequency)*
- [ ] 5. Clean Palindrome — Palindrome check ignoring non-alphanumerics *(Two pointers)*
- [ ] 6. Longest Uniform Run — Longest run of the same character *(Sliding window)*
- [ ] 7. Rotation Checker — Is string B a rotation of string A *(Frequency/concat trick)*
- [ ] 8. Common Prefix Finder — Longest common prefix among a list of strings *(Two pointers)*
- [ ] 9. Isomorphic Strings — Can string A map 1-to-1 onto string B *(Frequency/mapping)*
- [ ] 10. Adjacent Non-Repeat Check — Can letters rearrange so no two adjacent match *(Frequency)*

### Tier 3 — Pattern + Edge Cases
- [ ] 1. Case-Insensitive Anagram Groups — Group words by anagram signature *(Frequency)*
- [ ] 2. Longest No-Repeat Run — Longest substring with zero repeated chars *(Sliding window + frequency)*
- [ ] 3. The Compressor — Run-length encode a string *(Traversal + counting)*
- [ ] 4. The Decompressor — Decode a run-length-encoded string back *(Parsing)*
- [ ] 5. Longest Palindromic Substring — Longest palindrome inside a string *(Two pointers, expand from center)*
- [ ] 6. Group Shifted Strings — Group shift-equivalent words (abc→bcd) *(Normalization)*
- [ ] 7. Compression With Counts — Run-length encode, handling counts >9 *(Traversal + counting)*
- [ ] 8. Find All Anagram Starts — Every index where an anagram of P starts in T *(Sliding window + frequency)*
- [ ] 9. Two Distinct Characters — Longest substring with at most 2 distinct chars *(Sliding window)*
- [ ] 10. Word Pattern Match — Does "abba" match "dog cat cat dog" *(Bijection/mapping)*

### Tier 4 — Combined
- [ ] 1. Minimum Window Substring — Smallest substring containing all chars of another string *(Sliding window + frequency)*
- [ ] 2. Longest No-Repeat (full version) — Same as T3#2, adversarial input *(Sliding window + frequency)*
- [ ] 3. Reorganize String — Rearrange so no two adjacent chars match, or impossible *(Frequency + greedy)*
- [ ] 4. Smallest Substring With K Distinct — Smallest window w/ exactly K distinct chars *(Sliding window)*
- [ ] 5. Longest Palindromic Substring (optimized) — Same as T3#5, efficiently *(Two pointers, expand-around-center)*

---

## Phase 2 — Arrays / Lists

**Core patterns:** Two Pointers → Sliding Window → Prefix Sum

### Tier 1 — Foundation
- [ ] 1. Running Total — Build a prefix sum array from scratch
- [ ] 2. The Flipper — Reverse array in place
- [ ] 3. Peak Finder — Find max without built-in max()
- [ ] 4. The Rotator — Rotate array by K positions (brute force)
- [ ] 5. Second Highest — Find second largest without sorting
- [ ] 6. Array Merge — Merge two sorted arrays into one sorted array
- [ ] 7. Element Counter — Frequency count of every element
- [ ] 8. Missing Number Finder — Find the missing number in 1..N
- [ ] 9. Unique Filter — Remove duplicates from an unsorted array
- [ ] 10. Array Intersection — Common elements between two arrays

### Tier 2 — Single Pattern
- [ ] 1. Pair Target — Two numbers in sorted array summing to target *(Two pointers)*
- [ ] 2. Fixed Window Max Sum — Max sum of any K consecutive elements *(Sliding window)*
- [ ] 3. Zero Mover — Move all zeros to the end, in place *(Two pointers)*
- [ ] 4. Sorted Squares — Square every element, return sorted (has negatives) *(Two pointers)*
- [ ] 5. Container Capacity — Max area between two lines *(Two pointers)*
- [ ] 6. Remove Duplicates In Place — Sorted array, remove dupes in place *(Two pointers, slow/fast)*
- [ ] 7. Longest Consecutive Run — Longest run of the same value *(Sliding window)*
- [ ] 8. Equilibrium Index — Index where left-sum equals right-sum *(Prefix sum)*
- [ ] 9. Three-Reversal Rotate — Rotate array in place using reversal trick *(Two pointers)*
- [ ] 10. Range Sum Query — Precompute so any range-sum query is O(1) *(Prefix sum)*

### Tier 3 — Pattern + Edge Cases
- [ ] 1. Dynamic Window Target — Smallest subarray with sum ≥ target *(Sliding window)*
- [ ] 2. Product Except Self — Product of array except self, no division *(Prefix/suffix product)*
- [ ] 3. Subarray Sum Equals K — Count subarrays that sum to K *(Prefix sum + frequency)*
- [ ] 4. Max Consecutive Ones — Max consecutive 1s allowing K flips of 0→1 *(Sliding window)*
- [ ] 5. Equal Zeros And Ones — Longest subarray with equal count of 0s and 1s *(Prefix sum + frequency)*
- [ ] 6. Rainfall Catcher — Trapped rainwater between bars (1D) *(Two pointers / prefix max)*
- [ ] 7. Find All Duplicates — Find every duplicate using O(1) extra space *(Index-marking trick)*
- [ ] 8. Max Subarray Sum — Classic max subarray (Kadane's) *(Running sum / greedy)*
- [ ] 9. Minimum Size Subarray — Smallest subarray length with sum ≥ target *(Sliding window)*
- [ ] 10. Majority Element — Element appearing more than N/2 times *(Frequency / O(1) space trick)*

### Tier 4 — Combined
- [ ] 1. Three-Way Split — Triplets that sum to zero *(Sorting + two pointers)*
- [ ] 2. Max Subarray Product — Like Kadane's but for product, sign-flip edge case *(Sliding window + min/max tracking)*
- [ ] 3. Sliding Window Maximum — Max of every window of size K, efficiently *(Monotonic deque — stretch)*
- [ ] 4. K Distinct Values Window — Longest subarray with at most K distinct values *(Sliding window + frequency)*
- [ ] 5. Four-Way Split — Quadruplets that sum to target *(Sorting + two pointers, generalized)*

---

## Phase 3 — Stacks & Queues *(not yet built)*
## Phase 4 — Dictionaries / Hashmaps *(not yet built)*
## Phase 5 — Trees *(foundational only — not yet built)*
## Phase 6 — Linked Lists *(not yet built)*
## Phase 7 — Mixed *(combines all — not yet built)*

*Excluded from this roadmap: Graphs beyond basics, Dynamic Programming, Advanced/Expert tree structures, Segment Trees, Tries, Disjoint Sets, Game Theory, NP-Complete. Low-yield for backend/systems roadmap — competitive programming specialization.*

---

## Repo structure
```
coding-practice/
├── hackerrank/
│   ├── algorithms/
│   │   ├── warmup/
│   │   ├── implementation/
│   │   ├── strings/
│   │   └── sorting/
│   └── data-structures/
├── foundry-set/
└── bedrock/
    ├── strings/
    │   ├── tier-1-foundation/
    │   ├── tier-2-single-pattern/
    │   ├── tier-3-pattern-edge-cases/
    │   └── tier-4-combined/
    └── arrays/
        ├── tier-1-foundation/
        ├── tier-2-single-pattern/
        ├── tier-3-pattern-edge-cases/
        └── tier-4-combined/
```

## Rules
- One problem per session per day
- 7-step protocol before every problem (write it out until it's automatic, ~2 weeks)
- No starter code — design the interface yourself
- Commit after every session, even partial/failed attempts
