import re

from playwright.sync_api import Page

from components.base_component import BaseComponent
from components.navigation.sidebar_list_item_component import SidebarListItemComponent


class SidebarComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)
        self.logout_list_item = SidebarListItemComponent(page)
        self.courses_list_item = SidebarListItemComponent(page)
        self.dashboard_list_item = SidebarListItemComponent(page)

    def check_visible(self) -> None:
        self.logout_list_item.check_visible('Logout', identifier='logout')
        self.courses_list_item.check_visible('Courses', identifier='courses')
        self.dashboard_list_item.check_visible('Dashboard', identifier='dashboard')

    def click_logout(self) -> None:
        # .* в регулярке значит, что левая часть - любая
        self.logout_list_item.navigate(
            re.compile(r'.*/#/auth/login'),
            identifier='logout'
        )

    def click_courses(self) -> None:
        self.courses_list_item.navigate(
            re.compile(r'.*/#/courses'),
            identifier='courses'
        )

    def click_dashboard(self) -> None:
        self.dashboard_list_item.navigate(
            re.compile(r'.*/#/dashboard'),
            identifier='dashboard'
        )
