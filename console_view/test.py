import os
import json
# if not os.path.exists("./preset/time-slice.json"):
#     fp = open("./preset/time-slice.json",'w')
#     fp.write("[]")
#     fp.close()

# def is_has_slice(one_slice)->bool:
#     if not os.path.exists("./preset/time-slice.json"):
#         fp = open("./preset/time-slice.json",'w')
#         fp.write("[]")
#         fp.close()
#     with open("./preset/time-slice.json") as file:
#         time_slices = json.load(file)
#     slice_set=[]
#     for time_slice in time_slices:
#         slice_set.append(time_slice)
#     # print(slice_set)
#     if one_slice in slice_set:
#         return True
#     else:
#         return False
    
# one_time_slice = {
#     "roomId": "1864",
#     "seatNum": "016",
#     "startTime": "8:00",
#     "endTime": "9:00"
#     }
    
# print(is_has_slice(one_time_slice))