# Helix like shell
KEYTIMEOUT=1

typeset -gA hx_modes
: ${hx_modes[insert]:='INSERT'}
: ${hx_modes[select]:='SELECT'}
: ${hx_modes[normal]:='NORMAL'}

export hx_mode=$hx_modes[normal]

switch-mode(){
    if [[ $hx_mode != $hx_modes[$1] ]]; then
        export hx_mode=$hx_modes[$1]
        export RPS1=$hx_mode
        zle reset-prompt
        bindkey -A "hx-$1" main
    fi
}
hx-insert-mode(){
    switch-mode insert
}
hx-normal-mode(){
    switch-mode normal
}
hx-select-mode(){
    switch-mode select
}
hx-next-word(){
    zle deactivate-region
}


zle -N hx-insert-mode 
zle -N hx-select-mode 
zle -N hx-normal-mode 
zle -N hx-next-word

bindkey -N hx-select
bindkey -N hx-insert 
bindkey -N hx-normal 


#################################################
# Insert Keymap                                 #
#################################################

# basic keys
bindkey -R -M hx-insert "^N"-"\M-^?" .self-insert
bindkey -R -M hx-insert "^K"-"^L" .self-insert
bindkey -R -M hx-insert "^@"-"^I" .self-insert
bindkey -M hx-insert "^J" .accept-line
bindkey -M hx-insert "^M" .accept-line
bindkey -M hx-insert "^?" backward-delete-char
bindkey -M hx-insert "^[[3~" delete-char

# access history with arrow keys
bindkey -M hx-insert "^[OA" up-line-or-beginning-search
bindkey -M hx-insert "^[OB" down-line-or-beginning-search

# switching modes
bindkey -M hx-insert "^[" hx-normal-mode

#################################################
# Normal Keymap                                 #
#################################################

# basic keys
bindkey -M hx-normal "h" vi-backward-char
bindkey -M hx-normal "j" down-line
bindkey -M hx-normal "k" up-line
bindkey -M hx-normal "l" vi-forward-char
bindkey -M hx-normal "w" hx-next-word
bindkey -M hx-normal ";" deactivate-region

# bindkey -M hx-normal "d" hx-delete
bindkey -M hx-normal "d" vi-delete-char

# switching modes
bindkey -M hx-normal "i" hx-insert-mode
bindkey -M hx-normal "v" hx-select-mode


#################################################
# Select Keymap                                 #
#################################################

# switching modes
bindkey -M hx-select "i" hx-insert-mode
bindkey -M hx-select "^[" hx-normal-mode

export RPS1="$hx_mode"

bindkey -A hx-normal main
