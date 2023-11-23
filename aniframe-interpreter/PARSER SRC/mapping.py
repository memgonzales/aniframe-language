from collections import defaultdict, OrderedDict
from collections.abc import Iterable

# CONFIGURABLES
MAX_FRAMES = int(1e100)

# DICTIONARY
VARIABLES = defaultdict(OrderedDict)

CLASSES = defaultdict(OrderedDict)
CLASSES_HIERARCHY = defaultdict(OrderedDict)

EXPR_NO_IDENTIFIER_CTR = 0
COMPOSITE_OBJ_NO_IDENTIFIER_CTR = 0

DRAW_CLASSES = defaultdict(OrderedDict)

FILL_IDX = 0
STROKE_IDX = 1

START_FRAME_IDX = 0
END_FRAME_IDX = 1
SCRIPT_IDX = 2

DEFAULT_FILL = '#FFFFFF'
DEFAULT_STROKE = '#000000'

def clean_identifier(name):
    return '_' + name

def is_function(name):
    return name.endswith('()')

def write(src_code):
    with open('src.anf-int', 'w') as f:
        f.write(src_code)

def flatten_list(xs):
    for x in xs:
        if isinstance(x, Iterable) and not isinstance(x, (str, bytes)):
            yield from flatten_list(x)
        else:
            yield x

def print_src_code(background=DEFAULT_FILL):
    ret = 'function setup() {createCanvas(1000, 1000);}\n'

    ret += 'function draw() {\n'
    ret += f'    background("{background}");\n'

    ret += print_display()

    ret += '}\n'

    ret += print_classes()

    return ret

def print_display_object(object):
    frames = set()
    for command in object:
        frames.add(command[START_FRAME_IDX])
        frames.add(command[END_FRAME_IDX])

    frames = list(frames)
    frames.sort()

    final_frames = [(frames[0], frames[1])]
    for i in range(1, len(frames) - 1):
        final_frames.append((frames[i]+1, frames[i+1]))

    final_commands = []
    for final_frame in final_frames:
        start_final_frame = final_frame[START_FRAME_IDX]
        end_final_frame = final_frame[END_FRAME_IDX]

        final_commands_str = ''
        for command in object:
            start_frame = command[START_FRAME_IDX]
            end_frame = command[END_FRAME_IDX]

            if start_frame <= start_final_frame and end_final_frame <= end_frame:
                final_commands_str += command[SCRIPT_IDX]
            
        final_commands.append(final_commands_str)

    ret = ''
    for frame, command in zip(final_frames, final_commands):
        ret += f'if ({frame[START_FRAME_IDX]} <= frameCount && frameCount <= {frame[END_FRAME_IDX]}) {{\n'
        ret += f'    {command}'
        ret += '}\n'

    return ret

def print_display():
    print(DRAW_CLASSES)
    ret = ''

    for _, object in DRAW_CLASSES.items():
        ret += 'push();\n'
        ret += print_display_object(object)
        ret += 'pop();\n'

    return ret

def print_classes():
    ret = '\n'
    for class_name, methods in CLASSES.items():
        ret += f'class {class_name} {{\n'

        for method, body in methods.items():
            if not is_function(method):
                continue

            if method != 'display()':
                ret += f'    {method} {{\n'
                ret += ';\n        '.join(body)
                ret += '    }\n'

            else:
                ret += f'    {method} {{\n'
                for entry in body:
                    for prop, value in entry.items():
                        if value is None:
                            continue
                        
                        if prop == 'shape':
                            ret += f'{value};\n'
                        
                        else:
                            ret += f'{prop}("{value}");\n'

                ret += '    }\n'

        ret += '}\n'

    return ret

def convert_object_to_p5(name):
    CLASSES[name] = OrderedDict()
    CLASSES[name]['constructor()'] = OrderedDict()
    
    CLASSES[name]['display()'] = [OrderedDict([('fill', None),
                                                ('stroke', None),
                                                ('shape', None)])]

    CLASSES_HIERARCHY[name] = [name]

def convert_object_new_to_p5(name):
    convert_object_to_p5(clean_identifier(name))

def convert_shape_to_p5(name, shape, fill=DEFAULT_FILL, stroke=DEFAULT_STROKE):
    convert_object_to_p5(name)
    CLASSES[name]['display()'][0]['fill'] = fill
    CLASSES[name]['display()'][0]['stroke'] = stroke
    CLASSES[name]['display()'][0]['shape'] = shape

def convert_point_to_p5(name, x, y):
    convert_shape_to_p5(clean_identifier(name), f'point({x}, {y})')

def convert_line_to_p5(name, x1, y1, x2, y2):
    convert_shape_to_p5(clean_identifier(name), f'line({x1}, {y1}, {x2}, {y2})')

def convert_curve_to_p5(name, x1, y1, x2, y2, x3, y3):
    convert_shape_to_p5(clean_identifier(name), f'curve({x1}, {y1}, {x2}, {y2}, {x3}, {y3})')

def convert_circle_to_p5(name, x, y, radius):
    convert_shape_to_p5(clean_identifier(name), f'circle({x}, {y}, {radius})')

def convert_ellipse_to_p5(name, x, y, width, height):
    convert_shape_to_p5(clean_identifier(name), f'ellipse({x}, {y}, {width}, {height})')

def convert_triangle_to_p5(name, x1, y1, x2, y2, x3, y3):
    convert_shape_to_p5(clean_identifier(name), f'triangle({x1}, {y1}, {x2}, {y2}, {x3}, {y3})')

def convert_rectangle_to_p5(name, x, y, width, height):
    convert_shape_to_p5(clean_identifier(name), f'rect({x}, {y}, {width}, {height})')

def convert_quad_to_p5(name, x1, y1, x2, y2, x3, y3, x4, y4):
    convert_shape_to_p5(clean_identifier(name), f'quad({x1}, {y1}, {x2}, {y2}, {x3}, {y3}, {x4}, {y4})')

def convert_polygon_to_p5(name, coordinates):
    polygon_script = 'beginShape();\n'
    for coordinate in coordinates:
        polygon_script += f'vertex({coordinate[0]}, {coordinate[1]});\n'

    polygon_script += 'endShape(CLOSE)'

    convert_shape_to_p5(clean_identifier(name), polygon_script)
    
def convert_write_to_p5(name, text, x, y):
    convert_shape_to_p5(clean_identifier(name), f'text("{text}", {x}, {y})', fill=DEFAULT_STROKE)

def convert_color_to_p5(name, value):
    VARIABLES[clean_identifier(name)] = value

def convert_fill_to_p5(object, color):
    for shape in CLASSES[clean_identifier(object)]['display()']:
        shape['fill'] = color

def convert_stroke_to_p5(object, color):
    for shape in CLASSES[clean_identifier(object)]['display()']:
        shape['stroke'] = color

def convert_object_assign_to_p5(base_object, new_object):
    base_object = clean_identifier(base_object)
    new_object = clean_identifier(new_object)

    CLASSES[base_object]['display()'] += CLASSES[new_object]['display()']
    CLASSES_HIERARCHY[base_object].append(CLASSES_HIERARCHY[new_object])

def convert_object_add_to_p5(operand1, operand2):
    # Identifier cleaning is done by convert_object_assign_to_p5

    global COMPOSITE_OBJ_NO_IDENTIFIER_CTR
    mock_identifier = f'${COMPOSITE_OBJ_NO_IDENTIFIER_CTR}'
    convert_object_new_to_p5(mock_identifier)

    try:
        convert_object_assign_to_p5(mock_identifier, operand1)
    except:
        convert_object_new_to_p5(operand1)

    try:
        convert_object_assign_to_p5(mock_identifier, operand2)
    except:
        convert_object_new_to_p5(operand2)

    COMPOSITE_OBJ_NO_IDENTIFIER_CTR += 1

    # Subtract 1 to return name of mock identifier
    return mock_identifier

def convert_object_expr_to_p5(function_name, param):
    global EXPR_NO_IDENTIFIER_CTR
    mock_identifier = f'_{EXPR_NO_IDENTIFIER_CTR}'

    match function_name:
        case 'point':
            convert_point_to_p5(mock_identifier, param[0], param[1])

        case 'line':
            convert_line_to_p5(mock_identifier, param[0], param[1], param[2], param[3])

        case 'curve':
            convert_curve_to_p5(mock_identifier, param[0], param[1], param[2], param[3], param[4], param[5])

        case 'circle':
            convert_circle_to_p5(mock_identifier, param[0], param[1], param[2])

        case 'ellipse':
            convert_ellipse_to_p5(mock_identifier, param[0], param[1], param[2], param[3])

        case 'triangle':
            convert_triangle_to_p5(mock_identifier, param[0], param[1], param[2], param[3], param[4], param[5])

        case 'rectangle':
            convert_rectangle_to_p5(mock_identifier, param[0], param[1], param[2], param[3])

        case 'quad':
            convert_quad_to_p5(mock_identifier, param[0], param[1], param[2], param[3], param[4], param[5], param[6], param[7])

        case 'polygon':
            convert_polygon_to_p5(mock_identifier, param[0])

        case 'write':
            convert_write_to_p5(mock_identifier, param[0], param[1], param[2])

    EXPR_NO_IDENTIFIER_CTR += 1

    return mock_identifier

def convert_move_to_p5(name, x, y, start_frame, end_frame):
    name = clean_identifier(name)
    if name not in DRAW_CLASSES:
        DRAW_CLASSES[name] = OrderedDict()

    script = f'translate(new p5.Vector(frameCount - {start_frame} + {x}, frameCount - {start_frame} + {y}));\n'
    try:
        DRAW_CLASSES[name].append([start_frame, end_frame, script])
    except:
        DRAW_CLASSES[name] = [[start_frame, end_frame, script]]

    end_script = f'translate(new p5.Vector({end_frame} - {start_frame} + {x}, {end_frame} - {start_frame} + {y}));\n'
    try:
        DRAW_CLASSES[name].append([end_frame, MAX_FRAMES, end_script])
    except:
        DRAW_CLASSES[name] = [[end_frame, MAX_FRAMES, end_script]]

def convert_rotate_to_p5(name, angle, start_frame, end_frame):
    name = clean_identifier(name)
    if name not in DRAW_CLASSES:
        DRAW_CLASSES[name] = OrderedDict()

    script = f'rotate((frameCount - {start_frame}) * radians({angle}) / ({end_frame} - {start_frame} + 1));\n'
    try:
        DRAW_CLASSES[name].append([start_frame, end_frame, script])
    except:
        DRAW_CLASSES[name] = [[start_frame, end_frame, script]]

    end_script = f'rotate(({end_frame} - {start_frame}) * radians({angle}) / ({end_frame} - {start_frame} + 1));\n'
    try:
        DRAW_CLASSES[name].append([end_frame, MAX_FRAMES, end_script])
    except:
        DRAW_CLASSES[name] = [[end_frame, MAX_FRAMES, end_script]]

def draw(name, start_frame, end_frame):
    name = clean_identifier(name)
    if name not in DRAW_CLASSES:
        DRAW_CLASSES[name] = OrderedDict()

    script = f'new {name}().display();\n'
    try:
        DRAW_CLASSES[name].append([start_frame, end_frame, script])
    except:
        DRAW_CLASSES[name] = [[start_frame, end_frame, script]]



convert_rectangle_to_p5('car_body', 0, 0, 95.4, 79.5)
convert_circle_to_p5('wheel1', 80, 80, 33)
convert_triangle_to_p5('window1', 30, 75, 58, 20, 86, 75)

convert_color_to_p5('window_color', '#ADD8E6')

convert_fill_to_p5('car_body', '#ADD8E6')
convert_fill_to_p5('window1', '#000000')
convert_stroke_to_p5('wheel1', '#ADD8FF')

convert_object_new_to_p5('car')
convert_object_add_to_p5('car', 'car_body')
convert_object_add_to_p5('car', 'window1')
convert_object_add_to_p5('car', 'wheel1')

# =====================

convert_rectangle_to_p5('car_body1', 200, 200, 95.4, 79.5)
convert_circle_to_p5('wheel11', 280, 280, 33)
convert_triangle_to_p5('window11', 230, 275, 258, 220, 286, 275)

convert_fill_to_p5('car_body1', '#ADD8E6')
convert_fill_to_p5('window11', '#000000')
convert_stroke_to_p5('wheel11', '#ADD8FF')

convert_object_assign_to_p5('car1', convert_object_add_to_p5('car1', 'car_body1'))
convert_object_assign_to_p5('car1', convert_object_add_to_p5('car1', 'window11'))
convert_object_assign_to_p5('car1', convert_object_add_to_p5('car1', 'wheel11'))

convert_object_add_to_p5('car1', convert_object_add_to_p5('car1', 'car'))
convert_move_to_p5('car1', 10, 20, 200, 300)
convert_rotate_to_p5('car1', 45, 250, 300)

draw('car1', 100, 400)

convert_polygon_to_p5('star', [(30, 20), (85, 20), (85, 75), (30, 75)])
draw('star', 1, 400)

convert_write_to_p5('dog', 'awooo', 80, 90)
draw('dog', 50, 400)

# ========================

# draw(convert_object_expr_to_p5('line', [100, 200, 300, 400]))
# draw(convert_object_add_to_p5(convert_object_expr_to_p5('line', [100, 200, 300, 400]), convert_object_expr_to_p5('rectangle', [10, 20, 30, 40])))

# ========================

write(print_src_code())
