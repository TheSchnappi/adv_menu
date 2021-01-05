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
init offset = -1

# Switch for the display mode of the ADV menu
#   0 = actions of a verb are displayed as accordion widget
#   1 = actions of a verb are presented in a separate window (traditional ADV)
define module_adv_mode = 0

define module_adv_spacing = 0

define module_adv_action_menu_background = None

define module_adv_menu_position_xalign = 0.01
define module_adv_menu_position_yalign = 0.5

#### Variables for the design of the ADV verbs

## Variables for styling the verb menu

## Margin and padding of the verb menu
define module_adv_verb_menu_margin                              = (0, 0, 0, 0)
define module_adv_verb_menu_padding                             = (12, 12, 12, 12)

# The size of the verb menu
# - If module_adv_mode is 0, this defines the overall size of the menu
define module_adv_verb_menu_width                               = 512

# Background of the verb menu
define module_adv_verb_menu_background                          = "#000000cc"

## Verb button variables
# The height of the verb buttons
define module_adv_verb_menu_button_height                       = 58

## Background of the verb buttons
define module_adv_verb_menu_button_background                   = None
define module_adv_verb_menu_button_background_hover             = "#ffffff88"
define module_adv_verb_menu_button_background_selected          = "#88888888"
define module_adv_verb_menu_button_background_selected_hover    = "#ffffff88"

## Verb icon font variables
define module_adv_verb_icon_font                                = "DejaVuSans.ttf"
define module_adv_verb_icon_size                                = 40
define module_adv_verb_icon_font_color                          = "#888888"
define module_adv_verb_icon_font_color_hover                    = "#dddddd"
define module_adv_verb_icon_font_color_selected                 = "#ffffff"
define module_adv_verb_icon_font_color_selected_hover           = "#ffffff"
define module_adv_verb_icon_font_outline                        = [ (absolute(2), "#000", absolute(0), absolute(0)) ]

# Icon font correction variables
# Defines the center position of the icons inside the verb button
define module_adv_verb_icon_xcenter                             = 26

# Middle align the icons. This value should work in nearly every case.
define module_adv_verb_icon_yalign                              = 0.5

## Verb text font variables
define module_adv_verb_font                                     = "DejaVuSans.ttf"
define module_adv_verb_font_size                                = 36
define module_adv_verb_font_color                               = "#888888"
define module_adv_verb_font_color_hover                         = "#dddddd"
define module_adv_verb_font_color_selected                      = "#ffffff"
define module_adv_verb_font_color_selected_hover                = "#ffffff"
define module_adv_verb_font_outline                             = [ (absolute(2), "#000", absolute(0), absolute(0)) ]


# how much pixel should the text of the verb text be shifted to make space for the icons
# If you use no icons, you can set this to 0
define module_adv_verb_text_shift                               = 52


## Text prefix and suffix for a verb with at least one new action,
# i.e. the player hasn't interacted with this option yet
define module_adv_verb_text_new_prefix                          = ""
define module_adv_verb_text_new_suffix                          = "{color=#E43}{b}{size=14} NEW{/size}{/b}{/color}"

define module_adv_verb_icon_new_prefix                          = ""
define module_adv_verb_icon_new_suffix                          = ""

## Text prefix and suffix for verbs
# i.e. the player interacted with this option at least once
define module_adv_verb_text_prefix                              = ""
define module_adv_verb_text_suffix                              = ""

define module_adv_verb_icon_prefix                              = ""
define module_adv_verb_icon_suffix                              = ""

## Text prefix and suffix for a verb with only exhausted actions
# i.e. the player has exhausted all interactions with this option
define module_adv_verb_text_exhaust_prefix                      = "{i}{color=#444444}"
define module_adv_verb_text_exhaust_suffix                      = "{/color}{/i}"

define module_adv_verb_icon_exhaust_prefix                      = "{color=#444444}"
define module_adv_verb_icon_exhaust_suffix                      = "{/color}"

#### Variables for the design of the ADV actions

## Margin and padding of the action menu
define module_adv_action_menu_margin                            = (0, 0, 0, 0)
define module_adv_action_menu_padding                           = (0, 0, 0, 0)

## Background of the verb menu
define module_adv_action_menu_background                        = None #"#000000cc"

# The size of the verb menu
# - If module_adv_mode is 0, this should be set to the size of the menu width, minus the left and right
#   padding of the verb menu and the margin of the action menu
define module_adv_action_menu_width                             = module_adv_verb_menu_width - 24

# The height of the verb buttons
define module_adv_action_menu_button_height                     = 52

## Background of the action buttons
define module_adv_action_menu_button_background                 = None
define module_adv_action_menu_button_background_hover           = "#ffffff88"

## Action text font variables
define module_adv_action_font                                   = "DejaVuSans.ttf"
define module_adv_action_font_size                              = 36
define module_adv_action_font_color                             = "#aaaaaa"
define module_adv_action_font_color_hover                       = "#aaaaaa"
define module_adv_action_font_color_selected                    = "#aaaaaa"
define module_adv_action_font_color_selected_hover              = "#aaaaaa"
define module_adv_action_font_outline                           = [ (absolute(2), "#000", absolute(0), absolute(0)) ]


## Padding of the text inside the action button
define module_adv_action_menu_button_margin                     = (0, 0, 0, 0)
define module_adv_action_menu_button_padding                    = (58, 0, 0, 0)

## Text prefix and suffix for new actions,
#i.e. the player hasn't interacted with this option yet
define module_adv_action_text_new_prefix                        = ""
define module_adv_action_text_new_suffix                        = "{color=#E43}{b}{size=14} NEW{/size}{/b}{/color}"

## Text prefix and suffix for actions
#i.e. the player interacted with this option at least once
define module_adv_action_text_prefix                            = ""
define module_adv_action_text_suffix                            = ""

## Text prefix and suffix for exhausted actions
#i.e. the player has exhausted all interactions with this option
define module_adv_action_text_exhaust_prefix                    = "{i}{color=#444444}"
define module_adv_action_text_exhaust_suffix                    = "{/color}{/i}"

label init_module_adv_verbs:
    # Here you create the verbs you want to support in the game in calling the
    # register_verb function of the previously initialized adv_mode class

    # For creating a verb you need to pass register_verb() three parameters:
    #   - The first parameter is the internal name of the verb that only
    #   - The second parameter is an icon for the verb, for example a speech bubble for talking
    #   - The third parameter is how the verb is displayed in the ADV menu
    $ adv_mode.register_verb("look",  "\uA66D", "Look")
    $ adv_mode.register_verb("think", "\uFFFD", "Think")
    $ adv_mode.register_verb("talk",  "\u263B", "Talk")
    $ adv_mode.register_verb("use",   "\u2699", "Use")
    $ adv_mode.register_verb("move",  "\u27A5", "Move")
    return
