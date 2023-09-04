from libqtile import bar, layout, widget, hook
from libqtile.config import Click, Drag, Group, Key, Match, Screen, DropDown, ScratchPad
from libqtile.lazy import lazy

# slightly modified groupbox widget
from widget.groupbox import CustomGroupBox

import os
import subprocess

# Qtile Configuration for 󰣇

# General stuff
BORDER_WIDTH = 0
# BORDER_WIDTH = 5
GAPS = 5

mod = "mod4"

NORD = {
    "nord0": "#2E3440",
    "nord1": "#3B4252",
    "nord2": "#434C5E",
    "nord3": "#4C566A",
    "nord4": "#D8DEE9",
    "nord5": "#E5E9F0",
    "nord6": "#ECEFF4",
    "nord7": "#8FBCBB",
    "nord8": "#88C0D0",
    "nord9": "#81A1C1",
    "nord10": "#5E81AC",
    "nord11": "#bf616a",
    "nord12": "#d08770",
    "nord13": "#ebcb8b",
    "nord14": "#a3be8c"
}

BORDER_COLOR=(NORD["nord8"], NORD["nord9"])

keys = [
    Key([mod], "h", lazy.layout.left()),
    Key([mod], "l", lazy.layout.right()),
    Key([mod], "j", lazy.layout.down()),
    Key([mod], "k", lazy.layout.up()),
    Key([mod], "space", lazy.layout.next()),
    Key([mod, "control"], "h", lazy.layout.shuffle_left()),
    Key([mod, "control"], "l", lazy.layout.shuffle_right()),
    Key([mod, "control"], "j", lazy.layout.shuffle_down()),
    Key([mod, "control"], "k", lazy.layout.shuffle_up()),
    Key([mod, "shift"], "h", lazy.layout.grow_left()),
    Key([mod, "shift"], "l", lazy.layout.grow_right()),
    Key([mod, "shift"], "j", lazy.layout.grow_down()),
    Key([mod, "shift"], "k", lazy.layout.grow_up()),
    Key([mod], "n", lazy.layout.normalize()),
    Key([mod], "Tab", lazy.next_layout()),
    Key([mod], "w", lazy.window.kill()),
    Key([mod, "control"], "r", lazy.reload_config()),
    Key([mod, "control"], "q", lazy.shutdown()),
    # maximize
    Key([mod], "y", lazy.window.toggle_maximize(), desc="Toggle maximize"),
    # Keyboard layout
    Key([mod], "period", lazy.widget["keyboardlayout"].next_keyboard()),
    # Applications
    Key([mod], "r", lazy.spawncmd()),
    Key([mod], "return", lazy.spawn("alacritty")),
    Key([mod], "f", lazy.spawn("firefox")),
    Key([mod], "c", lazy.spawn("code")),
    Key([mod], "t", lazy.spawn("thunderbird")),
    Key([mod, "shift"], "t", lazy.spawn("teams-for-linux")),
    Key([mod, "shift"], "m", lazy.spawn("mattermost-desktop")),
    Key([mod], "m", lazy.spawn("slock")),
    Key([mod], "o", lazy.spawn("obsidian")),
    Key([mod], "g", lazy.spawn("geogebra")),
    Key([mod], "e", lazy.spawn("alacritty --title 'Ranger' --class ranger -e ranger")),
    Key([mod, "shift"], "s", lazy.spawn("stuff-screenshot")),
    Key([mod], "equal", lazy.spawn("stuff-sc")),
    # Audio and brightness
    Key(
        [],
        "XF86AudioRaiseVolume",
        lazy.spawn("pactl set-sink-volume 0 +5%"),
        desc="Volume Up",
    ),
    Key(
        [],
        "XF86AudioLowerVolume",
        lazy.spawn("pactl set-sink-volume 0 -5%"),
        desc="volume down",
    ),
    Key(
        [], "XF86AudioMute", lazy.spawn("pulsemixer --toggle-mute"), desc="Volume Mute"
    ),
    Key(
        [],
        "XF86MonBrightnessUp",
        lazy.spawn("brightnessctl s 10%+"),
        desc="brightness UP",
    ),
    Key(
        [],
        "XF86MonBrightnessDown",
        lazy.spawn("brightnessctl s 10%-"),
        desc="brightness Down",
    ),
]

GROUP_NAMES = ["dev", "web", "social-stuff", "school", "office"]
GROUP_LABELS = ["", "", "", "", ""]
GROUP_KEYS = [str(i) for i in range(1, 6)]
GROUP_MATCHES = [
    ["Alacritty", "Code"],
    ["firefox", "google-chrome-stable"],
    ["Mattermost", "thunderbird", "teams-for-linux"],
    ["geogebra", "obsidian", "firefox"],
    ["DesktopEditors"]
]
GROUP_SCREENS = [0, 1, 2, 0, 1]
FONT = "Droid Sans"
FONT_MONO = "Droid Sans Mono"
FONT_ICON = "Font Awesome 6 Free"
groups = [
    Group(
        name,
        label=label,
        screen_affinity=screen,
        matches=[Match(wm_class=app) for app in matches],
    )
    for name, label, screen, matches in zip(
        GROUP_NAMES, GROUP_LABELS, GROUP_SCREENS, GROUP_MATCHES
    )
]

for group, key in zip(groups, GROUP_KEYS):
    keys.extend(
        [
            Key([mod], key, lazy.group[group.name].toscreen()),
            Key([mod, "shift"], key, lazy.window.togroup(group.name)),
        ]
    )

groups.append(
    ScratchPad(
        "scratchpad",
        [
            DropDown(
                "term",
                f"alacritty --config-file={os.environ['XDG_CONFIG_HOME']}/alacritty/scratchpad.yml",
                height=0.5,
                y=0.2,
            ),
            DropDown("volume", "pavucontrol"),
        ],
    )
)
keys.extend(
    [
        Key(
            [mod, "shift"],
            "Return",
            lazy.group["scratchpad"].dropdown_toggle("term"),
        ),
        Key(
            [mod],
            "backslash",
            lazy.group["scratchpad"].dropdown_toggle("volume"),
        ),
    ]
)

layouts = [
    layout.Columns(
        margin=GAPS,
        border_width=BORDER_WIDTH,
        border_focus=BORDER_COLOR,
        border_normal=NORD["nord0"],
        border_on_single=True,
    ),
]

widget_defaults = dict(
    font=FONT,
    fontsize=16,
    padding=3,
    foreground=NORD["nord4"],
)

extension_defaults = widget_defaults.copy()

CLOCK_FORMATS = {"date": "%Y-%m-%d", "time": "%H:%M:%S"}


def switch_clock_format(widget):
    if widget.format == CLOCK_FORMATS["date"]:
        widget.format = CLOCK_FORMATS["time"]
    else:
        widget.format = CLOCK_FORMATS["date"]


CLOCK = widget.Clock(
    format=CLOCK_FORMATS["date"],
    padding=9,
    mouse_callbacks={"Button1": lazy.widget["clock"].function(switch_clock_format)},
)

group_box_defaults = dict(
    highlight_method="line",
    padding=5,
    fontsize=21,
    disable_drag=True,
    this_current_screen_border=NORD["nord8"],
    this_screen_border=NORD["nord9"],
    other_screen_border=NORD["nord10"],
    other_current_screen_border=NORD["nord10"],
    foreground="#ff00ff",
    borderwidth=4,
    highlight_color="#00000000",
    background=None,
    active=NORD["nord5"],
    inactive=NORD["nord4"],
    hide_unused=True,
    font=FONT_ICON,
    unfocused_border=NORD["nord10"],
)

BAR_DEFAULTS = dict(
    margin=[10, GAPS * 2, GAPS, GAPS * 2],
    background=NORD["nord0"] + "CC",
    size=45,
    border_width=BORDER_WIDTH,
    border_color=NORD["nord0"]
)

SCREEN_DEFAULTS = dict(
    bottom=bar.Gap(GAPS),
    left=bar.Gap(GAPS),
    right=bar.Gap(GAPS),
    wallpaper="/etc/wallpapers/mountain.jpg",
    wallpaper_mode="fill",
)

screens = [
    Screen(
        top=bar.Bar(
            [
                CustomGroupBox(**group_box_defaults),
                widget.Prompt(),
                widget.WindowName(),
                widget.Spacer(length=3),
                widget.WidgetBox(
                    text_open="",
                    text_closed="",
                    fontsize=20,
                    close_button_location="right",
                    widgets=[
                        widget.Volume(fmt="Volume: {}"),
                        widget.Systray(),
                        widget.Spacer(length=9),
                    ],
                ),
                widget.KeyboardLayout(
                    configured_keyboards=["us", "ch"],
                    font=FONT_MONO,
                    fontsize=0,
                ),
            widget.GenPollCommand(cmd="stuff-get-overtime --username arthurd", update_interval=60, shell=True),
                widget.Battery(
                    fmt="󰁹 {}",
                    format="{percent:2.0%}",
                    hide_threshold=0.99,
                ),
                CLOCK,
            ],
            **BAR_DEFAULTS,
        ),
        **SCREEN_DEFAULTS,
    ),
    Screen(
        top=bar.Bar(
            [
                CustomGroupBox(**group_box_defaults),
                widget.Prompt(),
                widget.WindowName(),
                widget.TextBox("", font=FONT_ICON),
                widget.Memory(fmt="{}", format="{MemPercent: .1f}%"),
                widget.TextBox("", font=FONT_ICON),
                widget.Net(
                    fmt="{}",
                    format="{down} ↓↑ {up}",
                    prefix="k",
                ),
                widget.TextBox("", font=FONT_ICON),
                widget.CPU(fmt="{}", format="{load_percent:02.1f}%"),
                widget.Spacer(length=9),
            ],
            **BAR_DEFAULTS,
        ),
        **SCREEN_DEFAULTS,
    ),
    Screen(
        top=bar.Bar(
            [
                CustomGroupBox(**group_box_defaults),
                widget.Prompt(),
                widget.WindowName(),
                widget.Clock(padding=9, format="%H:%M:%S"),
            ],
            **BAR_DEFAULTS,
        ),
        **SCREEN_DEFAULTS,
    ),
]

# Drag floating layouts.
mouse = [
    Drag(
        [mod],
        "Button1",
        lazy.window.set_position_floating(),
        start=lazy.window.get_position(),
    ),
    Drag(
        [mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()
    ),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
    ],
    border_width=BORDER_WIDTH,
    border_focus=BORDER_COLOR,
)
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True


@hook.subscribe.startup_once
def autostart():
    xdg_config_home = os.getenv("XDG_CONFIG_HOME")
    if not xdg_config_home:
        return
    subprocess.call(f"{xdg_config_home}/qtile/autostart.sh")


# wmname = "Qtile"
