import trimesh
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Line3DCollection


def load_mesh(file_path):
    return trimesh.load(file_path)


def calculate_height(mesh):
    return mesh.bounds[1][1] - mesh.bounds[0][1]


def slice_at_height(mesh, height_fraction):
    total_height = calculate_height(mesh)
    slice_height = mesh.bounds[0][1] + total_height * height_fraction
    slice = mesh.section(
        plane_origin=[0, slice_height, 0], plane_normal=[0, 1, 0])
    return slice, slice_height


def calculate_circumference(slice):
    if slice is None:
        return 0
    polyline = slice.to_planar()[0]
    return polyline.length


def visualize_slice(mesh, slice, slice_height):
    fig = plt.figure(figsize=(10, 10))
    ax = fig.add_subplot(111, projection='3d')
    mesh.visual.face_colors = [100, 100, 250, 100]  # Slightly transparent

    # Display the mesh
    mesh.show(axes=ax)

    # Convert slice to 3D line for visualization, with dotted style
    if slice is not None:
        slice_3d = slice.to_3D()
        edges = np.array(slice_3d.entities[0].segments)
        verts = np.array(slice_3d.vertices)
        lc = Line3DCollection(
            verts[edges], colors='r', linewidths=2, linestyles=':')
        ax.add_collection3d(lc)

    # Adjust plot limits and add scales
    for axis, axis_limit in zip(['X', 'Y', 'Z'], [ax.set_xlim, ax.set_ylim, ax.set_zlim]):
        axis_limit(mesh.bounds[:, 0])
        ax.set_xlabel(f'{axis} axis (m)')
        ax.set_ylabel(f'{axis} axis (m)')
        ax.set_zlabel(f'{axis} axis (m)')

    # Add a grid for better scale visualization
    ax.xaxis._axinfo['grid'].update(color='k', linestyle='--')
    ax.yaxis._axinfo['grid'].update(color='k', linestyle='--')
    ax.zaxis._axinfo['grid'].update(color='k', linestyle='--')

    plt.title(f"Slice at Height: {slice_height:.2f} meters")
    plt.show()


# Example usage
if __name__ == "__main__":
    mesh_path = 'Realistic_White_Male_Low_Poly.obj'  # Update to your mesh file path
    mesh = load_mesh(mesh_path)
    chest_slice, slice_height = slice_at_height(mesh, 0.6)  # Adjust as needed
    chest_circumference = calculate_circumference(chest_slice)
    print(f"Chest Circumference: {chest_circumference:.2f} meters")
    visualize_slice(mesh, chest_slice, slice_height)
