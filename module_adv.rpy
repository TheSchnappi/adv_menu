####################################
# Japanese Style Adventure Menu
####################################
# By TheSchnappi
#
# Version 1.1
#
#
# License:
# Japanese Style Adventure Menu for RenPy by TheSchnappi
# MIT License
# 
# Copyright (c) 2020 TheSchnappi
# 
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
# 
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
#
#
# Changelog:
# 0.1   - Start of a complete rewrite for a possible internet release
# 0.2a  - Added module_adv_mode for switching between traditional mode with actions as a separate window and
#         a more modern mode where the actions appear like an accordion widget.
# 0.2b  - Added the option to display icons before the verbs, old version had to include it in
#         the text of the verb button with an ugly side effect that the following text was hard to align if
#         the icon had different widths
# 0.3   - Basic styling customization with global variables
# 0.4   - even more styling variables defined
# 0.5   - removed special styling blocks for action interactions, now they are controlled by using the
#         prefix and suffix attributes. This should enable overall a more flexible text styling
# 0.6   - Now verbs show if there is at least one new interaction or all options are exhaust using
#         prefix and suffix attributes, just like the action styling
# 0.7   - Split the module in two files for a better backward compatibility in the future:
#           - One config where the module can be customized (module_adv_config.rpy)
#           - One static file that hosts all the code one should not need any edits (module_adv.rpy)
# 0.8   - Added feature:
#           - Each actively displayed verb is now associated with the press of a number key from 1-9
# 0.9   - Separated the verb action menu into its own screen to reduce code redundancy
# 1.0   - "Fixed" rollback and roll forward bug that did not change values back to their values. Now the menu
#         uses Return() and returns the targeted label as a string. So now the value increase and jump have to
#         evaluate _return and happen right after the screen call
# 1.1   - Made the screen fit for upcoming changes to roll forward feature change in 7.4.2+
#
#
####################################


#### Definition of the ADV Menu class and the support functions
init python:
    class ModuleADVMenuContainer:
        """
        This class contains the basic menu structure for the interaction menu
        screen for the adv_menu.
        """
        def __init__(self):
            # This variable contains all allowed verbs and in which order
            # the verbs should be displayed
            self.verb_order = []
            # The verb action dictionary contains all registered actions for
            # a verb
            self.verb_actions = {}
            # Variable for determining which verb actions are is currently displayed

        def register_verb(self, verb_id, icon, name):
            """
            Registers the given verb id for the ADV Menu.
            The name represents the value that is displayed in the menu.
            """
            self.verb_order.append(verb_id)
            self.verb_actions[verb_id] = {"name": name, "icon": icon, "action_list": []}

        def register_action(self, verb_id, action_text, jump_id):
            """
            Registers an action for the given verb id.
            It needs the verb_id in which the action should reside, the
            displayed text and a jump point, that the action later calls.
            """
            self.verb_actions[verb_id]['action_list'].append((action_text, jump_id))

        def clear_actions(self):
            """
            Clears all actions for all verbs.
            This should always be called before creating new action lists.
            """
            for verb_id in self.verb_actions:
                self.verb_actions[verb_id]['action_list'] = []


    def increase_choice_repeat(label_id):
        """
        This function increases the given label_id for keeping track how
        often the player has repeated an action.
        
        Calling this function for a label_id the first time, results in the
        creation of this id. So it is just a wrapper around a dictionary for
        easier control.
        """
        if label_id in _module_adv_repeat_list.keys():
            _module_adv_repeat_list[label_id][0] += 1
        else:
            _module_adv_repeat_list[label_id] = [0, False]


    def get_choice_repeat(label_id):
        """
        This function returns how often an action was repeated, or more
        precise, how often increase_choice_repeat() was called with the given
        label.
        """
        if label_id in _module_adv_repeat_list.keys():
            return _module_adv_repeat_list[label_id][0]
        else:
            _module_adv_repeat_list[label_id] = [-1, False]
            return -1


    def set_choice_exhaust(label_id, change_to=True):
        """
        Marks the given label_id as exhaust by default. If change_to is
        False, it removes the exhaust state.
        """
        if label_id in _module_adv_repeat_list.keys():
            _module_adv_repeat_list[label_id][1] = change_to
        else:
            _module_adv_repeat_list[label_id] = [-1, change_to]


    def get_choice_exhaust(label_id):
        """
        Returns if the given label_id was exhaust
        """
        if label_id in _module_adv_repeat_list.keys():
            return _module_adv_repeat_list[label_id][1]
        else:
            return False


screen adv_menu_verb_actions(verb_actions_visible):
    frame:
        style "module_adv_action_menu"
        for verb_id in adv_mode.verb_order:
            if verb_id == verb_actions_visible:
                $ verb_content = adv_mode.verb_actions[verb_id]
                vbox:
                    for verb_action in verb_content["action_list"]:
                        $ tmp_action_text = verb_action[0]
                        if get_choice_repeat(verb_action[1]) == -1:
                            $ tmp_action_text = "{}{}{}".format(module_adv_action_text_new_prefix,
                                                                verb_action[0],
                                                                module_adv_action_text_new_suffix)
                        elif get_choice_exhaust(verb_action[1]) == True:
                            $ tmp_action_text = "{}{}{}".format(module_adv_action_text_exhaust_prefix,
                                                                verb_action[0],
                                                                module_adv_action_text_exhaust_suffix)
                        else:
                            $ tmp_action_text = "{}{}{}".format(module_adv_action_text_prefix,
                                                                verb_action[0],
                                                                module_adv_action_text_suffix)
                        textbutton tmp_action_text:
                            style "style_module_adv_action_menu_button"
                            action [Return(verb_action[1])]


#### The screen of the ADV menu
screen adv_menu():
    default verb_actions_visible = None
    frame at adv_menu_transform:
        style "module_adv_position"
        hbox:
            frame:
                style "module_adv_verb_menu"
                vbox:
                    spacing module_adv_spacing
                    $ tmp_keymap_index = 0
                    for verb_id in adv_mode.verb_order:
                        $ verb_content = adv_mode.verb_actions[verb_id]
                        # Check if there is a new action below this verb
                        $ tmp_verb_action_style_new = False
                        $ tmp_verb_action_style_exhaust = True
                        for verb_action in verb_content["action_list"]:
                            if get_choice_repeat(verb_action[1]) == -1:
                                $ tmp_verb_action_style_new = True
                            else:
                                # Check if at least one action is not exhaust
                                if get_choice_exhaust(verb_action[1]) == False:
                                    $ tmp_verb_action_style_exhaust = False
                        # Only if the verb has actions registered, its button should be created
                        if len(verb_content["action_list"]) != 0:
                            $ tmp_keymap_index += 1
                            if  tmp_verb_action_style_new:
                                $ tmp_icon_text = "{}{}{}".format(module_adv_verb_icon_new_prefix,
                                                                  verb_content['icon'],
                                                                  module_adv_verb_icon_new_suffix)
                                $ tmp_verb_text = "{}{}{}".format(module_adv_verb_text_new_prefix,
                                                                  verb_content['name'],
                                                                  module_adv_verb_text_new_suffix)
                            elif tmp_verb_action_style_exhaust:
                                $ tmp_icon_text = "{}{}{}".format(module_adv_verb_icon_exhaust_prefix,
                                                                  verb_content['icon'],
                                                                  module_adv_verb_icon_exhaust_suffix)
                                $ tmp_verb_text = "{}{}{}".format(module_adv_verb_text_exhaust_prefix,
                                                                  verb_content['name'],
                                                                  module_adv_verb_text_exhaust_suffix)
                            else:
                                $ tmp_icon_text = "{}{}{}".format(module_adv_verb_icon_prefix,
                                                                  verb_content['icon'],
                                                                  module_adv_verb_icon_suffix)
                                $ tmp_verb_text = "{}{}{}".format(module_adv_verb_text_prefix,
                                                                  verb_content['name'],
                                                                  module_adv_verb_text_suffix)
                            # Here we create the button for the verb
                            button:
                                keysym str(tmp_keymap_index)
                                style "module_adv_verb_menu_button"
                                text tmp_verb_text style "module_adv_verb_menu_button_text"
                                fixed:
                                    text tmp_icon_text style "module_adv_verb_menu_button_icon"
                                action SetScreenVariable('verb_actions_visible', verb_id)
                            # This part is used if the action buttons are displayed as an accordion widget (module_adv_mode = 0)
                            if module_adv_mode == 0:
                                if verb_actions_visible == verb_id:
                                    use adv_menu_verb_actions(verb_actions_visible)
            # This part is used if the action buttons are displayed as a separate menu (module_adv_mode = 1)
            if module_adv_mode == 1:
                if verb_actions_visible is not None:
                    use adv_menu_verb_actions(verb_actions_visible)


style module_adv_position:
    background                  None
    padding                     (0, 0, 0, 0)
    margin                      (0, 0, 0, 0)
    xalign                      module_adv_menu_position_xalign
    yalign                      module_adv_menu_position_yalign

style module_adv_verb_menu:
    background                  module_adv_verb_menu_background
    margin                      module_adv_verb_menu_margin
    padding                     module_adv_verb_menu_padding
    xsize                       module_adv_verb_menu_width

style module_adv_verb_menu_button:
    background                  module_adv_verb_menu_button_background
    hover_background            module_adv_verb_menu_button_background_hover
    selected_background         module_adv_verb_menu_button_background_selected
    selected_hover_background   module_adv_verb_menu_button_background_selected_hover
    ysize                       module_adv_verb_menu_button_height

style module_adv_verb_menu_button_text:
    font                        module_adv_verb_font
    size                        module_adv_verb_font_size
    color                       module_adv_verb_font_color
    hover_color                 module_adv_verb_font_color_hover
    selected_color              module_adv_verb_font_color_selected
    selected_hover_color        module_adv_verb_font_color_selected_hover
    outlines                    module_adv_verb_font_outline
    xpos                        module_adv_verb_text_shift

style module_adv_verb_menu_button_icon:
    size                        module_adv_verb_icon_size
    xcenter                     module_adv_verb_icon_xcenter
    yalign                      module_adv_verb_icon_yalign
    font                        module_adv_verb_icon_font
    color                       module_adv_verb_icon_font_color
    hover_color                 module_adv_verb_icon_font_color_hover
    selected_color              module_adv_verb_icon_font_color_selected
    selected_hover_color        module_adv_verb_icon_font_color_selected_hover
    outlines                    module_adv_verb_icon_font_outline

style module_adv_action_menu:
    background                  module_adv_action_menu_background
    margin                      module_adv_action_menu_margin
    padding                     module_adv_action_menu_padding
    xsize                       module_adv_action_menu_width

style style_module_adv_action_menu_button:
    background                  module_adv_action_menu_button_background
    hover_background            module_adv_action_menu_button_background_hover
    padding                     module_adv_action_menu_button_padding
    margin                      module_adv_action_menu_button_margin
    ysize                       module_adv_action_menu_button_height
    xfill                       True

style style_module_adv_action_menu_button_text:
    font                        module_adv_action_font
    size                        module_adv_action_font_size
    outlines                    module_adv_action_font_outline
    yalign      0.5

transform adv_menu_transform:
    on show:
        parallel:
            alpha 0
            easein 0.2 alpha 1
        parallel:
            xoffset -32
            easein 0.2 xoffset 0
    on hide:
        parallel:
            alpha 1
            linear 0.2 alpha 0
        parallel:
            xoffset 0
            easein 0.2 xoffset -32

###########################################
# INITIALISATION LABEL FOR THE ADV MODULE
###########################################
default _module_adv_repeat_list = {}

label init_module_adv:
    # This part initializes the module - DO NOT TOUCH ANYTHING INSIDE THIS LABEL!
    # Call this label at the games start once before using the menu
    #$ _module_adv_repeat_list = {}
    $ adv_mode = ModuleADVMenuContainer()
    call init_module_adv_verbs
    return
   
