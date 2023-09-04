export ZSH="$HOME/.programms/oh-my-zsh"

export ZSH_CUSTOM="$XDG_CONFIG_HOME/oh-my-zsh" 

ZSH_THEME="eastwood-time" 

export SSH_AUTH_SOCK="$XDG_RUNTIME_DIR/ssh-agent.socket" 

plugins=(zsh-syntax-highlighting)

source $ZSH/oh-my-zsh.sh 

# stop the syntax highlighting from being bold
export ZSH_HIGHLIGHT_STYLES[unknown-token]=fg=red 

export PATH="$HOME/.local/bin:$PATH"

# pnpm
export PNPM_HOME="$HOME/.local/share/pnpm"
case ":$PATH:" in
  *":$PNPM_HOME:"*) ;;
  *) export PATH="$PNPM_HOME:$PATH" ;;
esac
# pnpm end

# volta
export VOLTA_HOME="$HOME/.volta"
export PATH="$VOLTA_HOME/bin:$PATH"

export EDITOR='hx'

export PROJECTS_DIR="$HOME/dev/projects"
export SCREENSHOTS_DIR="$HOME/juicepad/screenshots"

# neofetch
alias no="neofetch"
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
alias hex='sudoedit'

# make these into a function maybe
alias hxconf="hx $XDG_CONFIG_HOME/helix"
alias hxqconf="hx $XDG_CONFIG_HOME/qtile/"
alias hxzconf="hx $XDG_CONFIG_HOME/zsh/"
alias hxaconf="hx $XDG_CONFIG_HOME/alacritty"
alias hxpconf="hx $XDG_CONFIG_HOME/picom/picom.conf"
alias hxhconf="hx $XDG_CONFIG_HOME/hypr"
alias hxtconf="hx $XDG_CONFIG_HOME/tmux"

# ripgrep
alias grep='\rg'

# ranger
alias rg='ranger'

# git stuff
alias gitrmb='git branch -D $(git branch --list | fzf -m | tr "\n" " ")'

# general file stuff
alias rmds='rm -rf $(ls --no-icons --only-dirs | fzf --prompt "Select directories to delete: " -m --preview "tree -C {} | head -200 " | tr "\n" " ")'

# alias the shell scripts
alias sc='stuff-sc'
alias pr='. prx' # stuff-pr has its own repo now: https://github.com/C0rydoras/prx

# clear
alias clear='clear -x'
alias ql='clear'

# docker compose
alias dc='docker compose'
alias dcu='docker compose up -d'
alias dcf='docker compose logs -f'
alias dcb='docker compose build'
alias dcr='docker compose run'
alias dce='docker compose exec'

# docker
alias dv='docker volume'

# make
alias m='make'
alias mx='sudo make'

# pacman
alias px='pacman'
alias pax='sudo pacman'

# systemcuddle
alias sx='systemctl'
alias syx='systemctl'

function TRAPWINCH() {
  zle && { zle reset-prompt; zle -R }
}
