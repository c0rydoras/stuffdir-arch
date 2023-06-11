export ZSH="$HOME/.programms/oh-my-zsh"
export ZSH_CUSTOM="$XDG_CONFIG_HOME/oh-my-zsh"

ZSH_THEME="eastwood-time"


export SSH_AUTH_SOCK="$XDG_RUNTIME_DIR/ssh-agent.socket"

plugins=(git
    poetry
    docker
    yarn
    ember-cli
    docker-compose
    zsh-syntax-highlighting
    # helix-mode
)

source $ZSH/oh-my-zsh.sh

export ZSH_HIGHLIGHT_STYLES[unknown-token]=fg=red

export PATH="$HOME/.local/bin:$PATH"

export EDITOR='hx'

export PROJECTS_DIR="$HOME/dev/projects"
export SCREENSHOTS_DIR="$HOME/juicepad/screenshots"

# remove the need for sudo
alias systemctl='sudo systemctl'
alias pacman="sudo pacman"

# neofetch
alias neo="neofetch"
alias cneo="clear; neofetch"

# use exa instead of ls
alias ls='exa --icons'
alias lsa='ls -a'
alias tree='exa --tree -I "node_modules"'

# use bat instead of cat
alias cat='bat'

# use procs instead of ps
alias ps='procs'

# helix
alias vi='hx'
alias vim='hx'

# make these into a function maybe
alias hxconf="hx $XDG_CONFIG_HOME/helix"
alias hxqconf="hx $XDG_CONFIG_HOME/qtile/"
alias hxzconf="hx $XDG_CONFIG_HOME/zsh/"
alias hxaconf="hx $XDG_CONFIG_HOME/alacritty"
alias hxpconf="hx $XDG_CONFIG_HOME/picom/picom.conf"

# ripgrep
alias grep='\rg'

# ranger
alias rg='ranger'

# git stuff
alias gitrmb='git branch -D $(git branch --list | fzf -m | tr "\n" " ")'

# general file stuff
alias rmds='rm -rf $(ls --no-icons --only-dirs | fzf --prompt "Select directories to delete: " -m --preview "tree -C {} | head -200 " | tr "\n" " ")'

# alias the juice utils
alias sc='stuff-sc'
alias pr='. stuff-pr'


function TRAPWINCH() {
  zle && { zle reset-prompt; zle -R }
}
