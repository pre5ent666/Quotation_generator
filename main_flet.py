import flet as ft


def main(page: ft.Page):
    # page.window_maximized = True
    page.scroll = "auto"
    page.title = "記帳小幫手"

    # create all the menu buttons we will use
    menu_buttons = {
        "home": ft.ElevatedButton("返回主畫面", on_click=lambda _: page.go("/")),
        "new_record": ft.ElevatedButton("單日記帳", on_click=lambda _: page.go("/new_record")),
        "query_print": ft.ElevatedButton("統計與列印", on_click=lambda _: page.go("/query_print")),
        "clients": ft.ElevatedButton("客戶名單", on_click=lambda _: page.go("/clients")),
        "products": ft.ElevatedButton("產品列表", on_click=lambda _: page.go("/products")),
    }

    # this function will only pick the buttons needed in certain view
    def buttons_in_view(view_name: str):
        view_list = list(menu_buttons.keys())
        view_list.remove(view_name)
        return list( map(menu_buttons.get, view_list) )

    def route_change(route):
        page.views.clear()
        match page.route:
            case "/":
                page.views.append(
                    ft.View(
                        "/",
                        [
                            ft.AppBar(title=ft.Text("功能列表"), bgcolor=ft.colors.SURFACE_VARIANT),
                            ft.Column(controls=buttons_in_view("home")) # list menu buttons as a column in home page
                        ],
                    )
                )
            case "/new_record":
                page.views.append(
                    ft.View(
                        "/new_record",
                        [
                            ft.AppBar(title=ft.Text("單日記帳"), bgcolor=ft.colors.SURFACE_VARIANT),
                            ft.Row(controls=buttons_in_view("new_record")) # list menu buttons as a row on the top of this page
                        ],
                    )
                )
            case "/query_print":
                page.views.append(
                    ft.View(
                        "/query_print",
                        [
                            ft.AppBar(title=ft.Text("統計與列印"), bgcolor=ft.colors.SURFACE_VARIANT),
                            ft.Row(controls=buttons_in_view("query_print")) # list menu buttons as a row on the top of this page
                        ],
                    )
                )
            case "/clients":
                page.views.append(
                    ft.View(
                        "/clients",
                        [
                            ft.AppBar(title=ft.Text("客戶名單"), bgcolor=ft.colors.SURFACE_VARIANT),
                            ft.Row(controls=buttons_in_view("clients")) # list menu buttons as a row on the top of this page
                        ],
                    )
                )
            case "/products":
                page.views.append(
                    ft.View(
                        "/products",
                        [
                            ft.AppBar(title=ft.Text("產品列表"), bgcolor=ft.colors.SURFACE_VARIANT),
                            ft.Row(controls=buttons_in_view("products")) # list menu buttons as a row on the top of this page
                        ],
                    )
                )
        page.update()

    page.on_route_change = route_change
    #TODO: if clinet/product data is None, then add client
    page.go(page.route)

ft.app(target=main)
