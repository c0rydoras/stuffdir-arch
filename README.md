# Stuff directory for archlinux

My personal directory with stuff for archlinux, containing scripts and application configurations for archlinux.

Heavily inspired by [localdir](https://github.com/ayekat/localdir).

## Requirements

- `git`
- `base-devel`
- `zsh` the install has to be executed in zsh otherwise it will break stuff

## Installation

1. `git clone https://github.com/c0rydoras/stuffdir-arch ~/.stuff`
2. `cd ~/.stuff`
3. `make setup`
4. `systemctl edit user@<user_id>.service`

```bash
[Service]
Environment=XDG_CONFIG_HOME=/home/<username>/.stuff/config
```

5. restart/start a qtile session
   This can be achieved by either rebooting or restarting your display manager.
   Example with sddm:

```bash
systemctl restart sddm
```

## Notes

- Wallpaper by [Daniel Leone](https://unsplash.com/photos/g30P1zcOzXo), licensed under the [Unsplash License](https://unsplash.com/license)
- I haven't fully tested the install target in the makefile yet

## License

This code is licensed under the [MIT](LICENSE) license.
