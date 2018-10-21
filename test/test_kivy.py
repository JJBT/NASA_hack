from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.network.urlrequest import UrlRequest


class Example(FloatLayout):
    def __init__(self, **kwargs):
        super(Example, self).__init__(**kwargs)

    def on_success(self, req, result, *args):
        res = result
        layout = BoxLayout(orientation='vertical')

        for item in res:
            layout2 = BoxLayout(orientation='horizontal')
            name = item['nama']
            email = item['email']
            label = Label(text=name)
            label2 = Label(text=email)
            layout2.add_widget(label)
            layout2.add_widget(label2)
            layout.add_widget(layout2)

        self.add_widget(layout)


class Demo(App):
    def build(self):
        return Example()


if __name__ == '__main__':
    Demo().run()
