# some-linear-algebra
## Cross Product: 
- def: A vector made up of the product of the magnitudes of two vectors and the sine of the angle between them.
  The cross product of vector **A** and **B** in three-dimensional space is defined as:

$$
\vec{A} \times \vec{B} = \begin{vmatrix}
\mathbf{i} & \mathbf{j} & \mathbf{k} \\
A_x & A_y & A_z \\
B_x & B_y & B_z
\end{vmatrix}
$$

Where:
- $$\(\mathbf{i}, \mathbf{j}, \mathbf{k}\)$$ are the unit vectors in the **x**, **y**, and **z** directions respectively.
- $$\(A_x, A_y, A_z\)$$ are the components of vector **A**.
- $$\(B_x, B_y, B_z\)$$ are the components of vector **B**.

The result of the cross product is a vector that is perpendicular to both **A** and **B**.

An easier and quicker way to compute this is:
Suppose $\vec{A}$ = (1,2,3) and $\vec{B}$ = (4,5,6) is to 
write out:

$$
\begin{vmatrix}
1 & 2 & 3 & 1 & 2 & 3\\
4 & 5 & 6 & 4 & 5 & 6
\end{vmatrix}
$$

then cover the first and the last column, computing the determinant of each two adjacent column, which would be:

$$
\text{det}\begin{vmatrix} 2 & 3 \\ 
5 & 6 \end{vmatrix}+ \quad
\text{det}\begin{vmatrix} 3 & 1 \\ 
6 & 4 \end{vmatrix}+ \quad
\text{det}\begin{vmatrix} 1 & 2 \\ 
4 & 5 \end{vmatrix}
$$
