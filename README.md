# Japanese Style Adventure Menu
Japanese Style Adventure Menu for RenPy

This module adds a menu based interaction system to RenPy, like it was popularized by "The Portopia Serial Murder Case" and was used by many japanese adventure games in the 80's and 90's.

## How to install the module
Simply copy the two files `module_adv.rpy` and `module_adv_config.rpy` somewhere into your project directory.

## Change the styling
You can easily customize the styling with `module_adv_config.rpy` to your liking. The basic structure of this configuration file is similar to the `options.rpy` or `gui.rpy` files within RenPy. 

## How to initalize the module
To initialize the module simply call the label `init_module_adv_verbs`. This will register all verbs your game should use.

## Create new verbs/modify existing ones
To add or modify verbs you have to modify the label `init_module_adv_verbs` in the file `module_adv_config.rpy`.
Adding a new verb can be done with the adv_mode.register_verb() function that takes three parameters: 

- The first parameter defines the verbs internal name you will use when registering actions.
- The second parameter defines the icon of the verb. You can either add images as a text tag or use a special font icon. I would suggest the use of a special font for more styling options.
- The third parameter is the displayed name of the verb in the game itself.

## How do I use and display the Adventure Menu?

The Adventure Menu at its core is a screen that, based on the players choice, will jump to different labels that then describe the logic of the specific interaction.
To better explain this, let us look at a simple example:

### A simple example:
```
$ adv_mode.clear_actions()
$ adv_mode.register_action("look", "Room", "look_room_label")
$ adv_mode.register_action("look", "Chair", "look_chair_label")
$ adv_mode.register_action("use", "Chair", "use_chair_label")
$ adv_mode.register_action("move", "Other Room", "move_other_room_label")
call screen adv_menu
$ increase_choice_repeat(_return)
jump expression _return
```

- First you want to clear all previously registered actions with the adv_mode.clear_actions() function.
- Then you need to register your different actions the player should interact with. To register an action you simply call the `adv_mode.register_action()` function with three parameters:
  - The first parameter is the verbs internal name you want to use for this action, like "use" or "look".
  - The second parameter is the text of the action, something like "Room" or "Chair".
  - The third parameter is simply the name of the label the action will jump to when clicked.
- Then call the screen `adv_menu`
- Then you have to add the two lines `$ increase_choice_repeat(_return)` and `jump expression _return` that execute and jump to the label.
