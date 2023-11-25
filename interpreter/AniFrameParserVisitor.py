# Generated from AniFrameParser.g4 by ANTLR 4.13.1
from antlr4 import *
from ast import literal_eval
import mapping
from collections import defaultdict, OrderedDict
from copy import deepcopy
import re
import random
import math


if "." in __name__:
    from .AniFrameParser import AniFrameParser
else:
    from AniFrameParser import AniFrameParser

# This class defines a complete generic visitor for a parse tree produced by AniFrameParser.
def check_type(value):
    try:
        if type(literal_eval(value)) == int or type(literal_eval(value)) == float:
            return "Number"
        elif '"' in value:
            return "Text"
    except:
        return "Text"
    
def default_value():
    return '_'

def valid_dtype(dtype):
    dtypes = ['Object','Number','Color','Coord','List','Text']

    return True if dtype in dtypes else False
def invert(colors):
    for i in range(3):
        colors[i] = 255-colors[i]
    
    return colors
def assign_member_value(val,idx,expr,assignment,ctx):
    assignment = assignment[0] if len(assignment) == 2 else None
    not_allowed = ["List","Object"]
    dtype = expr['data_type']

    if type(idx) != int:
        if type(idx) == float:
            idx = int(idx)
        raiseError(ctx,TypeError,f'Index must be a number')
    if dtype in not_allowed:
        #THROW error
        raiseError(ctx,TypeError,f'Invalid data type {dtype}')
    
    if isinstance(VARIABLES[val]['value'],list) and idx >=0 and idx <= len(VARIABLES[val]['value']):
        match assignment:
            case None:
                if VARIABLES[val]['value'][idx]['data_type'] == dtype:
                    VARIABLES[val]['value'][idx]['value'] = expr['value']
                else:
                    #throw error
                    raiseError(ctx,TypeError,f" {dtype} to {VARIABLES[val]['value'][idx]['data_type']} assignment is not supported")
            case '+':
                match VARIABLES[val]['value'][idx]['data_type'],dtype:
                    case "Number","Number":
                        VARIABLES[val]['value'][idx]['value'] += expr['value']
                    case "Text","Text":
                        VARIABLES[val]['value'][idx]['value'] += expr['value']
                    case "Color","Color":
                        VARIABLES[val]['value'][idx]['value'][0] = int((VARIABLES[val]['value'][idx]['value'][0] + expr['value'][0])/2)
                        VARIABLES[val]['value'][idx]['value'][1] = int((VARIABLES[val]['value'][idx]['value'][1] + expr['value'][1])/2)
                        VARIABLES[val]['value'][idx]['value'][2] = int((VARIABLES[val]['value'][idx]['value'][2] + expr['value'][2])/2)
                    case "Coord","Coord":
                        VARIABLES[val]['value'][idx]['value'] = (VARIABLES[val]['value'][idx]['value'][0] + expr['value'][0], VARIABLES[val]['value'][idx]['value'][1] + expr['value'][1])
                    case _:
                        #throw error
                        raiseError(ctx,TypeError,f"{assignment} operator between {VARIABLES[val]['value'][idx]['data_type']} and {dtype} is not supported")
            case '-':
                match VARIABLES[val]['value'][idx]['data_type'],dtype:
                    case "Number","Number":
                        VARIABLES[val]['value'][idx]['value'] = VARIABLES[val]['value'][idx]['value'] - expr['value']
                    case "Color","Color":
                        expr['value'] = invert(expr['value'])
                        VARIABLES[val]['value'][idx]['value'][0] = int((VARIABLES[val]['value'][idx]['value'][0] + expr['value'][0])/2)
                        VARIABLES[val]['value'][idx]['value'][1] = int((VARIABLES[val]['value'][idx]['value'][1] + expr['value'][1])/2)
                        VARIABLES[val]['value'][idx]['value'][2] = int((VARIABLES[val]['value'][idx]['value'][2] + expr['value'][2])/2)
                    case "Coord","Coord":
                        VARIABLES[val]['value'][idx]['value'] = (VARIABLES[val]['value'][idx]['value'][0] - expr['value'][0], VARIABLES[val]['value'][idx]['value'][1] - expr['value'][1])
                    case _:
                        #throw error
                        raiseError(ctx,TypeError,f"{assignment} operator between {VARIABLES[val]['value'][idx]['data_type']} and {dtype} is not supported")
            case '*':
                match VARIABLES[val]['value'][idx]['data_type'],dtype:
                    case "Number","Number":
                        VARIABLES[val]['value'][idx]['value'] = VARIABLES[val]['value'][idx]['value'] * expr['value']
                    case "Coord","Number":
                        VARIABLES[val]['value'][idx]['value']= (VARIABLES[val]['value'][idx]['value'][0]*expr['value'],VARIABLES[val]['value'][idx]['value'][1] * expr['value'])
                    case "Coord","Coord":
                        VARIABLES[val]['value'][idx]['value'] = (VARIABLES[val]['value'][idx]['value'][0] * expr['value'][0], VARIABLES[val]['value'][idx]['value'][1] * expr['value'][1])
                    case _:
                        # throw error
                        raiseError(ctx,TypeError,f"{assignment} operator between {VARIABLES[val]['value'][idx]['data_type']} and {dtype} is not supported")
            case '/':
                match VARIABLES[val]['value'][idx]['data_type'],dtype:
                    case "Number","Number":
                        VARIABLES[val]['value'][idx]['value'] = VARIABLES[val]['value'][idx]['value'] / expr['value']
                    case "Coord","Number":
                        VARIABLES[val]['value'][idx]['value'] = (VARIABLES[val]['value'][idx]['value'][0]/expr['value'],VARIABLES[val]['value'][idx]['value'][1] / expr['value'])
                    case "Coord","Coord":
                        VARIABLES[val]['value'][idx]['value'] = (VARIABLES[val]['value'][idx]['value'][0] / expr['value'][0], VARIABLES[val]['value'][idx]['value'][1] / expr['value'][1])
                    case _:
                        # throw error
                        raiseError(ctx,TypeError,f"{assignment} operator between {VARIABLES[val]['value'][idx]['data_type']} and {dtype} is not supported")
            case '%':
                match VARIABLES[val]['value'][idx]['data_type'],dtype:
                    case "Number","Number":
                        VARIABLES[val]['value'][idx]['value'] = VARIABLES[val]['value'][idx]['value'] % expr['value']
                    case _:
                        # throw error
                        raiseError(ctx,TypeError,f"{assignment} operator between {VARIABLES[val]['value'][idx]['data_type']} and {dtype} is not supported")
        return val, VARIABLES[val]['value'][idx]
    else:
        # throw error
        raiseError(ctx,TypeError,f'Member assignment to {val} is invalid')
        return 

def raiseError(ctx, error_type, error_msg):
        line = ctx.start.line
        raise error_type(f'Error on line {line}: {error_msg}')

def check_parameters(name,params,ctx):
    match name:
        case 'type':
            check = True if len(params) == 1 else False
            if check:
                return params
            else:
                raiseError(ctx,ValueError,f"Invalid parameters for type")
        case 'info':
            check = True if len(params) == 1 else False
            if check:
                return params
            else:
                raiseError(ctx,ValueError,f"Invalid parameters for info")
        case 'add':
            check = True if len(params) == 1 else False
            if check:
                if params[0]['data_type'] == "List":
                    check = False
                if params[0]['data_type'] == "Object":
                    if isinstance(params[0]['value'],OrderedDict):
                        params = params[0].get('identifier')
                    else:
                        params = mapping.convert_object_expr_to_p5(params[0]['value'][0],params[0]['value'][1])
            if check:
                return params
            else:
                #THROW ERROR
                raiseError(ctx,TypeError,f'Invalid data types for add')
        case 'remove':
            check = True if len(params) == 1 else False
            if check:
                for param in params:
                    if param['data_type'] != "Number":
                        check = False
                        break
            if check:
                return [int(params[0])]
            else:
                #THROW ERROR
                raiseError(ctx,TypeError,f'Invalid index ')
        case 'draw':
            check = True if len(params) == 2 else False
            if check:
                for param in params:
                    if param['data_type'] != "Number":
                        check = False
                        break
            if check:
                params = [int(params[0]['value']),int(params[1]['value'])]
                return params
            else:
                #THROW ERROR
                raiseError(ctx,ValueError,f'Wrong parameters for {name}')
        case 'move':
            check = True if len(params) == 4 else False
            if check:
                for param in params:
                    if param['data_type'] != "Number":
                        check = False
                        break
            if check:
                params = [params[0]['value'],params[1]['value'],int(params[2]['value']),int(params[3]['value'])]
                return params
            else:
                #THROW ERROR
                raiseError(ctx,ValueError,f'Wrong parameters for {name}')
        case 'turn':
            check = True if len(params) == 3 else False
            if check:
                for param in params:
                    if param['data_type'] != "Number":
                        check = False
                        break
            if check:
                params = [params[0]['value'],int(params[1]['value']),int(params[2]['value'])]
                return params
            else:
                #THROW ERROR
                raiseError(ctx,ValueError,f'Wrong parameters for {name}')
        case 'turnC':
            check = True if len(params) == 3 else False
            if check:
                for param in params:
                    if param['data_type'] != "Number":
                        check = False
                        break
            if check:
                params = [params[0]['value'],int(params[1]['value']),int(params[2]['value'])]
                return params
            else:
                #THROW ERROR
                raiseError(ctx,ValueError,f'Wrong parameters for {name}')
        case 'turnCC':
            check = True if len(params) == 3 else False
            if check:
                for param in params:
                    if param['data_type'] != "Number":
                        check = False
                        break
            if check:
                params = [params[0]['value'],int(params[1]['value']),int(params[2]['value'])]
                return params
            else:
                #THROW ERROR
                raiseError(ctx,ValueError,f'Wrong parameters for {name}')
        case 'moveX':
            check = True if len(params) == 3 else False
            if check:
                for param in params:
                    if param['data_type'] != "Number":
                        check = False
                        break
            if check:
                params = [params[0]['value'],int(params[1]['value']),int(params[2]['value'])]
                return params
            else:
                #THROW ERROR
                raiseError(ctx,ValueError,f'Wrong parameters for {name}')
        case 'moveY':
            check = True if len(params) == 3 else False
            if check:
                for param in params:
                    if param['data_type'] != "Number":
                        check = False
                        break
            if check:
                params = [params[0]['value'],int(params[1]['value']),int(params[2]['value'])]
                return params
            else:
                #THROW ERROR
                raiseError(ctx,ValueError,f'Wrong parameters for {name}')
        case 'shear':
            check = True if len(params) == 3 else False
            if check:
                for param in params:
                    if param['data_type'] != "Number":
                        check = False
                        break
            if check:
                params = [params[0]['value'],int(params[1]['value']),int(params[2]['value'])]
                return params
            else:
                #THROW ERROR
                raiseError(ctx,ValueError,f'Wrong parameters for {name}')
        case 'shearX':
            check = True if len(params) == 3 else False
            if check:
                for param in params:
                    if param['data_type'] != "Number":
                        check = False
                        break
            if check:
                params = [params[0]['value'],int(params[1]['value']),int(params[2]['value'])]
                return params
            else:
                #THROW ERROR
                raiseError(ctx,ValueError,f'Wrong parameters for {name}')
        case 'shearY':
            check = True if len(params) == 3 else False
            if check:
                for param in params:
                    if param['data_type'] != "Number":
                        check = False
                        break
            if check:
                params = [params[0]['value'],int(params[1]['value']),int(params[2]['value'])]
                return params
            else:
                #THROW ERROR
                raiseError(ctx,ValueError,f'Wrong parameters for {name}')
        case 'write':
            check = True if len(params) == 3 else False
            if check:

                for param in params[1:]:
                    if param['data_type'] != "Number":
                        check = False
                        break
                if params[0]['data_type'] == "Text":
                    check = False
            if check:
                params = [params[0]['value'],params[1]['value'],params[2]['value']]
                return params
            else:
                #THROW ERROR
                raiseError(ctx,ValueError,f'Wrong parameters for {name}')
        case 'resize':
            check = True if len(params) == 3 else False
            if check:
                for param in params:
                    if param['data_type'] != "Number":
                        check = False
                        break
            if check:
                params = [params[0]['value'],int(params[1]['value']),int(params[2]['value'])]
                return params
            else:
                #THROW ERROR
                raiseError(ctx,ValueError,f'Wrong parameters for {name}')
        case 'resizeX':
            check = True if len(params) == 3 else False
            if check:
                for param in params:
                    if param['data_type'] != "Number":
                        check = False
                        break
            if check:
                params = [params[0]['value'],int(params[1]['value']),int(params[2]['value'])]
                return params
            else:
                #THROW ERROR
                raiseError(ctx,ValueError,f'Wrong parameters for {name}')
        case 'resizeY':
            check = True if len(params) == 3 else False
            if check:
                for param in params:
                    if param['data_type'] != "Number":
                        check = False
                        break
            if check:
                params = [params[0]['value'],int(params[1]['value']),int(params[2]['value'])]
                return params
            else:
                #THROW ERROR
                raiseError(ctx,ValueError,f'Wrong parameters for {name}')
        case 'fill':
            check = True if len(params) == 1 else False
            if check and (len(params[0]['value']) == 3 and params[0]['data_type'] == "Color"):
                params = params[0]['value']
                return params
            if check and (is_hexColor(params[0]['value']) or is_rgb(params[0]['value'])):
                params[0]['data_type'] = "Color"
                params = hexrgb_to_colors(params[0]['value'])
                return params
            if check:
                check = True if params[0]['data_type'] == "Color" else False
            if check:
                params = [params[0]['value']]
                return params
            else:
                raiseError(ctx,ValueError,f'Wrong parameters for {name}')
        case 'stroke':
            check = True if len(params) == 1 else False
            if check and (len(params[0]['value']) == 3 and params[0]['data_type'] == "Color"):
                params = params[0]['value']
                return params
            if check and (is_hexColor(params[0]['value']) or is_rgb(params[0]['value'])):
                params[0]['data_type'] = "Color"
                params = hexrgb_to_colors(params[0]['value'])
                return params
            if check:
                check = True if params[0]['data_type'] == "Color" else False
            if check:
                params = [params[0]['value']]
                return params
            else:
                raiseError(ctx,ValueError,f'Wrong parameters for {name}')
        case _:
            return None
    return None

def is_hexColor(value):
    regex = r'^#[0-9A-Fa-f]{6}$'
    return bool(re.match(regex,value))

def hexrgb_to_colors(value):
    colors = [0,0,0]
    if is_hexColor(value):
        colors[0] = int(value[1:3],16)
        colors[1] = int(value[3:5],16)
        colors[2] = int(value[5:],16)
    elif is_rgb(value):
        regex = r'^rgb\(\s*(\d{1,3})\,\s*(\d{1,3})\,\s*(\d{1,3})\)$'
        vals = re.match(regex,value)
        for i in range(1,4):
            colors[i-1] = int(vals.group(i))

    return colors

def rgb_to_colors(value):
    colors = [0,0,0]
    regex = r'^rgb\((\d{1,3})\,\s*(\d{1,3})\,\s*(\d{1,3})\)$'
    vals = re.match(regex,value)
    for i in range(1,4):
        colors[i-1] = vals.group(i)
    return colors

def is_rgb(value):
    regex = r'^rgb\(\s*(\d{1,3})\,\s*(\d{1,3})\,\s*(\d{1,3})\)$'
    vals = re.match(regex,value)
    if  vals != None:
        for i in range(1,4):
            if not (int(vals.group(i)) >= 0 and int(vals.group(i)) <= 255):
                return False
        return True
    else:
        return False

def check_user_params(name,params,ctx):
    func_params = user_functions[name]['parameters']
    check = True if len(params) == len(func_params) else False
    if check:
        for i in range(len(params)):
            if params[i]['data_type'] != func_params[i]['data_type']:
                check = False
                raiseError(ctx,ValueError,f"Invalid parameters for {name}")
            func_params[i]['value'] = params[i]['value']
                
    if check:
        return func_params
    else:
        raiseError(ctx,ValueError,f"Invalid parameters for {name}")

VARIABLES = defaultdict(lambda: defaultdict(default_value))
function_ctr = -1
user_functions = defaultdict()
user_function_names = []
built_in_func_names = ['point','line','curve','circle','ellipse','triangle','rectangle','quad','polygon','write','move','moveX','moveY','turn','turnC','turnCC','shear','shearX','shearY','resize','resizeX','resizeY','fill','stroke','add','remove','rand_num','rand_int','sqrt','sin','cos','tan','asin','acos','atan','atan2','to_rad','to_deg','get_input','type','info','draw']

class AniFrameParserVisitor(ParseTreeVisitor):

    def __init__(self):
        self.memory = {}

    # Visit a parse tree produced by AniFrameParser#start_.
    def visitStart_(self, ctx:AniFrameParser.Start_Context):
        self.visitChildren(ctx)
        mapping.write(mapping.print_src_code())
        return

    def visitDraw_statement(self, ctx:AniFrameParser.Draw_statementContext):
        var_name = ctx.getChild(0).getText()
        params = self.visit(ctx.getChild(4))

        result = check_parameters('draw',params,ctx)
        if result == None:
            raiseError(ctx,ValueError,f'Invalid parameters for draw')
        if VARIABLES.get(var_name) == None:
            raiseError(ctx,ValueError,f'identifier {var_name} does not exist')
        if VARIABLES[var_name]['data_type'] != "Object":
            raiseError(ctx,TypeError,f"{VARIABLES[var_name]['data_type']} does not have method draw")
        
        mapping.draw(var_name,result[0],result[1])

        return
    # Visit a parse tree produced by AniFrameParser#simple_statement.
    def visitSimple_statement(self, ctx:AniFrameParser.Simple_statementContext):
        global function_ctr
        if ctx.getChildCount() == 4:
            var_name = ctx.getChild(0).getText()
            func_name,result = self.visit(ctx.getChild(2))

            if VARIABLES.get(var_name) == None:
                raiseError(ctx,ValueError,f'identifier {var_name} does not exist')
            result  = check_parameters(func_name,result,ctx)
            if result == None:
                raiseError(ctx,ValueError,f'{func_name} parameters are invalid')

            if VARIABLES[var_name]['data_type'] == 'List':
                if func_name == 'add':
                    if isinstance(result[0],dict):
                        VARIABLES[var_name]['value'].append(result[0])
                    else:
                        raiseError(ctx,TypeError,f"List variables cannot add objects")
                elif func_name == 'remove':
                    if result[0] >= len(VARIABLES[var_name]['value']) or result[0] < 0:
                        raiseError(ctx,ValueError,f"List index out of range")
                    VARIABLES[var_name]['value'].pop(result[0])
                else:
                    raiseError(ctx,TypeError,f"List does not have method {func_name}")
                    
            elif VARIABLES[var_name]['data_type'] == "Object":
                match func_name:
                    case 'add':
                        # result[0] should be identifier of object
                        iden = mapping.convert_object_add_to_p5(var_name,result[0])
                        mapping.convert_object_assign_to_p5(var_name,iden)
                    case 'draw':
                        mapping.draw(var_name,result[0],result[1])
                    case 'turn':
                        mapping.convert_rotate_to_p5(var_name,result[0],result[1],result[2])
                    case 'turnC':
                        mapping.convert_rotateC_to_p5(var_name,result[0],result[1],result[2])
                    case 'turnCC':
                        mapping.convert_rotateCC_to_p5(var_name,result[0],result[1],result[2])
                    case 'move':
                        mapping.convert_move_to_p5(var_name,result[0],result[1],result[2],result[3])
                    case 'moveX':
                        mapping.convert_moveX_to_p5(var_name,result[0],result[1],result[2])
                    case 'moveY':
                        mapping.convert_moveY_to_p5(var_name,result[0],result[1],result[2])
                    case 'shear':
                        mapping.convert_shear_to_p5(var_name,result[0],result[1],result[2])
                    case 'shearX':
                        mapping.convert_shearX_to_p5(var_name,result[0],result[1],result[2])
                    case 'shearY':
                        mapping.convert_shearY_to_p5(var_name,result[0],result[1],result[2])
                    case 'write':
                        mapping.convert_write_to_p5(var_name,result[0],result[1],result[2])
                    case 'resize':
                        mapping.convert_resize_to_p5(var_name,result[0],result[1],result[2])
                    case 'resizeX':
                        mapping.convert_resizeX_to_p5(var_name,result[0],result[1],result[2])
                    case 'resizeY':
                        mapping.convert_resizeY_to_p5(var_name,result[0],result[1],result[2])
                    case 'fill':
                        mapping.convert_fill_to_p5(var_name,result[0],result[1],result[2])
                    case 'stroke':
                        mapping.convert_stroke_to_p5(var_name,result[0],result[1],result[2])
                    case _:
                        raiseError(ctx,ValueError,f"List does not have method {func_name}")
            else:
                raiseError(ctx,TypeError,f"{VARIABLES[var_name]['data_type']} method calls are not supported")

        else:
            stmnt = self.visit(ctx.getChild(0))
            if isinstance(stmnt,defaultdict) or isinstance(stmnt,dict):
                return
            var_name = stmnt[0]
            if var_name in VARIABLES:
                return
            
            func_name,params = self.visit(ctx.getChild(0)) 
            result = check_parameters(func_name,params,ctx)
            match func_name:
                case 'type':
                    print(result[0]['data_type'])
                case 'info':
                    if result[0]['data_type'] == "Object":
                        print(mapping.CLASSES[mapping.clean_identifier(result[0]['identifier'])])
                    elif result[0]['data_type'] == "Color":
                        print(f"rgb{result[0]['value'][0],result[0]['value'][1],result[0]['value'][2]}")
                    else:
                        print(result[0]['value'])
                case 'length':
                    check = True if len(params) == 1 else False
                    if check:
                        check = True if params[0]['data_type'] == "List" else False
                    if check:
                        return
                    else:
                        raiseError(ctx,ValueError,f'Wrong parameters for {func_name}')
                case func_name if func_name in user_function_names:
                        context = user_functions[func_name]['context']
                        return_value = user_functions[func_name]['returns']
                        function_ctr +=1
                        val = self.visitFunction_declaration_definition(context,params,return_value)
                        function_ctr-=1
                        if val == None:
                            return
                        return val
                case _: 
                    raiseError(ctx,ValueError,f"{func_name} is not a valid function")

        return
    # Visit a parse tree produced by AniFrameParser#compound_statement.
    def visitCompound_statement(self, ctx:AniFrameParser.Compound_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AniFrameParser#expression.
    def visitExpression(self, ctx:AniFrameParser.ExpressionContext):
        global function_ctr
        if ctx.getChildCount() == 3:
            #Take the value in parenthesis
            if ctx.getChild(0).getText() == "(":
                return self.visit(ctx.getChild(1))
            expr1 = self.visit(ctx.getChild(0))
            operator = ctx.getChild(1).getText()
            expr2 = self.visit(ctx.getChild(2))

            if expr1['data_type'] == '_':
                #THROW ERROR
                raiseError(ctx,ValueError,f'Identifier {expr1["identifier"]} has not been initialized')
            if expr2['data_type'] == '_':
                #THROW ERROR
                raiseError(ctx,ValueError,f'Identifier {expr2["identifier"]} has not been initialized')
            match operator:
                case '+':
                    match expr1['data_type'],expr2['data_type']:
                        case "Object","Object":
                            iden = mapping.convert_object_add_to_p5(expr1['identifier'],expr2['identifier'])
                            return {'value': mapping.CLASSES[iden], 'data_type': "Object", "identifier": iden}
                        case "Number","Number":
                            res = expr1['value'] + expr2['value']
                            return {'value': res, 'data_type': "Number"}
                        case "Text","Text":
                            res = expr1['value'] + expr2['value']
                            return {'value': res, 'data_type': "Text"}
                        case "Color","Color":
                            res = [int((expr1['value'][0] + expr2['value'][0])/2),int((expr1['value'][1] + expr2['value'][1])/2),int((expr1['value'][2] + expr2['value'][2])/2)]
                            return {'value': res, 'data_type': "Color"}
                        case "Color","Text":
                            iscolor = is_rgb(expr2['value']) or is_hexColor(expr2['value'])
                            if iscolor:
                                colors = hexrgb_to_colors(expr2['value'])
                            else:
                                raiseError(ctx,TypeError,f"{operator} operator between {expr1['data_type']} and {expr2['data_type']} is not supported")
                            res = [int((expr1['value'][0] + colors[0])/2),int((expr1['value'][1] + colors[1])/2),int((expr1['value'][2] + colors[2])/2)]
                            return {'value': res, 'data_type': "Color"}
                        case "Text","Color":
                            iscolor = is_rgb(expr1['value']) or is_hexColor(expr1['value'])
                            if iscolor:
                                colors = hexrgb_to_colors(expr1['value'])
                            else:
                                raiseError(ctx,TypeError,f"{operator} operator between {expr1['data_type']} and {expr2['data_type']} is not supported")
                            res = [int((expr2['value'][0] + colors[0])/2),int((expr2['value'][1] + colors[1])/2),int((expr2['value'][2] + colors[2])/2)]
                            return {'value': res, 'data_type': "Color"}
                        case "Coord","Coord":
                            res = (expr1['value'][0] + expr2['value'][0],expr1['value'][1] + expr2['value'][1])
                            return {'value': res, 'data_type': "Coord"}
                        case "List","List":
                            res = expr1['value'] + expr2['value']
                            return {'value': res, 'data_type': "List"}
                        case _:
                            # throw error
                            raiseError(ctx,TypeError,f"{operator} operator between {expr1['data_type']} and {expr2['data_type']} is not supported")
                case "-":
                    match expr1['data_type'],expr2['data_type']:
                        case "Number","Number":
                            res = expr1['value'] - expr2['value']
                            return {'value': res, 'data_type': "Number"}
                        case "Color","Color":
                            expr2['value'] = invert(expr2['value'])
                            res = [int((expr1['value'][0] + expr2['value'][0])/2),int((expr1['value'][1] + expr2['value'][1])/2),int((expr1['value'][2] + expr2['value'][2])/2)]
                            return {'value': res, 'data_type': "Color"}
                        case "Color","Text":
                            iscolor = is_rgb(expr2['value']) or is_hexColor(expr2['value'])
                            if iscolor:
                                colors = invert(hexrgb_to_colors(expr2['value']))
                            else:
                                raiseError(ctx,TypeError,f"{operator} operator between {expr1['data_type']} and {expr2['data_type']} is not supported")
                            res = [int((expr1['value'][0] + colors[0])/2),int((expr1['value'][1] + colors[1])/2),int((expr1['value'][2] + colors[2])/2)]
                            return {'value': res, 'data_type': "Color"}
                        case "Text","Color":
                            iscolor = is_rgb(expr1['value']) or is_hexColor(expr1['value'])
                            if iscolor:
                                colors = hexrgb_to_colors(expr1['value'])
                                colors2 = invert(expr2['value'])
                            else:
                                raiseError(ctx,TypeError,f"{operator} operator between {expr1['data_type']} and {expr2['data_type']} is not supported")
                            res = [int((colors[0] + colors2[0] )/2),int((colors[1] + colors2[1] )/2),int((colors[1] + colors2[1] )/2)]
                            return {'value': res, 'data_type': "Color"}
                        case "Coord","Coord":
                            res = (expr1['value'][0] - expr2['value'][0],expr1['value'][1] - expr2['value'][1])
                            return {'value': res, 'data_type': "Coord"}
                        case _:
                            #throw error
                            raiseError(ctx,TypeError,f"{operator} operator between {expr1['data_type']} and {expr2['data_type']} is not supported")
                case "*":
                    match expr1['data_type'],expr2['data_type']:
                        case "Number","Number":
                            res = expr1['value'] * expr2['value']
                            return {'value': res, 'data_type': "Number"}
                        case "Coord","Number":
                            res = (expr1['value'][0] * expr2['value'],expr1['value'][1] * expr2['value'])
                            return {'value': res, 'data_type': "Coord"}
                        case "Number","Coord":
                            res = (expr1['value'] * expr2['value'][0],expr1['value'] * expr2['value'][1])
                            return {'value': res, 'data_type': "Coord"}
                        case "Coord","Coord":
                            res = (expr1['value'][0] * expr2['value'][0],expr1['value'][1] * expr2['value'][1])
                            return {'value': res, 'data_type': "Coord"}
                        case _:
                            #throw error
                            raiseError(ctx,TypeError,f"{operator} operator between {expr1['data_type']} and {expr2['data_type']} is not supported")
                case "/":
                    match expr1['data_type'],expr2['data_type']:
                        case "Number","Number":
                            res = expr1['value'] / expr2['value']
                            return {'value': res, 'data_type': "Number"}
                        case "Coord","Number":
                            res = (expr1['value'][0] / expr2['value'],expr1['value'][1] / expr2['value'])
                        case "Coord","Coord":
                            res = (expr1['value'][0] / expr2['value'][0],expr1['value'][1] / expr2['value'][1])
                            return {'value': res, 'data_type': "Coord"}    
                        case _:
                            # throw error
                            raiseError(ctx,TypeError,f"{operator} operator between {expr1['data_type']} and {expr2['data_type']} is not supported")
                case "%":
                    match expr1['data_type'],expr2['data_type']:
                        case "Number","Number":
                            res = int(expr1['value']) % int(expr2['value'])
                            return {'value': res, 'data_type': "Number"}
                        case _:
                            # throw error
                            raiseError(ctx,TypeError,f"{operator} operator between {expr1['data_type']} and {expr2['data_type']} is not supported")
                case "<":
                    match expr1['data_type'],expr2['data_type']:
                        case "Number","Number":
                            res = 1 if expr1['value'] < expr2['value'] else 0
                            return {'value': res, 'data_type': "Number"}
                        case "Text","Text":
                            res = 1 if expr1['value'] < expr2['value'] else 0
                            return {'value': res, 'data_type': "Number"}
                        case "Color","Color":
                            res = 0
                            for i in range(3):
                                comp = expr1['value'][i] - expr2['value'][i]
                                if comp < 0:
                                    res = 1
                                    break
                            return {'value': res, 'data_type': "Number"}
                        case "Coord","Coord":
                            res = 1 if expr1['value'][0] < expr2['value'][0] or (expr1['value'][0] == expr2['value'][0] and expr1['value'][1] < expr2['value']['1']) else 0
                            return {'value': res, 'data_type': "Number"}
                        case _:
                            # throw error
                            raiseError(ctx,TypeError,f"{operator} operator between {expr1['data_type']} and {expr2['data_type']} is not supported")
                case ">":
                    match expr1['data_type'],expr2['data_type']:
                        case "Number","Number":
                            res = 1 if expr1['value'] > expr2['value'] else 0
                            return {'value': res, 'data_type': "Number"}
                        case "Text","Text":
                            res = 1 if expr1['value'] < expr2['value'] else 0
                            return {'value': res, 'data_type': "Number"}
                        case "Color","Color":
                            res = 0
                            for i in range(3):
                                comp = expr1['value'][i] - expr2['value'][i]
                                if comp > 0:
                                    res = 1
                                    break
                            return {'value': res, 'data_type': "Number"}
                        case "Coord", "Coord":
                            res = 1 if expr1['value'][0] > expr2['value'][0] or (expr1['value'][0] == expr2['value'][0] and expr1['value'][1] > expr2['value']['1']) else 0
                            return {'value': res, 'data_type': "Number"}
                        case _:
                            # throw error
                            raiseError(ctx,TypeError,f"{operator} operator between {expr1['data_type']} and {expr2['data_type']} is not supported")
                case "<=":
                    match expr1['data_type'],expr2['data_type']:
                        case "Number","Number":
                            res = 1 if expr1['value'] <= expr2['value'] else 0
                            return {'value': res, 'data_type': "Number"}
                        case "Text","Text":
                            res = 1 if expr1['value'] <= expr2['value'] else 0
                            return {'value': res, 'data_type': "Number"}
                        case "Color","Color":
                            res = 0
                            for i in range(3):
                                comp = expr1['value'][i] - expr2['value'][i]
                                if comp <= 0:
                                    res = 1
                                    break
                            return {'value': res, 'data_type': "Number"}
                        case "Coord", "Coord":
                            res = 1 if expr1['value'][0] <= expr2['value'][0] else 0
                            return {'value': res, 'data_type': "Number"}
                        case _:
                            # throw error
                            raiseError(ctx,TypeError,f"{operator} operator between {expr1['data_type']} and {expr2['data_type']} is not supported")
                case ">=":
                    match expr1['data_type'],expr2['data_type']:
                        case "Number","Number":
                            res = 1 if expr1['value'] >= expr2['value'] else 0
                            return {'value': res, 'data_type': "Number"}
                        case "Text","Text":
                            res = 1 if expr1['value'] >= expr2['value'] else 0
                            return {'value': res, 'data_type': "Number"}
                        case "Color","Color":
                            res = 0
                            for i in range(3):
                                comp = expr1['value'][i] - expr2['value'][i]
                                if comp <= 0:
                                    res = 1
                                    break
                            return {'value': res, 'data_type': "Number"}
                        case "Coord", "Coord":
                            res = 1 if expr1['value'][0] >= expr2['value'][0] else 0
                            return {'value': res, 'data_type': "Number"}
                        case _:
                            # throw error
                            raiseError(ctx,TypeError,f"{operator} operator between {expr1['data_type']} and {expr2['data_type']} is not supported")
                case "==":
                    match expr1['data_type'],expr2['data_type']:
                        case "Number","Number":
                            res = 1 if expr1['value'] == expr2['value'] else 0
                            return {'value': res, 'data_type': "Number"}
                        case "Text","Text":
                            res = 1 if expr1['value'] == expr2['value'] else 0
                            return {'value': res, 'data_type': "Number"}
                        case "Color","Color":
                            res = 1 if expr1['value'] == expr2['value'] else 0
                            return {'value': res, 'data_type': "Number"}
                        case "Coord", "Coord":
                            res = 1 if expr1['value'] == expr2['value'] else 0
                            return {'value': res, 'data_type': "Number"}
                        case _:
                            # throw error
                            raiseError(ctx,TypeError,f"{operator} operator between {expr1['data_type']} and {expr2['data_type']} is not supported")
                case "!=":
                    match expr1['data_type'],expr2['data_type']:
                        case "Number","Number":
                            res = 0 if expr1['value'] == expr2['value'] else 1
                            return {'value': res, 'data_type': "Number"}
                        case "Text","Text":
                            res = 0 if expr1['value'] == expr2['value'] else 1
                            return {'value': res, 'data_type': "Number"}
                        case "Color","Color":
                            res = 0 if expr1['value'] == expr2['value'] else 1
                            return {'value': res, 'data_type': "Number"}
                        case "Coord", "Coord":
                            res = 0 if expr1['value'] == expr2['value'] else 1
                            return {'value': res, 'data_type': "Number"}
                        case _:
                            # throw error
                            raiseError(ctx,TypeError,f"{operator} operator between {expr1['data_type']} and {expr2['data_type']} is not supported")
                case "in":
                    #TODO refine this
                    match expr2['data_type']:
                        case "List":
                            res = 1 if expr1['value'] in expr2['value'] else 0
                            return {'value': res, 'data_type': "Number"}
                        case "Text":
                            if expr1['data_type'] == "Text":
                                res = 1 if expr1['value'] in expr2['value'] else 0
                                return {'value': res, 'data_type': "Number"}
                        case _:
                            # throw error
                            raiseError(ctx,TypeError,f"{operator} operator between {expr1['data_type']} and {expr2['data_type']} is not supported")
                case "&&":
                    match expr1['data_type'],expr2['data_type']:
                        case "Number","Number":
                            res = 1 if expr1['value'] and expr2['value'] else 0
                            return {'value': res, 'data_type': "Number"}
                        case _:
                            # throw error
                            raiseError(ctx,TypeError,f"{operator} operator between {expr1['data_type']} and {expr2['data_type']} is not supported")
                case "||":
                    match expr1['data_type'],expr2['data_type']:
                        case "Number","Number":
                            res = 1 if expr1['value'] or expr2['value'] else 0
                            return {'value': res, 'data_type': "Number"}
                        case _:
                            # throw error
                            raiseError(ctx,TypeError,f"{operator} operator between {expr1['data_type']} and {expr2['data_type']} is not supported")         
                case _:
                    raiseError(ctx,ValueError,f'Expression operator {operator} does not exist')
        elif ctx.getChildCount() == 2:
            opr = ctx.getChild(0).getText()
            expr = self.visit(ctx.getChild(1))
            if opr == '!':
                res = 1 if not expr['value'] else 0 
                return {'value': res, 'data_type': "Number"}
            else:
                if expr['data_type'] != "Number":
                    #THROW SOME ERROR
                    raiseError(ctx,TypeError,f'Unary operator {opr} cannot be evaluated with {expr["data_type"]}')
                res = eval("".join([opr,str(expr['value'])]))
                return {'value': res, 'data_type': "Number"}
        elif ctx.getChildCount() == 1:
            val = self.visit(ctx.getChild(0))
            
            if isinstance(val,dict):
                return val
            else:
                func_name,params = self.visit(ctx.getChild(0))

                match func_name:
                    case 'length':
                        check = True if len(params) == 1 else False
                        if check:
                            check = True if params[0]['data_type'] == "List" else False
                        if check:
                            return {'value': len(params[0]['value']), 'data_type': "Number"}
                        else:
                            raiseError(ctx,ValueError,f'Wrong parameters for {func_name}')
                    case 'get_input':
                        check = True if len(params) == 1 else False
                        if check:
                            if params[0]['data_type'] != "Text":
                                check = False
                        if check:
                            try:
                                file = open(params[0]['value'],'r')
                                lines = [line[:-2] for line in file.readlines()]
                                file.close()
                            except:
                                raiseError(ctx,ValueError,f'File {params[0]["value"]} does not exist')
                            return {'value': lines, 'data_type': 'List'}
                        else:
                            raiseError(ctx,ValueError,f'Wrong parameters for {func_name}')
                    case 'type':
                        check = check_parameters('type',params,ctx)
                        if check:
                            # print(check[0]['data_type'])
                            return {'value': check[0]['data_type'], 'data_type': 'Text'}
                        else:
                            raiseError(ctx,ValueError,f'Wrong parameters for {func_name}')
                    case 'sqrt':
                        check = True if len(params) == 1 else False
                        if check:
                            for param in params:
                                if param['data_type'] != "Number":
                                    check = False
                                    break
                        if check:
                            return {'value': math.sqrt(params[0]['value']), 'data_type': 'Number'}
                        else:
                            #THROW ERROR
                            raiseError(ctx,ValueError,f'Wrong parameters for {func_name}')
                    case 'sin':
                        check = True if len(params) == 1 else False
                        if check:
                            for param in params:
                                if param['data_type'] != "Number":
                                    check = False
                                    break
                        if check:
                            return {'value': math.sin(params[0]['value']), 'data_type': 'Number'}
                        else:
                            #THROW ERROR
                            raiseError(ctx,ValueError,f'Wrong parameters for {func_name}')
                    case 'cos':
                        check = True if len(params) == 1 else False
                        if check:
                            for param in params:
                                if param['data_type'] != "Number":
                                    check = False
                                    break
                        if check:
                            return {'value': math.cos(params[0]['value']), 'data_type': 'Number'}
                        else:
                            #THROW ERROR
                            raiseError(ctx,ValueError,f'Wrong parameters for {func_name}')
                    case 'tan':
                        check = True if len(params) == 1 else False
                        if check:
                            for param in params:
                                if param['data_type'] != "Number":
                                    check = False
                                    break
                        if check:
                            return {'value': math.tan(params[0]['value']), 'data_type': 'Number'}
                        else:
                            #THROW ERROR
                            raiseError(ctx,ValueError,f'Wrong parameters for {func_name}')
                    case 'asin':
                        check = True if len(params) == 1 else False
                        if check:
                            for param in params:
                                if param['data_type'] != "Number":
                                    check = False
                                    break
                        if check:
                            return {'value': math.asin(params[0]['value']), 'data_type': 'Number'}
                        else:
                            #THROW ERROR
                            raiseError(ctx,ValueError,f'Wrong parameters for {func_name}')
                    case 'acos':
                        check = True if len(params) == 1 else False
                        if check:
                            for param in params:
                                if param['data_type'] != "Number":
                                    check = False
                                    break
                        if check:
                            return {'value': math.acos(params[0]['value']), 'data_type': 'Number'}
                        else:
                            #THROW ERROR
                            raiseError(ctx,ValueError,f'Wrong parameters for {func_name}')
                    case 'atan':
                        check = True if len(params) == 1 else False
                        if check:
                            for param in params:
                                if param['data_type'] != "Number":
                                    check = False
                                    break
                        if check:
                            return {'value': math.atan(params[0]['value']), 'data_type': 'Number'}
                        else:
                            #THROW ERROR
                            raiseError(ctx,ValueError,f'Wrong parameters for {func_name}')
                    case 'atan2':
                        check = True if len(params) == 1 else False
                        if check:
                            for param in params:
                                if param['data_type'] != "Number":
                                    check = False
                                    break
                        if check:
                            return {'value': math.atan2(params[0]['value']), 'data_type': 'Number'}
                        else:
                            #THROW ERROR
                            raiseError(ctx,ValueError,f'Wrong parameters for {func_name}')
                    case 'to_rad':
                        check = True if len(params) == 1 else False
                        if check:
                            for param in params:
                                if param['data_type'] != "Number":
                                    check = False
                                    break
                        if check:
                            return {'value': math.radians(params[0]['value']), 'data_type': 'Number'}
                        else:
                            #THROW ERROR
                            raiseError(ctx,ValueError,f'Wrong parameters for {func_name}')
                    case 'to_deg':
                        check = True if len(params) == 1 else False
                        if check:
                            for param in params:
                                if param['data_type'] != "Number":
                                    check = False
                                    break
                        if check:
                            return {'value': math.degrees(params[0]['value']), 'data_type': 'Number'}
                        else:
                            #THROW ERROR
                            raiseError(ctx,ValueError,f'Wrong parameters for {func_name}')        
                    case 'rand_num':
                        check = True if len(params) == 2 else False
                        if check:
                            for param in params:
                                if param['data_type'] != "Number":
                                    check = False
                                    break
                        if check:
                            return {'value': random.uniform(params[0]['value'],params[1]['value']), 'data_type': 'Number'}
                        else:
                            #THROW ERROR
                            raiseError(ctx,ValueError,f'Wrong parameters for {func_name}')
                    case 'rand_int':
                        check = True if len(params) == 2 else False
                        if check:
                            for param in params:
                                if param['data_type'] != "Number":
                                    check = False
                                    break
                        if check:
                            return {'value': random.randint(int(params[0]['value']),int(params[1]['value'])), 'data_type': 'Number'}
                        else:
                            #THROW ERROR
                            raiseError(ctx,ValueError,f'Wrong parameters for {func_name}')
                    case 'point':
                        check = True if len(params) == 2 else False
                        if check:
                            for param in params:
                                if param['data_type'] != "Number":
                                    check = False
                                    break
                        if check:
                            params = [param['value'] for param in params]
                            return {'value': [func_name,params], 'data_type': 'Object'}
                        else:
                            #THROW ERROR
                            raiseError(ctx,ValueError,f'Wrong parameters for {func_name}')
                    case 'line':
                        check = True if len(params) == 4 else False
                        if check:
                            for param in params:
                                if param['data_type'] != "Number":
                                    check = False
                                    break
                            
                        if check:
                            return {'value': [func_name,params], 'data_type': 'Object'}
                        else:
                            #THROW ERROR
                            raiseError(ctx,ValueError,f'Wrong parameters for {func_name}')
                    case 'curve':
                        check = True if len(params) == 8 else False
                        if check:
                            for param in params:
                                if param['data_type'] != "Number":
                                    check = False
                                    break
                            
                        if check:
                            params = [param['value'] for param in params]
                            return {'value': [func_name,params], 'data_type': 'Object'}
                        else:
                            #THROW ERROR
                            raiseError(ctx,ValueError,f'Wrong parameters for {func_name}')
                    case 'circle':
                        check = True if len(params) == 3 else False
                        if check:
                            for param in params:
                                if param['data_type'] != "Number":
                                    check = False
                                    break
                            
                        if check:
                            params = [param['value'] for param in params]
                            return {'value': [func_name,params], 'data_type': 'Object'}
                        else:
                            #THROW ERROR
                            raiseError(ctx,ValueError,f'Wrong parameters for {func_name}')
                    case 'ellipse':
                        check = True if len(params) == 4 else False
                        if check:
                            for param in params:
                                if param['data_type'] != "Number":
                                    check = False
                                    break
                            
                        if check:
                            params = [param['value'] for param in params]
                            return {'value': [func_name,params], 'data_type': 'Object'}
                        else:
                            #THROW ERROR
                            raiseError(ctx,ValueError,f'Wrong parameters for {func_name}')
                    case 'triangle':
                        check = True if len(params) == 6 else False
                        if check:
                            for param in params:
                                if param['data_type'] != "Number":
                                    check = False
                                    break
                            
                        if check:
                            params = [param['value'] for param in params]
                            return {'value': [func_name,params], 'data_type': 'Object'}
                        else:
                            #THROW ERROR
                            raiseError(ctx,ValueError,f'Wrong parameters for {func_name}')
                    case 'rectangle':
                        check = True if len(params) == 4 else False
                        if check:
                            for param in params:
                                if param['data_type'] != "Number":
                                    check = False
                                    break
                            
                        if check:
                            params = [param['value'] for param in params]
                            return {'value': [func_name,params], 'data_type': 'Object'}
                        else:
                            #THROW ERROR
                            raiseError(ctx,ValueError,f'Wrong parameters for {func_name}')
                    case 'quad':
                        check = True if len(params) == 8 else False
                        if check:
                            for param in params:
                                if param['data_type'] != "Number":
                                    check = False
                                    break
                            
                        if check:
                            params = [param['value'] for param in params]
                            return {'value': [func_name,params], 'data_type': 'Object'}
                        else:
                            #THROW ERROR
                            raiseError(ctx,ValueError,f'Wrong parameters for {func_name}')
                    case 'polygon':
                        check = True if len(params) == 1 else False
                        if check:
                            for param in params:
                                if param['data_type'] != "List":
                                    check = False
                                    break
                                for item in param['value']:
                                    if item['data_type'] != "Coord":
                                        check = False
                                        break
                            
                        if check:
                            params = [coord['value'] for coord in param['value'] for param in params]
                            return {'value': [func_name,params], 'data_type': 'Object'}
                        else:
                            #THROW ERROR
                            raiseError(ctx,ValueError,f'Wrong parameters for {func_name}')
                    case func_name if func_name in user_function_names:
                        context = user_functions[func_name]['context']
                        return_value = user_functions[func_name]['returns']
                        function_ctr+=1
                        val = self.visitFunction_declaration_definition(context,params,return_value)
                        function_ctr-=1
                        if val == None:
                            raiseError(ctx,ValueError,f"{func_name} has no return value")
                        return val
                    case _:
                        raiseError(ctx,ValueError,f"{func_name} is not a valid function")
    # Visit a parse tree produced by AniFrameParser#coordinates.
    def visitCoordinates(self, ctx:AniFrameParser.CoordinatesContext):
        x_val = self.visit(ctx.getChild(1))
        y_val = self.visit(ctx.getChild(3))
        if x_val['data_type'] != "Number" or y_val['data_type'] != "Number":
            #throw error
            raiseError(ctx,ValueError,f'Coordinates must be numbers')
        return {'value': (x_val['value'],y_val['value']), 'data_type': "Coord"}


    # Visit a parse tree produced by AniFrameParser#list.
    def visitList(self, ctx:AniFrameParser.ListContext):
        res = []
        for i in range(1,ctx.getChildCount()-1,2):
            val = self.visit(ctx.getChild(i))
            if val['data_type'] == "List":
                #throw error
                raiseError(ctx,ValueError,f'List cannot be inside of list')
            res.append(val)
        
        return {'value': res, 'data_type': "List"}


    # Visit a parse tree produced by AniFrameParser#member.
    def visitMember(self, ctx:AniFrameParser.MemberContext):
        iden = ctx.getChild(0).getText()
        expr = self.visit(ctx.getChild(2))
        expr_2 = {'value': 0, 'data_type': None}
        children = ctx.getChildCount()
        if  children > 4:
            expr_2 = self.visit(ctx.getChild(5))
        if expr['data_type'] != "Number" or expr_2['data_type'] != "Number" and expr_2['data_type'] != None:
            #throw error
            raiseError(ctx,TypeError,f'Invalid index data type')
        idx = int(expr['value'])
        if VARIABLES[iden]['data_type'] == "List" or VARIABLES[iden]['data_type'] == "Coord":
            list_len =  len(VARIABLES[iden]['value'])
            if idx >= list_len or idx < 0 or expr_2['value'] > 1:
                #throw error
                raiseError(ctx,ValueError,f'List index out of range')
            else:
                if children > 4:
                    if VARIABLES[iden]['value'][idx]['data_type'] != 'Coord':
                        #throw error
                        raiseError(ctx,TypeError,f"{VARIABLES[iden]['value'][idx]['data_type']} is not iterable")
                    idx2 = int(expr_2['value'])
                    val = VARIABLES[iden]['value'][idx]['value'][idx2]
                    dtype = "Number"
                    identi = VARIABLES[iden]['value'][idx].get('identifier')
                else:
                    if VARIABLES[iden]['data_type'] == "List":
                        val = VARIABLES[iden]['value'][idx]['value']
                        dtype = VARIABLES[iden]['value'][idx]['data_type']
                        identi = VARIABLES[iden]['value'][idx].get('identifier')
                    elif VARIABLES[iden]['data_type'] == "Coord":
                        val  = VARIABLES[iden]['value'][idx]
                        dtype = "Number"
                        try:
                            identi = VARIABLES[iden]['value'][idx].get('identifier')
                        except:
                            identi = None
                return {'value': val, 'data_type': dtype, 'identifier' : identi}
        else:
            #throw error not a list
            raiseError(ctx,TypeError,f'{iden} is not iterable')

    # Visit a parse tree produced by AniFrameParser#function_call.
    def visitFunction_call(self, ctx:AniFrameParser.Function_callContext):
        func_name = ctx.getChild(0).getText()
        if func_name not in built_in_func_names and func_name not in user_function_names:
            raiseError(ctx,ValueError,f'Function {func_name} is not defined')
        else:
            if ctx.getChild(2).getText() != ')':
                params = self.visit(ctx.getChild(2))
            else:
                params = []
        if func_name in user_function_names:
            new_params = check_user_params(func_name,params,ctx)
            return func_name,new_params
        
        else:
            return func_name,params
    # Visit a parse tree produced by AniFrameParser#actual_parameters.
    def visitActual_parameters(self, ctx:AniFrameParser.Actual_parametersContext):
        children = ctx.getChildCount()
        params = []
        for i in range(0,children,2):
            #get each parameter
            params.append(self.visit(ctx.getChild(i)))
        return params
        


    # Visit a parse tree produced by AniFrameParser#actual_parameter.
    def visitActual_parameter(self, ctx:AniFrameParser.Actual_parameterContext):
        return self.visit(ctx.getChild(0))


    # Visit a parse tree produced by AniFrameParser#positional_argument.
    def visitPositional_argument(self, ctx:AniFrameParser.Positional_argumentContext):
        return self.visit(ctx.getChild(0))

    # Visit a parse tree produced by AniFrameParser#variable_declaration.
    def visitVariable_declaration(self, ctx:AniFrameParser.Variable_declarationContext):
        iden,dtype = ctx.getText().split(':')
        if not valid_dtype(dtype):
            #THROW ERROR
            raiseError(ctx,ValueError,f'{dtype} is an invalid data type')
        if VARIABLES[iden]['data_type'] == '_' or 'data_type' not in VARIABLES[iden] or VARIABLES[iden]['data_type'] == dtype:
            VARIABLES[iden]['data_type'] = dtype 
            VARIABLES[iden]['identifier'] = iden
            if dtype == "Object":
                mapping.convert_object_new_to_p5(iden)
            return VARIABLES[iden]
        else:
            #THROW SOME ERROR
            raiseError(ctx,TypeError,f'{iden} has already been declared with data type {VARIABLES[iden]["data_type"]}')


    # Visit a parse tree produced by AniFrameParser#assignment_statement.
    def visitAssignment_statement(self, ctx:AniFrameParser.Assignment_statementContext):
        idxstart = 0
        constant = False
        if ctx.getChild(0).getText() == 'const':
            idxstart = 1
            constant = True

        val = ctx.getChild(idxstart).getText()
        assignment = ctx.getChild(idxstart+1).getText()
        expr = self.visit(ctx.getChild(idxstart+2))

        if expr.get('value') == None:
            iden = expr['identifier']
            raiseError(ctx,NameError,f"Identifier {iden} is not defined")

        #assign to array access member
        if '[' == ctx.getChild(1).getText():
            iden = ctx.getChild(0).getText()
            idx = self.visit(ctx.getChild(2))
            expr = self.visit(ctx.getChild(5))
            assignment = ctx.getChild(4).getText()
            res = assign_member_value(iden,idx['value'],expr,assignment,ctx)
            return res

        
        if ':' in val:
            self.visit(ctx.getChild(idxstart))
            val,_ = val.split(':')
        else:
            VARIABLES[val]['data_type'] = '_' if 'data_type' not in VARIABLES[val] else VARIABLES[val]['data_type']
        
        if expr['data_type'] == "Object":
            if not isinstance(expr['value'],OrderedDict):
                object_expr_iden = mapping.convert_object_expr_to_p5(expr['value'][0],expr['value'][1])
            else:
                object_expr_iden = expr.get('identifier')
        #TODO implement text to color convert
        if len(assignment) == 1:
            if 'constant' in VARIABLES[val]:
                #THROW SOME ERROR SINCE CONSTANT
                raiseError(ctx,TypeError,f'Cannot change value of const variable {val}')
            elif VARIABLES[val]['data_type'] == "Color" and expr['data_type'] == "Text":
                color = is_hexColor(expr['value']) or is_rgb(expr['value']) 
                if color:
                    VARIABLES[val]['value'] = hexrgb_to_colors(expr['value'])
                    return val, VARIABLES[val]
                else:
                    raiseError(ctx,TypeError,f'Invalid assignment statement. Text can not be converted to color')
            else:
                if VARIABLES[val]['data_type'] == expr['data_type'] or VARIABLES[val]['data_type'] == '_':
                    VARIABLES[val]['value'] = expr['value']
                    if VARIABLES[val]['data_type'] == '_':
                        VARIABLES[val]['data_type'] = expr['data_type']
                        if expr['data_type'] == "Object":
                            mapping.convert_object_new_to_p5(val)
                    if constant:
                        VARIABLES[val]['constant'] = True
                    VARIABLES[val]['identifier'] = val
                    if  VARIABLES[val]['data_type'] == "Object" and expr['data_type'] == "Object":
                        mapping.convert_object_assign_to_p5(val,object_expr_iden)
                    return val,VARIABLES[val]
                else:
                    raiseError(ctx,TypeError,f'Invalid assignment statement. Data type mismatch')


        elif len(assignment) == 2 and not VARIABLES[val].get('constant'):
            #COMPOUND STATEMENTS
            if VARIABLES[val]['data_type'] == '_':
                #THROW ERROR
                raiseError(ctx,ValueError,f'Identifier {val} has not been initialized')
            match assignment[0]:
                case '+':
                    match VARIABLES[val]['data_type'],expr['data_type']:
                        case "Object","Object":
                            iden = mapping.convert_object_add_to_p5(val,object_expr_iden)
                            mapping.convert_object_assign_to_p5(val,iden)
                            return val, VARIABLES[val]
                        case "Number","Number":
                            VARIABLES[val]['value'] += expr['value']
                            return val,VARIABLES[val]
                        case "Text","Text":
                            VARIABLES[val]['value'] += expr['value']
                            return val,VARIABLES[val]
                        case "Color","Color":
                            VARIABLES[val]['value'][0] = int((VARIABLES[val]['value'][0] + expr['value'][0])/2)
                            VARIABLES[val]['value'][1] = int((VARIABLES[val]['value'][1] + expr['value'][1])/2)
                            VARIABLES[val]['value'][2] = int((VARIABLES[val]['value'][2] + expr['value'][2])/2)
                        case "Color","Text":
                            iscolor = is_rgb(expr['value']) or is_hexColor(expr['value'])
                            if iscolor:
                                colors = hexrgb_to_colors(expr['value'])
                                VARIABLES[val]['value'][0] = int((VARIABLES[val]['value'][0] + colors[0])/2)
                                VARIABLES[val]['value'][1] = int((VARIABLES[val]['value'][1] + colors[1])/2)
                                VARIABLES[val]['value'][2] = int((VARIABLES[val]['value'][2] + colors[2])/2)
                            else:
                                raiseError(ctx,ValueError,f"{expr['value']} can not be treated as color")
                        case "Coord", "Coord":
                            VARIABLES[val]['value'] = (VARIABLES[val]['value'][0] + expr['value'][0], VARIABLES[val]['value'][1] + expr['value'][1])
                            return val,VARIABLES[val]
                        case "List","List":
                            VARIABLES[val]['value'] += expr['value']
                            return val,VARIABLES[val]
                        case _:
                            #throw error
                            raiseError(ctx,TypeError,f"{assignment[0]} operator between {VARIABLES[val]['data_type']} and {expr['data_type']} is not supported")
                case '-':
                    match VARIABLES[val]['data_type'],expr['data_type']:
                        case "Number","Number":
                            VARIABLES[val]['value'] = VARIABLES[val]['value'] - expr['value']
                            return val,VARIABLES[val]
                        case "Color","Color":
                            expr['value'] = invert(expr['value'])
                            VARIABLES[val]['value'][0] = int((VARIABLES[val]['value'][0] + expr['value'][0])/2)
                            VARIABLES[val]['value'][1] = int((VARIABLES[val]['value'][1] + expr['value'][1])/2)
                            VARIABLES[val]['value'][2] = int((VARIABLES[val]['value'][2] + expr['value'][2])/2)
                        case "Color","Text":
                            iscolor = is_rgb(expr['value']) or is_hexColor(expr['value'])
                            if iscolor:
                                colors = invert(hexrgb_to_colors(expr['value']))
                                VARIABLES[val]['value'][0] = int((VARIABLES[val]['value'][0] + colors[0])/2)
                                VARIABLES[val]['value'][1] = int((VARIABLES[val]['value'][1] + colors[1])/2)
                                VARIABLES[val]['value'][2] = int((VARIABLES[val]['value'][2] + colors[2])/2)
                            else:
                                raiseError(ctx,ValueError,f"{expr['value']} can not be treated as color")
                        case "Coord","Coord":
                            VARIABLES[val]['value'] = (VARIABLES[val]['value'][0]- expr['value'][0], VARIABLES[val]['value'][1] - expr['value'][1])
                            return val,VARIABLES[val]
                        case _:
                            # throw error
                            raiseError(ctx,TypeError,f"{assignment[0]} operator between {VARIABLES[val]['data_type']} and {expr['data_type']} is not supported")
                case '*':
                    match VARIABLES[val]['data_type'],expr['data_type']:
                        case "Number","Number":
                            VARIABLES[val]['value'] = VARIABLES[val]['value'] * expr['value']
                            return val,VARIABLES[val]
                        case "Coord","Number":
                            VARIABLES[val]['value'] = (VARIABLES[val]['value'][0]* expr['value'], VARIABLES[val]['value'][1] * expr['value'])
                            return val,VARIABLES[val]
                        case "Coord", "Coord":
                            VARIABLES[val]['value'] = (VARIABLES[val]['value'][0] *expr['value'][0],VARIABLES[val]['value'][1] * expr['value'][1])
                            return val,VARIABLES[val]
                        case _:
                            # throw error
                            raiseError(ctx,TypeError,f"{assignment[0]} operator between {VARIABLES[val]['data_type']} and {expr['data_type']} is not supported")
                case '/':
                    match VARIABLES[val]['data_type'],expr['data_type']:
                        case "Number","Number":
                            VARIABLES[val]['value'] = VARIABLES[val]['value'] / expr['value']
                            return val,VARIABLES[val]
                        case "Coord","Number":
                            VARIABLES[val]['value'] = (VARIABLES[val]['value'][0]/expr['value'],VARIABLES[val]['value'][1] / expr['value'])
                            
                            return val,VARIABLES[val]
                        case "Coord", "Coord":
                            VARIABLES[val]['value'] = (VARIABLES[val]['value'][0]/ expr['value'][0],VARIABLES[val]['value'][1] / expr['value'][1])
                            return val,VARIABLES[val]
                        case _:
                            #throw error
                            raiseError(ctx,TypeError,f"{assignment[0]} operator between {VARIABLES[val]['data_type']} and {expr['data_type']} is not supported")
                case '%':
                    match VARIABLES[val]['data_type'],expr['data_type']:
                        case "Number","Number":
                            VARIABLES[val]['value'] = VARIABLES[val]['value'] % expr['value']
                            return val,VARIABLES[val]
                        case _:
                            #throw error
                            raiseError(ctx,TypeError,f"{assignment[0]} operator between {VARIABLES[val]['data_type']} and {expr['data_type']} is not supported")
                case _:
                    raiseError(ctx,TypeError,f"{assignment[0]}= compound operator is not supported")
        else:
            #THROW ERROR
            raiseError(ctx,ValueError,f'Invalid assignment operator')
        

    # Visit a parse tree produced by AniFrameParser#config_statement.
    def visitConfig_statement(self, ctx:AniFrameParser.Config_statementContext):
        configurable = ctx.getChild(1).getText()
        value = self.visit(ctx.getChild(3))
        if configurable == "CANVAS_BACKGROUND":
            try:
                if is_rgb(value['value']) or is_hexColor(value['value']):
                    VARIABLES[configurable]['data_type'] = configurable
                    VARIABLES[configurable]['value'] = hexrgb_to_colors(value['value'])
                    mapping.configure_canvas_background = VARIABLES[configurable]['value']
                else:
                    raiseError(ctx,ValueError,f'Invalid value for {configurable}')
            except:
                raiseError(ctx,ValueError,f'Invalid value for {configurable}')
        else:
            if value['data_type'] != "Number":
                raiseError(ctx,ValueError,f'Invalid value for {configurable}')
            VARIABLES[configurable]['data_type'] = configurable
            VARIABLES[configurable]['value'] = value['value']

            match configurable:
                case 'FRAME_RATE':
                    mapping.configure_frame_rate(VARIABLES[configurable]['value'])
                case 'CANVAS_WIDTH':
                    mapping.configure_canvas_width(VARIABLES[configurable]['value'])
                case 'CANVAS_HEIGHT':
                    mapping.configure_canvas_height(VARIABLES[configurable]['value'])
                case 'MAX_NUM_OF_FRAMES':
                    mapping.configure_max_num_frames(VARIABLES[configurable]['value'])
        return

    # Visit a parse tree produced by AniFrameParser#flow_control_statement.
    def visitFlow_control_statement(self, ctx:AniFrameParser.Flow_control_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AniFrameParser#return_statement.
    def visitReturn_statement(self, ctx:AniFrameParser.Return_statementContext):
        val = self.visit(ctx.getChild(1))
        return val

    # Visit a parse tree produced by AniFrameParser#break_statement.
    def visitBreak_statement(self, ctx:AniFrameParser.Break_statementContext):
        return False


    # Visit a parse tree produced by AniFrameParser#conditional.
    def visitConditional(self, ctx:AniFrameParser.ConditionalContext):
        for i in range(ctx.getChildCount()):
            if self.visit(ctx.getChild(i)):
                break
        return


    # Visit a parse tree produced by AniFrameParser#if_statement.
    def visitIf_statement(self, ctx:AniFrameParser.If_statementContext):
        if self.visit(ctx.getChild(0)):
            self.visit(ctx.getChild(1))
            return True

        return


    # Visit a parse tree produced by AniFrameParser#if_line.
    def visitIf_line(self, ctx:AniFrameParser.If_lineContext):
        condition = self.visit(ctx.getChild(1))
        return True if condition['value'] else None


    # Visit a parse tree produced by AniFrameParser#else_if_statement.
    def visitElse_if_statement(self, ctx:AniFrameParser.Else_if_statementContext):
        if self.visit(ctx.getChild(0)):
            self.visit(ctx.getChild(1))
            return True
        else:
            return


    # Visit a parse tree produced by AniFrameParser#else_if_line.
    def visitElse_if_line(self, ctx:AniFrameParser.Else_if_lineContext):
        condition = self.visit(ctx.getChild(1))
        return True if condition['value'] else None


    # Visit a parse tree produced by AniFrameParser#else_statement.
    def visitElse_statement(self, ctx:AniFrameParser.Else_statementContext):
        self.visit(ctx.getChild(1))
        return True


    # Visit a parse tree produced by AniFrameParser#else_line.
    def visitElse_line(self, ctx:AniFrameParser.Else_lineContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AniFrameParser#loop.
    def visitLoop(self, ctx:AniFrameParser.LoopContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AniFrameParser#for_loop.
    def visitFor_loop(self, ctx:AniFrameParser.For_loopContext):
        ctr = 0
        storage,idens,expr = self.visitFor_line(ctx.getChild(0),ctr,first=True)
        end = len(expr['value'])
        while ctr < end:
            _,_,expr = self.visitFor_line(ctx.getChild(0),ctr)
            end = len(expr['value'])
            val = self.visit(ctx.getChild(1))
            if val == False:
                break
            ctr+=1

        for i in idens:
            VARIABLES.pop(i)
        for iden,item in storage:
            VARIABLES[iden] = item

        return

    def visitFor_line(self, ctx:AniFrameParser.For_lineContext,ctr,first=False):
        global VARIABLES
        children = ctx.getChildCount()
        idens = []
        iden = ctx.getChild(1).getText() 
        idens.append(iden)
        if children == 7:
            iden2 = ctx.getChild(3).getText()
            idens.append(iden2)
        elif children == 5:
            iden2 = None
        storage = []
        if first:
            if VARIABLES.get(iden) != None:
                storage.append([iden,deepcopy(VARIABLES[iden])])
            if iden2 != None and VARIABLES.get(iden2) != None:
                storage.append([iden2,deepcopy(VARIABLES[iden2])])
    
        expr = self.visit(ctx.getChild(children-2))
        if expr['data_type'] != "List" and expr['data_type'] != "Coord":
            raiseError(ctx,TypeError,f'{expr["data_type"]} is not iterable')
        
        if iden2 != None and expr['value'][ctr]['data_type'] != "Coord":
                raiseError(ctx,TypeError,f"{expr['value'][ctr]['data_type']} is not iterable")
        
        if iden2 == None:
            VARIABLES[iden] = expr['value'][ctr]
        else:
            VARIABLES[iden]['value'] = expr['value'][ctr]['value'][0]
            VARIABLES[iden]['data_type'] = "Number"
            VARIABLES[iden]['identifier'] = iden
            VARIABLES[iden2]['value'] = expr['value'][ctr]['value'][1]
            VARIABLES[iden2]['data_type'] = "Number"
            VARIABLES[iden2]['identifier'] = iden2

        return storage,idens,expr

        

    # Visit a parse tree produced by AniFrameParser#while_loop.
    def visitWhile_loop(self, ctx:AniFrameParser.While_loopContext):
        #while condition, visit the block if block encounters break exit the loop
        while self.visit(ctx.getChild(0)):
            val = self.visit(ctx.getChild(1))
            if val == False:
                break
        return 


    # Visit a parse tree produced by AniFrameParser#while_line.
    def visitWhile_line(self, ctx:AniFrameParser.While_lineContext):
        condition = self.visit(ctx.getChild(1))
        return True if condition['value'] else False 

    # Visit a parse tree produced by AniFrameParser#repeat_loop.
    def visitRepeat_loop(self, ctx:AniFrameParser.Repeat_loopContext):
        value = self.visit(ctx.getChild(0))
        for i in range(value):
            val = self.visit(ctx.getChild(1))
            if val == False:
                break
        return


    # Visit a parse tree produced by AniFrameParser#repeat_line.
    def visitRepeat_line(self, ctx:AniFrameParser.Repeat_lineContext):
        expr = self.visit(ctx.getChild(1))
        if expr['data_type'] != "Number":
            # throw error 
            raiseError(ctx,TypeError,f'Repeat value must be Number instead of {expr["data_type"]}')
        else:
            return expr['value']



    # Visit a parse tree produced by AniFrameParser#function_declaration_definition.
    def visitFunction_declaration_definition(self, ctx:AniFrameParser.Function_declaration_definitionContext,params = None,retval = None):
        global VARIABLES
        global function_ctr
        if function_ctr == -1:
            header = self.visitFunction_declaration(ctx.getChild(0),ctx)
            return

        storage = deepcopy(VARIABLES)
        return_val = self.visitFunction_block(ctx.getChild(1),params,retval)
        VARIABLES = storage
        del storage

        if return_val != None:
            return return_val
        else:
            return None

        



    # Visit a parse tree produced by AniFrameParser#function_declaration.
    def visitFunction_declaration(self, ctx:AniFrameParser.Function_declarationContext,parent = None):
        func_name = ctx.getChild(1).getText()
        if ctx.getChild(3).getText() != ')':
            params = self.visit(ctx.getChild(3))
        else:
            params = []

        if func_name not in user_function_names: user_function_names.append(func_name)
        retval = None
        txt = ctx.getText()
        if "returns" in txt:
            retval = ctx.getChild(ctx.getChildCount()-2).getText()

        user_functions[func_name] = {'parameters': params,'returns':retval,'context':parent}
        return func_name,params


    # Visit a parse tree produced by AniFrameParser#formal_parameters.
    def visitFormal_parameters(self, ctx:AniFrameParser.Formal_parametersContext):
        children = ctx.getChildCount()
        params = []
        for i in range(0,children,2):
            params.append(self.visit(ctx.getChild(i)))

        return params

    # Visit a parse tree produced by AniFrameParser#formal_parameter.
    def visitFormal_parameter(self, ctx:AniFrameParser.Formal_parameterContext):
        txt = ctx.getText()
        iden, dtype = txt.split(':')
        return {'identifier':iden,'data_type': dtype}


    # Visit a parse tree produced by AniFrameParser#return_value_data_types.
    def visitReturn_value_data_types(self, ctx:AniFrameParser.Return_value_data_typesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AniFrameParser#return_value_data_type.
    def visitReturn_value_data_type(self, ctx:AniFrameParser.Return_value_data_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AniFrameParser#function_name.
    def visitFunction_name(self, ctx:AniFrameParser.Function_nameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AniFrameParser#conditional_block.
    def visitConditional_block(self, ctx:AniFrameParser.Conditional_blockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AniFrameParser#conditional_with_break.
    def visitConditional_with_break(self, ctx:AniFrameParser.Conditional_with_breakContext):
        children = ctx.getChildCount()

        for i in range(children):
            val = self.visit(ctx.getChild(i))
            if val == False:
                return False
            if val:
                break
        
        return

    # Visit a parse tree produced by AniFrameParser#if_statement_with_break.
    def visitIf_statement_with_break(self, ctx:AniFrameParser.If_statement_with_breakContext):
        if self.visit(ctx.getChild(0)):
            val = self.visit(ctx.getChild(1))
            if val == False:
                return False
            return True

        return


    # Visit a parse tree produced by AniFrameParser#else_if_statement_with_break.
    def visitElse_if_statement_with_break(self, ctx:AniFrameParser.Else_if_statement_with_breakContext):
        if self.visit(ctx.getChild(0)):
            val = self.visit(ctx.getChild(1))
            if val == False:
                return False
            return True

        return

    # Visit a parse tree produced by AniFrameParser#else_statement_with_break.
    def visitElse_statement_with_break(self, ctx:AniFrameParser.Else_statement_with_breakContext):
        val = self.visit(ctx.getChild(1))
        if val == False:
            return False
        return True


    # Visit a parse tree produced by AniFrameParser#conditional_block_with_break.
    def visitConditional_block_with_break(self, ctx:AniFrameParser.Conditional_block_with_breakContext):
        children = ctx.getChildCount()

        for i in range(2,children-1):
            val = self.visit(ctx.getChild(i))
            if val == False:
                return False
        return

    # Visit a parse tree produced by AniFrameParser#conditional_with_return.
    def visitConditional_with_return(self, ctx:AniFrameParser.Conditional_with_returnContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AniFrameParser#if_statement_with_return.
    def visitIf_statement_with_return(self, ctx:AniFrameParser.If_statement_with_returnContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AniFrameParser#else_if_statement_with_return.
    def visitElse_if_statement_with_return(self, ctx:AniFrameParser.Else_if_statement_with_returnContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AniFrameParser#else_statement_with_return.
    def visitElse_statement_with_return(self, ctx:AniFrameParser.Else_statement_with_returnContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AniFrameParser#conditional_block_with_return.
    def visitConditional_block_with_return(self, ctx:AniFrameParser.Conditional_block_with_returnContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AniFrameParser#conditional_with_break_return.
    def visitConditional_with_break_return(self, ctx:AniFrameParser.Conditional_with_break_returnContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AniFrameParser#if_statement_with_break_return.
    def visitIf_statement_with_break_return(self, ctx:AniFrameParser.If_statement_with_break_returnContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AniFrameParser#else_if_statement_with_break_return.
    def visitElse_if_statement_with_break_return(self, ctx:AniFrameParser.Else_if_statement_with_break_returnContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AniFrameParser#else_statement_with_break_return.
    def visitElse_statement_with_break_return(self, ctx:AniFrameParser.Else_statement_with_break_returnContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AniFrameParser#conditional_block_with_break_return.
    def visitConditional_block_with_break_return(self, ctx:AniFrameParser.Conditional_block_with_break_returnContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AniFrameParser#loop_block.
    def visitLoop_block(self, ctx:AniFrameParser.Loop_blockContext):
        children = ctx.getChildCount()
        for i in range(2,children-1):
            val = self.visit(ctx.getChild(i))
            if val == False:
                return False
        
        return


    # Visit a parse tree produced by AniFrameParser#loop_with_return.
    def visitLoop_with_return(self, ctx:AniFrameParser.Loop_with_returnContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AniFrameParser#for_loop_with_return.
    def visitFor_loop_with_return(self, ctx:AniFrameParser.For_loop_with_returnContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AniFrameParser#while_loop_with_return.
    def visitWhile_loop_with_return(self, ctx:AniFrameParser.While_loop_with_returnContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AniFrameParser#repeat_loop_with_return.
    def visitRepeat_loop_with_return(self, ctx:AniFrameParser.Repeat_loop_with_returnContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AniFrameParser#loop_block_with_return.
    def visitLoop_block_with_return(self, ctx:AniFrameParser.Loop_block_with_returnContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AniFrameParser#function_block.
    def visitFunction_block(self, ctx:AniFrameParser.Function_blockContext,params,return_type):
        for param in params:
            iden = param['identifier']
            VARIABLES[iden]['value'] = param['value']
            VARIABLES[iden]['data_type'] = param['data_type']
            VARIABLES[iden]['identifier'] = iden
            
        children = ctx.getChildCount()
        for i in range(2,children-1):
            value = self.visit(ctx.getChild(i))
            if value != None:
                break
        
        if return_type == None:
            return None
        if value['data_type'] == return_type:
            return value
        else:
            raiseError(ctx,ValueError,f"Return value data type does not match declared type")

        return None



    # Visit a parse tree produced by AniFrameParser#configurable.
    def visitConfigurable(self, ctx:AniFrameParser.ConfigurableContext):
        value = ctx.getText()
        VARIABLES[value]['data_type'] = value
        return VARIABLES[value]

    # Visit a parse tree produced by AniFrameParser#built_in_function.
    def visitBuilt_in_function(self, ctx:AniFrameParser.Built_in_functionContext):
        return ctx.getText()


    # Visit a parse tree produced by AniFrameParser#unary_operator.
    def visitUnary_operator(self, ctx:AniFrameParser.Unary_operatorContext):
        return ctx.getText()


    # Visit a parse tree produced by AniFrameParser#binary_logical_operator.
    def visitBinary_logical_operator(self, ctx:AniFrameParser.Binary_logical_operatorContext):
        return ctx.getText()


    # Visit a parse tree produced by AniFrameParser#relational_operator.
    def visitRelational_operator(self, ctx:AniFrameParser.Relational_operatorContext):
        return ctx.getText()


    # Visit a parse tree produced by AniFrameParser#assignment_operator.
    def visitAssignment_operator(self, ctx:AniFrameParser.Assignment_operatorContext):
        return ctx.getText()


    # Visit a parse tree produced by AniFrameParser#compound_assignment_operator.
    def visitCompound_assignment_operator(self, ctx:AniFrameParser.Compound_assignment_operatorContext):
        return ctx.getText()


    # Visit a parse tree produced by AniFrameParser#atom.
    def visitAtom(self, ctx:AniFrameParser.AtomContext):
        atom_text = ctx.getText()
        val = self.visit(ctx.getChild(0))
        if isinstance(val,dict):
            return val
        elif val == None:
            if atom_text == "FRAME":
                VARIABLES[atom_text]['data_type'] = atom_text
            else:
                VARIABLES[atom_text]['data_type'] = '_' if VARIABLES[atom_text].get('data_type') == None else VARIABLES[atom_text]['data_type']
                VARIABLES[atom_text]['identifier'] = atom_text
            return VARIABLES[atom_text]

    # Visit a parse tree produced by AniFrameParser#literal.
    def visitLiteral(self, ctx:AniFrameParser.LiteralContext):
        val = ctx.getText()
        dtype = check_type(val)
        if dtype == "Number":
            val = literal_eval(val)
        else:
            val = val[1:-1]
        return {'value': val, 'data_type': dtype}



del AniFrameParser