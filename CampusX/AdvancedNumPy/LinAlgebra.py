import numpy as np

# Euclidean distance from the origin to the point (1,2,3,4,5)
# --------------------------------------------------------------------
a = np.array([1,2,3,4,5])
distance = np.linalg.norm(a)
# linalg means linear algebra, and norm is a function that calculates the length of a vector

print("Distance from the origin to the point (1,2,3,4,5) is:", distance)

# distance between two points (1,2,3) and (4,5,6)
# --------------------------------------------------------
point1 = np.array([1,2,3])
point2 = np.array([4,5,6])
distance_between_points = np.linalg.norm(point1 - point2)
print("Distance between points (1,2,3) and (4,5,6) is:", distance_between_points)

# Dot product of two vectors
# -----------------------------------
vector1 = np.array([1,2,3])
vector2 = np.array([4,5,6])
dot_product = np.dot(vector1, vector2)
dot_product1= vector1@vector2  # this is another way to calculate the dot product in Python 3.5 and later
print("Dot product of vectors (1,2,3) and (4,5,6) is:", dot_product)
print("Dot product calculated using @ operator is:", dot_product1)


# Cosine similarity between two vectors
# ------------------------------------------------
# cosine_similarity = dot_product / (np.linalg.norm(vector1) * np.linalg.norm(vector2))
a = np.random.rand(5)  # random vector of size 5
b = np.random.rand(5)  # another random vector of size 5
c = np.random.rand(5)  # another random vector of size 5
# cosine similarity between a and b
cosine_similarity_ab = np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))
# cosine similarity between a and c
cosine_similarity_ac = np.dot(a, c) / (np.linalg.norm(a) * np.linalg.norm(c))
print("Cosine similarity between vector a and b is:", cosine_similarity_ab)
print("Cosine similarity between vector a and c is:", cosine_similarity_ac)


# inverse
# inverse of a matrix is a matrix when multiplied to original results in a identity matrix
arr1 = np.array([[1,2],[4,5]])
inv = np.linalg.inv(arr1)
print(inv)

# Power
# ----------

pow = np.linalg.matrix_power(arr1,2)
print(pow)
pow = np.linalg.matrix_power(arr1,0)
print(pow)
pow = np.linalg.matrix_power(arr1,-2)
print(pow)

# Determinant
# -------------

det = np.linalg.det(arr1)
print(det)

# for determinant and inverse square matrix is required (n*n)