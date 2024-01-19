# Stellaris-Pop-Fiction-Empires
This is a resource for the PC game Stellaris. It contains empires from pop-fiction that can be imported to your game and played by human or computer oppenents.

## Simple Install
The only file you need from this repo is the "user_empire_designs_v3.4.txt". Open your own 'user_empire_designs_v3.4.txt' file, usually found in '(One Drive/)Documents/Paradox Interactive/Stellaris/' and paste the contents of our file to the end of your file.

#### Requirements
Keep those force spawn flags on, allow spawn only has a 1% chance of happening.

## Advanced Install
Create a directory in your Stellaris directory and clone this repo into it. The import command will add the pop empires to your game. The export command will create/update the empire files for pop empires so you can commit and make a pull request.

#### Requirements
Written using python 3.9.10

## Instructions
The species bio should have the source, a dash, and then the name of the alien race. Franchises that don't have multiple aliens can be listed as TV, Misc, etc. Specific starting systems are used to prevent similar looking/acting aliens from spawning in the same game. The AI doesn't know how to use jump drives so explorer type empires have ai spawning turned off.

## How to Help
Did I really do the research, or did I just mash the randomize button and say good enough? What you can double-check or improve:
*Short bio 
*Empire name
*Flag design
*native envirnment
*more aliens
