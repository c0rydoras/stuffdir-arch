.DEFAULT_GOAL := help

.PHONY: help
help:
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort -k 1,1 | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

.PHONY: setup-zshenv
setup-zshenv: ## Set up zshenv
	@ln -sf ${HOME}/.stuff/config/zsh/.zshenv ~/.zshenv 

.PHONY: setup-omz
setup-omz:	## Set up oh-my-zsh
	@git clone https://github.com/ohmyzsh/ohmyzsh.git ~/.programms/oh-my-zsh

.PHONY: setup-zsh-syntax-highlighting
setup-zsh-syntax-highlighting: ## Set up zsh syntax highlighting
	@git clone https://github.com/zsh-users/zsh-syntax-highlighting config/oh-my-zsh/plugins/zsh-syntax-highlighting/

.PHONY: setup-zsh-default
setup-zsh-default: ## Set up zsh as default shell
	@sudo chsh $(which zsh)

.PHONY: source-zsh
source-zsh: ## Source zsh
	@source ${HOME}/.stuff/config/zsh/.zshrc 

.PHONY: setup-zsh
setup-zsh: setup-omz setup-zshenv setup-zsh-syntax-highlighting setup-zsh-default source-zsh ## Set up zsh

.PHONY: setup-bin
setup-bin:  ## Set up the binaries & their completions
	@sudo ln -sf ${HOME}/.stuff/bin/* /usr/local/bin/ && \
	sudo ln -sf ${HOME}/.stuff/completions/* /usr/share/zsh/site-functions/

.PHONY: setup-directories
setup-directories: ## Set up directories
	@mkdir -p ~/.programms ~/dev/projects ~/dev/packages ~/juicepad/.bloat && mkdir /etc/wallpapers && \
	cd ~/juicepad && mkdir documents downloads notes onedrive postman screenshots && \
	cd .bloat && mkdir desktop music pictures public templates videos && cd

.PHONY: setup-xdg-dirs
setup-xdg-dirs: ## Update xdg-user-dirs
	@xdg-user-dirs

.PHONY: setup-yay
setup-yay: ## Install yay
	@git clone https://aur.archlinux.org/yay.git _yay042374 && cd yay && makepkg -si && cd .. && rm -rf _yay042374 && \
	
.PHONY: setup-core-packages
setup-core-packages: ## Install core packages
	yay -Sy  curl fd exa ripgrep qtile alacritty firefox xdg-user-dirs rofi fzf imagemagick mlocate neofetch neovim python-dbus-next python-psutil python-pyxdg slock sddm ranger ttf-droid ttf-font-awesome udiskie udisks2 ueberzug rofi-themes-collection helix-git bolt gnome-keyring nm-applet networkmanager intel-ucode htop wget curl --noconfirm --needed && \
	updatedb 

.PHONY: setup-wallpapers
setup-wallpapers:
	@sudo ln -sf ${HOME}/.stuff/wallpapers/* /etc/wallpapers/

.PHONY: setup
setup: setup-yay setup-core-packages setup-directories setup-zsh setup-bin setup-xdg-dirs setup-wallpaper ## Set up everything
