import trimesh
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


def load_mesh(file_path):
    return trimesh.load(file_path)


def calculate_height(mesh):
    # Calculate height as the difference between the maximum and minimum Y coordinates
    return mesh.bounds[1][1] - mesh.bounds[0][1]


def visualize_mesh(mesh):
    # Assumes the mesh is a trimesh.Trimesh object
    figure = plt.figure(figsize=(10, 10))
    ax = figure.add_subplot(111, projection='3d')
    mesh.show()


# Example usage
if __name__ == "__main__":
    # Update this path to your .obj file
    mesh_path = 'Realistic_White_Male_Low_Poly.obj'
    mesh = load_mesh(mesh_path)
    height = calculate_height(mesh)
    print(f"Height: {height:.2f} meters")
    visualize_mesh(mesh)
