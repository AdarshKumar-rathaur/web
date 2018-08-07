from django.conf import settings
from jinja2 import Environment, FileSystemLoader
import os
import datetime
import pdfkit
import tempfile


TEMPLATES_DIRS = [os.path.join(settings.BASE_DIR, *app.split('.'), 'reports')
                  for app in settings.INSTALLED_APPS if app.startswith('apps')]

RENDERED_TEMPLATES_DIR = "/tmp/"

ENV = Environment(loader=FileSystemLoader(TEMPLATES_DIRS))

PDFKIT_OPTIONS = {
    'encoding': 'UTF-8',
    'disable-smart-shrinking': None,
    'margin-top': '4cm',
    'margin-bottom': '3cm',
    'margin-left': '2cm',
    'margin-right': '2cm',
    'header-spacing': '10',
    'footer-spacing': '10'
}


class Report():
    def __init__(
        self,
        template_path,
        mapping,
        header_path=None,
        footer_path=None
    ):
        """
        Constructor of the class.

        Args:
            template_path: path to the template.
            mapping: dictionary with keys-values to render with.
            header_path: path to the header (optional).
            footer_path: path to the footer (optional).
        """
        self.template = ENV.get_template(template_path)
        self.template_html = tempfile.NamedTemporaryFile(
            delete=False,
            suffix='.html'
        )
        self.template_pdf = tempfile.NamedTemporaryFile(delete=False)
        self.options = PDFKIT_OPTIONS
        if header_path:
            self.header = ENV.get_template(header_path)
            self.header_html = tempfile.NamedTemporaryFile(
                delete=False,
                suffix='.html'
            )
            self.options['header-html'] = self.header_html.name
        else:
            self.header = None
        if footer_path:
            self.footer = ENV.get_template(footer_path)
            self.footer_html = tempfile.NamedTemporaryFile(
                delete=False,
                suffix='.html'
            )
            self.options['footer-html'] = self.footer_html.name
        else:
            self.footer = None

        self.mapping = mapping

        # add custom mappings to the template
        self.mapping['timestamp'] = datetime.datetime.now()
        self.mapping['commons_dir'] = os.path.join(
            settings.BASE_DIR, 'apps/commons/reports/commons'
        )
        self.mapping['mybase_dir'] = os.path.dirname(
            os.path.abspath(self.template.filename)
        )
        self.mapping['load_fonts'] = settings.LOAD_FONTS_IN_REPORTS

    def render(self, http_response=True):
        """
        Render the template.

        Args:
            http_response: True if you want to return an instance of
                django.http.HttpResponse (optional).

        Returns:
            If http_response is True, returns a Django like HttpResponse.
        """
        rendered_template = self.template.render(self.mapping)
        with self.template_html as f:
            f.write(rendered_template.encode('utf-8'))
        if self.header:
            rendered_template = self.header.render(self.mapping)
            with self.header_html as f:
                f.write(rendered_template.encode('utf-8'))
        if self.footer:
            rendered_template = self.footer.render(self.mapping)
            with self.footer_html as f:
                f.write(rendered_template.encode('utf-8'))

        pdfkit.from_file(
            self.template_html.name,
            self.template_pdf.name,
            options=self.options
        )

        if http_response:
            from django.http import HttpResponse
            response = HttpResponse(open(self.template_pdf.name, 'rb'))
            response['Content-Type'] = 'application/pdf'
            response['Content-Disposition'] = \
                'attachment; filename="ticket.pdf"'
            return response