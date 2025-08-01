import flet as ft

name = (
    "ElevatedButton with style attributes configured for different ControlState values"
)


def example():
    return ft.ElevatedButton(
        "Styled button 1",
        style=ft.ButtonStyle(
            color={
                ft.ControlState.HOVERED: ft.Colors.WHITE,
                ft.ControlState.FOCUSED: ft.Colors.BLUE,
                ft.ControlState.DEFAULT: ft.Colors.BLACK,
            },
            bgcolor={ft.ControlState.FOCUSED: ft.Colors.PINK_200, "": ft.Colors.YELLOW},
            padding={ft.ControlState.HOVERED: 20},
            overlay_color=ft.Colors.TRANSPARENT,
            elevation={"pressed": 0, "": 1},
            animation_duration=500,
            side={
                ft.ControlState.DEFAULT: ft.BorderSide(1, ft.Colors.BLUE),
                ft.ControlState.HOVERED: ft.BorderSide(2, ft.Colors.BLUE),
            },
            shape={
                ft.ControlState.HOVERED: ft.RoundedRectangleBorder(radius=20),
                ft.ControlState.DEFAULT: ft.RoundedRectangleBorder(radius=2),
            },
        ),
    )
