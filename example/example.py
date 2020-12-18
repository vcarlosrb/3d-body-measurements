import pywavefront
import numpy as np
import os

from body_measurements.measurement import Body3D

current_dir = os.path.dirname(os.path.realpath(__file__))
data_dir = os.path.join(current_dir, 'data')

def main():
    person = pywavefront.Wavefront(
        os.path.join(data_dir, 'person.obj'),
        create_materials=True,
        collect_faces=True
    )
    faces = np.array(person.mesh_list[0].faces)
    vertices = np.array(person.vertices)

    body = Body3D(vertices, faces)

    body_measurements = body.getMeasurements()

    height = body.height()


if __name__ == '__main__':
    main()