from sana_framework.templator import render


class Index:
    def __call__(self, request):
        return '200 OK', render('index.html', data=request.get('data', None))


class About:
    def __call__(self, request):
        return '200 OK', 'about'


class NotFound404:
    def __call__(self, request):
        return 'ERROR 404', '404 PAGE Not Found'
