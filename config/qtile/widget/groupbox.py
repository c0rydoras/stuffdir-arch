from libqtile.widget import GroupBox, base


class CustomGroupBox(GroupBox):
    """
    A widget that graphically displays the current group.
    All groups are displayed by their label.
    If the label of a group is the empty string that group will not be displayed.
    """

    orientations = base.ORIENTATION_HORIZONTAL
    defaults = [
        ("block_highlight_text_color", None, "Selected group font colour"),
        ("active", "FFFFFF", "Active group font colour"),
        ("inactive", "404040", "Inactive group font colour"),
        (
            "highlight_method",
            "border",
            "Method of highlighting ('border', 'block', 'text', or 'line')"
            "Uses `*_border` color settings",
        ),
        ("rounded", True, "To round or not to round box borders"),
        ("unfocused_border", None, "Border or line colour for unfocused groups"),
        (
            "this_current_screen_border",
            "215578",
            "Border or line colour for group on this screen when focused.",
        ),
        (
            "this_screen_border",
            "215578",
            "Border or line colour for group on this screen when unfocused.",
        ),
        (
            "other_current_screen_border",
            "404040",
            "Border or line colour for group on other screen when focused.",
        ),
        (
            "other_screen_border",
            "404040",
            "Border or line colour for group on other screen when unfocused.",
        ),
        (
            "highlight_color",
            ["000000", "282828"],
            "Active group highlight color when using 'line' highlight method.",
        ),
        (
            "urgent_alert_method",
            "border",
            "Method for alerting you of WM urgent "
            "hints (one of 'border', 'text', 'block', or 'line')",
        ),
        ("urgent_text", "FF0000", "Urgent group font color"),
        ("urgent_border", "FF0000", "Urgent border or line color"),
        (
            "disable_drag",
            False,
            "Disable dragging and dropping of group names on widget",
        ),
        ("invert_mouse_wheel", False, "Whether to invert mouse wheel group movement"),
        ("use_mouse_wheel", True, "Whether to use mouse wheel events"),
        (
            "visible_groups",
            None,
            "Groups that will be visible. "
            "If set to None or [], all groups will be visible."
            "Visible groups are identified by name not by their displayed label.",
        ),
        (
            "hide_unused",
            False,
            "Hide groups that have no windows and that are not displayed on any screen.",
        ),
        (
            "spacing",
            None,
            "Spacing between groups" "(if set to None, will be equal to margin_x)",
        ),
    ]

    def draw(self):
        self.drawer.clear(self.background or self.bar.background)

        offset = self.margin_x
        for i, g in enumerate(self.groups):
            to_highlight = False
            is_block = self.highlight_method == "block"
            is_line = self.highlight_method == "line"

            bw = self.box_width([g])

            if self.group_has_urgent(g) and self.urgent_alert_method == "text":
                text_color = self.urgent_text
            elif g.windows:
                text_color = self.active
            else:
                text_color = self.inactive

            if g.screen:
                if self.highlight_method == "text":
                    border = None
                    text_color = self.this_current_screen_border
                else:
                    if self.block_highlight_text_color:
                        text_color = self.block_highlight_text_color
                    if self.bar.screen.group.name == g.name:
                        if self.qtile.current_screen == self.bar.screen:
                            border = self.this_current_screen_border
                            to_highlight = True
                        else:
                            border = self.this_screen_border
                    else:
                        if self.qtile.current_screen == g.screen:
                            border = self.other_current_screen_border
                        else:
                            border = self.other_screen_border
            elif self.group_has_urgent(g) and self.urgent_alert_method in (
                "border",
                "block",
                "line",
            ):
                border = self.urgent_border
                if self.urgent_alert_method == "block":
                    is_block = True
                elif self.urgent_alert_method == "line":
                    is_line = True
            else:
                border = self.unfocused_border

            self.drawbox(
                offset,
                g.label,
                border,
                text_color,
                highlight_color=self.highlight_color,
                width=bw,
                rounded=self.rounded,
                block=is_block,
                line=is_line,
                highlighted=to_highlight,
            )
            offset += bw + self.spacing
        self.drawer.draw(offsetx=self.offset, offsety=self.offsety, width=self.width)
