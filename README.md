# Python Sorting Algorithms

This project provides Python implementations of several common sorting algorithms within the `Sorting.py` file.
These implementations are primarily intended for educational and demonstrational purposes, allowing users to study and compare the behavior of different sorting techniques.

## Helper Functions

### `exch(a, i, j)`
*   **Purpose**: Swaps the elements at index `i` and `j` within the list `a`.
*   **Parameters**:
    *   `a`: The list containing the elements.
    *   `i`: Index of the first element.
    *   `j`: Index of the second element.
*   **Mechanism**: Uses a temporary variable to perform the in-place swap.
*   **Usage**: This function is utilized by several sorting algorithms (`selectionSort`, `insertionSort`, `shellSort`, `Quick.partition`) to rearrange elements.

## Implemented Algorithms

Below is a list of the sorting algorithms implemented in `Sorting.py`. Each algorithm sorts the list in ascending order.

### 1. Selection Sort (`selectionSort`)
*   **Description**: A simple comparison sort that divides the list into a sorted and an unsorted region. In each pass, it finds the smallest (or largest) element in the unsorted region and swaps it with the first element of that unsorted region, moving the boundary between the sorted and unsorted regions one element to the right.
*   **Logic**:
    1.  Iterate from the first element to the second-to-last element (outer loop, index `i`). This `i` marks the beginning of the unsorted part.
    2.  Assume the element `a[i]` is the smallest in the unsorted part (initialize `min_index = i`).
    3.  Iterate from `i+1` to the end of the list (inner loop, index `j`) to find the actual minimum element in the unsorted part.
    4.  If an element `a[j]` is smaller than `a[min_index]`, update `min_index = j`.
    5.  After the inner loop, `min_index` holds the index of the smallest element in `a[i:]`. Swap `a[i]` with `a[min_index]` using the `exch` function.
*   **Characteristics**:
    *   Time Complexity: O(n²) in all cases (worst, average, best).
    *   Space Complexity: O(1) (in-place).
    *   Stable: No (can change the relative order of equal elements).
*   **Note**: The implementation in `Sorting.py` includes a `print(i)` statement for tracing the main passes.

### 2. Insertion Sort (`insertionSort`)
*   **Description**: A simple sorting algorithm that builds the final sorted list one item at a time. It iterates through an input array and for each element, it shifts elements greater than it one position to the right and then inserts the current element into the correct position.
*   **Logic**:
    1.  Iterate from the second element (`i=1`) to the end of the list (outer loop). The sub-list `a[0...i-1]` is considered sorted.
    2.  The current element `a[i]` (stored as `a[pos]`) is the one to be inserted into the sorted sub-list.
    3.  Iterate backwards (inner `while` loop, `pos > 0`) as long as `a[pos]` is less than the element to its left (`a[pos-1]`).
    4.  In each step of the inner loop, swap `a[pos]` with `a[pos-1]` using `exch(a, pos, pos-1)`, effectively moving `a[pos]` one position to the left. Decrement `pos`.
    5.  The inner loop stops when `a[pos]` is no longer less than `a[pos-1]`, or when `pos` reaches 0. `a[pos]` is now in its correct sorted position.
*   **Characteristics**:
    *   Time Complexity:
        *   Worst-case: O(n²) (e.g., for a reverse-sorted list).
        *   Average-case: O(n²).
        *   Best-case: O(n) (e.g., for an already sorted list).
    *   Space Complexity: O(1) (in-place).
    *   Stable: Yes (maintains the relative order of equal elements).
*   **Note**: The implementation in `Sorting.py` includes a `print(i)` statement for tracing which element is currently being inserted.

### 3. Shell Sort (`shellSort`)
*   **Description**: An improvement over Insertion Sort that allows the comparison and exchange of elements that are far apart. It sorts elements at a specific interval (gap `h`) and gradually reduces the interval. This makes it more efficient than Insertion Sort for larger lists.
*   **Logic (using Knuth's sequence `h = 3*h + 1` for gap generation)**:
    1.  **Initialize Gap `h`**: Start with `h=1`. Calculate an initial large gap `h` using the sequence `h = 3*h + 1` such that `h` is the first value in this sequence that is `>= N/3` (where `N` is list length).
    2.  **Outer Loop (Decreasing Gaps)**: Loop as long as `h >= 1`.
    3.  **h-Sorting (Gapped Insertion Sort)**: For the current gap `h`:
        *   Iterate from `i = h` to `N-1`.
        *   For each element `a[i]`, perform an insertion sort-like operation, but compare `a[i]` (as `a[j]`) with elements `h` positions behind it (`a[j-h]`).
        *   Inner loop: `while (j >= h and a[j] < a[j-h])`, swap `a[j]` with `a[j-h]` using `exch`, and decrement `j` by `h`.
    4.  **Reduce Gap**: After a full h-sort pass for the current `h`, update `h = int(h/3)`.
    5.  The final pass occurs when `h=1`, which is equivalent to a standard Insertion Sort on a nearly sorted list, making it efficient.
*   **Characteristics**:
    *   Time Complexity: Depends on the gap sequence. For Knuth's sequence, it's roughly O(n^(3/2)) in the worst case, but often performs better, approaching O(n log n) in some scenarios.
    *   Space Complexity: O(1) (in-place).
    *   Stable: No (can change the relative order of equal elements due to long-distance swaps).

### 4. Quick Sort (`Quick` class)
*   **Description**: A highly efficient divide-and-conquer sorting algorithm. It works by selecting a 'pivot' element from the array and partitioning the other elements into two sub-arrays, according to whether they are less than or greater than the pivot. The sub-arrays are then sorted recursively.
*   **Implementation (`Quick` class)**:
    *   `sort_main(self, a)`:
        1.  **Shuffle**: `random.shuffle(a)` is called first. This is crucial to prevent worst-case O(n²) behavior on sorted or nearly-sorted lists by ensuring a more random pivot selection on average.
        2.  Calls the recursive `self.sort(a, 0, len(a)-1)`.
    *   `sort(self, a, lo, hi)` (Recursive method):
        1.  **Base Case**: If `hi <= lo`, the sub-array is sorted.
        2.  **Partition**: `j = self.partition(a, lo, hi)` partitions `a[lo...hi]`. The pivot (initially `a[lo]`) is placed at its correct sorted position `j`. Elements `a[lo...j-1]` are `<= a[j]`, and `a[j+1...hi]` are `>= a[j]`.
        3.  **Recurse**: Calls `self.sort(a, lo, j-1)` and `self.sort(a, j+1, hi)` on the sub-arrays.
    *   `partition(self, a, lo, hi)`:
        1.  Selects pivot `v = a[lo]`.
        2.  Uses two pointers, `i` (from `lo+1`) and `j` (from `hi`), to scan the array.
        3.  `i` scans right to find an element `a[i] >= v`.
        4.  `j` scans left to find an element `a[j] <= v`.
        5.  If `i < j`, `exch(a, i, j)` swaps these elements.
        6.  Loop continues until `i >= j`.
        7.  Finally, `exch(a, lo, j)` places the pivot `v` into its correct position `j`. Returns `j`.
*   **Characteristics**:
    *   Time Complexity:
        *   Worst-case: O(n²) (rare with initial shuffle).
        *   Average-case: O(n log n).
        *   Best-case: O(n log n).
    *   Space Complexity: O(log n) on average (due to recursion stack). Worst-case O(n).
    *   Stable: No (typically, depends on partitioning details).
*   **Note**: The `partition` method in `Sorting.py` includes `print` statements for tracing. The `sort_main` sorts in-place.

### 5. Top-Down Merge Sort (`Merge` class and `merge` function)
*   **Description**: A divide-and-conquer algorithm that recursively divides the list into two halves, sorts each half, and then merges the sorted halves to produce a fully sorted list.
*   **Implementation (`Merge` class and standalone `merge` function)**:
    *   `Merge.sort_main(self, a)`: Calls the recursive `self.sort(a, 0, len(a)-1)`.
    *   `Merge.sort(self, a, lo, hi)` (Recursive method):
        1.  **Base Case**: If `hi <= lo`, the sub-array is sorted.
        2.  **Divide**: Calculates `mid = lo + (hi - lo) // 2`.
        3.  **Conquer**: Recursively calls `self.sort(a, lo, mid)` for the left half and `self.sort(a, mid + 1, hi)` for the right half.
        4.  **Combine**: Calls `merge(a, lo, mid, hi)` to merge the two sorted halves.
    *   `merge(a, lo, mid, hi)` (Standalone function):
        1.  **Auxiliary Array**: This function is intended to copy `a[lo...hi]` to an auxiliary array `aux`.
        2.  **Pointers**: Uses pointers `i` (for left half, starting `lo`) and `j` (for right half, starting `mid+1`) for `aux`.
        3.  **Merge**: Iterates `k` from `lo` to `hi` (inclusive). In each step, it compares `aux[i]` and `aux[j]`, copies the smaller one to `a[k]`, and advances the corresponding pointer (`i` or `j`). Handles cases where one half is exhausted.
*   **Characteristics**:
    *   Time Complexity: O(n log n) in all cases (worst, average, best).
    *   Space Complexity: O(n) due to the auxiliary array used during merging.
    *   Stable: Yes (if implemented carefully, preserving relative order of equal elements).
*   **Note**: The `merge` function in `Sorting.py` is shared with Bottom-Up Merge Sort. It has significant issues with auxiliary array initialization and loop bounds (see "Identified Issues and Bugs" section below). The `Merge.sort` method's `mid` calculation also needs `//` for integer division in Python 3.

### 6. Bottom-Up Merge Sort (`MergeBU` class and `merge` function)
*   **Description**: An iterative version of Merge Sort. It starts by merging pairs of individual elements (sub-lists of size 1), then merges pairs of sorted sub-lists of size 2, then size 4, and so on, until the entire list is sorted.
*   **Implementation (`MergeBU` class and standalone `merge` function)**:
    *   `MergeBU.sort(self, a)` (Iterative method):
        1.  `N = len(a)`.
        2.  Outer loop: `sz` (sub-list size) starts at 1 and doubles in each iteration (`sz = sz + sz`) as long as `sz < N`.
        3.  Inner loop: `lo` (starting index of a pair of sub-lists) iterates from `0` to `N-sz` with a step of `sz+sz`.
        4.  For each `lo`, it calls `merge(a, lo, lo+sz-1, min(lo+sz+sz-1, N-1))`.
            *   `mid = lo+sz-1` (end of the first sub-list).
            *   `hi = min(lo+sz+sz-1, N-1)` (end of the second sub-list, capped at `N-1`).
*   **Characteristics**:
    *   Time Complexity: O(n log n) in all cases.
    *   Space Complexity: O(n) due to the auxiliary array used by the `merge` function.
    *   Stable: Yes (if `merge` is implemented carefully).
*   **Note**: Uses the same problematic `merge` function as Top-Down Merge Sort. The `MergeBU.sort` method includes `print` statements for tracing `sz`, `lo`, and merge boundaries. Sorts in-place.

## Identified Issues and Bugs

The implementations in `Sorting.py`, while useful for demonstration, contain some notable issues:

1.  **`selectionSort` Function:**
    *   **Incorrect Inner Loop Range**: The inner loop `for pos in range(i+1, len(a) - 1):` fails to check the very last element of the list. It should be `range(i+1, len(a))`.
    *   **Premature Swapping**: The `exch(a, i, min)` call is located *inside* the inner loop. This causes incorrect swaps before the actual minimum of the unsorted portion is found. It should be placed *after* the inner loop.

2.  **`merge` Function (Standalone - Affects both Top-Down and Bottom-Up Merge Sorts):**
    *   **Incorrect Auxiliary Array (`aux`) Handling**:
        *   The initialization `aux = list(range(lo, hi+1))` and subsequent population loop `for k_copy in range(lo, hi+1): aux[k_copy] = a[k_copy]` are fundamentally flawed. `aux` has 0-based indexing relative to its own length (`hi-lo+1`). The copy attempt using original indices (`k_copy`) will cause an `IndexError` if `lo > 0`.
        *   This means the `merge` function cannot work correctly for sub-arrays not starting at index 0, unless `aux` is managed externally as a full-sized copy (which it is not in the current structure).
    *   **Merge Loop Bound**: The main merging loop `for k in range(lo, hi):` does not include the element at index `hi`. It should be `for k in range(lo, hi + 1):` to correctly fill the segment `a[lo...hi]`.

3.  **`Merge.sort` Method (Top-Down Merge Sort specific issue):**
    *   **`mid` Calculation**: The calculation `mid = lo + (hi-lo)/2` can result in a float for `mid` in Python 3 if `(hi-lo)` is odd (e.g., `(5-0)/2 = 2.5`). A float `mid` would cause errors when used as a list index. It should be `mid = lo + (hi - lo) // 2` for integer division.

These issues would need to be addressed for the sorting algorithms (Selection Sort and both Merge Sorts) to function correctly and robustly in all scenarios.

## Example Usage

The `Sorting.py` file includes a section at the end demonstrating the usage of these sorting algorithms. It initializes a sample list `a = [190, 33, 454, 3, 5, 12, 10, 2, 9]`, then shows:
*   A direct call to `exch(a, 2, 4)` modifying the list.
*   Instantiation of `Quick`, `Merge`, and `MergeBU` classes.
*   Calls to `case_Quick.partition(a,...)`, `case_Quick.sort_main(a)`, `case_Merge.sort_main(a)`, and `case_MergeBU.sort(a)`.
*   It's important to note that the list `a` is modified in-place by these operations, and subsequent calls operate on the list's state from the previous operation, as it's not reset.

The example usage section also contains commented-out calls to `selectionSort(a)`, `insertionSort(a)`, and `shellSort(a)`.

## How to Run
To execute the script and see the sorting algorithms in action (including any `print` statements for tracing), run the following command in your terminal from the root directory of the project: 
```bash
python Sorting.py
```

## Future Work / Improvements
- Fix the identified bugs in `selectionSort` and the `merge` function to ensure correctness for all cases.
- Add Big O notation (time and space complexity) for each implemented algorithm.
- Implement unit tests for each sorting algorithm to verify correctness systematically.
- Add more sorting algorithms (e.g., Heap Sort, Counting Sort, Radix Sort).
- Include performance comparisons or visualizations of the sorting process.
