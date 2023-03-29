from ursina import *
import random


class Smoke(Entity):
    "This class produces smokes"
    def __init__(self, x, y, custom_color:tuple):
        super().__init__()
        self.parent = camera.ui
        self.model = "quad"
        self.texture = "smoke"
        self.color = custom_color
        self.x = x
        self.y = y
        self.scale = .02
        self.alpha = 255

    def update(self):
        self.x += random.uniform(-4,4)/1000
        self.y += random.uniform(15,20)/1000
        self.scale += Vec2(.001, .001)
        self.alpha -= .7
        self.color = (self.color[0], self.color[1], self.color[2], self.alpha)
        if self.y > 8:
            destroy(self)

def make_smokes():
    num = 500
    smoke_list = [None] * num
    custom_color = color.random_color()

    for index, liste in enumerate(smoke_list):
        smoke_list[index] = Smoke(mouse.x, mouse.y, custom_color)


app = Ursina(borderless=True)
window.color = color.black

button = Button(text="", color = color.rgba(255,255,255, 0), scale = 2)
button.on_click = make_smokes

app.run()
