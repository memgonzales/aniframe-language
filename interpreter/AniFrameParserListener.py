# Generated from AniFrameParser.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .AniFrameParser import AniFrameParser
else:
    from AniFrameParser import AniFrameParser

# This class defines a complete listener for a parse tree produced by AniFrameParser.
class AniFrameParserListener(ParseTreeListener):

    # Enter a parse tree produced by AniFrameParser#start_.
    def enterStart_(self, ctx:AniFrameParser.Start_Context):
        pass

    # Exit a parse tree produced by AniFrameParser#start_.
    def exitStart_(self, ctx:AniFrameParser.Start_Context):
        pass


    # Enter a parse tree produced by AniFrameParser#simple_statement.
    def enterSimple_statement(self, ctx:AniFrameParser.Simple_statementContext):
        pass

    # Exit a parse tree produced by AniFrameParser#simple_statement.
    def exitSimple_statement(self, ctx:AniFrameParser.Simple_statementContext):
        pass


    # Enter a parse tree produced by AniFrameParser#compound_statement.
    def enterCompound_statement(self, ctx:AniFrameParser.Compound_statementContext):
        pass

    # Exit a parse tree produced by AniFrameParser#compound_statement.
    def exitCompound_statement(self, ctx:AniFrameParser.Compound_statementContext):
        pass


    # Enter a parse tree produced by AniFrameParser#draw_statement.
    def enterDraw_statement(self, ctx:AniFrameParser.Draw_statementContext):
        pass

    # Exit a parse tree produced by AniFrameParser#draw_statement.
    def exitDraw_statement(self, ctx:AniFrameParser.Draw_statementContext):
        pass


    # Enter a parse tree produced by AniFrameParser#expression.
    def enterExpression(self, ctx:AniFrameParser.ExpressionContext):
        pass

    # Exit a parse tree produced by AniFrameParser#expression.
    def exitExpression(self, ctx:AniFrameParser.ExpressionContext):
        pass


    # Enter a parse tree produced by AniFrameParser#coordinates.
    def enterCoordinates(self, ctx:AniFrameParser.CoordinatesContext):
        pass

    # Exit a parse tree produced by AniFrameParser#coordinates.
    def exitCoordinates(self, ctx:AniFrameParser.CoordinatesContext):
        pass


    # Enter a parse tree produced by AniFrameParser#list.
    def enterList(self, ctx:AniFrameParser.ListContext):
        pass

    # Exit a parse tree produced by AniFrameParser#list.
    def exitList(self, ctx:AniFrameParser.ListContext):
        pass


    # Enter a parse tree produced by AniFrameParser#member.
    def enterMember(self, ctx:AniFrameParser.MemberContext):
        pass

    # Exit a parse tree produced by AniFrameParser#member.
    def exitMember(self, ctx:AniFrameParser.MemberContext):
        pass


    # Enter a parse tree produced by AniFrameParser#function_call.
    def enterFunction_call(self, ctx:AniFrameParser.Function_callContext):
        pass

    # Exit a parse tree produced by AniFrameParser#function_call.
    def exitFunction_call(self, ctx:AniFrameParser.Function_callContext):
        pass


    # Enter a parse tree produced by AniFrameParser#actual_parameters.
    def enterActual_parameters(self, ctx:AniFrameParser.Actual_parametersContext):
        pass

    # Exit a parse tree produced by AniFrameParser#actual_parameters.
    def exitActual_parameters(self, ctx:AniFrameParser.Actual_parametersContext):
        pass


    # Enter a parse tree produced by AniFrameParser#actual_parameter.
    def enterActual_parameter(self, ctx:AniFrameParser.Actual_parameterContext):
        pass

    # Exit a parse tree produced by AniFrameParser#actual_parameter.
    def exitActual_parameter(self, ctx:AniFrameParser.Actual_parameterContext):
        pass


    # Enter a parse tree produced by AniFrameParser#positional_argument.
    def enterPositional_argument(self, ctx:AniFrameParser.Positional_argumentContext):
        pass

    # Exit a parse tree produced by AniFrameParser#positional_argument.
    def exitPositional_argument(self, ctx:AniFrameParser.Positional_argumentContext):
        pass


    # Enter a parse tree produced by AniFrameParser#variable_declaration.
    def enterVariable_declaration(self, ctx:AniFrameParser.Variable_declarationContext):
        pass

    # Exit a parse tree produced by AniFrameParser#variable_declaration.
    def exitVariable_declaration(self, ctx:AniFrameParser.Variable_declarationContext):
        pass


    # Enter a parse tree produced by AniFrameParser#assignment_statement.
    def enterAssignment_statement(self, ctx:AniFrameParser.Assignment_statementContext):
        pass

    # Exit a parse tree produced by AniFrameParser#assignment_statement.
    def exitAssignment_statement(self, ctx:AniFrameParser.Assignment_statementContext):
        pass


    # Enter a parse tree produced by AniFrameParser#config_statement.
    def enterConfig_statement(self, ctx:AniFrameParser.Config_statementContext):
        pass

    # Exit a parse tree produced by AniFrameParser#config_statement.
    def exitConfig_statement(self, ctx:AniFrameParser.Config_statementContext):
        pass


    # Enter a parse tree produced by AniFrameParser#flow_control_statement.
    def enterFlow_control_statement(self, ctx:AniFrameParser.Flow_control_statementContext):
        pass

    # Exit a parse tree produced by AniFrameParser#flow_control_statement.
    def exitFlow_control_statement(self, ctx:AniFrameParser.Flow_control_statementContext):
        pass


    # Enter a parse tree produced by AniFrameParser#return_statement.
    def enterReturn_statement(self, ctx:AniFrameParser.Return_statementContext):
        pass

    # Exit a parse tree produced by AniFrameParser#return_statement.
    def exitReturn_statement(self, ctx:AniFrameParser.Return_statementContext):
        pass


    # Enter a parse tree produced by AniFrameParser#break_statement.
    def enterBreak_statement(self, ctx:AniFrameParser.Break_statementContext):
        pass

    # Exit a parse tree produced by AniFrameParser#break_statement.
    def exitBreak_statement(self, ctx:AniFrameParser.Break_statementContext):
        pass


    # Enter a parse tree produced by AniFrameParser#conditional.
    def enterConditional(self, ctx:AniFrameParser.ConditionalContext):
        pass

    # Exit a parse tree produced by AniFrameParser#conditional.
    def exitConditional(self, ctx:AniFrameParser.ConditionalContext):
        pass


    # Enter a parse tree produced by AniFrameParser#if_statement.
    def enterIf_statement(self, ctx:AniFrameParser.If_statementContext):
        pass

    # Exit a parse tree produced by AniFrameParser#if_statement.
    def exitIf_statement(self, ctx:AniFrameParser.If_statementContext):
        pass


    # Enter a parse tree produced by AniFrameParser#if_line.
    def enterIf_line(self, ctx:AniFrameParser.If_lineContext):
        pass

    # Exit a parse tree produced by AniFrameParser#if_line.
    def exitIf_line(self, ctx:AniFrameParser.If_lineContext):
        pass


    # Enter a parse tree produced by AniFrameParser#else_if_statement.
    def enterElse_if_statement(self, ctx:AniFrameParser.Else_if_statementContext):
        pass

    # Exit a parse tree produced by AniFrameParser#else_if_statement.
    def exitElse_if_statement(self, ctx:AniFrameParser.Else_if_statementContext):
        pass


    # Enter a parse tree produced by AniFrameParser#else_if_line.
    def enterElse_if_line(self, ctx:AniFrameParser.Else_if_lineContext):
        pass

    # Exit a parse tree produced by AniFrameParser#else_if_line.
    def exitElse_if_line(self, ctx:AniFrameParser.Else_if_lineContext):
        pass


    # Enter a parse tree produced by AniFrameParser#else_statement.
    def enterElse_statement(self, ctx:AniFrameParser.Else_statementContext):
        pass

    # Exit a parse tree produced by AniFrameParser#else_statement.
    def exitElse_statement(self, ctx:AniFrameParser.Else_statementContext):
        pass


    # Enter a parse tree produced by AniFrameParser#else_line.
    def enterElse_line(self, ctx:AniFrameParser.Else_lineContext):
        pass

    # Exit a parse tree produced by AniFrameParser#else_line.
    def exitElse_line(self, ctx:AniFrameParser.Else_lineContext):
        pass


    # Enter a parse tree produced by AniFrameParser#loop.
    def enterLoop(self, ctx:AniFrameParser.LoopContext):
        pass

    # Exit a parse tree produced by AniFrameParser#loop.
    def exitLoop(self, ctx:AniFrameParser.LoopContext):
        pass


    # Enter a parse tree produced by AniFrameParser#for_loop.
    def enterFor_loop(self, ctx:AniFrameParser.For_loopContext):
        pass

    # Exit a parse tree produced by AniFrameParser#for_loop.
    def exitFor_loop(self, ctx:AniFrameParser.For_loopContext):
        pass


    # Enter a parse tree produced by AniFrameParser#for_line.
    def enterFor_line(self, ctx:AniFrameParser.For_lineContext):
        pass

    # Exit a parse tree produced by AniFrameParser#for_line.
    def exitFor_line(self, ctx:AniFrameParser.For_lineContext):
        pass


    # Enter a parse tree produced by AniFrameParser#while_loop.
    def enterWhile_loop(self, ctx:AniFrameParser.While_loopContext):
        pass

    # Exit a parse tree produced by AniFrameParser#while_loop.
    def exitWhile_loop(self, ctx:AniFrameParser.While_loopContext):
        pass


    # Enter a parse tree produced by AniFrameParser#while_line.
    def enterWhile_line(self, ctx:AniFrameParser.While_lineContext):
        pass

    # Exit a parse tree produced by AniFrameParser#while_line.
    def exitWhile_line(self, ctx:AniFrameParser.While_lineContext):
        pass


    # Enter a parse tree produced by AniFrameParser#repeat_loop.
    def enterRepeat_loop(self, ctx:AniFrameParser.Repeat_loopContext):
        pass

    # Exit a parse tree produced by AniFrameParser#repeat_loop.
    def exitRepeat_loop(self, ctx:AniFrameParser.Repeat_loopContext):
        pass


    # Enter a parse tree produced by AniFrameParser#repeat_line.
    def enterRepeat_line(self, ctx:AniFrameParser.Repeat_lineContext):
        pass

    # Exit a parse tree produced by AniFrameParser#repeat_line.
    def exitRepeat_line(self, ctx:AniFrameParser.Repeat_lineContext):
        pass


    # Enter a parse tree produced by AniFrameParser#function_declaration_definition.
    def enterFunction_declaration_definition(self, ctx:AniFrameParser.Function_declaration_definitionContext):
        pass

    # Exit a parse tree produced by AniFrameParser#function_declaration_definition.
    def exitFunction_declaration_definition(self, ctx:AniFrameParser.Function_declaration_definitionContext):
        pass


    # Enter a parse tree produced by AniFrameParser#function_declaration.
    def enterFunction_declaration(self, ctx:AniFrameParser.Function_declarationContext):
        pass

    # Exit a parse tree produced by AniFrameParser#function_declaration.
    def exitFunction_declaration(self, ctx:AniFrameParser.Function_declarationContext):
        pass


    # Enter a parse tree produced by AniFrameParser#formal_parameters.
    def enterFormal_parameters(self, ctx:AniFrameParser.Formal_parametersContext):
        pass

    # Exit a parse tree produced by AniFrameParser#formal_parameters.
    def exitFormal_parameters(self, ctx:AniFrameParser.Formal_parametersContext):
        pass


    # Enter a parse tree produced by AniFrameParser#formal_parameter.
    def enterFormal_parameter(self, ctx:AniFrameParser.Formal_parameterContext):
        pass

    # Exit a parse tree produced by AniFrameParser#formal_parameter.
    def exitFormal_parameter(self, ctx:AniFrameParser.Formal_parameterContext):
        pass


    # Enter a parse tree produced by AniFrameParser#return_value_data_types.
    def enterReturn_value_data_types(self, ctx:AniFrameParser.Return_value_data_typesContext):
        pass

    # Exit a parse tree produced by AniFrameParser#return_value_data_types.
    def exitReturn_value_data_types(self, ctx:AniFrameParser.Return_value_data_typesContext):
        pass


    # Enter a parse tree produced by AniFrameParser#return_value_data_type.
    def enterReturn_value_data_type(self, ctx:AniFrameParser.Return_value_data_typeContext):
        pass

    # Exit a parse tree produced by AniFrameParser#return_value_data_type.
    def exitReturn_value_data_type(self, ctx:AniFrameParser.Return_value_data_typeContext):
        pass


    # Enter a parse tree produced by AniFrameParser#function_name.
    def enterFunction_name(self, ctx:AniFrameParser.Function_nameContext):
        pass

    # Exit a parse tree produced by AniFrameParser#function_name.
    def exitFunction_name(self, ctx:AniFrameParser.Function_nameContext):
        pass


    # Enter a parse tree produced by AniFrameParser#conditional_block.
    def enterConditional_block(self, ctx:AniFrameParser.Conditional_blockContext):
        pass

    # Exit a parse tree produced by AniFrameParser#conditional_block.
    def exitConditional_block(self, ctx:AniFrameParser.Conditional_blockContext):
        pass


    # Enter a parse tree produced by AniFrameParser#conditional_with_break.
    def enterConditional_with_break(self, ctx:AniFrameParser.Conditional_with_breakContext):
        pass

    # Exit a parse tree produced by AniFrameParser#conditional_with_break.
    def exitConditional_with_break(self, ctx:AniFrameParser.Conditional_with_breakContext):
        pass


    # Enter a parse tree produced by AniFrameParser#if_statement_with_break.
    def enterIf_statement_with_break(self, ctx:AniFrameParser.If_statement_with_breakContext):
        pass

    # Exit a parse tree produced by AniFrameParser#if_statement_with_break.
    def exitIf_statement_with_break(self, ctx:AniFrameParser.If_statement_with_breakContext):
        pass


    # Enter a parse tree produced by AniFrameParser#else_if_statement_with_break.
    def enterElse_if_statement_with_break(self, ctx:AniFrameParser.Else_if_statement_with_breakContext):
        pass

    # Exit a parse tree produced by AniFrameParser#else_if_statement_with_break.
    def exitElse_if_statement_with_break(self, ctx:AniFrameParser.Else_if_statement_with_breakContext):
        pass


    # Enter a parse tree produced by AniFrameParser#else_statement_with_break.
    def enterElse_statement_with_break(self, ctx:AniFrameParser.Else_statement_with_breakContext):
        pass

    # Exit a parse tree produced by AniFrameParser#else_statement_with_break.
    def exitElse_statement_with_break(self, ctx:AniFrameParser.Else_statement_with_breakContext):
        pass


    # Enter a parse tree produced by AniFrameParser#conditional_block_with_break.
    def enterConditional_block_with_break(self, ctx:AniFrameParser.Conditional_block_with_breakContext):
        pass

    # Exit a parse tree produced by AniFrameParser#conditional_block_with_break.
    def exitConditional_block_with_break(self, ctx:AniFrameParser.Conditional_block_with_breakContext):
        pass


    # Enter a parse tree produced by AniFrameParser#conditional_with_return.
    def enterConditional_with_return(self, ctx:AniFrameParser.Conditional_with_returnContext):
        pass

    # Exit a parse tree produced by AniFrameParser#conditional_with_return.
    def exitConditional_with_return(self, ctx:AniFrameParser.Conditional_with_returnContext):
        pass


    # Enter a parse tree produced by AniFrameParser#if_statement_with_return.
    def enterIf_statement_with_return(self, ctx:AniFrameParser.If_statement_with_returnContext):
        pass

    # Exit a parse tree produced by AniFrameParser#if_statement_with_return.
    def exitIf_statement_with_return(self, ctx:AniFrameParser.If_statement_with_returnContext):
        pass


    # Enter a parse tree produced by AniFrameParser#else_if_statement_with_return.
    def enterElse_if_statement_with_return(self, ctx:AniFrameParser.Else_if_statement_with_returnContext):
        pass

    # Exit a parse tree produced by AniFrameParser#else_if_statement_with_return.
    def exitElse_if_statement_with_return(self, ctx:AniFrameParser.Else_if_statement_with_returnContext):
        pass


    # Enter a parse tree produced by AniFrameParser#else_statement_with_return.
    def enterElse_statement_with_return(self, ctx:AniFrameParser.Else_statement_with_returnContext):
        pass

    # Exit a parse tree produced by AniFrameParser#else_statement_with_return.
    def exitElse_statement_with_return(self, ctx:AniFrameParser.Else_statement_with_returnContext):
        pass


    # Enter a parse tree produced by AniFrameParser#conditional_block_with_return.
    def enterConditional_block_with_return(self, ctx:AniFrameParser.Conditional_block_with_returnContext):
        pass

    # Exit a parse tree produced by AniFrameParser#conditional_block_with_return.
    def exitConditional_block_with_return(self, ctx:AniFrameParser.Conditional_block_with_returnContext):
        pass


    # Enter a parse tree produced by AniFrameParser#conditional_with_break_return.
    def enterConditional_with_break_return(self, ctx:AniFrameParser.Conditional_with_break_returnContext):
        pass

    # Exit a parse tree produced by AniFrameParser#conditional_with_break_return.
    def exitConditional_with_break_return(self, ctx:AniFrameParser.Conditional_with_break_returnContext):
        pass


    # Enter a parse tree produced by AniFrameParser#if_statement_with_break_return.
    def enterIf_statement_with_break_return(self, ctx:AniFrameParser.If_statement_with_break_returnContext):
        pass

    # Exit a parse tree produced by AniFrameParser#if_statement_with_break_return.
    def exitIf_statement_with_break_return(self, ctx:AniFrameParser.If_statement_with_break_returnContext):
        pass


    # Enter a parse tree produced by AniFrameParser#else_if_statement_with_break_return.
    def enterElse_if_statement_with_break_return(self, ctx:AniFrameParser.Else_if_statement_with_break_returnContext):
        pass

    # Exit a parse tree produced by AniFrameParser#else_if_statement_with_break_return.
    def exitElse_if_statement_with_break_return(self, ctx:AniFrameParser.Else_if_statement_with_break_returnContext):
        pass


    # Enter a parse tree produced by AniFrameParser#else_statement_with_break_return.
    def enterElse_statement_with_break_return(self, ctx:AniFrameParser.Else_statement_with_break_returnContext):
        pass

    # Exit a parse tree produced by AniFrameParser#else_statement_with_break_return.
    def exitElse_statement_with_break_return(self, ctx:AniFrameParser.Else_statement_with_break_returnContext):
        pass


    # Enter a parse tree produced by AniFrameParser#conditional_block_with_break_return.
    def enterConditional_block_with_break_return(self, ctx:AniFrameParser.Conditional_block_with_break_returnContext):
        pass

    # Exit a parse tree produced by AniFrameParser#conditional_block_with_break_return.
    def exitConditional_block_with_break_return(self, ctx:AniFrameParser.Conditional_block_with_break_returnContext):
        pass


    # Enter a parse tree produced by AniFrameParser#loop_block.
    def enterLoop_block(self, ctx:AniFrameParser.Loop_blockContext):
        pass

    # Exit a parse tree produced by AniFrameParser#loop_block.
    def exitLoop_block(self, ctx:AniFrameParser.Loop_blockContext):
        pass


    # Enter a parse tree produced by AniFrameParser#loop_with_return.
    def enterLoop_with_return(self, ctx:AniFrameParser.Loop_with_returnContext):
        pass

    # Exit a parse tree produced by AniFrameParser#loop_with_return.
    def exitLoop_with_return(self, ctx:AniFrameParser.Loop_with_returnContext):
        pass


    # Enter a parse tree produced by AniFrameParser#for_loop_with_return.
    def enterFor_loop_with_return(self, ctx:AniFrameParser.For_loop_with_returnContext):
        pass

    # Exit a parse tree produced by AniFrameParser#for_loop_with_return.
    def exitFor_loop_with_return(self, ctx:AniFrameParser.For_loop_with_returnContext):
        pass


    # Enter a parse tree produced by AniFrameParser#while_loop_with_return.
    def enterWhile_loop_with_return(self, ctx:AniFrameParser.While_loop_with_returnContext):
        pass

    # Exit a parse tree produced by AniFrameParser#while_loop_with_return.
    def exitWhile_loop_with_return(self, ctx:AniFrameParser.While_loop_with_returnContext):
        pass


    # Enter a parse tree produced by AniFrameParser#repeat_loop_with_return.
    def enterRepeat_loop_with_return(self, ctx:AniFrameParser.Repeat_loop_with_returnContext):
        pass

    # Exit a parse tree produced by AniFrameParser#repeat_loop_with_return.
    def exitRepeat_loop_with_return(self, ctx:AniFrameParser.Repeat_loop_with_returnContext):
        pass


    # Enter a parse tree produced by AniFrameParser#loop_block_with_return.
    def enterLoop_block_with_return(self, ctx:AniFrameParser.Loop_block_with_returnContext):
        pass

    # Exit a parse tree produced by AniFrameParser#loop_block_with_return.
    def exitLoop_block_with_return(self, ctx:AniFrameParser.Loop_block_with_returnContext):
        pass


    # Enter a parse tree produced by AniFrameParser#function_block.
    def enterFunction_block(self, ctx:AniFrameParser.Function_blockContext):
        pass

    # Exit a parse tree produced by AniFrameParser#function_block.
    def exitFunction_block(self, ctx:AniFrameParser.Function_blockContext):
        pass


    # Enter a parse tree produced by AniFrameParser#configurable.
    def enterConfigurable(self, ctx:AniFrameParser.ConfigurableContext):
        pass

    # Exit a parse tree produced by AniFrameParser#configurable.
    def exitConfigurable(self, ctx:AniFrameParser.ConfigurableContext):
        pass


    # Enter a parse tree produced by AniFrameParser#built_in_function.
    def enterBuilt_in_function(self, ctx:AniFrameParser.Built_in_functionContext):
        pass

    # Exit a parse tree produced by AniFrameParser#built_in_function.
    def exitBuilt_in_function(self, ctx:AniFrameParser.Built_in_functionContext):
        pass


    # Enter a parse tree produced by AniFrameParser#unary_operator.
    def enterUnary_operator(self, ctx:AniFrameParser.Unary_operatorContext):
        pass

    # Exit a parse tree produced by AniFrameParser#unary_operator.
    def exitUnary_operator(self, ctx:AniFrameParser.Unary_operatorContext):
        pass


    # Enter a parse tree produced by AniFrameParser#binary_logical_operator.
    def enterBinary_logical_operator(self, ctx:AniFrameParser.Binary_logical_operatorContext):
        pass

    # Exit a parse tree produced by AniFrameParser#binary_logical_operator.
    def exitBinary_logical_operator(self, ctx:AniFrameParser.Binary_logical_operatorContext):
        pass


    # Enter a parse tree produced by AniFrameParser#relational_operator.
    def enterRelational_operator(self, ctx:AniFrameParser.Relational_operatorContext):
        pass

    # Exit a parse tree produced by AniFrameParser#relational_operator.
    def exitRelational_operator(self, ctx:AniFrameParser.Relational_operatorContext):
        pass


    # Enter a parse tree produced by AniFrameParser#assignment_operator.
    def enterAssignment_operator(self, ctx:AniFrameParser.Assignment_operatorContext):
        pass

    # Exit a parse tree produced by AniFrameParser#assignment_operator.
    def exitAssignment_operator(self, ctx:AniFrameParser.Assignment_operatorContext):
        pass


    # Enter a parse tree produced by AniFrameParser#compound_assignment_operator.
    def enterCompound_assignment_operator(self, ctx:AniFrameParser.Compound_assignment_operatorContext):
        pass

    # Exit a parse tree produced by AniFrameParser#compound_assignment_operator.
    def exitCompound_assignment_operator(self, ctx:AniFrameParser.Compound_assignment_operatorContext):
        pass


    # Enter a parse tree produced by AniFrameParser#atom.
    def enterAtom(self, ctx:AniFrameParser.AtomContext):
        pass

    # Exit a parse tree produced by AniFrameParser#atom.
    def exitAtom(self, ctx:AniFrameParser.AtomContext):
        pass


    # Enter a parse tree produced by AniFrameParser#literal.
    def enterLiteral(self, ctx:AniFrameParser.LiteralContext):
        pass

    # Exit a parse tree produced by AniFrameParser#literal.
    def exitLiteral(self, ctx:AniFrameParser.LiteralContext):
        pass



del AniFrameParser