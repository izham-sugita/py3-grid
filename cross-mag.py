import numpy as np

vec1 = np.ndarray((3))
vec2 = np.ndarray((3))
vec3 = np.ndarray((3))
vec4 = np.ndarray((3))

vec1[:] = [0.0,-0.5,-0.5]
vec2[:] = [0.0,0.5,-0.5]
vec3[:] = [0.0,0.5,0.5]
vec4[:] = [0.0,-0.5,0.5]

cross1 = np.ndarray((3))
cross2 = np.ndarray((3))
cross3 = np.ndarray((3))
cross4 = np.ndarray((3))

cross1 = np.cross(vec1,vec2)
cross2 = np.cross(vec2,vec3)
cross3 = np.cross(vec3,vec4)
cross4 = np.cross(vec4,vec1)

print(cross1)
print(cross2)
print(cross3)
print(cross4)

mag1 = np.linalg.norm(cross1)
mag2 = np.linalg.norm(cross2)
mag3 = np.linalg.norm(cross3)
mag4 = np.linalg.norm(cross4)
print(mag1,mag2,mag3,mag4)

#print(vec1)
#print(type(vec1))
