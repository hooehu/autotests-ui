from playwright.sync_api import Page

from components.base_component import BaseComponent
from components.views.empty_view_component import EmptyViewComponent
from elements.button import Button
from elements.file_input import FileInput
from elements.icon import Icon
from elements.image import Image
from elements.text import Text


class ImageUploadWidgetComponent(BaseComponent):
    def __init__(self, page: Page, identifier: str):
        super().__init__(page)

        self.preview_empty_view = EmptyViewComponent(page, identifier=identifier)

        self.preview_image = Image(
            page=page,
            locator=f'{identifier}-image-upload-widget-preview-image',
            name='Preview image'
        )
        self.image_upload_info_icon = Icon(
            page=page,
            locator=f'{identifier}-image-upload-widget-info-icon',
            name='Image upload info icon'
        )
        self.image_upload_info_title = Text(
            page=page,
            locator=f'{identifier}-image-upload-widget-info-title-text',
            name='Image upload info title'
        )
        self.image_upload_info_description = Text(
            page=page,
            locator=f'{identifier}-image-upload-widget-info-description-text',
            name='Image upload info description'
        )
        self.upload_button = Button(
            page=page,
            locator=f'{identifier}-image-upload-widget-upload-button',
            name='Upload button'
        )
        self.remove_button = Button(
            page=page,
            locator=f'{identifier}-image-upload-widget-remove-button',
            name='Remove button'
        )
        self.upload_input = FileInput(
            page=page,
            locator=f'{identifier}-image-upload-widget-input',
            name='Upload file input'
        )

    def check_visible(
        self,
        is_image_uploaded: bool = False
    ) -> None:
        self.image_upload_info_icon.check_visible()

        self.image_upload_info_title.check_visible()
        self.image_upload_info_title.check_have_text(
            text='Tap on "Upload image" button to select file'
        )

        self.image_upload_info_description.check_visible()
        self.image_upload_info_description.check_have_text(
            text='Recommended file size 540X300'
        )

        self.upload_button.check_visible()

        if is_image_uploaded:
            self.remove_button.check_visible()
            self.preview_image.check_visible()
        else:
            self.preview_empty_view.check_visible(
                title='No image selected',
                description='Preview of selected image will be displayed here'
            )

    def click_remove_image_button(self) -> None:
        self.remove_button.click()

    def check_visible_preview_image(self) -> None:
        self.preview_image.check_visible()

    def upload_preview_image(self, file: str) -> None:
        self.upload_input.set_input_files(file)
