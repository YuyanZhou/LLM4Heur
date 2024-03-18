# Rounding heuristic

Input:  Optimal LP solution x^{lp} of current subproblem  
Output: If available, one feasible integral solutions

    Set x^{tmp} := x^{lp}
    for j $\in$ F := {j \in I |  x^{lp}_j \notin  }