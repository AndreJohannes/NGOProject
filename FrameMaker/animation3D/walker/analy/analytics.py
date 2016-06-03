# frame 7=
crotch = (216, 362)
neck = (216, 302)
knee1 = (221, 412)
foot1 = (227, 461)
knee2 = (218, 412)
foot2 = (193, 455)
elbow1 = (218, 342)
hand1 = (227, 381)
elbow2 = (209, 341)
hand2 = (213, 381)
frame7 = {"crotch": crotch, "neck": neck, "knee_1": knee1, "knee_2": knee2, "elbow_1": elbow1, "hand_1": hand1,
          "elbow_2": elbow2, "hand_2": hand2, "foot_1": foot1, "foot_2": foot2}

# frame 8=
crotch = (230, 361)
neck = (230, 301)
knee1 = (229, 411)
foot1 = (226, 461)
knee2 = (243, 409)
foot2 = (235, 459)
elbow1 = (223, 341)
hand1 = (227, 381)
elbow2 = (231, 341)
hand2 = (242, 379)
frame8 = {"crotch": crotch, "neck": neck, "knee_1": knee1, "knee_2": knee2, "elbow_1": elbow1, "hand_1": hand1,
          "elbow_2": elbow2, "hand_2": hand2, "foot_1": foot1, "foot_2": foot2}

# frame 9=
crotch = (241, 361)
neck = (241, 301)
knee1 = (235, 411)
foot1 = (226, 460)
knee2 = (259, 410)
foot2 = (256, 460)
elbow1 = (231, 340)
hand1 = (229, 380)
elbow2 = (247, 341)
hand2 = (262, 378)
frame9 = {"crotch": crotch, "neck": neck, "knee_1": knee1, "knee_2": knee2, "elbow_1": elbow1, "hand_1": hand1,
          "elbow_2": elbow2, "hand_2": hand2, "foot_1": foot1, "foot_2": foot2}

# frame 10=
crotch = (253, 362)
neck = (253, 302)
knee1 = (249, 412)
foot1 = (228, 458)
knee2 = (264, 411)
foot2 = (272, 460)
elbow1 = (240, 340)
hand1 = (234, 379)
elbow2 = (262, 341)
hand2 = (281, 376)
frame10 = {"crotch": crotch, "neck": neck, "knee_1": knee1, "knee_2": knee2, "elbow_1": elbow1, "hand_1": hand1,
           "elbow_2": elbow2, "hand_2": hand2, "foot_1": foot1, "foot_2": foot2}

# frame 11=
crotch = (268, 360)
neck = (268, 300)
knee1 = (266, 410)
foot1 = (241, 453)
knee2 = (274, 410)
foot2 = (277, 460)
elbow1 = (259, 339)
hand1 = (257, 379)
elbow2 = (272, 340)
hand2 = (285, 377)
frame11 = {"crotch": crotch, "neck": neck, "knee_1": knee1, "knee_2": knee2, "elbow_1": elbow1, "hand_1": hand1,
           "elbow_2": elbow2, "hand_2": hand2, "foot_1": foot1, "foot_2": foot2}

# frame 12=
crotch = (284, 360)
neck = (284, 300)
knee1 = (293, 410)
foot1 = (278, 457)
knee2 = (282, 410)
foot2 = (277, 460)
elbow1 = (279, 340)
hand1 = (282, 380)
elbow2 = (282, 340)
hand2 = (294, 379)
frame12 = {"crotch": crotch, "neck": neck, "knee_1": knee1, "knee_2": knee2, "elbow_1": elbow1, "hand_1": hand1,
           "elbow_2": elbow2, "hand_2": hand2, "foot_1": foot1, "foot_2": foot2}

# frame 13=
crotch = (300, 362)
neck = (300, 302)
knee1 = (313, 410)
foot1 = (305, 460)
knee2 = (291, 411)
foot2 = (278, 460)
elbow1 = (306, 342)
hand1 = (319, 379)
elbow2 = (290, 341)
hand2 = (290, 381)
frame13 = {"crotch": crotch, "neck": neck, "knee_1": knee1, "knee_2": knee2, "elbow_1": elbow1, "hand_1": hand1,
           "elbow_2": elbow2, "hand_2": hand2, "foot_1": foot1, "foot_2": foot2}

# frame 14=
crotch = (311, 362)
neck = (311, 302)
knee1 = (324, 410)
foot1 = (332, 460)
knee2 = (302, 411)
foot2 = (276, 454)
elbow1 = (323, 340)
hand1 = (342, 375)
elbow2 = (296, 339)
hand2 = (292, 379)
frame14 = {"crotch": crotch, "neck": neck, "knee_1": knee1, "knee_2": knee2, "elbow_1": elbow1, "hand_1": hand1,
           "elbow_2": elbow2, "hand_2": hand2, "foot_1": foot1, "foot_2": foot2}

# frame 15=
crotch = (327, 360)
neck = (327, 300)
knee1 = (332, 410)
foot1 = (334, 460)
knee2 = (329, 410)
foot2 = (307, 455)
elbow1 = (330, 340)
hand1 = (340, 378)
elbow2 = (318, 339)
hand2 = (321, 380)
frame15 = {"crotch": crotch, "neck": neck, "knee_1": knee1, "knee_2": knee2, "elbow_1": elbow1, "hand_1": hand1,
           "elbow_2": elbow2, "hand_2": hand2, "foot_1": foot1, "foot_2": foot2}

list1 = [frame7, frame8, frame9, frame10, frame11, frame12, frame13, frame14]
import pickle

pickle.dump(list1, open("frames.p", "wb"))
