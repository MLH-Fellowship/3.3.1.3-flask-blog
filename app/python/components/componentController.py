class ComponentController:
    def __init__(componentIndex = -1, componentCount = -1, component = None):
        self.componentIndex = componentIndex
        self.componentCount = componentCount
        self.component = component

    def increaseIndex(self):
        self.componentIndex = self.componentIndex + 1 if  self.componentIndex + 1 < self.componentCount else 0

    def decreaseIndex(self):
        self.componentIndex = self.componentIndex - 1 if  self.componentIndex - 1 > -1 else self.componentCount - 1

        