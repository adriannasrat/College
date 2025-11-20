#!/bin/bash
multipass start ubuntu

# Only mount if not already mounted
if ! multipass info ubuntu | grep -q "/home/ubuntu/lab3"; then
  multipass mount "$HOME/Documents/DU/Tredje året/Data storage and Management Technologies/Lab 3/Part 2 - Script" ubuntu:/home/ubuntu/lab3
fi

multipass shell ubuntu