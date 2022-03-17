function_list = [{'function_id': 72, 'list_file': ['http://test.com/input-folder/test_file.blend', 'aaaaaaa.blend'],
'order_no': 1, 'step_no': [], 'height': 0, 'width': 0, 'length': 0, 'dx': 1, 'dy': 1, 'dz': 1, 'radius': 0, 'percent': 0, 'degree': 0, 'unit': '%', 'text': '', 'time_stop': 0,
'bend_rate_a': 0, 'bend_rate_b': 0, 'segments': 0, 'level': 0, 'point_line': [], 'empty_location': [],
'current_location': [[-5, 2, 5]], 'color': '0xA4BFFF', 'angle': 0, 'axis': '', 'plane_co': [], 'plane_no': []}]

func_id = function_list[0].get('function_id')
list_files = function_list[0].get('list_file')
print(func_id)
print(list_files)
