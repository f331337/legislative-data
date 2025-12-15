## WRITEUP

### 1. Time Complexity and Tradeoffs

The solution processes all input data using in-memory Python data structures and performs aggregation with a single pass over the voting records.

**Time complexity:**
- Reading CSV files: **O(N)**, where N is the total number of rows across all input files
- Aggregation over `vote_results`: **O(V)**, where V is the number of vote result rows
- Dictionary lookups for joins (legislators, votes, bills): **O(1)** average case

Overall time complexity is **O(N)**, and memory usage is **O(N)**, proportional to the input size.

**Tradeoffs:**
- I chose a dependency-free approach using only Python’s standard library. While tools like `pandas` could reduce code size, they would introduce unnecessary overhead for a relatively small and well-defined dataset.
- I intentionally avoided using a database or ORM, since the problem does not require persistence, indexing, or concurrency.

---

### 2. Handling Future Columns (e.g. Vote Date, Co-Sponsors)

The current design separates data loading, aggregation, and report generation, which makes it easy to extend.

To support additional columns:
- New fields can be added to the internal data structures without affecting existing aggregation logic.
- Report-generation functions can be extended to include new columns while keeping computation logic unchanged.
- For more complex relationships (e.g. multiple co-sponsors), additional mappings or collections could be introduced without redesigning the core processing flow.

This modular structure allows the solution to evolve incrementally as new reporting requirements are introduced.

---

### 3. If Input Were a Subset of Legislators or Bills

If the input were a predefined list of legislators or bills rather than full CSV files:
- The aggregation logic would remain the same.
- Input data could be filtered during the loading phase or before report generation.
- Alternatively, reports could be generated only for the requested IDs by filtering the final result sets.

Because the computation is driven by dictionary lookups and not by positional assumptions, restricting the output scope would require minimal changes.

---

### 4. Time Spent on the Assignment

I spent approximately **2–3 hours** on this assignment.  
This included understanding the problem, implementing the solution, writing tests, and preparing the final output and documentation.

---

P.S. I was almost ready to go with DuckDB (since it is not real DB), but no-deps solution was too attractive :D.
