import pywavefront
import numpy as np
import os

from body_measurements_copy.measurement import Body3D

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
    weight = body.weight()
    shoulder_2d, shoulder_location, shoulder_length = body.shoulder()
    chest_2d, chest_location, chest_length = body.chest()
    hip_2d, hip_location, hip_length = body.hip()
    waist_2d, waist_location, waist_length = body.waist()
    thigh_2d, thigh_location, thigh_length = body.thighOutline()
    outer_leg_length = body.outerLeg()
    inner_leg_length = body.innerLeg()
    neck_2d, neck_location, neck_length = body.neck()
    neck_hip_length = body.neckToHip()


if __name__ == '__main__':
    main()