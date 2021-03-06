#!/usr/bin/env python

import roslib
roslib.load_manifest("view_controller_msgs")

import rospy
from math import *
from view_controller_msgs.msg import CameraPlacement
from geometry_msgs.msg import Point, Vector3

rospy.init_node("camera_test", anonymous = True)

pub = rospy.Publisher("/rviz/camera_placement", CameraPlacement, queue_size = 1)

rate_float = 0.2
rate = rospy.Rate(rate_float)

# 225
# path = [{'p':[2.0792, 6.2794, 2.6703], 'f':[1.8809, 1.4659, 1.0109], 'up':[-0.070096, 0.32769, -0.94218]},
#         {'p':[1.7857, 1.5678, 2.1333], 'f':[1.79, 1.1656, 0.61911], 'up':[0.0050031, 0.96647, -0.25672]},
#         {'p':[1.1327, 1.6579, 0.72757], 'f':[1.8954, 1.3394, 0.80091], 'up':[0.38626, 0.92232, -0.01134]},
#         # {'p':[0.8827, 1.651, 1.0386], 'f':[2.0855, 1.2543, 1.5775], 'up':[0.27962, 0.95676, 0.080169]},
#         {'p':[1.241, 2.0163, 1.152], 'f':[2.0922, 1.4754, 1.5255], 'up':[0.52312, 0.85128, 0.040771]},
         
#         {'p':[1.901, 1.9396, 0.40787], 'f':[1.9336, 1.7325, 0.9809], 'up':[0.0079425, 0.94055, 0.33955]},  
#         {'p':[3.0331, 1.634, 1.5389], 'f':[2.1462, 1.1412, 1.6413], 'up':[-0.21408, 0.9651, -0.15081]}, 
#         {'p':[2.3477, 1.5263, 1.9091], 'f':[1.9081, 1.2857, 1.0234], 'up':[-0.11631, 0.97157, -0.2062]}, 
#         {'p':[2.4691, 4.3237, 4.5364], 'f':[1.7567, 1.4448, 1.0869], 'up':[-0.049591, 0.77181, -0.63391]}, 
#         {'p':[2.0792, 6.2794, 2.6703], 'f':[1.8809, 1.4659, 1.0109], 'up':[-0.070096, 0.32769, -0.94218]}]


# 249
# path = [{'p':[-0.031314, 5.9988, 0.42727], 'f':[0.13814, 0.6726, 0.27686], 'up':[0.010019, -0.027908, 0.99956]},
#         # {'p':[0.48717, 1.7817, -1.2816], 'f':[0.86287, 1.1304, 0.0015847], 'up':[0.039457, 0.89564, 0.44302]},
#         {'p':[0.67768, 1.6953, -0.67042], 'f':[0.92067, 1.026, 0.16793], 'up':[0.096014, 0.79124, 0.60392]},
#         # {'p':[0.46693, 1.6491, -1.1424], 'f':[-0.42506, 0.7585, 0.91055], 'up':[-0.18719, 0.92827, 0.32136]},
#         {'p':[0.49396, 1.2217, -0.93795], 'f':[0.066097, 0.81215, 0.16029], 'up':[0.066097, 0.81215, 0.16029]},
#         {'p':[0.99497, 1.4939, 0.194], 'f':[-0.67942, 0.6113, -0.23049], 'up':[-0.44201, 0.89049, -0.108]},
#         {'p':[0.82454, 1.7705, 1.241], 'f':[0.88583, 0.81525, -0.67565], 'up':[0.016033, 0.8951, -0.44558]},
#         {'p':[-0.59091, 1.4017, 0.32837], 'f':[1.3288, 0.70893, 0.14317], 'up':[0.34214, 0.93904, 0.033878]},
#         {'p':[0.28657, 3.7072, -0.45613], 'f':[0.23666, 0.83573, 0.16661], 'up':[0.22076, 0.20305, 0.95396]},
#         {'p':[-0.031314, 5.9988, 0.42727], 'f':[0.13814, 0.6726, 0.27686], 'up':[0.010019, -0.027908, 0.99956]}]

# 322
# path = [{'p':[-2.9527, 7.6897, -0.53354], 'f':[-0.49898, -0.24912, 1.2344], 'up':[0.8469, 0.35076, 0.39967]},
#         {'p':[-2.5644, 2.3232, -0.23513], 'f':[-0.80702, 0.44662, 2.7219], 'up':[0.20202, 0.87679, 0.43637]},
#         {'p':[-3.3041, 2.2738, 0.49982], 'f':[-0.021185, -0.012851, 0.12982], 'up':[0.5513, 0.81804, -0.16395]},
#         # {'p':[-1.3302, 2.1509, 2.3563], 'f':[-0.64009, 0.24533, -0.50381], 'up':[0.024419, 0.83467, -0.5502]},
#         {'p':[-0.53848, 2.6244, 2.0039], 'f':[-0.22622, 0.030989, -0.82648], 'up':[0.015827, 0.73807, -0.67454]},
#         {'p':[0.94423, 2.4145, 2.1827], 'f':[0.91677, 0.67205, -0.41103], 'up':[0.061828, 0.8282, -0.55701]},
#         {'p':[1.3654, 4.8262, 0.83217], 'f':[2.1912, 1.0155, 0.85124], 'up':[0.94585, 0.20623, 0.25069]},
#         {'p':[2.6704, 2.007, -0.28873], 'f':[1.5846, 1.0704, 1.4028], 'up':[-0.1892, 0.90545, 0.37994]},
#         {'p':[0.60941, 1.8556, -0.21542], 'f':[0.28653, 1.3619, 0.99271], 'up':[-0.012292, 0.92676, 0.37546]},
#         {'p':[-0.83948, 1.9629, -0.25252], 'f':[-0.94225, 1.6355, 0.77613], 'up':[-0.045725, 0.95321, 0.29885]},
#         {'p':[-1.525, 5.0078, -4.1053], 'f':[-0.69537, 1.3954, 0.54557], 'up':[0.00038153, 0.78978, 0.61339]},
#         {'p':[-2.9527, 7.6897, -0.53354], 'f':[-0.49898, -0.24912, 1.2344], 'up':[0.8469, 0.35076, 0.39967]}]

# 001(231)
# path = [{'p':[-1.3976, 6.767, 0.32308], 'f':[-1.2618, 1.3198, -0.073559], 'up':[-0.015871, -0.073008, 0.99721]}, 
#         {'p':[-2.5477, 2.0603, -0.96347], 'f':[-2.2096, 1.1676, 0.41095], 'up':[0.011045, 0.83983, 0.54274]},    
#         {'p':[-1.3353, 1.9854, -1.3036], 'f':[-0.86395, 1.2551, 0.13768], 'up':[-0.0035347, 0.89154, 0.45293]},   
#         {'p':[-1.8301, 1.5739, -0.328736], 'f':[-0.8106, 1.0799, -0.16019], 'up':[0.43984, 0.89758, -0.029803]},   
#         {'p':[-1.1653, 1.8163, 0.77735], 'f':[-0.7817, 1.0728, -0.1539], 'up':[0.20431, 0.80432, -0.55796]},   
#         {'p':[-1.586, 1.744, 0.67238], 'f':[-1.5335, 1.018, -0.34058], 'up':[0.019836, 0.81315, -0.58171]},   
#         {'p':[-2.0143, 1.5872, 0.78747], 'f':[-2.6775, 0.97777, -0.25651], 'up':[-0.073697, 0.88096, -0.46742]},    
#         {'p':[-1.0678, 1.4853, -0.33118], 'f':[-2.6808, 0.94026, -0.18951], 'up':[-0.32129, 0.94686, -0.015076]},  
#         {'p':[1.4055, 6.9586, -0.61133], 'f':[-1.7221, 0.45665, 0.40254], 'up':[-0.87046, 0.44987, 0.1998]},  
#         {'p':[-1.3976, 6.767, 0.32308], 'f':[-1.2618, 1.3198, -0.073559], 'up':[-0.015871, -0.073008, 0.99721]}]

# 011
# path = [{'p':[0.92364, 7.857, -0.42901], 'f':[0.18895, 1.599, 0.76925], 'up':[-0.077368, -0.17873, -0.98085]}, 
#         {'p':[0.0059375, 1.5812, 1.944], 'f':[0.61826, 1.22, 0.50646], 'up':[-0.012551, 0.9685, -0.24869]}, 
#         {'p':[2.0603, 1.9352, 0.64172], 'f':[0.58275, 1.3139, 0.57313], 'up':[-0.38678, 0.92197, -0.019412]}, 
#         {'p':[1.227, 1.8368, -0.33176], 'f':[0.96837, 1.2306, 0.71368], 'up':[-0.20562, 0.86782, 0.45234]}, 
#         {'p':[-0.81844, 3.6744, -0.6253], 'f':[0.86196, 0.84701, 0.60671], 'up':[0.73058, 0.58654, 0.34961]}, 
#         {'p':[0.92364, 7.857, -0.42901], 'f':[0.18895, 1.599, 0.76925], 'up':[-0.077368, -0.17873, -0.98085]}]

# 061
# path = [{'p':[-1.9657, 6.2077, 0.45861], 'f':[-1.6885, 0.79247, 1.4597], 'up':[0.0092251, 0.18224, 0.98321]},
#         {'p':[-1.9381, 2.3236, -2.1435], 'f':[-1.7558, 0.23113, 0.74198], 'up':[-0.013301, 0.80908, 0.58755]}, 
#         {'p':[-2.0246, 2.1487, -0.32256], 'f':[-2.4196, 1.0217, 0.95491], 'up':[-0.086629, 0.76022, 0.64387]}, 
#         {'p':[-1.7704, 2.2, 0.069197], 'f':[-1.5375, 1.2672, 1.0033], 'up':[0.053056, 0.71319, 0.69896]}, 
#         {'p':[-1.9657, 6.2077, 0.45861], 'f':[-1.6885, 0.79247, 1.4597], 'up':[0.0092251, 0.18224, 0.98321]}]

# 069
# path = [{'p':[-0.97919, 6.8481, -0.013629], 'f':[-1.2041, 1.3481, -0.0026072], 'up':[-0.0067052, -0.0017298, -0.99998]}, 
#         {'p':[-2.5589, 2.3258, 1.5304], 'f':[-2.5768, 1.3667, 0.015433], 'up':[0.0085186, 0.84482, -0.53498]}, 
#         {'p':[-0.67709, 2.3164, 1.5419], 'f':[-0.69523, 1.3447, 0.0071134], 'up':[0.0085186, 0.84482, -0.53498]}, 
#         {'p':[-1.2155, 1.4466, 1.8523], 'f':[0.12734, 1.0076, 0.68415], 'up':[0.19791, 0.97056, -0.13724]},
#         {'p':[-0.97919, 6.8481, -0.013629], 'f':[-1.2041, 1.3481, -0.0026072], 'up':[-0.0067052, -0.0017298, -0.99998]}]

# 223
# path = [{'p':[-1.2475, 6.5434, -0.52579], 'f':[-0.56465, 0.8186, -0.85061], 'up':[-0.99297, -0.11838, -0.00098005]}, 
#         {'p':[-0.031946, 1.4011, -3.3694], 'f':[-1.4249, 0.69158, -2.1226], 'up':[-0.3165, 0.93197, 0.17678]}, 
#         {'p':[-0.33388, 1.9903, -2.3883], 'f':[-0.58973, 1.1254, -1.4569], 'up':[-0.23544, 0.74355, 0.62586]}, 
#         {'p':[0.087906, 2.0657, -2.2189], 'f':[-0.18298, 1.0037, -1.2127], 'up':[-0.24867, 0.69884, 0.67066]},
#         {'p':[-1.2475, 6.5434, -0.52579], 'f':[-0.56465, 0.8186, -0.85061], 'up':[-0.99297, -0.11838, -0.00098005]}]
      
# 276
# path = [{'p':[-1.5168, 7.684, 0.20538], 'f':[-0.54271, 0.45347, 0.11327], 'up':[0.99048, 0.13298, 0.035681]}, 
#         {'p':[-0.72654, 1.9507, 0.71503], 'f':[-0.62699, 1.289, -0.52263], 'up':[0.0081406, 0.88213, -0.47093]}, 
#         {'p':[-1.519, 1.5234, 0.47194], 'f':[0.70442, 0.89073, 0.12475], 'up':[0.27124, 0.96237, -0.016578]}, 
#         {'p':[-1.1649, 1.9644, -0.32068], 'f':[0.045749, 1.2891, 0.26675], 'up':[0.42967, 0.89205, 0.14008]}, 
#         {'p':[-1.5168, 7.684, 0.20538], 'f':[-0.54271, 0.45347, 0.11327], 'up':[0.99048, 0.13298, 0.035681]}]  

# 286
# path = [{'p':[0.80885, 5.9052, 1.3259], 'f':[0.56213, 1.043, -0.054427], 'up':[0.007024, 0.27275, -0.96206]}, 
#         {'p':[-0.73659, 3.1691, 1.9993], 'f':[-0.81185, 0.90654, -0.043073], 'up':[-0.0052067, 0.67015, -0.7422]}, 
#         {'p':[1.9145, 3.117, 1.9903], 'f':[1.8388, 0.83903, -0.065952], 'up':[-0.0052067, 0.67015, -0.7422]}, 
#         {'p':[0.80885, 5.9052, 1.3259], 'f':[0.56213, 1.043, -0.054427], 'up':[0.007024, 0.27275, -0.96206]}]

# 521
path = [{'p':[-0.39378, 6.1707, 0.076383], 'f':[0.043622, 1.7802, -0.83193], 'up':[0.01708, 0.2042, -0.97878]}, 
        {'p':[-0.63509, 2.1583, 0.62481], 'f':[0.2033, 0.77997, -0.29165], 'up':[0.3428, 0.65576, -0.67266]}, 
        {'p':[-1.0117, 1.99, -0.59969], 'f':[-0.0010551, 0.84455, -0.77543], 'up':[0.74043, 0.66655, -0.086507]}, 
        {'p':[-0.39378, 6.1707, 0.076383], 'f':[0.043622, 1.7802, -0.83193], 'up':[0.01708, 0.2042, -0.97878]}]   

        
          

while not rospy.is_shutdown():

    print "Top of loop!"
    
    for i in range(len(path)):
        t = rospy.get_time()
        cp = CameraPlacement()

        cp.target_frame = "Room_0_link"
        
        path_p = path[i]['p']
        path_f = path[i]['f']
        path_up = path[i]['up']
        p = Point(path_p[0], path_p[1], path_p[2])
        f = Point(path_f[0], path_f[1], path_f[2])
        up = Point(path_up[0], path_up[1], path_up[2])

        # if i == 1:
        #     p = Point(1.7, 1.8, 2.0)
        #     f = Point(1.8697, 0.70853, -0.41507)
        #     up = Vector3(0.01, 0.9, -0.3)
        #     i = i + 1
        # else:
        #     p = Point(1.07, 1.98, 0.77)
        #     f = Point(2.8572, 0.78972, 0.77447)
        #     up = Vector3(0.54, 0.84, -0.01)
        #     i = 1


        #   p = Point(r*sin(2*pi*t/10), 0, r*cos(2*pi*t/10))
        cp.eye.point = p
        # cp.eye.header.frame_id = "Room_0_link"

        #f = Point(0, 0, 2*cos(2*pi*t/5))
        #   f = Point(0, 0, 0)
        cp.focus.point = f
        # cp.focus.header.frame_id = "Room_0_link"

        #   up = Vector3(0.01, 0.9, -0.3)
        #up = Vector3(0, sin(2*pi*t/10), cos(2*pi*t/10))
        cp.up.vector = up
        # cp.up.header.frame_id = "Room_0_link"
        #cp.up.header.frame_id = "rotating_frame"

        cp.allow_free_yaw_axis = True

        cp.time_from_start = rospy.Duration(1.0/rate_float)
        print "Publishing a message!"
        pub.publish(cp)
        #print "Sleeping..."
        rate.sleep()
        #print "End of loop!"

